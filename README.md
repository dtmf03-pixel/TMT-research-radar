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
_최종 갱신: 2026-09-28 10:34 KST_

**수집 현황** — DART 공시 157 · 뉴스 335 · 회계법인 리포트 1

### 📄 DART 공시 (회계 이슈 필터)
_종류별: 실적 72 · 📘정기 54 · 🔴정정 13 · 🟡주요사항 18_

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
| 🟡주요사항 | 게임 | 시프트업 | 20260910 | [주요사항보고서(자기주식취득신탁계약해지결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260910000386) |
| 🟡주요사항 | 통신 | 케이티 | 20260909 | [주요사항보고서(자기주식취득신탁계약해지결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260909000349) |
| 🟡주요사항 | 통신 | 에스케이브로드밴드 | 20260827 | [주요사항보고서(회사분할결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260827001001) |
| 🟡주요사항 | 통신 | 에스케이텔레콤 | 20260827 | [주요사항보고서(자기주식처분결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260827000390) |
| 🟡주요사항 | 엔터 | 하이브 | 20260825 | [주요사항보고서(자기주식처분결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260825000350) |
| 🟡주요사항 | IT | 카카오 | 20260821 | [주요사항보고서(회사합병결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260821000052) |
| 🟡주요사항 | IT | 카카오 | 20260821 | [주요사항보고서(회사분할결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260821000047) |
| 🟡주요사항 | IT | 무신사 | 20260813 | [주요사항보고서(자기주식처분결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260813001369) |
| 🟡주요사항 | 게임 | 네오위즈 | 20260812 | [주요사항보고서(자기주식취득신탁계약체결결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260812000035) |
| 🟡주요사항 | 미디어 | 나스미디어 | 20260806 | [주요사항보고서(자기주식취득신탁계약해지결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260806000438) |
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
_구분: 🔴회계신호 15 · 🔵회계이슈 9 · 일반 311_

| 구분 | 업종 | 기업 | 기사 | 회계토픽 | 출처 |
|---|---|---|---|---|---|
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권 피해자 대리인단, 금감원에 감리 요청 - 법률신문](https://news.google.com/rss/articles/CBMibkFVX3lxTFB4OEZyLVFxM2lFejNpZm5vRmgwNDAzeWh5TElpVEpxNFhWZ3FJRndLTk5fTF9kWGE0aUdrTjM3S0lCamZ2V3Y4TE03LUNSTmpfTHZsaXROZ1JJeEYzaC1jek9ZRTZudnU2dWRORFdR0gFyQVVfeXFMTlJuUTUzcVYwLTIyMWhZWnFRYVBNc2FPU251QVYyU0V2cXUzU2RvV3RlTS1PMWVXeVNvNElNOTIwWnhXcXRrV1pKdURYZHo5emlVcWR0cC1tc0kxTUlZSVZ0TFBKSGxCUmZDNndnZGg4ZHNR?oc=5) | - | 법률신문 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권투자자들, 금감원에 감리 요구…"회계처리 의문" - 연합뉴스](https://news.google.com/rss/articles/CBMiW0FVX3lxTFB1Ukx0THpTTk1DSVh2VGtQU2hsZTBuZWhlRWhzLUFKNGY0dm1RZkgwdDIxMXdaTzhkTXozUXltRTlOS2VOZ25SdGlfLVY1WVhsYUVfWmMxTERDUmvSAWBBVV95cUxQRDRMM1RQYmYwcGlUY1o2YmZfWTNKQlRDU2JkTmxWNnFlVEs4cTFCOElOR1MyUjhyb0twN18zMkNINldZOE1ZSTNKVVJWdmRDOFZ4S2M2OTVoVHVaWDRHUHo?oc=5) | - | 연합뉴스 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [“돌려막기로 자본잠식 숨겼나”…중앙그룹 채권투자 피해자들, 감리 요구 - 한](https://news.google.com/rss/articles/CBMickFVX3lxTFBDSS1uQk52SXBhb1kycHJkNU5na0w1cmtyUm1hSW5KM2YtQkZWUy1TYlVfT2F5NHhUdElibTdhaExkblFZWExucFBXeVRpM1FkcTNvdm41dHpaODZEVzhScldkQ2FwTnRjZmJWTll0Z3p6dw?oc=5) | - | 한겨레 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 투자자들 “회계처리 의문”… 금감원에 감리 요청 - v.daum.n](https://news.google.com/rss/articles/CBMiVEFVX3lxTE1fS1hlUE9VYWpjdnRpb2JiTGxsVjJpUHNDZV9lQ1hmUVBkUDg3SVpBTjdiVG56R0w1OVlKT1VtVS1mbkZRRkkwSUR1cEpCeHFrSXRKRw?oc=5) | - | v.daum.net |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권투자자들, 금감원에 감리 요구…"JTBC 등 회계처리 조사" -](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9USmdOS04yVzNFQUhINmFtemVYdjhqYkpJYmN6TnlYMU9mdXQxWGtRQTVmek5kMXpZbjNOZ2kydEJWbFVzaGlZQS1vbUhJUmxDWkc0N3dZLVd1c2VhTURv?oc=5) | - | 조세일보 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권 피해자들, 금감원에 JTBC 등 회계감리 요구 - 뉴스핌](https://news.google.com/rss/articles/CBMiXEFVX3lxTE5udHFnRVZpejlOOVNLQmRVVERsNkxrUmRBckhHS0p3cmZkUkZ1WlcxMXlyR3loRktZOGRaaU1WX3RxYUdldkpReVlkV25ZUy1uVkg0MDJhZFhsZWcz?oc=5) | - | 뉴스핌 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권 투자자 금감원에 감리 요구 - 조선비즈 - Chosunbiz](https://news.google.com/rss/articles/CBMigwFBVV95cUxOZ1BZZWVoNlItVU8zZTdWOTBmWVpncDBDUnMyenNPYUhNbWFDRDRlTjZpbzd6MnFxWHhzeWdmb01Jci1QRnN4UU83M0FmcHNTZ21HQmpxSF80WmxIMWRmcldCYmZhZUd4amk0bUtFazJnMVNOZklrZUp2ZjVPb2dFY2xJUdIBlwFBVV95cUxObmZVWHNYUEZEcU9BUUpKQXl1bmNJblA1ZkVvWlZ6bDExdWZkT2JWdFlnR3B0SGdBMWxQVmZrTUdzSlZiQ3FiV1pHU19FZ3M0WHlVMng2dDdpRW1ZUTRnalV3Ri1keE1rOHJVSkpHVUE3Y29jNzltSFNtZ0pOWUQ0OWJHOV9laHY3X2Z4WkdxZktNaHlzTWhn?oc=5) | - | Chosunbiz |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | ["재무제표 왜곡·우회 자본 순환 의혹"…중앙그룹 피해자들 검사 촉구 - 뉴스](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9TelEtWGVBbnNXSF9DQXhOQlVSRHdRRklJTWpISUVwNjJ3ZkI0XzZJcm42bEswT1I1ZURrOTlCWThKZExpakxBeEcwVjNWdmxDQ0hsSmJ0bG5SaXktVkE00gFkQVVfeXFMTVRqblZaVkV0Z0ZEWTJlRjJKYjh3WUd2aWJ0VDVGZTBsTnVQTlBqWUFXckM2Mm9IMm52MVNKQVpILUJfVXFMOTRFNGF3OTlsTFJ6TjE1cFI2N2FWWnp1a21LTF9kNw?oc=5) | - | 뉴스1 |
| 🔴회계신호 | IT | 네이버 | [두나무 美 상장설 다시 고개…“회계기준·행선지 결정 안 돼” - 이투데이](https://news.google.com/rss/articles/CBMiVEFVX3lxTE5rR0JabEc4RWVrazRoMUIxOWlwb2h6NzI1VjFzWUI3MnFRbThXcnRlbl8yNk13TVBzZXVMLVpNR2hLdWNwWHktYnpQSFNtX3ZqWGFwZw?oc=5) | - | 이투데이 |
| 🔴회계신호 | IT | 네이버 | [두나무 "美 회계기준 검토…주식교환 마치면 IPO" - news.bizwat](https://news.google.com/rss/articles/CBMiakFVX3lxTE5XdU00TXFrTEJLcHI4RFFYcjVUMlIzV1VuVUVrSzFIcGwtdGVvc2pkQzJDOFgtTzlDZnVLNUxFM01ZNUNZVlNUUWNZV3cyTnYtZ3VqMkFyVEdTaGV4dUZoOGpMNndodC1Zd3c?oc=5) | - | news.bizwatch.co.kr |
| 🔴회계신호 | IT | 네이버 | [[단독] 두나무, 美 SEC 위원장 면담, 회계기준 전환 완료...나스닥행 ](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPTE5PSW1ya182NWtnSDlMTmFrSkhvVC1xUmhPNG9zb3ZDZWd2RVVGalBvSFdmT0xMYUd3bWIxbkE1TkF3YVpPTWtxdlVZTUszdGExSTBNMFhBdkZaMkV3V2JpT196UXV0aDVFMmczaWpYbU5YVXpWbDd1Q1cxVmtEMWtfdzZ5WHZydGhB?oc=5) | - | 조선일보 |
| 🔴회계신호 | IT | 카카오 | [카카오 노조가 놓친 '새 회계기준 함정'…"내년엔 성과급 0원 될 수도" -](https://news.google.com/rss/articles/CBMiaEFVX3lxTE8yRnFCUUFIUzY3YTR1cDZqdmRVODJWd0pWT3E2SnNFQjBlTlpLZ0ZQQV90cTk3bldhRmdDUm1WVmN6WUZ5aDhrRjlWOXFYZzUwRzJhVktoejFha051VjRCUEVDb2x2UE1u?oc=5) | - | ebn.co.kr |
| 🔴회계신호 | IT | 카카오 | [토스 재무제표 간단 분석 - brunch.co.kr](https://news.google.com/rss/articles/CBMiTkFVX3lxTE5ISHpzQXZzNnJmb1A1ZWlFeGlFYzBBTlRhYXBkeFJ1WU1vamtEemhuVjhvaUpFbHp0R01wN051WnRTWDdiZmRXZ0MxeDNPdw?oc=5) | - | brunch.co.kr |
| 🔴회계신호 | IT | 두나무 | [‘445억 해킹’ 두나무 제재 돌입…금감원, 감사의견서 발송 - 데일리안](https://news.google.com/rss/articles/CBMigwJBVV95cUxQdjlHNElLRGJXMFBlQ2RTM3pDM1FJbTk1LTJrQ3lUbkdMQlI5Y2JNTjQwcmRST3A4RXlPeXlRanJpdFBKbXh4Z3JyWGk3QWxqY2ktLThTRDk3V0pTT3hua1JWV1NoRW4yMUctUXNNT2JMbkF2Tm1qVXl2YkNEeWUwSXhKemkwenhFbWsxbEUwb3pGa0hJR1N3U29JZVhhakFXVkxSRjZta1puN1ZKeTA2VW5ma3Nqa1JCYnhtd00tUXIyRGJGdm5TNGxBaTdaaEhtTFpkczRVSnAtY3hWaDRNNnZvc1RfZVZlZjV4enhvYUtXYkFrZllDZjd3QWVRMWhGYkg4?oc=5) | - | 데일리안 |
| 🔴회계신호 | IT | 더존비즈온 | [AI 거래관계망 신용평가 모형, 재무제표 한계 넘는다 - 전자신문](https://news.google.com/rss/articles/CBMiTkFVX3lxTFAyTXpadGpRZkN6M090ZElpTDFqQ1FHZEZnUERfcW43V1JQR2FGX0E0emRyNTFKZjB1V2tPWjJtQXJZa0M4WWFPOTNnTGxiQQ?oc=5) | - | 전자신문 |
| 🔵회계이슈 | 게임 | 크래프톤 | [크래프톤, M&A로 무형자산 6562억→1조8628억…성과 시험대 - 마이데](https://news.google.com/rss/articles/CBMiYEFVX3lxTE9EME14WWNpRi1UbFdsOUtHdDNsT2lZZ1hCQVpMZW4zWThESjR4TE1ka0NfNER1V2ZPSnhkbkpsbW95bmhTVjg5WUNBNmpZZVh0NVI3SzJwRzVic00tVFdURA?oc=5) | intangible-assets | 마이데일리 |
| 🔵회계이슈 | 게임 | 위메이드 | [위메이드 2분기 영업손실 210억 원... 라이선스 매출 제외로 적자 전환 ](https://news.google.com/rss/articles/CBMiaEFVX3lxTE1nZHF1TXVhVUNLRnVZVnpTUzdSZlBnZjhZRHZIU3owYl9RQjNUQkY2aDBicjFQa3hmLVlGbmlNaGJhVVEyRkVxa2NYeE1CZ0Nsc2hkWFJtTkVqcjI1c1kwU1djVXV4a3dM?oc=5) | intangible-assets | ipnn.co.kr |
| 🔵회계이슈 | 엔터 | 하이브 | [하이브, 역대 최대 실적에도 M&A는 ‘마이너스’… 1조원대 영업권도 부담 ](https://news.google.com/rss/articles/CBMicEFVX3lxTE1EclZkd2RpcVphX0ZoLUh2SHpodTZEZlBUazZxVTVfSWlXcWNQbXJKOHF0MUQ1MVcxc2puQlVOUV9zUjZlZDIzOEg2MmRFSmYyZ0V3cWlLaEtOSlV4QVA4NTRBUEgzVGNzX01BTnBXbW3SAXRBVV95cUxQNFZxR3lGNmx5Z0FHVlVOZjdEd0N2Yk1jaVNLem5zMHJWWmhpcFE0N1F3b3BZTXNyZTRIeU1CS0VNbGJ1cWdQWDZuUzM2cHlNWXRxS3NqYmRWalQ1cTJYM2FOWDVDa0hQNkhvd3lVTkI1alczVg?oc=5) | intangible-assets | IT조선 |
| 🔵회계이슈 | 엔터 | 큐브엔터 | [[더벨]큐브엔터 소연, 신곡 '퇴사할게여' 주요 음원차트 1위 - 머니투데이](https://news.google.com/rss/articles/CBMiaEFVX3lxTE5vMURKb1JiaGlzRTNyQXpycVZiMjVUTVFxbEM1WFAzVEdfZGtLRGZyTlFSUDZxdkpDZWZ1NklqNnZVVm1qQ3lVNVV3X2NtRDBPbmZZQ2xDbmY1T1ZWLS1sc0Y1SDF1ZjJK0gFuQVVfeXFMTWR5SUNMblBlb0dSUjRfMU1IbWc5OTNxUG1NaHhMTVVVd3dOZ3RxV0JNQUNOREVqLXMzRzV2Y09wNkV3cVI4QWZkSm82TjhqSWtGZk96Z3B6enFERnUxa01IaUFFdzg1UzNLZHR3UVE?oc=5) | intangible-assets | 머니투데이 |
| 🔵회계이슈 | 미디어 | 위지윅스튜디오 | [초상권 라이선스 시대 온다…AI 버추얼 프로덕션의 미래[AI 생존법] - v](https://news.google.com/rss/articles/CBMiS0FVX3lxTE1kWFh1M0VROG1fY0ZIanUxSXdfV0RZY2JpVUVqLXJmRUJIX1VxU29qXzBWOTdqY1NXZUxUcGFndTlLMzhVMjZpa0pHRQ?oc=5) | intangible-assets | v.daum.net |
| 🔵회계이슈 | 미디어 | 스튜디오드래곤 | [[스튜디오드래곤 톺아보기] 판권 상각기준 전격 변경…'수익·비용 매치' 변동](https://news.google.com/rss/articles/CBMiT0FVX3lxTE9QU0VkMFAzbnhsQnl6amZPVTZYbUtabUVibF9FbmFlNXpLWnRJa0RneFJSNmE5T08xSGtOVFRGS1lpYzRweHdYSGdrUkhYWms?oc=5) | intangible-assets | 딜사이트 |
| 🔵회계이슈 | 미디어 | 스튜디오드래곤 | [[스튜디오드래곤 톺아보기] 판권 상각기준 전격 변경…'수익·비용 매치' 변동](https://news.google.com/rss/articles/CBMijwFBVV95cUxOeWRaSDJiY0JzY0l6SXlzMGtRVmdaYjZncDdubVBfUjlaNldjS081VlZicUM2UXRsXzVKbTZpdVlnb2xRa1JyNnY1cmxEaFNKQUNuZkZqRXppV2pSYW9iMFVsaFhHcHBzRHNZZmVVNm5hMjNtdTE2a3VsT21qam9YYU5uREpJOG1HQmdLR25Xaw?oc=5) | intangible-assets | Naver Blog |
| 🔵회계이슈 | IT | 카페24 | [카페24, 2분기 거래액 역대 최대…공격적 투자에 영업익은 27%↓ - 디지](https://news.google.com/rss/articles/CBMiYkFVX3lxTE9zQllFX284RGRhUFBRMnFWdnc4UVNEUXVVMjJsLUpXMnpLZHlMSUFESHBBX0xrTEJMNUNEUnFlRFR6Nl9ydjJyZVJxSFJkNHV1V0tVY2NlUXVPck1fenQ0OW5B?oc=5) | platform-cases | 디지털데일리 |
| 🔵회계이슈 | IT | 컬리 | [‘네이버와 컬리의 성공 만남’…‘컬리N마트’ 월 거래액 1년 만에10배로 -](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5PRHFIeGV3Y094amt3Q0NSWjFad2txejVGNFhBVUg1cWVhZF9CY3ZQQVBzV0NUNFdWR0ZjamViaklYT1JmZGdHX2hQYXQ4NUlnUmlRaXNvOEJxQQ?oc=5) | platform-cases | 농민신문 |
| 일반 | 게임 | 넷마블 | [넷마블 '몬길: 스타 다이브' 등 게임 3종…'올해의 우수게임' 수상 - 머](https://news.google.com/rss/articles/CBMiZ0FVX3lxTFA2ZmNJcV95N09UWERxSlNLQ0ZiVm8yNGlMTEpWWFBQeHNsbGRUNlJSR1EwTDl0em1UWGRYV3FIMzljVlBuM25vWGo3LXA3azNpVjdaU2ZRdXJISU50M3QxM0NnR2kycHfSAWxBVV95cUxONFFKU28zMTVmXzZzSGhySGluSlBmUmttakdhMnQtQjhWNkdYRU11dXJqTElHaDJiU095YnNIV1VWNURVblE2LU5OSjc2SlRxRGNmX0N3b2h5MDlscExyS3JQbVJsMVVMNy1Cb3M?oc=5) | - | 머니투데이 |
| 일반 | 게임 | 넷마블 | [넷마블 '하이브 주가 급락'에 지분가치 줄어, 김병규 투자금 조달 위해 비핵](https://news.google.com/rss/articles/CBMic0FVX3lxTFBINWVNbWVfRi1GYzlNTDRpOWFMN0dUNlNtZ2FHLVAzblBiTGFNQ2dnQmFWNEZjRXhQbXVUWGpEYmtLV0ZYdFNDYi1LbDZQbGdUaElBSExaRDhFYm9wRlpETWdkRG9oWFhsZjdOeTZVZktLMDA?oc=5) | - | 비즈니스포스트 |
| 일반 | 게임 | 넷마블 | [도쿄게임쇼 찾은 넷마블 방준혁 “지스타 참가, 당연”... 내년 복귀 시사[](https://news.google.com/rss/articles/CBMiTkFVX3lxTE5MV1pXS1RJYjhDSmIydU5KUDVEdUptQmJWNGVYYTFSZUh4TDhzaGoyNkhIRGxocUV5VkNBaGM4aEMxdWkyTkRlMzFuMUhwZw?oc=5) | - | 전자신문 |
| 일반 | 게임 | 넷마블 | [“日 검증 더욱 철저하게”…넷마블의 ‘절치부심’ - v.daum.net](https://news.google.com/rss/articles/CBMiT0FVX3lxTE5vTUNocHZSZFV6akRhTmRrRWRLRGxSYV9Kc1Vxek5qT1BwWFdyR3AxRVFQamJYZmkydmdXWGx1SU1qR0ZLQlZlcnZWWkVoVE0?oc=5) | - | v.daum.net |
| 일반 | 게임 | 넷마블 | [넷마블, 신작 3종으로 ‘TGS 2026’ 공략···일본 게이머 호응 - k](https://news.google.com/rss/articles/CBMiWkFVX3lxTE50NnJpc0NKdG5wWkgyYTF2c2QxamF3dnc5RWtycVFWaG9tdGVKNlcyaFpvRFM0cVpBaldqZF9sWGpNX0tIZVVuMFRWdlhLalFtdXhIME1sTTNVUdIBX0FVX3lxTE11SmplRjEyQm9oeW9NU0YteXAxOVVUMTZLUVlXRkhSa1R6ejE1a0UtRXpNQm54Ull4cUhiTU4wYWZ1aDJLc3JMdW9pckI1RXNuSWRVTkRjZGNiaFF1WVA0?oc=5) | - | khan.co.kr |
| 일반 | 게임 | 엔씨소프트 | [매출도 무대도 '글로벌'…엔씨, 포트폴리오 다변화 본궤도 - 지디넷코리아](https://news.google.com/rss/articles/CBMiVkFVX3lxTFBhbWRtOGxRNGd4UGV2d2IyUTZNQnNEdzFnT1FhemVLcVB2eDNIUmE4d2g2Z1hhWFQxb3hxanhSMTdrc0w3c2VjT19rSm5Md0ViTHFWbHpn?oc=5) | - | 지디넷코리아 |
| 일반 | 게임 | 엔씨소프트 | [엔씨소프트, 신규 IP 5종 공개...장르 다변화 추진 - OSEN](https://news.google.com/rss/articles/CBMiVEFVX3lxTE1sZnhWYzBEci05Zk5lWHR0RElCbWZ4LVlUZlFUTFYtZDB3QktlLXQzeGN1Z3F1WEc2VzhYekJnZVhxSFpYVXI3dWtEX2J1Ym9VMXgzRw?oc=5) | - | OSEN |
| 일반 | 게임 | 엔씨소프트 | [3D로 만나는 '아스트라에 오라티오'…엔씨·삼성전자, ‘TGS 2026’ 부](https://news.google.com/rss/articles/CBMiT0FVX3lxTE1hTlBWc19rZy02eDE3TUVwanJqY3RVRzNUYmE1RkMtUVZaVjJFYW9YTlVSTTVqY0FZMGoxQ25zcXRuR2FsRjVKUlJCMG1lODA?oc=5) | - | v.daum.net |
| 일반 | 게임 | 엔씨소프트 | [엔씨-MS 맞손, ‘아이온2’ 글로벌 흥행 정조준 - 미주중앙일보](https://news.google.com/rss/articles/CBMiYkFVX3lxTE9hRXhJazhzbUxkQ0dkeHhJZkM3amN3eGhreW5qRVplTFJsY3BiTEhvdFNqNDlTc2VaeWxaQ3BYRUJqMzlKaEhmSmtScG5FNDBuVmNQOW9vMHdWcjRUcDNJdEt3?oc=5) | - | 미주중앙일보 |
| 일반 | 게임 | 엔씨소프트 | [엔씨소프트 8.23% 상승한 22만3500원…‘아이온2’ 성과 재평가 - 잡](https://news.google.com/rss/articles/CBMibkFVX3lxTE1UbnFzdWlDajZaQzVoLVJuNXRyVWRRUzVfMzl3UVJ4NHRTNUt4MDFENHhuUThCcHFGWU42NUpBUmRPUGlJNHlrX1NqVTNzUW1EUWZsdE4tWUQyektCdEVQWm55UFlKNUJqeExMUy130gFyQVVfeXFMTnZpQWRjT3VWOVQ1cWl6R3dMOXlZczhtcklmeHpUWUUyODc4UkczaGl5b1hIVWVaQnBUZ0xJajNqeUJLVC1KWjAxcGxhNUNya19QUGdJZUVZMFc5YUh4eTVpbUU0NFFWVnBJdV92SEhaWVd3?oc=5) | - | 잡포스트 |
| 일반 | 게임 | 크래프톤 | [[게임위드인] 판 키우는 크래프톤 vs 집중하는 넥슨…누가 웃을까 - yna](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1jMThNM0twSk5tZ094YVRyRUR4VG1heHRoT1lzLWg3QWhGbW80TkRuMkZFdDkzZWM3cTBzV2Nid0NCTmxZVHRXYXRIbzA0cFQ5Q2lmQzdydEttUWvSAWBBVV95cUxPS2JRa3dyWkRaTXZQNkN3b01DOFQ4Y1dpWVIwSThCdFpGZldCYmt0QUVDZC1mMGxkWmVGdkQ3WlV1ZFBOcGppakZab1gySUxoMTB1WHlXMWhxQllMcWphUGk?oc=5) | - | yna.co.kr |
| 일반 | 게임 | 크래프톤 | [크래프톤 500억 베팅… '넥스트 리벨리온' 하이퍼엑셀, 몸값 8000억 '](https://news.google.com/rss/articles/CBMia0FVX3lxTE9HVTV5cFdiMVZlMUJTR3VFT0dta2R4WDFyMzFEZGJjSnAyQ2JkUFdoLUFoZjE2Smd5R2VGU2o0Y3FtTWpadURLUTItV0ktdjF4WGhQYkxmdFo1OFc3SWhhQUhPUWFTaWh1SUk40gFvQVVfeXFMTUItaFE5bm9CRTJicHFlRDBuVGdfaHd5UzRORzdHQm1QRWdzbjZrUC1FWXNSYkt3d3Y4NzRfcW5jQ1h6NWQ0eDlqb1ktRjN6NWhZZGRUZ1dQQ0ZVcWFTQnhZOFRseV96NW5uOTlQdkNz?oc=5) | - | 더퍼블릭 |
| 일반 | 게임 | 크래프톤 | ['방플' 논란 지속에 백기 든 크래프톤… "전적으로 잘못" - 뉴스1](https://news.google.com/rss/articles/CBMiYEFVX3lxTE5rUUgzQ0Z1TlJMUXlLRXpseDVyLUliTFpWdEp3Sm9DLXVrOXNibDVhSWliNWJ6ZmFGeU5mczlIbEh6d05BYU1iaTVmLXFmWXN0al9kOFl6REp0ckExQjlVMNIBZkFVX3lxTE1yM3ByNE1JN0h5Sm1wNjJNVDdlSHNLRXl3ZmY2LUF0cjA4TzQ4OWwzNnpCU2dkU2tOU1ZzOUJzUlRuOGh4Z3BPa2xvekxwQ2xYZjJzMXZkWW5rdzZ1M05VdnJQekFhdw?oc=5) | - | 뉴스1 |
| 일반 | 게임 | 크래프톤 | [크래프톤, 배그 대회 '외부정보 확인' 사과…마지막 경기 결국 취소 - 뉴시](https://news.google.com/rss/articles/CBMiYEFVX3lxTFBqVnVfYnJHd2tLLTRDc0ZYSjZBLUhlSWhld2xuNjB1MXFDNmFWemR6d1ltQzJ1SV82S3RMVk8teHc1WmViU2hmcGRzbmtRUDYtSTJUZmZIU3lvb2ZTdFhxUdIBeEFVX3lxTE4yeU5oWkIxRWV5dVdnQUd4VXBmNEl1eURoZkN1TlBycXd4dEk4WEZrTjNCWFdkNF91N0ZTTHZnSGlWZWw4cEdUdEtxN1Jjc3VwR2hWdlFtY3RyOTgwWnRKd3p1Y0I3NUJZZmtla2oxLVc0SmtwV2U0Xw?oc=5) | - | 뉴시스 |
| 일반 | 게임 | 크래프톤 | [경기 파행에 스폰서 줄줄이 발 뺐다…크래프톤 'PUBG' 무슨 일이 - 한국](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBuOVdncEJjWE1KQUxsbkhRd1hnTG5iVG5renBuODBKOTZ0NFdrT2YySjBjRkl1UGVtUEo3YklwOENvYXBERm5RcXJETzBIZDlLX2FvSzdSV1M2QQ?oc=5) | - | 한국경제 |
| 일반 | 게임 | 펄어비스 | [펄어비스, ‘붉은사막 인핸스드’ 첫 DLC ‘미지의 여정’ 10월 16일 출](https://news.google.com/rss/articles/CBMiZEFVX3lxTE96R0R3c2UxRlFGS2dzNU9aam8ybnFMdE8wWWpSb082MFZrb1FKbVRBME1ud1JMeW9VRTVjdmVPLUQxOGZXYXljTHR2TXpndzRQbWdwckFXV3M5MHNIS0tyN3RYZU0?oc=5) | - | Pearl Abyss |
| 일반 | 게임 | 펄어비스 | [펄어비스, 붉은사막 DLC 일정 공개에 10% 급등 - 뉴시스](https://news.google.com/rss/articles/CBMiYEFVX3lxTE1xeldrUUZaNUhhUHUtXzRJWnpzRTNMVlVJMDJRXzhYeEcwUG41TkYzbWtzb2F1aDlDTzlHV2pJTjl3VGt5Qkp6TG1xOEhieHlTYWhjNFMtTXNEMHNQbXF0Q9IBeEFVX3lxTE9oOXVxam9sVEZSRVI1UWpMWFhpWDJhZnVYS0pKekE3VU9jd0tRMFZudTh4Wm9BWm1uR2hPX1B0blhaZGc5aTJNMFk2YTdHTWpfZkdtNWg1eWN5MmUxNGlieDdQTE9ERWNSNW9HQklicUhBTHhIdm5VNw?oc=5) | - | 뉴시스 |
| 일반 | 게임 | 펄어비스 | [펄어비스 '붉은사막' 다시 타올랐다…업그레이드·할인 효과 - news.biz](https://news.google.com/rss/articles/CBMiakFVX3lxTE5jdXczS0hObVBvZmdrOFhSaFJxdlhVbjFiWFpBN1l1U2xuN2I3WHBkYzNPNlJzSE5iMmVXNEY0OTQtcHF1Y0Z3QkIzZnFxeEdNYk9Fdy1ER2NyckdQdW5vbU1OM3NGOFR4SUE?oc=5) | - | news.bizwatch.co.kr |
| 일반 | 게임 | 펄어비스 | [[특징주] 펄어비스, '붉은사막' DLC 공개에 10%↑ - v.daum.n](https://news.google.com/rss/articles/CBMiXEFVX3lxTE45SzRWSzBNenJxeDdDTGJjaTJELUp0OElXam85TEhvTU1tcG11dURDVHc0VnlzMkdhS0xLMHZOblN6MDlWVHFwMU9ZWWJVTHNqUHlwRlZ3eUc0Q0tK?oc=5) | - | v.daum.net |
| 일반 | 게임 | 펄어비스 | [12년간 매주 업데이트…펄어비스 '검은사막' 장수 비결 - 머니투데이 - 머](https://news.google.com/rss/articles/CBMiZ0FVX3lxTFA3YXhHTkY5bDhFbjVic0xpXzVaU0t1b0ZoWkdlaVhicW9WSWlTSUNXalRBZ29LQjVCSnVkV2d6R1VfeDFnU002Y1pjdzQtTmNKYkk4blFuNmdOMzNjR0ZWcE14YzUzd2fSAWxBVV95cUxQak9zSndzTnNaUjZtTkFjaHlwZ0pxemdETXVwYTA4aFpMWlNveUE2N3g2THJ2QUtRdFRBNEMxMkZOWnJuUTJLV0NJWUI4ZHdiT1N5VjFHRzFuUndTLTdTTWNwYkQtbU1kd0kzR1E?oc=5) | - | 머니투데이 |

### 🏢 회계법인 산업 리포트
**최근 수집된 발간물**

| 법인 | 리포트 |
|---|---|
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
