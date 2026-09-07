# 📡 TMT Research Radar

### TMT(Technology·Media·Telecom) 산업 회계 이슈 자동 모니터링

> **TMT 산업 감사를 준비하며 만든 회계 이슈 자동 리서치 저장소**입니다.
> DART 공시 · 뉴스 · 회계법인 산업 리포트를 매주 자동으로 수집해, 업종과 회계 토픽으로
> 분류하고 대시보드로 정리합니다. 커밋 히스토리가 그대로 리서치 로그가 됩니다.
>
> **업종 5분류** — 엔터 · 미디어 · 통신 · 게임 · IT
> **대상 기업 67개사** — 삼정KPMG 연결재무제표 감사실적(사업보고서) 중 TMT 관련 피감사회사
> 39곳(`kpmg: true`)에, 산업 커버리지 보강을 위한 규모 있는 기업 28곳을 더했습니다.
> ([config/companies.yml](config/companies.yml))

## 왜 TMT인가
회계법인은 이 산업군을 **TMT(Technology, Media & Telecommunications)** 부문으로 묶어 다룹니다.
그리고 TMT는 회계처리 판단이 특히 어려운 영역입니다.

| 판단이 갈리는 지점 | 기준 |
|---|---|
| 게임 아이템 결제를 **언제** 수익으로 볼 것인가 | IFRS 15 |
| 플랫폼 중개 매출을 **총액이냐 순액이냐** | IFRS 15 |
| 콘텐츠 제작비·개발비를 **자산화할 수 있는가**, 손상은 | IAS 38 / IAS 36 |
| 데이터센터 계약이 **리스인가 용역인가** | IFRS 16 |

실무에서 반복 쟁점이 되는 이 판단들을 **공시(1차 근거) + 뉴스(최신 사례) + 회계법인 리포트(실무 해석)**
세 갈래로 추적하도록 자동화했습니다.

## 구조
```
config/     대상 기업(업종 5분류) · 회계 키워드 · 리포트 소스
scripts/    ① DART 공시  ② 뉴스 모니터링  ③ 회계법인 리포트  → 대시보드 렌더
topics/     회계 토픽별 심화 정리 문서 (수동 분석 + 자동 사례 축적)
.github/    매주 자동 실행 워크플로
```

## 파이프라인
| # | 스크립트 | 소스 | 산출 |
|---|---|---|---|
| ① | `dart_collector.py` | DART Open API | 대상 기업 공시 중 회계이슈 건 |
| ② | `news_monitor.py` | Google 뉴스 RSS | 주요 뉴스 + 회계·감사 기사(태깅) |
| ③ | `report_collector.py` | 삼일·삼정·딜로이트·EY 인사이트 | 산업/회계 리포트 |
| → | `build_dashboard.py` | 위 3종 통합 | 아래 대시보드 + 커밋 |

## 로컬 실행
```bash
pip install -r requirements.txt
export DART_API_KEY=...            # https://opendart.fss.or.kr (무료)
python scripts/update_corp_codes.py   # 최초 1회: corp_code 자동 채움
python scripts/dart_collector.py      # DART 공시 (DART_API_KEY 필요)
python scripts/news_monitor.py        # 뉴스 (Google 뉴스 RSS — 키 불필요)
python scripts/report_collector.py    # 회계법인 리포트 (키 불필요)
python scripts/build_dashboard.py
```
뉴스·리포트는 API 키가 필요 없습니다. GitHub 저장소 Settings → Secrets 에 **`DART_API_KEY`** 하나만
등록하면 매주 자동 실행됩니다.

## 회계 토픽 심화 정리
- [IFRS 15 — 수익인식](topics/ifrs15-revenue.md)
- [IFRS 16 — 리스](topics/ifrs16-lease.md)
- [무형자산 (IAS 38)](topics/intangible-assets.md)
- [플랫폼 기업 회계 이슈](topics/platform-cases.md)
- [콘텐츠 산업 구조](topics/industry-structure.md)
- [엔터기업 회계 이슈](topics/entertainment-issues.md)

---

## 📊 최신 수집 대시보드
> 아래 내용은 **GitHub Actions가 매주 월요일 08:00(KST) 자동 실행**하여 갱신·커밋합니다
> (`.github/workflows/research.yml`). 즉 아래 표는 고정된 스냅샷이 아니라 **매주 새로 수집된 결과**로
> 교체되며, 커밋 히스토리에 주차별 리서치 기록이 쌓입니다. 수동 실행은 Actions 탭 → Run workflow.

<!--RADAR:START-->
_최종 갱신: 2026-09-07 09:50 KST_

**수집 현황** — DART 공시 166 · 뉴스 330 · 회계법인 리포트 2

### 📄 DART 공시 (회계 이슈 필터)
_종류별: 실적 73 · 📘정기 54 · 🔴정정 15 · 🟡주요사항 24_

| 종류 | 업종 | 기업 | 일자 | 공시 |
|---|---|---|---|---|
| 🔴정정 | 엔터 | 큐브엔터 | 20260831 | [[기재정정]주요사항보고서(유상증자결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260831001295) |
| 🔴정정 | IT | 카카오 | 20260824 | [[첨부정정]주요사항보고서(회사합병결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260824000219) |
| 🔴정정 | IT | 카카오 | 20260819 | [[기재정정]반기보고서 (2026.06)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260819000055) |
| 🔴정정 | IT | 다우데이타 | 20260811 | [[기재정정]회사합병결정(종속회사의주요경영사항)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260811900833) |
| 🔴정정 | 게임 | 넷마블 | 20260807 | [[기재정정]증권발행실적보고서(합병등)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260807000552) |
| 🔴정정 | 게임 | 더블유게임즈 | 20260724 | [[기재정정]사업보고서 (2025.12)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260724000595) |
| 🔴정정 | 통신 | 에스케이텔레콤 | 20260723 | [[기재정정]타법인주식및출자증권취득결정](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260723801025) |
| 🔴정정 | IT | 엔에이치엔 | 20260710 | [[첨부정정]주요사항보고서(회사합병결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260710000147) |
| 🔴정정 | 게임 | 크래프톤 | 20260630 | [[기재정정]타법인주식및출자증권취득결정](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260630800855) |
| 🔴정정 | 게임 | 위메이드 | 20260630 | [[기재정정]최대주주변경을수반하는주식양수도계약체결](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260630901591) |
| 📘정기 | IT | 당근마켓 | 20260831 | [반기보고서 (2026.06)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260831000269) |
| 📘정기 | IT | 무신사 | 20260831 | [반기보고서 (2026.06)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260831000288) |
| 📘정기 | 게임 | 넷마블 | 20260814 | [반기보고서 (2026.06)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260814002548) |
| 📘정기 | 게임 | 엔씨소프트 | 20260814 | [반기보고서 (2026.06)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260814003764) |
| 📘정기 | 게임 | 크래프톤 | 20260814 | [반기보고서 (2026.06)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260814003894) |
| 📘정기 | 게임 | 펄어비스 | 20260814 | [반기보고서 (2026.06)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260814003642) |
| 📘정기 | 게임 | 넵튠 | 20260814 | [반기보고서 (2026.06)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260814002821) |
| 📘정기 | 게임 | 위메이드플레이 | 20260814 | [반기보고서 (2026.06)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260814001998) |
| 📘정기 | 게임 | 컴투스 | 20260814 | [반기보고서 (2026.06)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260814003984) |
| 📘정기 | 게임 | 위메이드 | 20260814 | [반기보고서 (2026.06)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260814003490) |
| 🟡주요사항 | 통신 | 에스케이브로드밴드 | 20260827 | [주요사항보고서(회사분할결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260827001001) |
| 🟡주요사항 | 통신 | 에스케이텔레콤 | 20260827 | [주요사항보고서(자기주식처분결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260827000390) |
| 🟡주요사항 | 엔터 | 하이브 | 20260825 | [주요사항보고서(자기주식처분결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260825000350) |
| 🟡주요사항 | IT | 카카오 | 20260821 | [주요사항보고서(회사합병결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260821000052) |
| 🟡주요사항 | IT | 카카오 | 20260821 | [주요사항보고서(회사분할결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260821000047) |
| 🟡주요사항 | IT | 무신사 | 20260813 | [주요사항보고서(자기주식처분결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260813001369) |
| 🟡주요사항 | 게임 | 네오위즈 | 20260812 | [주요사항보고서(자기주식취득신탁계약체결결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260812000035) |
| 🟡주요사항 | 미디어 | 나스미디어 | 20260806 | [주요사항보고서(자기주식취득신탁계약해지결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260806000438) |
| 🟡주요사항 | 게임 | 크래프톤 | 20260729 | [주요사항보고서(자기주식취득결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260729000354) |
| 🟡주요사항 | 통신 | 엘지유플러스 | 20260729 | [주요사항보고서(자기주식취득신탁계약체결결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260729000479) |
| 실적 | 게임 | 위메이드플레이 | 20260812 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260812900504) |
| 실적 | 게임 | 컴투스 | 20260812 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260812900071) |
| 실적 | 게임 | 위메이드 | 20260812 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260812900664) |
| 실적 | 게임 | 네오위즈 | 20260812 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260812900051) |
| 실적 | 게임 | 더블유게임즈 | 20260812 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260812800023) |
| 실적 | 게임 | 더블유게임즈 | 20260812 | [영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260812800020) |
| 실적 | 엔터 | 제이와이피엔터테인먼트 | 20260812 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260812900607) |
| 실적 | 통신 | 케이티 | 20260812 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260812800090) |
| 실적 | 통신 | 케이티 | 20260812 | [영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260812800089) |
| 실적 | 게임 | 엔씨소프트 | 20260811 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260811800245) |

### 📰 뉴스 모니터링 (🔴 = 감사·재무제표 신호)
_구분: 🔴회계신호 19 · 🔵회계이슈 10 · 일반 301_

| 구분 | 업종 | 기업 | 기사 | 회계토픽 | 출처 |
|---|---|---|---|---|---|
| 🔴회계신호 | 게임 | 넷마블 | [[재무제표 이야기] '정수기 게임' 우려 딛고 넷마블의 ‘황금알’ 된 코웨이](https://news.google.com/rss/articles/CBMibEFVX3lxTE56UWVmcFpXTmhHZm1hanhhWFFjNUljbWpuZndaYUdQckRQTmUzTEtJb3hkU0p2b21jZ1RjSXZhZ0dQc19BRlhkTzFJTlVTM1NtbDB5emxnb1k0MDFQd1JkY3owVVItN3dkZjYzdA?oc=5) | - | 생생비즈플러스 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [금감원, 메가박스·콘텐트리중앙 회계심사 돌입…자금 조달·회계처리 점검 - v](https://news.google.com/rss/articles/CBMiT0FVX3lxTE55eHlOanhSb0VrOFJ6MmpaaWhvRVh2SGZKSVJsWktINkNYcGpZRnBRLTUwdFBBWGJoUHFlZm1MUkZTR0tQTzZCanBvWW9xOEk?oc=5) | - | v.daum.net |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권투자자들, 금감원에 감리 요구…"회계처리 의문" - yna.co](https://news.google.com/rss/articles/CBMiW0FVX3lxTFB1Ukx0THpTTk1DSVh2VGtQU2hsZTBuZWhlRWhzLUFKNGY0dm1RZkgwdDIxMXdaTzhkTXozUXltRTlOS2VOZ25SdGlfLVY1WVhsYUVfWmMxTERDUmvSAWBBVV95cUxQRDRMM1RQYmYwcGlUY1o2YmZfWTNKQlRDU2JkTmxWNnFlVEs4cTFCOElOR1MyUjhyb0twN18zMkNINldZOE1ZSTNKVVJWdmRDOFZ4S2M2OTVoVHVaWDRHUHo?oc=5) | - | yna.co.kr |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [“돌려막기로 자본잠식 숨겼나”…중앙그룹 채권투자 피해자들, 감리 요구 - 한](https://news.google.com/rss/articles/CBMickFVX3lxTFBDSS1uQk52SXBhb1kycHJkNU5na0w1cmtyUm1hSW5KM2YtQkZWUy1TYlVfT2F5NHhUdElibTdhaExkblFZWExucFBXeVRpM1FkcTNvdm41dHpaODZEVzhScldkQ2FwTnRjZmJWTll0Z3p6dw?oc=5) | - | 한겨레 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 투자자들 “회계처리 의문”… 금감원에 감리 요청 - v.daum.n](https://news.google.com/rss/articles/CBMiVEFVX3lxTE1fS1hlUE9VYWpjdnRpb2JiTGxsVjJpUHNDZV9lQ1hmUVBkUDg3SVpBTjdiVG56R0w1OVlKT1VtVS1mbkZRRkkwSUR1cEpCeHFrSXRKRw?oc=5) | - | v.daum.net |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권투자자들, 금감원에 감리 요구…"JTBC 등 회계처리 조사" -](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9USmdOS04yVzNFQUhINmFtemVYdjhqYkpJYmN6TnlYMU9mdXQxWGtRQTVmek5kMXpZbjNOZ2kydEJWbFVzaGlZQS1vbUhJUmxDWkc0N3dZLVd1c2VhTURv?oc=5) | - | 조세일보 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [반기보고서 무더기 '의견거절'…투자 유의해야 - v.daum.net](https://news.google.com/rss/articles/CBMiRkFVX3lxTE1TQVowaC1JUEoyZm5zeGRHS1VwdGFKRWQ2ZWRUak9LRG1NVWppUEJGU0NlNm93Tnc4VDE5ZXkyeDRxMTZDc3c?oc=5) | - | v.daum.net |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | ["재무제표 왜곡·우회 자본 순환 의혹"…중앙그룹 피해자들 검사 촉구 - 뉴스](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9TelEtWGVBbnNXSF9DQXhOQlVSRHdRRklJTWpISUVwNjJ3ZkI0XzZJcm42bEswT1I1ZURrOTlCWThKZExpakxBeEcwVjNWdmxDQ0hsSmJ0bG5SaXktVkE00gFkQVVfeXFMTVRqblZaVkV0Z0ZEWTJlRjJKYjh3WUd2aWJ0VDVGZTBsTnVQTlBqWUFXckM2Mm9IMm52MVNKQVpILUJfVXFMOTRFNGF3OTlsTFJ6TjE1cFI2N2FWWnp1a21LTF9kNw?oc=5) | - | 뉴스1 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권 투자자 금감원에 감리 요구 - 조선비즈 - Chosunbiz](https://news.google.com/rss/articles/CBMigwFBVV95cUxOZ1BZZWVoNlItVU8zZTdWOTBmWVpncDBDUnMyenNPYUhNbWFDRDRlTjZpbzd6MnFxWHhzeWdmb01Jci1QRnN4UU83M0FmcHNTZ21HQmpxSF80WmxIMWRmcldCYmZhZUd4amk0bUtFazJnMVNOZklrZUp2ZjVPb2dFY2xJUdIBlwFBVV95cUxObmZVWHNYUEZEcU9BUUpKQXl1bmNJblA1ZkVvWlZ6bDExdWZkT2JWdFlnR3B0SGdBMWxQVmZrTUdzSlZiQ3FiV1pHU19FZ3M0WHlVMng2dDdpRW1ZUTRnalV3Ri1keE1rOHJVSkpHVUE3Y29jNzltSFNtZ0pOWUQ0OWJHOV9laHY3X2Z4WkdxZktNaHlzTWhn?oc=5) | - | Chosunbiz |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [콘텐트리중앙, 관리종목 지정사유 반기검토의견 의견거절로 변경 - 톱스타뉴스](https://news.google.com/rss/articles/CBMickFVX3lxTE03Ui10WThDS1ljYnBHOXI3MXhHb19Td3gwRkRxSG1qek5HcDR5TTc3cWFUd0dERXhJUzFveGNBOWJRYkF3VHJaV2VpbTRZWDRndHE2UU1mUG8tN1g5VmZTTmhwOWpsRWFTdnY5RmFKdTRudw?oc=5) | - | 톱스타뉴스 |
| 🔴회계신호 | IT | 네이버 | [[단독] 두나무, 美 SEC 위원장 면담, 회계기준 전환 완료...나스닥행 ](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPTE5PSW1ya182NWtnSDlMTmFrSkhvVC1xUmhPNG9zb3ZDZWd2RVVGalBvSFdmT0xMYUd3bWIxbkE1TkF3YVpPTWtxdlVZTUszdGExSTBNMFhBdkZaMkV3V2JpT196UXV0aDVFMmczaWpYbU5YVXpWbDd1Q1cxVmtEMWtfdzZ5WHZydGhB?oc=5) | - | 조선일보 |
| 🔴회계신호 | IT | 카카오 | [카카오 노조가 놓친 '새 회계기준 함정'…"내년엔 성과급 0원 될 수도" -](https://news.google.com/rss/articles/CBMiaEFVX3lxTE8yRnFCUUFIUzY3YTR1cDZqdmRVODJWd0pWT3E2SnNFQjBlTlpLZ0ZQQV90cTk3bldhRmdDUm1WVmN6WUZ5aDhrRjlWOXFYZzUwRzJhVktoejFha051VjRCUEVDb2x2UE1u?oc=5) | - | ebn.co.kr |
| 🔴회계신호 | IT | 카카오 | [토스 재무제표 간단 분석 - 브런치](https://news.google.com/rss/articles/CBMiTkFVX3lxTE5ISHpzQXZzNnJmb1A1ZWlFeGlFYzBBTlRhYXBkeFJ1WU1vamtEemhuVjhvaUpFbHp0R01wN051WnRTWDdiZmRXZ0MxeDNPdw?oc=5) | - | 브런치 |
| 🔴회계신호 | IT | 두나무 | [두나무, 美 회계기준 검토 …“아직 결정된 바 없어” - 전자신문](https://news.google.com/rss/articles/CBMiTkFVX3lxTE5HZTFwRHZlQ19keGRBM3pQYkk2THNlZjNKRzFmRjNnMV83OFRyLUQ4elVxV2M4ZUV5eTJTSFdleEZtZUNORTVpc1NNTU1iZw?oc=5) | - | 전자신문 |
| 🔴회계신호 | IT | 두나무 | [두나무 "美 회계기준 검토…주식교환 마치면 IPO" - 비즈워치](https://news.google.com/rss/articles/CBMiakFVX3lxTE5XdU00TXFrTEJLcHI4RFFYcjVUMlIzV1VuVUVrSzFIcGwtdGVvc2pkQzJDOFgtTzlDZnVLNUxFM01ZNUNZVlNUUWNZV3cyTnYtZ3VqMkFyVEdTaGV4dUZoOGpMNndodC1Zd3c?oc=5) | - | 비즈워치 |
| 🔴회계신호 | IT | 두나무 | [美 회계기준 문의한 두나무, 나스닥 상장說에 "정해진 바 없어" - 아시아경](https://news.google.com/rss/articles/CBMiYEFVX3lxTFB0MmlXbEZMR0dPcGJEU29yX2tSd2UyeG1zdlNHRWZwOGp6SkdDZWl2eDNBc29rQlZlOEpNMEdPVFI3QWNGNWRBZnpGQTRhQThXRW9NazdHa0VpdlI2Q1UtYg?oc=5) | - | 아시아경제 |
| 🔴회계신호 | IT | 두나무 | [두나무 美 상장설 다시 고개…“회계기준·행선지 결정 안 돼” - 이투데이](https://news.google.com/rss/articles/CBMiVEFVX3lxTE5rR0JabEc4RWVrazRoMUIxOWlwb2h6NzI1VjFzWUI3MnFRbThXcnRlbl8yNk13TVBzZXVMLVpNR2hLdWNwWHktYnpQSFNtX3ZqWGFwZw?oc=5) | - | 이투데이 |
| 🔴회계신호 | IT | 두나무 | [‘美 회계기준 전환’ 나스닥 상장설 솔솔…두나무 “사실 아냐, 상장국가 미정](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9OUmZtcHhBTExGamNBUDhBVXVkUEk2TzBCRjBTbmJhTXF4TEVZVGhraGNmUWZHVWl3SXlEN3Q1NTJxN1AzSGdHOGhtWjZKTDd5cS1uQ092b0pCN3FaRTJaYUdDNVJWQ1U?oc=5) | - | 디지털데일리 |
| 🔴회계신호 | IT | 두나무 | [‘445억 해킹’ 두나무 제재 돌입…금감원, 감사의견서 발송 - 데일리안](https://news.google.com/rss/articles/CBMigwJBVV95cUxQdjlHNElLRGJXMFBlQ2RTM3pDM1FJbTk1LTJrQ3lUbkdMQlI5Y2JNTjQwcmRST3A4RXlPeXlRanJpdFBKbXh4Z3JyWGk3QWxqY2ktLThTRDk3V0pTT3hua1JWV1NoRW4yMUctUXNNT2JMbkF2Tm1qVXl2YkNEeWUwSXhKemkwenhFbWsxbEUwb3pGa0hJR1N3U29JZVhhakFXVkxSRjZta1puN1ZKeTA2VW5ma3Nqa1JCYnhtd00tUXIyRGJGdm5TNGxBaTdaaEhtTFpkczRVSnAtY3hWaDRNNnZvc1RfZVZlZjV4enhvYUtXYkFrZllDZjd3QWVRMWhGYkg4?oc=5) | - | 데일리안 |
| 🔵회계이슈 | 엔터 | 하이브 | [하이브, 역대 최대 실적에도 M&A는 ‘마이너스’… 1조원대 영업권도 부담 ](https://news.google.com/rss/articles/CBMicEFVX3lxTE1EclZkd2RpcVphX0ZoLUh2SHpodTZEZlBUazZxVTVfSWlXcWNQbXJKOHF0MUQ1MVcxc2puQlVOUV9zUjZlZDIzOEg2MmRFSmYyZ0V3cWlLaEtOSlV4QVA4NTRBUEgzVGNzX01BTnBXbW3SAXRBVV95cUxQNFZxR3lGNmx5Z0FHVlVOZjdEd0N2Yk1jaVNLem5zMHJWWmhpcFE0N1F3b3BZTXNyZTRIeU1CS0VNbGJ1cWdQWDZuUzM2cHlNWXRxS3NqYmRWalQ1cTJYM2FOWDVDa0hQNkhvd3lVTkI1alczVg?oc=5) | intangible-assets | IT조선 |
| 🔵회계이슈 | 엔터 | 와이지엔터테인먼트 | [빅뱅, 데뷔 20주년 신곡 'BiiiG' 음원 차트 석권… 월드투어 포문 -](https://news.google.com/rss/articles/CBMiaEFVX3lxTE9KUlZoa2Y2VEYtY29HcGpjSjBiN1B1SW5GbTl4X2h3R3V4dndpYVdvamNjVktxRkN0RHdUZmpYMWhUcTdLckt5RXhMX0pzaUQwSTJlR184OWlwakJ1ZTZwT2dkUUpsOHhf0gFuQVVfeXFMT2E4RF83Q1ZNMjZPVTk1N1ByYmhsOEdUTnFxcHNnRFJ3cHloSGZ2aTh4M0VlT1ByV2t6TC01dll1azRmY3FxckVyWXhLemkyd2t5RDFGdTRKYWVPeTZWS0pKeThPR0E4aVFHMlJFanc?oc=5) | intangible-assets | 머니투데이 |
| 🔵회계이슈 | 미디어 | 스튜디오드래곤 | [[스튜디오드래곤 톺아보기] 판권 상각기준 전격 변경…'수익·비용 매치' 변동](https://news.google.com/rss/articles/CBMijwFBVV95cUxOeWRaSDJiY0JzY0l6SXlzMGtRVmdaYjZncDdubVBfUjlaNldjS081VlZicUM2UXRsXzVKbTZpdVlnb2xRa1JyNnY1cmxEaFNKQUNuZkZqRXppV2pSYW9iMFVsaFhHcHBzRHNZZmVVNm5hMjNtdTE2a3VsT21qam9YYU5uREpJOG1HQmdLR25Xaw?oc=5) | intangible-assets | Naver Blog |
| 🔵회계이슈 | IT | 카카오 | [[IB토마토]차바이오그룹, 카카오헬스 품었지만…CB·영업권 부담 '먼저' -](https://news.google.com/rss/articles/CBMiYEFVX3lxTE5oR2RicWlCR1pLcWtHNVVpY3Q2SGV0aERvc09adlVyajl2WkhibUNRMFVZV3FnUUZOUFJCTzFrS0JzZ2R0S2RpSHJLMUg3UEM1SVZXanh2V0dhYkhKSjE4RQ?oc=5) | intangible-assets | 뉴스토마토 |
| 🔵회계이슈 | IT | 컬리 | [네이버-컬리 '컬리N마트' 1년 만에 거래액 10배 성장 - 뉴스핌](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBVbjZjRDdTRGRtaHVNTHpMV19lR1MyRGxELWFDekJFOHQ2UUdLRFZkc2RhTTVhems2LTJGRjNXMDREUHltOGotUWFBX1AxQWRCYjNPc1haR0F1OHN6?oc=5) | platform-cases | 뉴스핌 |
| 🔵회계이슈 | IT | 컬리 | [‘네이버와 컬리의 성공 만남’…‘컬리N마트’ 월 거래액 1년 만에10배로 -](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5PRHFIeGV3Y094amt3Q0NSWjFad2txejVGNFhBVUg1cWVhZF9CY3ZQQVBzV0NUNFdWR0ZjamViaklYT1JmZGdHX2hQYXQ4NUlnUmlRaXNvOEJxQQ?oc=5) | platform-cases | 농민신문 |
| 🔵회계이슈 | IT | 컬리 | [네이버서 통했다…컬리N마트, 1년 만에 거래액 10배 - 서울경제TV](https://news.google.com/rss/articles/CBMiZEFVX3lxTE5YbnNTLVJ1dFNVTjJaYU9rZE9uQ0I1Z2x5RmtRY1pOWWRJRWdpcEhWUElrUjFJMG9NVERyay1MYnMzcGs4cmYzdlFYYUprY203TktYQnNXZTY2SUlja2szMENURks?oc=5) | platform-cases | 서울경제TV |
| 🔵회계이슈 | IT | 컬리 | [네이버와 장보기 ‘시너지’…컬리N마트 거래액, 1년 새 10배 성장 - 서울](https://news.google.com/rss/articles/CBMiUkFVX3lxTE9mdXJkQnNOZloydUFqMXVOSWluZXM4UVNDcUNiczJhNXc1bjRTclZObDZCYTdHdExfY2Jwc0FQUUNySFFlZnoyalNtLTdUd3lCV2fSAVNBVV95cUxOQmxjN0t1a1FkbFJWZHM0RXdCaGdZSGh0eEx2TXZQckRlZndibnlqXzZxSlUtZDdSNHFTNlpnWTM5NmlKaHM4QkhpM0VWanctdGJGUQ?oc=5) | platform-cases | 서울경제 |
| 🔵회계이슈 | IT | 컬리 | [네이버-컬리 온라인 장보기, 출시 1년 만에 거래액 10배 - 뉴스1](https://news.google.com/rss/articles/CBMiaEFVX3lxTE5uUWFJNEpOSGJ4ZjM5VVNuLVNtWWlpVTJzRkhXd2E5OWlHc1RtekFxcTBSTnUwdmhXa0RnYTYyOFpHSmdLLUV6SDRHYzc5VmdxY20xLUtwMEpMQXdkNGdwY0lFdEFub0lE0gFuQVVfeXFMUFBGcl8yX1dpR0FxS0F0T0h3Y05uUm5WengyRkQ0UnNXdFBqRWZqTktZUHFfTU5rcHJtRDN1R3l0RjBqU0llSVVfUjU3WUpZTGdabzFzdnltTWFVYkxXS3BnUDBiU1NfdDloRXc1R1E?oc=5) | platform-cases | 뉴스1 |
| 🔵회계이슈 | IT | 컬리 | [컬리N마트, 장보기 '단골' 잡으며 출시 1년 만에 거래액 10배 성장 - ](https://news.google.com/rss/articles/CBMickFVX3lxTE9BaTJ4bEVTRWRCSW9zRTVPc2hLZ0xmZFNqbG5VdC1pQWVfWG92Yk9CM0swTlRhS25SS2RQRlBvbUJNbTZXZmRjS1ExeFFpbERPVXloMGFLVHZUNUotVWxJTEVDUGY2SDJyU1lET1JOSWt6QQ?oc=5) | platform-cases | NAVERCorp. |
| 일반 | 게임 | 넷마블 | [도시 지키는 소녀, 넷마블 서브컬처 '펄 인 블루' 영상 공개 - 게임메카](https://news.google.com/rss/articles/CBMiWEFVX3lxTE5kRlVybE9xaGh0RWJGTE5KYTZMclhJbVBnZksyN3BCSVhoRmtTT1duSmNzQ1JBVWxBbHFlZlIydHh3ZEdMUFU5NzBaSURERTlZRV81THpMNmLSAVtBVV95cUxPa0FwSTRrc3dBeGFpeXNwakpETjhaeklSZ3RaWUZEc1duUG9aZVE0LWt4NU1KRk11RGJRd0xGcENKQm1pd21lR01GcEZEZXpYem1mX0hVYXpLRnFn?oc=5) | - | 게임메카 |
| 일반 | 게임 | 넷마블 | [넷마블 게임박물관:카지노 커뮤니티 - Platea Magazine](https://news.google.com/rss/articles/CBMiWkFVX3lxTE41M29xQXBYQURIdEZLM0NYa2dqUng2S043UGdhb0p4YUV6Q0czVmlLRXhlQTByX0tWYXBVdXZNWUhJZURCUFVneTBPNFdRQjJORG9iczhSZWxVdw?oc=5) | - | Platea Magazine |
| 일반 | 게임 | 넷마블 | [넷마블 '몬길' 개발기, TA가 서브컬처 감성을 살린 법 - 게임뷰](https://news.google.com/rss/articles/CBMiakFVX3lxTE9fN3VLSDM3eW9oTURfa0Q1Z1hTZEI0Rkxxcm1LNG1JQ0NKb3lQN3c2NlJKTUpMWDhtUnBtcHRfX09wdDMyZVlDZjllVTZtZlY5RzJfbDVyZTlUa09XeHVyOTRVQXRUaEJhemc?oc=5) | - | 게임뷰 |
| 일반 | 게임 | 넷마블 | [넷마블몬스터 "中 물량 공세 맞설 K-서브컬처 무기는 캐릭터" - v.dau](https://news.google.com/rss/articles/CBMiRkFVX3lxTE53ZlpxNG85Z19SVmNrd24zYVlrTEpSQjVPVjBTVEYxLVJrNFAtMENobXcxam1FdnB5Z0ZxYndXbU0xUnlQdkE?oc=5) | - | v.daum.net |
| 일반 | 게임 | 넷마블 | [방준혁 넷마블 의장, 텐센트 보유 지분 13.4% 인수 - 연합뉴스](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBIbEhXYkc3Y25KRGRWQjVHVndJM3d0a2x0eGotaTJYdkpyeUl3dUdOQ3FJSXJxRmpONXZVWXlVSWtpQV85cWoxVS1RMkFiaGpXY2ZPUlRwUU1CRVXSAWBBVV95cUxOVWhjOFhCQ0FXZV9menVwdGdoSnlmQWNwcTNIRjhrZmd1ckxtUy1SQzRJQV9ldTFJQUJyTWtucjUxLWtjUzNVSWdxZVZmUzNzWkhGWDdSQlRsUk9kN1ZMOWk?oc=5) | - | 연합뉴스 |
| 일반 | 게임 | 엔씨소프트 | [토토 3플3 비타임|폴드4 카메라 성능 - Platea Magazine](https://news.google.com/rss/articles/CBMiZEFVX3lxTE5ZM0ZiQnZVSUJkcDVvcFhqRURjeHBIcHVQV3g5QnU4N0ZfQWFuVTRBMU9ocXZxNGUxVFVWemRJZXNSZzl0NkxiMmJIMWE4X3BXdUEzMXZiODNHOWQ3bkllQjVGRkY?oc=5) | - | Platea Magazine |
| 일반 | 게임 | 엔씨소프트 | [엔씨소프트 노조 “그룹 통합교섭, 기업 경험과 기술 지키는 경쟁력” - 로리](https://news.google.com/rss/articles/CBMibEFVX3lxTE13Q1BjWGVwaUpSMmpuTkZLaXVPSURKR3VBTWNMTXRRMVRjbUVTMkl4OGF6bTlkMEk3aEVra1pGazBZRV9sVnJRS0J6dEFNUklIX2R2cW5LR1FDZjRLdlppcnVEWXBqTzJoMUJaNdIBcEFVX3lxTE9pR0c1LWNqNU1tVkJvTG9Jcl9xUGJmdHBEbkxkS0tYYzNwV1JXSGhkU1d5aFRPZE5IZEhVUEFtbDE2Y3k1OWFWWDRoMnNKTU84dXcwNEI0R0FpM1A5QzdzNWVSVmpfTzBJRTRmN3RBenQ?oc=5) | - | 로리더 |
| 일반 | 게임 | 엔씨소프트 | [1,739억원으로 돌아온 엔씨…‘리니지 회사’의 부활인가, 체질 개선의 첫 ](https://news.google.com/rss/articles/CBMiaEFVX3lxTE84TUVJZ2dXXzBWZUR1aE5QVmwxZEUxV1BBcXFMMmNlRnBkNFhHeGdubm9CRF8wWkZMenJFcUpCZ3BaV0NXNkx3NGs5djVVWmFwOTd6WTg1T3JDblJ3VmVGMF9HMEx3dHMx?oc=5) | - | 시사프리즘 |
| 일반 | 게임 | 엔씨소프트 | [엔씨 "모바일 캐주얼 지속 성장…내년까지 신작 10종 출시"(종합2보) - ](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9yRkpINUp5WFVxX3pYTnRnQTRNS2tOMERaYXlOblRibU9MM1BabjN3WW56VTVxaFFIMm1pM3cyM3pIbXY2QW84YXhDNTktdjBzb1JSLXlvYXc1VWPSAWBBVV95cUxPb0JSdTNzd2lEUmxGcWJLV3J2WDloZC1LdXd3aVZ3dkFkQUxUVlBtenRFbEJucFl3UlZZeFJNa2lETTI0akhsQndRYkpMVmlrMEVucjE2VVRfTzZtb1Z4VVc?oc=5) | - | 연합뉴스 |
| 일반 | 게임 | 엔씨소프트 | [네오위즈·엔씨소프트, 엇갈린 2026 전략… IP 확장과 아이온2 승부 - ](https://news.google.com/rss/articles/CBMiVEFVX3lxTE5nODZSOHdVS2NVYXgtWl90V2k5ZmF0Nm9nekxoc3dkaUY5MFd2WXpxTDJOTk5Na09uY25mYjFUR1JILTFmZGo3NTdUNlhkZmNDakZ4ag?oc=5) | - | :: 위즈경제 :: |
| 일반 | 게임 | 크래프톤 | [[게임스컴 2026] 배그가 배틀로얄을 버렸다... 크래프톤의 실험 - 게임](https://news.google.com/rss/articles/CBMiZkFVX3lxTFBvNkdGS2pBSGs0QllnQnJPcXFaV0JycXFid1F1dVpJNmtrd0RWSUtBakI3enNxWDlCN2hlb0oxVHRWRlJCQlo4anF0OWpmaGtTWHpvelFGd04tT0RJQmRDYS1kZmpXUdIBakFVX3lxTE5vT3A2c3ZDSmpKQzhYS3hsUFFiWXc2dFdiQ1hDTTZ5X1JRYmR3bUJkbEJ4SW1Pc2hYYlZZc1dFbnNPem02ekNwX29tbS1XOGVndEtkQUhkSkc4ZERmUWxwYWpqMzg0N2l2Y1E?oc=5) | - | 게임와이 |
| 일반 | 게임 | 크래프톤 | [5민랩, 신작 ‘세계허구관리연맹: WPCA’ 첫 공식 트레일러 공개 - 크래](https://news.google.com/rss/articles/CBMiswJBVV95cUxNejhMcTVvRDAzSkFweGlNVURXaFpvT21iWHM3WnFvdlhOY09aSjJzTERTZktCQnZ3ZjY1VGJXUzlXV1d4Q29wU3k3MzRZSGd6c21lWWxzU3lLdW02aGl4WmFqNnlPeEFYYjA2a0lVcFZNZ2w3UnV5QmdPa1VETHZxT1V5XzlrSWFZdm5uOTVFbVJacW5uR0F5T25HY3hBYlBmWTI5dnYwMkppbWVKd3BfZ2J4Tm9DU29nWEpDdUlrM0FCVWpETWtMQ1JDNE52dEZfd3pFSXUzMUN0Q1Zvc0ZVRUpqakV1a3M3YmV6dWFpS015eU5VVV9RS3BUQmM0X2tGU3RVQ0UyZUFJdUN3Mnl3dF92THEwVE5SLUVTdzFYbllPLXNDTGplZU15NjE2X2EyZ21n?oc=5) | - | 크래프톤 |
| 일반 | 게임 | 크래프톤 | [크래프톤, '배틀그라운드 다음' 찾는다... 신작 5종으로 IP 확장 승부수](https://news.google.com/rss/articles/CBMiTkFVX3lxTE5pbDBTaU4zdTlkTVB4ci1ja0RBMXk4a0hqMmY2cWFhZnNiQzZtdnhwSkRWdGlDWHBpbzBxUmlNWEh2LXNhMDhLTW9UYTRYUQ?oc=5) | - | 전자신문 |
| 일반 | 게임 | 크래프톤 | [크래프톤 장태석 총괄 "팬에 오랫동안 사랑받는 게임사 되겠다" - 연합뉴스](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBBRHN3d2NZZXRLc2VVZ1NkYTRTeDUxSEd4Tl9qYUFaVGhCTUUyNXp6TkdERkhVMEJXQ0V1UzBRbFdaRW9pUmxLRENaZmUtOFFIUVN5dWpObF9pcU3SAWBBVV95cUxOaVJZbVAzUUxIN3ctcjY4MXpNazJrTXI0eTZhM2R4aTZWMjB4QXllVzZ5X1p5WVRSblV6NGppSGRQOEtTblAxdGNQTDNHWmNxT2RBZUU3V2FQV1k5MHVGMkM?oc=5) | - | 연합뉴스 |
| 일반 | 게임 | 크래프톤 | [크래프톤, `배그 모바일` 아시안게임 국가대표 평가전 개최…5일부터 온라인 ](https://news.google.com/rss/articles/CBMiZEFVX3lxTE9GbWZhRjZjV0lMQlZLV0hYb3Z2WFY1TWRpQWhjdGpDYzRJNjd5dHBSN2ROOGd4RGFIMFBaQnU5bGxSd3M1Q0JMd05rX0UxNVBQNGJINXZ3RHA1NTV6Tkh0blZLMi0?oc=5) | - | 디지털데일리 |
| 일반 | 게임 | 펄어비스 | [“하이닉스 욕할 게 아니다” “역대 최악 기업” ‘석 달’ 만에 ‘–40%’](https://news.google.com/rss/articles/CBMiRkFVX3lxTE9lWkxwRFBSLVdJOWxVVWtXb3ZCMUhac01TM2pvX3FzQjIxRjhvbFJISFpMVmRHVm44YkotdDdQa3k2VWFTaHc?oc=5) | - | v.daum.net |
| 일반 | 게임 | 펄어비스 | [펄어비스, ‘붉은사막 인핸스드’ 첫 DLC ‘미지의 여정’ 10월 16일 출](https://news.google.com/rss/articles/CBMiZEFVX3lxTE96R0R3c2UxRlFGS2dzNU9aam8ybnFMdE8wWWpSb082MFZrb1FKbVRBME1ud1JMeW9VRTVjdmVPLUQxOGZXYXljTHR2TXpndzRQbWdwckFXV3M5MHNIS0tyN3RYZU0?oc=5) | - | Pearl Abyss |
| 일반 | 게임 | 펄어비스 | [600만장 흥행 뒤 찾아온 ‘신작 절벽’…펄어비스 주가 휘청 - 한국경제](https://news.google.com/rss/articles/CBMiWkFVX3lxTE4yUUZjZU1fdnkyNlJ5V2c4Tm1OdUhXM0dIT29OS1Zxd2E5UUswNkhMMWtaajlJRkIxMkVKaWpoX2Z6ZVVrSWl2a1pkTGdSUUpxVjNpNWJSR2JkZw?oc=5) | - | 한국경제 |
| 일반 | 게임 | 펄어비스 | [‘어닝쇼크’ 펄어비스에 日 노무라 “목표가 59% 하향” - 매일경제 마켓](https://news.google.com/rss/articles/CBMiUkFVX3lxTE1KV2JBZzlBWEJLU0FqUllzOGNmNHlzazNqbmFCcGtRTlNWQkwzMVUyLXRxeDVhOEtYRXo1NmtlNnFTdUpBTmUwYmVSQWhGVy05dEE?oc=5) | - | 매일경제 마켓 |
| 일반 | 게임 | 펄어비스 | [[특징주] 펄어비스, 기대치 밑돈 2분기 실적에 14%대 급락 마감(종합) ](https://news.google.com/rss/articles/CBMiW0FVX3lxTE81NWttUEpmSi1QTzVtX2Z1VmVRbEVkRHp5VFRhTXZjM05tYnMwWHdBdkJMeHhHbTh5XzQ0UWt0Q1pBTklvREJ0QlNET0Q5YmRLRFE2MmgwaWctSDTSAWBBVV95cUxQQUFEY0UyOC1mZHdQS2F4VFBLUlAtWnBHNWxiTlAzLVpRRzdJNVgtUXl0TzhBcmFVS1ZPaEdPdlAtTVNDZnpfSXNlOHo0TXVkSUZtemhEbWEyT2ZzYWh5WnA?oc=5) | - | 연합뉴스 |

### 🏢 회계법인 산업 리포트
**최근 수집된 발간물**

| 법인 | 리포트 |
|---|---|
| 삼정KPMG | [AI가 뒤흔든 콘텐츠 산업의 지형과 성장 전략](https://kpmg.com/kr/ko/insights/eri/2026/issuemonitor-0528.html) |
| EY한영 | [통신사는 어떻게 B2B 성장 전망을 재정의 할 수 있을까요?](https://www.ey.com/ko_kr/insights/telecommunications/reimagining-industry-futures-study-2026) |

**TMT 인사이트 허브** (상시 링크)

| 법인 | 페이지 |
|---|---|
| 삼일PwC | [IT·플랫폼 산업 (Software·AI·E-commerce)](https://www.pwc.com/kr/ko/industry/it-platform.html) |
| 삼일PwC | [Industry Focus (산업별 보고서)](https://www.pwc.com/kr/ko/insights/industry-focus.html) |
| 삼정KPMG | [경제연구원 이슈모니터 (콘텐츠·미디어·게임)](https://kpmg.com/kr/ko/insights/eri.html) |
| 딜로이트 | [첨단기술·미디어·통신(TMT) 부문](https://www.deloitte.com/kr/ko/Industries/tmt.html) |
| 딜로이트 | [통신·미디어·엔터테인먼트 산업](https://www.deloitte.com/kr/ko/Industries/telecom-media-entertainment.html) |
| EY한영 | [EY Korea Insights](https://www.ey.com/ko_kr/insights) |

<!--RADAR:END-->

---
_본 리포지토리는 학습·포트폴리오 목적의 공개 정보 정리이며, 투자 자문이나 감사 의견이 아닙니다._
