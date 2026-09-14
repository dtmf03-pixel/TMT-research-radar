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
_최종 갱신: 2026-09-14 09:58 KST_

**수집 현황** — DART 공시 160 · 뉴스 330 · 회계법인 리포트 1

### 📄 DART 공시 (회계 이슈 필터)
_종류별: 실적 72 · 📘정기 54 · 🔴정정 13 · 🟡주요사항 21_

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
_구분: 🔴회계신호 15 · 🔵회계이슈 7 · 일반 308_

| 구분 | 업종 | 기업 | 기사 | 회계토픽 | 출처 |
|---|---|---|---|---|---|
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [금감원, 메가박스·콘텐트리중앙 회계심사 돌입…자금 조달·회계처리 점검 - v](https://news.google.com/rss/articles/CBMiT0FVX3lxTE55eHlOanhSb0VrOFJ6MmpaaWhvRVh2SGZKSVJsWktINkNYcGpZRnBRLTUwdFBBWGJoUHFlZm1MUkZTR0tQTzZCanBvWW9xOEk?oc=5) | - | v.daum.net |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권 피해자 대리인단, 금감원에 감리 요청 - 법률신문](https://news.google.com/rss/articles/CBMibkFVX3lxTFB4OEZyLVFxM2lFejNpZm5vRmgwNDAzeWh5TElpVEpxNFhWZ3FJRndLTk5fTF9kWGE0aUdrTjM3S0lCamZ2V3Y4TE03LUNSTmpfTHZsaXROZ1JJeEYzaC1jek9ZRTZudnU2dWRORFdR0gFyQVVfeXFMTlJuUTUzcVYwLTIyMWhZWnFRYVBNc2FPU251QVYyU0V2cXUzU2RvV3RlTS1PMWVXeVNvNElNOTIwWnhXcXRrV1pKdURYZHo5emlVcWR0cC1tc0kxTUlZSVZ0TFBKSGxCUmZDNndnZGg4ZHNR?oc=5) | - | 법률신문 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권투자자들, 금감원에 감리 요구…"회계처리 의문" - 연합뉴스](https://news.google.com/rss/articles/CBMiW0FVX3lxTFB1Ukx0THpTTk1DSVh2VGtQU2hsZTBuZWhlRWhzLUFKNGY0dm1RZkgwdDIxMXdaTzhkTXozUXltRTlOS2VOZ25SdGlfLVY1WVhsYUVfWmMxTERDUmvSAWBBVV95cUxQRDRMM1RQYmYwcGlUY1o2YmZfWTNKQlRDU2JkTmxWNnFlVEs4cTFCOElOR1MyUjhyb0twN18zMkNINldZOE1ZSTNKVVJWdmRDOFZ4S2M2OTVoVHVaWDRHUHo?oc=5) | - | 연합뉴스 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [“돌려막기로 자본잠식 숨겼나”…중앙그룹 채권투자 피해자들, 감리 요구 - 한](https://news.google.com/rss/articles/CBMickFVX3lxTFBDSS1uQk52SXBhb1kycHJkNU5na0w1cmtyUm1hSW5KM2YtQkZWUy1TYlVfT2F5NHhUdElibTdhaExkblFZWExucFBXeVRpM1FkcTNvdm41dHpaODZEVzhScldkQ2FwTnRjZmJWTll0Z3p6dw?oc=5) | - | 한겨레 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권투자자들, 금감원에 감리 요구…"JTBC 등 회계처리 조사" -](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9USmdOS04yVzNFQUhINmFtemVYdjhqYkpJYmN6TnlYMU9mdXQxWGtRQTVmek5kMXpZbjNOZ2kydEJWbFVzaGlZQS1vbUhJUmxDWkc0N3dZLVd1c2VhTURv?oc=5) | - | 조세일보 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 투자자들 “회계처리 의문”… 금감원에 감리 요청 - v.daum.n](https://news.google.com/rss/articles/CBMiVEFVX3lxTE1fS1hlUE9VYWpjdnRpb2JiTGxsVjJpUHNDZV9lQ1hmUVBkUDg3SVpBTjdiVG56R0w1OVlKT1VtVS1mbkZRRkkwSUR1cEpCeHFrSXRKRw?oc=5) | - | v.daum.net |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [반기보고서 무더기 '의견거절'…투자 유의해야 - v.daum.net](https://news.google.com/rss/articles/CBMiRkFVX3lxTE1TQVowaC1JUEoyZm5zeGRHS1VwdGFKRWQ2ZWRUak9LRG1NVWppUEJGU0NlNm93Tnc4VDE5ZXkyeDRxMTZDc3c?oc=5) | - | v.daum.net |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | ["재무제표 왜곡·우회 자본 순환 의혹"…중앙그룹 피해자들 검사 촉구 - 뉴스](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9TelEtWGVBbnNXSF9DQXhOQlVSRHdRRklJTWpISUVwNjJ3ZkI0XzZJcm42bEswT1I1ZURrOTlCWThKZExpakxBeEcwVjNWdmxDQ0hsSmJ0bG5SaXktVkE00gFkQVVfeXFMTVRqblZaVkV0Z0ZEWTJlRjJKYjh3WUd2aWJ0VDVGZTBsTnVQTlBqWUFXckM2Mm9IMm52MVNKQVpILUJfVXFMOTRFNGF3OTlsTFJ6TjE1cFI2N2FWWnp1a21LTF9kNw?oc=5) | - | 뉴스1 |
| 🔴회계신호 | IT | 네이버 | [[단독] 두나무, 美 SEC 위원장 면담, 회계기준 전환 완료...나스닥행 ](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPTE5PSW1ya182NWtnSDlMTmFrSkhvVC1xUmhPNG9zb3ZDZWd2RVVGalBvSFdmT0xMYUd3bWIxbkE1TkF3YVpPTWtxdlVZTUszdGExSTBNMFhBdkZaMkV3V2JpT196UXV0aDVFMmczaWpYbU5YVXpWbDd1Q1cxVmtEMWtfdzZ5WHZydGhB?oc=5) | - | 조선일보 |
| 🔴회계신호 | IT | 네이버 | [두나무 美 상장설 다시 고개…“회계기준·행선지 결정 안 돼” - etoday](https://news.google.com/rss/articles/CBMiVEFVX3lxTE5rR0JabEc4RWVrazRoMUIxOWlwb2h6NzI1VjFzWUI3MnFRbThXcnRlbl8yNk13TVBzZXVMLVpNR2hLdWNwWHktYnpQSFNtX3ZqWGFwZw?oc=5) | - | etoday.co.kr |
| 🔴회계신호 | IT | 카카오 | [카카오 노조가 놓친 '새 회계기준 함정'…"내년엔 성과급 0원 될 수도" -](https://news.google.com/rss/articles/CBMiaEFVX3lxTE8yRnFCUUFIUzY3YTR1cDZqdmRVODJWd0pWT3E2SnNFQjBlTlpLZ0ZQQV90cTk3bldhRmdDUm1WVmN6WUZ5aDhrRjlWOXFYZzUwRzJhVktoejFha051VjRCUEVDb2x2UE1u?oc=5) | - | ebn.co.kr |
| 🔴회계신호 | IT | 카카오 | [토스 재무제표 간단 분석 - 브런치](https://news.google.com/rss/articles/CBMiTkFVX3lxTE5ISHpzQXZzNnJmb1A1ZWlFeGlFYzBBTlRhYXBkeFJ1WU1vamtEemhuVjhvaUpFbHp0R01wN051WnRTWDdiZmRXZ0MxeDNPdw?oc=5) | - | 브런치 |
| 🔴회계신호 | IT | 두나무 | [美 회계기준 문의한 두나무, 나스닥 상장說에 "정해진 바 없어" - v.da](https://news.google.com/rss/articles/CBMiRkFVX3lxTFBuVTZwMGdTUzQycTVOUHBUOWZLR2pKZzBnY2cySDdSaDFsd2xXSHJHT0Q4YmxDQkZCQVRPWmxRSG5TUEtteEE?oc=5) | - | v.daum.net |
| 🔴회계신호 | IT | 두나무 | [‘445억 해킹’ 두나무 제재 돌입…금감원, 감사의견서 발송 - 데일리안](https://news.google.com/rss/articles/CBMigwJBVV95cUxQdjlHNElLRGJXMFBlQ2RTM3pDM1FJbTk1LTJrQ3lUbkdMQlI5Y2JNTjQwcmRST3A4RXlPeXlRanJpdFBKbXh4Z3JyWGk3QWxqY2ktLThTRDk3V0pTT3hua1JWV1NoRW4yMUctUXNNT2JMbkF2Tm1qVXl2YkNEeWUwSXhKemkwenhFbWsxbEUwb3pGa0hJR1N3U29JZVhhakFXVkxSRjZta1puN1ZKeTA2VW5ma3Nqa1JCYnhtd00tUXIyRGJGdm5TNGxBaTdaaEhtTFpkczRVSnAtY3hWaDRNNnZvc1RfZVZlZjV4enhvYUtXYkFrZllDZjd3QWVRMWhGYkg4?oc=5) | - | 데일리안 |
| 🔴회계신호 | IT | 더존비즈온 | [AI 거래관계망 신용평가 모형, 재무제표 한계 넘는다 - etnews.com](https://news.google.com/rss/articles/CBMiTkFVX3lxTFAyTXpadGpRZkN6M090ZElpTDFqQ1FHZEZnUERfcW43V1JQR2FGX0E0emRyNTFKZjB1V2tPWjJtQXJZa0M4WWFPOTNnTGxiQQ?oc=5) | - | etnews.com |
| 🔵회계이슈 | 엔터 | 하이브 | [하이브, 역대 최대 실적에도 M&A는 ‘마이너스’… 1조원대 영업권도 부담 ](https://news.google.com/rss/articles/CBMicEFVX3lxTE1EclZkd2RpcVphX0ZoLUh2SHpodTZEZlBUazZxVTVfSWlXcWNQbXJKOHF0MUQ1MVcxc2puQlVOUV9zUjZlZDIzOEg2MmRFSmYyZ0V3cWlLaEtOSlV4QVA4NTRBUEgzVGNzX01BTnBXbW3SAXRBVV95cUxQNFZxR3lGNmx5Z0FHVlVOZjdEd0N2Yk1jaVNLem5zMHJWWmhpcFE0N1F3b3BZTXNyZTRIeU1CS0VNbGJ1cWdQWDZuUzM2cHlNWXRxS3NqYmRWalQ1cTJYM2FOWDVDa0hQNkhvd3lVTkI1alczVg?oc=5) | intangible-assets | it.chosun.com |
| 🔵회계이슈 | 미디어 | 위지윅스튜디오 | [초상권 라이선스 시대 온다…AI 버추얼 프로덕션의 미래[AI 생존법] - v](https://news.google.com/rss/articles/CBMiVEFVX3lxTE9BZ1MwYk9JVldfR3FUVExBdjZaZ00tSFVacFVEQnBTRDJQa3dWWTNtMDMtT3F6SFNtSWZhVUZybXJsYlJENWs0c0tnRTNuRF9EQnZHSA?oc=5) | intangible-assets | v.daum.net |
| 🔵회계이슈 | 미디어 | 스튜디오드래곤 | [[스튜디오드래곤 톺아보기] 판권 상각기준 전격 변경…'수익·비용 매치' 변동](https://news.google.com/rss/articles/CBMijwFBVV95cUxOeWRaSDJiY0JzY0l6SXlzMGtRVmdaYjZncDdubVBfUjlaNldjS081VlZicUM2UXRsXzVKbTZpdVlnb2xRa1JyNnY1cmxEaFNKQUNuZkZqRXppV2pSYW9iMFVsaFhHcHBzRHNZZmVVNm5hMjNtdTE2a3VsT21qam9YYU5uREpJOG1HQmdLR25Xaw?oc=5) | intangible-assets | blog.naver.com |
| 🔵회계이슈 | IT | 네이버 | [JTBC 회생신청종편 라이선스값 3000억…홍정도 마지막 베팅 : 네이버 블](https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBTbGgxVmQzc3dlUTNnbVRLaHhPbjcyOEh4MHRNTVN5QkZNTThCdlBVVTIwTmFFSTh4b0t4U0k2SjhUUElrS0kweDhEaHVuYjhkeFdZNHp2YWZBNjJqNDM5UEFERm1oc3c?oc=5) | intangible-assets | blog.naver.com |
| 🔵회계이슈 | IT | 카카오 | [[IB토마토]차바이오그룹, 카카오헬스 품었지만…CB·영업권 부담 '먼저' -](https://news.google.com/rss/articles/CBMiYEFVX3lxTE5oR2RicWlCR1pLcWtHNVVpY3Q2SGV0aERvc09adlVyajl2WkhibUNRMFVZV3FnUUZOUFJCTzFrS0JzZ2R0S2RpSHJLMUg3UEM1SVZXanh2V0dhYkhKSjE4RQ?oc=5) | intangible-assets | 뉴스토마토 |
| 🔵회계이슈 | IT | 무신사 | [무신사, 코스피 상장 예심 청구…글로벌 거래액 3조 목표 - fetv.co.](https://news.google.com/rss/articles/CBMiaEFVX3lxTE1UVklJWVBfMlJMYjhCV2ZHLTgxeThycmVKdURrRndORzFoQmRGdGFCemFDRXdTZVB3VjRBd2NrUTFOX29hdnByQk1raXFpQ005YTkxWEw3SDFkSmdPbDhCQ2kzT3RrVHpZ?oc=5) | platform-cases | fetv.co.kr |
| 🔵회계이슈 | IT | 컬리 | [컬리N마트, 장보기 '단골' 잡으며 출시 1년 만에 거래액 10배 성장 - ](https://news.google.com/rss/articles/CBMickFVX3lxTE9BaTJ4bEVTRWRCSW9zRTVPc2hLZ0xmZFNqbG5VdC1pQWVfWG92Yk9CM0swTlRhS25SS2RQRlBvbUJNbTZXZmRjS1ExeFFpbERPVXloMGFLVHZUNUotVWxJTEVDUGY2SDJyU1lET1JOSWt6QQ?oc=5) | platform-cases | navercorp.com |
| 일반 | 게임 | 넷마블 | [넷마블, TGS서 신작 3종 띄운다…배우·성우·스트리머 총출동 - 디지털데일](https://news.google.com/rss/articles/CBMiZEFVX3lxTE5nMlBOOFdXY1lVZVFNSVFlcmxpZmNaSVVWaUhDQnJjWDZWRVh6QTRiOUZoeTA5VlRGcmVLOV9qR2Z0S2JvTFZyZEhlQ3RhOVpwYlBJTUQySGFSZ3hlbFZHRnZnNGI?oc=5) | - | 디지털데일리 |
| 일반 | 게임 | 넷마블 | [넷마블, TGS 2026 출품작 3종 무대 라인업 공개... 17일 신작 정](https://news.google.com/rss/articles/CBMiTkFVX3lxTE9zajNDMWhTd2wzbHBSaWlVR2RTU0szS1hGdWM4ZlZ1TzF5T2VvOEYybHRCWVZBbTFGbWZoZHhMVEhJVU9pZDNVUlAwbGFmQQ?oc=5) | - | etnews.com |
| 일반 | 게임 | 넷마블 | [바카라 넷마블 특수 심벌이 적용되지 않는 경우 - Calgary Roughn](https://news.google.com/rss/articles/CBMi-AFBVV95cUxPYWgtVnNCdEZjTlRmYk80UFFXUlRUeGdaLWlhSzZlVjd4Y3lWSEp5cHNjUy03cjdQR2ZMWW9FSGFZaWYzTzlFQXlBdHBBVjI3M25mVi1CanlqZEcweGg4cHJYV0FsMWVoMldSQXJVZVlnMzMzLUN5b01iYnczd0N0NHBJRWNXZzB4S2tiZVh1eExWaldoUmJzeVRGYVJBci02TlhtZTN6X2YzV1ExeXRSdHlyQnExRUZzM2gtdHVTNk1zZnFtRGRVMWZnZTlRUFNYUGZoUXR1Sl80cG1RWmh6eEVrb2RRVFRWUHNSYklQRjlXUUlwQ29qWQ?oc=5) | - | Calgary Roughnecks |
| 일반 | 게임 | 넷마블 | [넷마블 엠엔비, 청강문화산업대·순천향대와 MOU 체결 - 디일렉](https://news.google.com/rss/articles/CBMiZkFVX3lxTE1IaHRObGg5eTNpX2RKekdKZmhPUi1iU3ROdjBJbVM0Vkt2RHlPOEhZMlpPMV9LSldncF9pMFg3VEg4TXJtMUJoZjF1N3czS2ZKTk1nTjI3Y3VwbDFzR0MzR2RNaUhMdw?oc=5) | - | 디일렉 |
| 일반 | 게임 | 넷마블 | [넷마블 엠엔비, 쿵야 IP 활용 로블록스 게임 공모전 개최 - 주간한국](https://news.google.com/rss/articles/CBMidEFVX3lxTE1BR2YydUZ0NFdOSUxfX0NjcTh0V0ZfUG9tdzBZLTlPSXEzdnJhdFZxTHlsWUxwTVNPaXN0SGpCVDNmVEZQSTctN0MxbnpYMlhxZWtQcHNHbXhXS1IwVjNNdXljMHpKcUdzVjNCNXQzcE9PS0dr0gF0QVVfeXFMTUFHZjJ1RnQ0V05JTF9fQ2NxOHRXRl9Qb213MFktOU9JcTN2cmF0VnFMeWxZTHBNU09pc3RIakJUM2ZURlBJNy03QzFuelgyWHFla1Bwc0dteFdLUjBWM011eWMwekpxR3NWM0I1dDNwT09LR2s?oc=5) | - | 주간한국 |
| 일반 | 게임 | 엔씨소프트 | [엔씨소프트, ‘아이온2’ 신규 성역 ‘비탄의 설원’ 업데이트 - 비즈니스리포](https://news.google.com/rss/articles/CBMib0FVX3lxTFBsOUMwZzVaUFMtMEVOU2dOSF9GYXRWRTNncmZJOXZVMlh2Y21iQVlGbE1WcFJfRWxpeHI3c0xodTc2d2NlSlFsMmUzVUxDeF9rSzB1ZGozMjFMOVByTElsT0pzaWJXUy1MbXZDdjhYQQ?oc=5) | - | 비즈니스리포트 |
| 일반 | 게임 | 엔씨소프트 | [엔씨 ‘아스트라에 오라티오’, 日 공략 속도…도쿄게임쇼 참가 - 팍스경제TV](https://news.google.com/rss/articles/CBMiaEFVX3lxTE5XeEhodVU5QkpOVzEwVjd5a1ZrRFpnUkFXbWZLdl9ZQmUyOGFUZ3NzRUNHR3E1Yk05TjVwQTM2T2VEUVAxdkJZaWl0VFlZa2FkVVRQVklXdDBoT2dMeDVOdzFUQWEzSU5x?oc=5) | - | 팍스경제TV |
| 일반 | 게임 | 엔씨소프트 | [매출도 무대도 '글로벌'…엔씨, 포트폴리오 다변화 본궤도 - 지디넷코리아](https://news.google.com/rss/articles/CBMiVkFVX3lxTFBhbWRtOGxRNGd4UGV2d2IyUTZNQnNEdzFnT1FhemVLcVB2eDNIUmE4d2g2Z1hhWFQxb3hxanhSMTdrc0w3c2VjT19rSm5Md0ViTHFWbHpn?oc=5) | - | 지디넷코리아 |
| 일반 | 게임 | 엔씨소프트 | [4년 침체 끝낸 엔씨…투톱 경영이 바꿨다 - 데이터뉴스](https://news.google.com/rss/articles/CBMiZEFVX3lxTE9xUnpVVkRhcTlzbXphejhRY2oyRmNSQ0c0andtQm0za3liSmhVXzNDcHN1aGhFbDlvT0lHQmo1dF9wZHloNmd5Q3cwd0lmbHVDMEM0dlF5cloySjFMSFF0cGhKbHo?oc=5) | - | 데이터뉴스 |
| 일반 | 게임 | 엔씨소프트 | [엔씨 퍼플, ‘창세기전 외전: 서풍의 광시곡 리마스터’ 입점 - NCsoft](https://news.google.com/rss/articles/CBMibEFVX3lxTE5xY0JORnoyVmRXQkg5Zkpod1Bna1Z6NEpDc1p3eWVrZnhwYk9vcDdUdHJHOVBzVnd2dEZoWkJMazVqMkV0R05uSDU3b0RxOENTeEppUjQ5eGo4UFFpRldvN0diVTBFUGdRZ25zZg?oc=5) | - | NCsoft |
| 일반 | 게임 | 크래프톤 | [5민랩, 신작 ‘세계허구관리연맹: WPCA’ 첫 공식 트레일러 공개 - 크래](https://news.google.com/rss/articles/CBMiswJBVV95cUxNejhMcTVvRDAzSkFweGlNVURXaFpvT21iWHM3WnFvdlhOY09aSjJzTERTZktCQnZ3ZjY1VGJXUzlXV1d4Q29wU3k3MzRZSGd6c21lWWxzU3lLdW02aGl4WmFqNnlPeEFYYjA2a0lVcFZNZ2w3UnV5QmdPa1VETHZxT1V5XzlrSWFZdm5uOTVFbVJacW5uR0F5T25HY3hBYlBmWTI5dnYwMkppbWVKd3BfZ2J4Tm9DU29nWEpDdUlrM0FCVWpETWtMQ1JDNE52dEZfd3pFSXUzMUN0Q1Zvc0ZVRUpqakV1a3M3YmV6dWFpS015eU5VVV9RS3BUQmM0X2tGU3RVQ0UyZUFJdUN3Mnl3dF92THEwVE5SLUVTdzFYbllPLXNDTGplZU15NjE2X2EyZ21n?oc=5) | - | 크래프톤 |
| 일반 | 게임 | 크래프톤 | [[단독] 크래프톤-한화에어로 방산 합작법인 설립 사실상 무산 - 조선일보](https://news.google.com/rss/articles/CBMigwFBVV95cUxQWm5EOFhGcl9pbkE1cVJfTi1Oa29wd0Zta1FnR1U0VExRN29sS0NMeVg0X3NTdkVRNFpOZVpFN0wtcWNHVld6UlBFQm1Jd3dKRUJWLUVERU9RakRNZXFkcUdIQXE4S2FuNVB6ajVzcTd6UHNHT0l1c3JlZUNMODRiQTVfbw?oc=5) | - | 조선일보 |
| 일반 | 게임 | 크래프톤 | [[게임위드인] 판 키우는 크래프톤 vs 집중하는 넥슨…누가 웃을까 - 연합뉴](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1jMThNM0twSk5tZ094YVRyRUR4VG1heHRoT1lzLWg3QWhGbW80TkRuMkZFdDkzZWM3cTBzV2Nid0NCTmxZVHRXYXRIbzA0cFQ5Q2lmQzdydEttUWvSAWBBVV95cUxPS2JRa3dyWkRaTXZQNkN3b01DOFQ4Y1dpWVIwSThCdFpGZldCYmt0QUVDZC1mMGxkWmVGdkQ3WlV1ZFBOcGppakZab1gySUxoMTB1WHlXMWhxQllMcWphUGk?oc=5) | - | 연합뉴스 |
| 일반 | 게임 | 크래프톤 | [크래프톤 '배틀그라운드', 애니메이션 '주술회전'과 협업 - etnews.c](https://news.google.com/rss/articles/CBMiTkFVX3lxTE55UzAzdUFMVFNIRWIzNUwxLURLTnBkYS1BOS1ZaFVfRFlDRW9zZzlkZjJZRHVVR2ZnUmt1ekxnT01OZ2xoalM3cDBHcG5IQQ?oc=5) | - | etnews.com |
| 일반 | 게임 | 크래프톤 | [장병규 크래프톤 의장, 나렌드라 모디 인도 총리와 회담 外 - 톱데일리](https://news.google.com/rss/articles/CBMiUEFVX3lxTFBjeDZ3YW1FTEFRbFduNHhIU296eHh3RGlvVEhPZDJyYTdocGNQWjBxZ3VWY2VpWDhqbmxyR0huWTY0Tm5GSzFINmFaLUlYbWhf?oc=5) | - | 톱데일리 |
| 일반 | 게임 | 펄어비스 | [펄어비스 '검은사막' 하반기 콘텐츠 확장으로 흥행 이어간다 - v.daum.](https://news.google.com/rss/articles/CBMiRkFVX3lxTFBkYUFzSjBFNm9ua3kyY1JjdjlTWnF2NDZXdnhWVDNVY3gtMzVsNlpWSmNYelFrNDhhWjVNWE5ySzhySVZ4TFE?oc=5) | - | v.daum.net |
| 일반 | 게임 | 펄어비스 | [펄어비스, ‘붉은사막 인핸스드’ 첫 DLC ‘미지의 여정’ 10월 16일 출](https://news.google.com/rss/articles/CBMiZEFVX3lxTE96R0R3c2UxRlFGS2dzNU9aam8ybnFMdE8wWWpSb082MFZrb1FKbVRBME1ud1JMeW9VRTVjdmVPLUQxOGZXYXljTHR2TXpndzRQbWdwckFXV3M5MHNIS0tyN3RYZU0?oc=5) | - | pearlabyss.com |
| 일반 | 게임 | 펄어비스 | [붉은사막 효과 꺾이니 '긴 사막'…펄어비스, 다음이 안 보인다 : 네이버 블](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBLTUR3VlBUeHRJVnRBZGxyLUFxY29jbjVncFhtMDVIeHVQMXZjUjY0NzdIdktNVWZ1WHp0aFFXb3VVdkJsb0dvaHBvVlZJbzhaMDRzaWF2MFB2Zw?oc=5) | - | blog.naver.com |
| 일반 | 게임 | 펄어비스 | [붉은사막 딛고 '고공비행'…펄어비스, 체질개선·주주가치 제고 '속도' - 청](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9KR2V4V3k2TEpMb3FiaHFhVGpjZ0c4X1JyVHVvQjhJTjJjRzM0bzNPR19QUmI5Vkswd1JzRWJ5SXc3OFhXYW1QdjdmdDc5aW9NOGJ0MHlJZ19tTFpCaS1iRnRWUnlMTkE?oc=5) | - | 청년일보 |
| 일반 | 게임 | 펄어비스 | [펄어비스 '붉은사막' 첫 DLC '미지의 여정' 내달 16일 출시 - 아시아](https://news.google.com/rss/articles/CBMiYEFVX3lxTE93MmZPRjBZRWhfa1VsNS1Ld0N1NkQ1eXlROF9lTi15bUlpbVotZkdoYzlOb3dKZjloeXk3czktZGNiU09JQXpiN0U4SWhLU0RhYzlacTZhV3BfN1JXc3h5bg?oc=5) | - | 아시아경제 |

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
