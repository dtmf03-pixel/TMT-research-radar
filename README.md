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
_최종 갱신: 2026-08-24 08:51 KST_

**수집 현황** — DART 공시 169 · 뉴스 331 · 회계법인 리포트 3

### 📄 DART 공시 (회계 이슈 필터)
_종류별: 실적 73 · 📘정기 54 · 🔴정정 18 · 🟡주요사항 24_

| 종류 | 업종 | 기업 | 일자 | 공시 |
|---|---|---|---|---|
| 🔴정정 | IT | 카카오 | 20260819 | [[기재정정]반기보고서 (2026.06)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260819000055) |
| 🔴정정 | IT | 다우데이타 | 20260811 | [[기재정정]회사합병결정(종속회사의주요경영사항)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260811900833) |
| 🔴정정 | 게임 | 넷마블 | 20260807 | [[기재정정]증권발행실적보고서(합병등)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260807000552) |
| 🔴정정 | 게임 | 더블유게임즈 | 20260724 | [[기재정정]사업보고서 (2025.12)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260724000595) |
| 🔴정정 | 통신 | 에스케이텔레콤 | 20260723 | [[기재정정]타법인주식및출자증권취득결정](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260723801025) |
| 🔴정정 | IT | 엔에이치엔 | 20260710 | [[첨부정정]주요사항보고서(회사합병결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260710000147) |
| 🔴정정 | 게임 | 크래프톤 | 20260630 | [[기재정정]타법인주식및출자증권취득결정](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260630800855) |
| 🔴정정 | 게임 | 위메이드 | 20260630 | [[기재정정]최대주주변경을수반하는주식양수도계약체결](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260630901591) |
| 🔴정정 | 미디어 | 콘텐트리중앙 | 20260630 | [[기재정정]타법인주식및출자증권취득결정](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260630801156) |
| 🔴정정 | 미디어 | 콘텐트리중앙 | 20260630 | [[기재정정]자기전환사채만기전취득결정](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260630801106) |
| 📘정기 | 게임 | 넷마블 | 20260814 | [반기보고서 (2026.06)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260814002548) |
| 📘정기 | 게임 | 엔씨소프트 | 20260814 | [반기보고서 (2026.06)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260814003764) |
| 📘정기 | 게임 | 크래프톤 | 20260814 | [반기보고서 (2026.06)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260814003894) |
| 📘정기 | 게임 | 펄어비스 | 20260814 | [반기보고서 (2026.06)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260814003642) |
| 📘정기 | 게임 | 넵튠 | 20260814 | [반기보고서 (2026.06)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260814002821) |
| 📘정기 | 게임 | 위메이드플레이 | 20260814 | [반기보고서 (2026.06)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260814001998) |
| 📘정기 | 게임 | 컴투스 | 20260814 | [반기보고서 (2026.06)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260814003984) |
| 📘정기 | 게임 | 위메이드 | 20260814 | [반기보고서 (2026.06)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260814003490) |
| 📘정기 | 게임 | 네오위즈 | 20260814 | [반기보고서 (2026.06)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260814003548) |
| 📘정기 | 게임 | 더블유게임즈 | 20260814 | [반기보고서 (2026.06)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260814003909) |
| 🟡주요사항 | IT | 카카오 | 20260821 | [주요사항보고서(회사합병결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260821000052) |
| 🟡주요사항 | IT | 카카오 | 20260821 | [주요사항보고서(회사분할결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260821000047) |
| 🟡주요사항 | IT | 무신사 | 20260813 | [주요사항보고서(자기주식처분결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260813001369) |
| 🟡주요사항 | 게임 | 네오위즈 | 20260812 | [주요사항보고서(자기주식취득신탁계약체결결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260812000035) |
| 🟡주요사항 | 미디어 | 나스미디어 | 20260806 | [주요사항보고서(자기주식취득신탁계약해지결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260806000438) |
| 🟡주요사항 | 게임 | 크래프톤 | 20260729 | [주요사항보고서(자기주식취득결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260729000354) |
| 🟡주요사항 | 통신 | 엘지유플러스 | 20260729 | [주요사항보고서(자기주식취득신탁계약체결결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260729000479) |
| 🟡주요사항 | IT | 비바리퍼블리카 | 20260728 | [주요사항보고서(회사합병결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260728000491) |
| 🟡주요사항 | IT | 네이버 | 20260727 | [주요사항보고서(유상증자결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260727000001) |
| 🟡주요사항 | 게임 | 위메이드 | 20260721 | [주요사항보고서(자기주식처분결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260721000875) |
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
_구분: 🔴회계신호 14 · 🔵회계이슈 7 · 일반 310_

| 구분 | 업종 | 기업 | 기사 | 회계토픽 | 출처 |
|---|---|---|---|---|---|
| 🔴회계신호 | 게임 | 카카오게임즈 | [[재무제표 이야기] 매출은 늘어도, 수익 질 나빠진 카카오..."미래 먹거리](https://news.google.com/rss/articles/CBMibEFVX3lxTE5RZUdDSmVsLXRLOWNKbkowWjdkZkhudUxHaWI2aFNieFF6MDRKOFBaUE5YUGRWVG9HTmZaWVdzbFJVVVN0ZURObGJvWUxaT3NWNkhSM2ZHUjNfdHVJTkRjbzBJOTRRR1lpMjd4cQ?oc=5) | - | 생생비즈플러스 |
| 🔴회계신호 | 엔터 | 에스엠엔터테인먼트 | [매출 73% 폭락·의견거절 속출…팬덤 환호에 가려진 K-엔터 ‘재무 잔혹사’](https://news.google.com/rss/articles/CBMibEFVX3lxTFBNdU5Mck5wR1lkdHBjaU9GV2laZ3EtZHF5eElXWkZ3SDJERVBXUWV5MlRScE0tdWpWMTltRE9kMmpEYmhOeWx6YTJmZUxKWVgyRms4V0w2a29GM0hOZ0F6a0UybVQ3TThtQmlvUQ?oc=5) | - | 한경매거진&북 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [금감원, 메가박스·콘텐트리중앙 회계심사 돌입…자금 조달·회계처리 점검 - v](https://news.google.com/rss/articles/CBMiVEFVX3lxTE9ta2pGSjBXYnlYS1JhRXZOc1RyUTNxSmI4cXlINVJnNU0xUFgwbnFVS1JIWWF6MDAwc0dzbXhKdTdUNmNIVjNSZ3l1Q3A4UnlMdFRSdw?oc=5) | - | v.daum.net |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [유동부채 1.4조 늪…’적정’ 받던 콘텐트리중앙, 5개월 만에 ‘의견거절’ ](https://news.google.com/rss/articles/CBMirAJBVV95cUxNVUpYMW9JNnd4Y0pRNVNyVkttRXZtOERwekxJX2JraWZrdlpIQkRVSU4taktUNHRCOVVvd21GcVAwd0NlVmJEYVN4WnVsOU5GenZnTlhBQVFpZnRqSVR4bUp4dEJyN081UDFzR2Izb1E4aWhqTFhSLUxyT09QUm1fN3pNbkxXa0xHdURhSGdQYkcwUUp5ODBOeEFwQUYtZG5QOGwxUmR0SVZuclNpRkFuQTB0SHY0QmhWaVVyX3BqaFg1OWVyZmsxWU9ybnp3WVM0eTBGRzJrQWpuRWZoUzVqbGV0QnZHOGhrRTZtUlJxeTRhTnpnUjVKeUZKYWdYd1RiVlRMRy1OSFVRdVdBUHhHSGRtQ0JGWVdOMDc0WWVleUh6WHlUX0VCRVQtdTc?oc=5) | - | 뉴스필드 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권투자자들, 금감원에 감리 요구…"회계처리 의문" - 연합뉴스](https://news.google.com/rss/articles/CBMiW0FVX3lxTFB1Ukx0THpTTk1DSVh2VGtQU2hsZTBuZWhlRWhzLUFKNGY0dm1RZkgwdDIxMXdaTzhkTXozUXltRTlOS2VOZ25SdGlfLVY1WVhsYUVfWmMxTERDUmvSAWBBVV95cUxQRDRMM1RQYmYwcGlUY1o2YmZfWTNKQlRDU2JkTmxWNnFlVEs4cTFCOElOR1MyUjhyb0twN18zMkNINldZOE1ZSTNKVVJWdmRDOFZ4S2M2OTVoVHVaWDRHUHo?oc=5) | - | 연합뉴스 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [금감원, 메가박스·콘텐트리중앙 회계심사 돌입…자금 조달·회계처리 점검 - K](https://news.google.com/rss/articles/CBMiW0FVX3lxTE54OUVMRE9hMTAyNThval9sRFV5ZDNOeFBHODQ2bmdNQmh5WU41UWtJU2RrZ2ttcEZ0SFhkRm03QjM5R3cxR21pbTJKUFU5ZzFCbEFTSFIwN3hWQUU?oc=5) | - | KBS 뉴스 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권투자자들, 금감원에 중앙그룹 5개사 회계 감리 요청 - 아주경제](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9tSk54eUp3YjcxUGlWM2RTWm5IQnVRcGk4dGdNSTlrMW1fNl9zY2xDdmVHblZRQm1YLVZvVF9HS1Z3bzJVT3BoQ2hzcHVxb3lKc3NhaEVsSml5QdIBWEFVX3lxTE9RY253VjVTSEVGVjJRQ1NkdUZqYUxkSnYyWm1iX3MtbUk0Yk53MTMzWkZaOXdpQ0J0NE1PdHBrNWdaMGU4TlFxUVlVNmplR0VXeGRITUdibWo?oc=5) | - | 아주경제 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [반기보고서 무더기 '의견거절'…투자 유의해야 - v.daum.net](https://news.google.com/rss/articles/CBMiS0FVX3lxTE0yQ3FYVmhLb0ZFXzlFMkZjajZuM2laaVlHUC1vNjdJU18zZW84dWpxSzFldEREbGMzOU5taG5HdjYxaHpjWnRZc2xPQQ?oc=5) | - | v.daum.net |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권 투자자 금감원에 감리 요구 - 조선비즈 - Chosunbiz](https://news.google.com/rss/articles/CBMigwFBVV95cUxOZ1BZZWVoNlItVU8zZTdWOTBmWVpncDBDUnMyenNPYUhNbWFDRDRlTjZpbzd6MnFxWHhzeWdmb01Jci1QRnN4UU83M0FmcHNTZ21HQmpxSF80WmxIMWRmcldCYmZhZUd4amk0bUtFazJnMVNOZklrZUp2ZjVPb2dFY2xJUdIBlwFBVV95cUxObmZVWHNYUEZEcU9BUUpKQXl1bmNJblA1ZkVvWlZ6bDExdWZkT2JWdFlnR3B0SGdBMWxQVmZrTUdzSlZiQ3FiV1pHU19FZ3M0WHlVMng2dDdpRW1ZUTRnalV3Ri1keE1rOHJVSkpHVUE3Y29jNzltSFNtZ0pOWUQ0OWJHOV9laHY3X2Z4WkdxZktNaHlzTWhn?oc=5) | - | Chosunbiz |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권투자자들, 금감원에 감리 요구…“회계처리 적정성 의문” - v.](https://news.google.com/rss/articles/CBMiRkFVX3lxTE1tWExvbGNFa0wzb21HbDBwUGlNY2pybXhhZlhNYVNlTFoyLWVWekgwbF9ZSjBzTzJ4N3g3RzluY3lUU3RFekE?oc=5) | - | v.daum.net |
| 🔴회계신호 | IT | 카카오 | [카카오 노조가 놓친 '새 회계기준 함정'…"내년엔 성과급 0원 될 수도" -](https://news.google.com/rss/articles/CBMiaEFVX3lxTE8yRnFCUUFIUzY3YTR1cDZqdmRVODJWd0pWT3E2SnNFQjBlTlpLZ0ZQQV90cTk3bldhRmdDUm1WVmN6WUZ5aDhrRjlWOXFYZzUwRzJhVktoejFha051VjRCUEVDb2x2UE1u?oc=5) | - | ebn.co.kr |
| 🔴회계신호 | IT | 카카오 | [토스 재무제표 간단 분석 - 브런치](https://news.google.com/rss/articles/CBMiTkFVX3lxTE5ISHpzQXZzNnJmb1A1ZWlFeGlFYzBBTlRhYXBkeFJ1WU1vamtEemhuVjhvaUpFbHp0R01wN051WnRTWDdiZmRXZ0MxeDNPdw?oc=5) | - | 브런치 |
| 🔴회계신호 | IT | 두나무 | [‘445억 해킹’ 두나무 제재 돌입…금감원, 감사의견서 발송 - 데일리안](https://news.google.com/rss/articles/CBMigwJBVV95cUxQdjlHNElLRGJXMFBlQ2RTM3pDM1FJbTk1LTJrQ3lUbkdMQlI5Y2JNTjQwcmRST3A4RXlPeXlRanJpdFBKbXh4Z3JyWGk3QWxqY2ktLThTRDk3V0pTT3hua1JWV1NoRW4yMUctUXNNT2JMbkF2Tm1qVXl2YkNEeWUwSXhKemkwenhFbWsxbEUwb3pGa0hJR1N3U29JZVhhakFXVkxSRjZta1puN1ZKeTA2VW5ma3Nqa1JCYnhtd00tUXIyRGJGdm5TNGxBaTdaaEhtTFpkczRVSnAtY3hWaDRNNnZvc1RfZVZlZjV4enhvYUtXYkFrZllDZjd3QWVRMWhGYkg4?oc=5) | - | 데일리안 |
| 🔴회계신호 | IT | 더존비즈온 | [AI 거래관계망 신용평가 모형, 재무제표 한계 넘는다 - 전자신문](https://news.google.com/rss/articles/CBMiTkFVX3lxTFAyTXpadGpRZkN6M090ZElpTDFqQ1FHZEZnUERfcW43V1JQR2FGX0E0emRyNTFKZjB1V2tPWjJtQXJZa0M4WWFPOTNnTGxiQQ?oc=5) | - | 전자신문 |
| 🔵회계이슈 | 게임 | 넥슨게임즈 | [[소외된 게임주]⑬ 넥슨게임즈, ‘퍼디’ 효과 사라지고 개발비만 쌓였다 - ](https://news.google.com/rss/articles/CBMiRkFVX3lxTE94dHBRbUlsV2dNTmwwenE5QjRmT0J1VEM1SE5XajM0Zk9Gb2d0RGVMMmdwMjR2enJHZXVrSjhhZnN2MEo4bEE?oc=5) | intangible-assets | v.daum.net |
| 🔵회계이슈 | 엔터 | 와이지엔터테인먼트 | [빅뱅, 데뷔 20주년 신곡 'BiiiG' 음원 차트 석권…월드투어 포문 - ](https://news.google.com/rss/articles/CBMiU0FVX3lxTE00ZnFSQXdTTlZuVDFzWUhaUmJDUFY0OFUxMFMyckpWSUlFUVBEcFEteWdtbEs1NGxKQVR3elI3cUhjcFZZN3hSZG1mT1BjdDF0bkZv?oc=5) | intangible-assets | 네이트 |
| 🔵회계이슈 | IT | 네이버 | [[핀포인트] [네이버] '1조 영업권' 시험대 오른 왈라팝 - 네이트](https://news.google.com/rss/articles/CBMiU0FVX3lxTE5wZHgtQy1XclFSak9sTjNsTm9KaVk3QnRUTUVYR2lBUlhNRWwwdE5hM0VVbU1HdWk0Z0xSS3BLbEczc2FoYVl2M2xldW0tR1ZLRnRz?oc=5) | intangible-assets | 네이트 |
| 🔵회계이슈 | IT | 카카오 | [[IB토마토]차바이오그룹, 카카오헬스 품었지만…CB·영업권 부담 '먼저' -](https://news.google.com/rss/articles/CBMiYEFVX3lxTE5oR2RicWlCR1pLcWtHNVVpY3Q2SGV0aERvc09adlVyajl2WkhibUNRMFVZV3FnUUZOUFJCTzFrS0JzZ2R0S2RpSHJLMUg3UEM1SVZXanh2V0dhYkhKSjE4RQ?oc=5) | intangible-assets | 뉴스토마토 |
| 🔵회계이슈 | IT | 카카오 | [업스테이지가 품은 ‘다음’ 평가액…무형자산 1413억 - 서울경제TV](https://news.google.com/rss/articles/CBMiZEFVX3lxTFBfUWJKZUJlbDlMWmxHSjFxZTZhcWJ2UVNkUlltY0tMYVZ5SFZWNF9oRnAzRmNGVlk1eWlaMDJmMmVueEs2SHFHSkZhSXFwVFBWTXA4LTVOYTNZZ3RqQk52a1lic1Q?oc=5) | intangible-assets | 서울경제TV |
| 🔵회계이슈 | IT | 야놀자 | [야놀자 상반기 거래액 21조 원, 매출은 14% 늘어 - 플래텀(Platum](https://news.google.com/rss/articles/CBMiSEFVX3lxTE9oLUxuSEtkVnhuYnVzd19uemVJTmUyUHM3aEZwcjM1WUtad0hfM2dVY0ZPYTh0Q2JUZVNBQS1GMTY5cS0zMzhUSA?oc=5) | platform-cases | 플래텀(Platum) |
| 🔵회계이슈 | IT | 컬리 | [[프리스탁 건강검진] 컬리, 현금창출력 개선 후 리스부채 부담은! - 프리스](https://news.google.com/rss/articles/CBMib0FVX3lxTFBqc1hSX1o2QUd1QVBVS3Zqd0R0R2N6R3dGRk8xRVU0Z244a1VNT1hqU0QwSVBHaTduZ2VfWWlBT1pCYnZGbHpMSUJiNEJBdTloZXhTeXZMY0ZYRnVYV1JKMU9BbVZDNVE3b1d0T1AwWQ?oc=5) | ifrs16-lease | 프리스탁뉴스 |
| 일반 | 게임 | 넷마블 | [방준혁, 텐센트 보유 넷마블 지분 13.4% 인수 - 비즈워치](https://news.google.com/rss/articles/CBMiakFVX3lxTE5RNFV3RnJRaWwtWU15LVlSSHdJc3JWalp4cmd2Y2ljVENRb0xBbkxGc1lkMjFPN1REd0hlRVpSeUtYVV9VSThRQUx4Wl9KUXJ1ODdWdDd1Q2RZcjJzdXpMNjBibE5qU05uT0E?oc=5) | - | 비즈워치 |
| 일반 | 게임 | 넷마블 | [방준혁 넷마블 의장, 텐센트 보유 지분 13.4% 인수 - 조선일보](https://news.google.com/rss/articles/CBMigwFBVV95cUxNaUVZamRtZzhFd01yRkVtNDF4RGVOMG1OaHExUGJsQ0t0ZHBpUmtfcHhXVS04V0F5ZXB6RmdxZUhMSWw2ZURPQUkxWTBDUmlyLUpOaGxBeWxteEVKM3FwUnRKZGZVa2ZRdGk4MWIzVWVjS0V5azlJTC1LdG13b0NERlpBNA?oc=5) | - | 조선일보 |
| 일반 | 게임 | 넷마블 | [[게임리뷰] 넷마블 '아스달 연대기', 뉴월드 시즌2 업데이트 사전등록 실시](https://news.google.com/rss/articles/CBMiY0FVX3lxTFAtZnVPWUZnVHZKLXV4ZVF2c09taC1acjA0Q2RzOVItOVI3RFFYdENPallDdFBhTEVXRGtFajA4bHc5cU1ab19DT2VYQ0lrYlplZXVxRGdBaWxRd1RBa2MtczdHZw?oc=5) | - | 더구루 |
| 일반 | 게임 | 넷마블 | [방준혁, 3740억원 들여 넷마블 지분 추가 인수... 지분율 38.34%로](https://news.google.com/rss/articles/CBMiTkFVX3lxTFBSYl9pRDB2QWdJWE1qc0NMQVNhVzNuLTBVVTkydFBJbVp3dG1aNHA4NHRvUW16VG9EbTdiODJKLTVxajM0VmtKR1ZSd2pmdw?oc=5) | - | 전자신문 |
| 일반 | 게임 | 넷마블 | [넷마블, 코웨이 지분 26.96%로 확대…133억 매수 - 연합인포맥스](https://news.google.com/rss/articles/CBMicEFVX3lxTE9VT1U0bWV4eF96cUZveGkzY1N6Wjgyb0VLODJnVWpBSTJPUzhZa0FfaDdXNHR5NWk4TWUzSzJ6MWlqN1QtMGlVTlUtdmVXbWNpblRURHNTaHFiY3RkREpjWTl5eGZBc2l5dDBzMFd1QV8?oc=5) | - | 연합인포맥스 |
| 일반 | 게임 | 엔씨소프트 | [엔씨, ‘아이온’으로 中·美 동시 공략…글로벌 확장 속도 - 문화일보](https://news.google.com/rss/articles/CBMiUEFVX3lxTFBHUmRySU03WVQ3MkVXOGhfZnlMeFpVUU1rTWRnSnRBNE1Zb1RERTJwNnpNNU5Qc2lscmZSTDg0b2NtUnBZbTZjVGFsWVBSUVpm?oc=5) | - | 문화일보 |
| 일반 | 게임 | 엔씨소프트 | [엔씨소프트 노조 “그룹 통합교섭, 기업 경험과 기술 지키는 경쟁력” - 로리](https://news.google.com/rss/articles/CBMibEFVX3lxTE13Q1BjWGVwaUpSMmpuTkZLaXVPSURKR3VBTWNMTXRRMVRjbUVTMkl4OGF6bTlkMEk3aEVra1pGazBZRV9sVnJRS0J6dEFNUklIX2R2cW5LR1FDZjRLdlppcnVEWXBqTzJoMUJaNQ?oc=5) | - | 로리더 |
| 일반 | 게임 | 엔씨소프트 | [엔씨는 고소, 넥슨은 환불, 넷마블은 정면돌파…게임사 위기관리 '3N 3색(](https://news.google.com/rss/articles/CBMidkFVX3lxTE41ckhXYlVHRXBpd3RMZWlzVGEyRXBrM3VxUXFEbTA0YXc1RE5CVFBqT0NGWU9wdTVyX09OM1N6RHVxNllsYm9KUjRPVEp3SmY2UU1WRDdDU29oU3hYWnBsZzFONWQxRjdHMXBOalNBbDNjOFFoM2c?oc=5) | - | 인포스탁데일리 |
| 일반 | 게임 | 엔씨소프트 | [엔씨, 2분기 실적 앞두고 '모바일 캐주얼' 주목…새 성장축 자리잡나 - v](https://news.google.com/rss/articles/CBMiRkFVX3lxTE9XdnE5aXFFMUF0V3RHNzh6a05mMXRST2FQb3ZTVkN0VW5rRF9wNVJFanZ0bjFRb2p6SkJhbVNwVHlDNlVOY1E?oc=5) | - | v.daum.net |
| 일반 | 게임 | 엔씨소프트 | [[실적] 엔씨, '리니지 클래식' 흥행에 영업익 10배↑…해외 매출 52% ](https://news.google.com/rss/articles/CBMiYEFVX3lxTE9lQ0VwVlR6YzBZcmZzeFdZWGVvN3I2ZVAteGt2Z2NHam9VenNtNHh0S19WXzdTekY2N0FjRnRiWWdmUlNTQURYcnB3cnZtOFV1VmUwYWhZb3R2RnpDY3pheA?oc=5) | - | 조세금융신문 |
| 일반 | 게임 | 크래프톤 | [크래프톤 5종·엔씨 3종… 베일 벗은 게임스컴 韓 출품작 - 국민일보](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9hZThqdV96TWwyWGJNaHVKM2gzRUtSSHRBOGVldmwtY0hGVUxoSmw0cGxuOUFjUHZEX0dZN0RXOW9Hbm5CenJfMkREQklNdFUwS3VNV08xSkYwLXBvd0FGNWVEVmNyNmPSAWxBVV95cUxQalJnMXpTQUJIMG1CRjdEWHBUUWJJZTAzdGtHWFdVTUgzc3hLSkN2QkRmSllzYi1Ca05pMC00VTNiS250aWlHTXo1M3NURkxSUmhBTEc2NmZmcVpvV2lsMndoUkg0MGVQTzctT18?oc=5) | - | 국민일보 |
| 일반 | 게임 | 크래프톤 | [[크래프톤 M&A 잔혹사] 8447억 베팅의 대가…크래프톤, 언노운월즈 가치](https://news.google.com/rss/articles/CBMiT0FVX3lxTE90VzJCQlVMVTM1QWFpNS1faWF3NzFMcWhUOG5ocVc3d2wzdDEwMDZ4NWFfWWN6dUlFOWx2UEMwSmVSQUJsQVNXRUpQQTJDSkE?oc=5) | - | 딜사이트 |
| 일반 | 게임 | 크래프톤 | [배틀그라운드, 42.3 업데이트 통해 신규 경기관총 출시 - 크래프톤](https://news.google.com/rss/articles/CBMiygJBVV95cUxQcllrMTBYejRGX1BIR0cwaUZxUTRmZ21ac0J6U0hkeDZNNDNmYmZrZEJKakRITE1zcUR0dFlfNEQ0bW41U3YtWVloNUlISXNxcFYwVGtwUHR0YlJXekxxdHcxYnVWV19hSUhvdTR6eFBCX3M3SkZiSkFYeUY4Q09xUWpDWEdhWHBOcmlNVjNkOEYteFdfSDlKTEZmSEtob1BoSDlzM2FfMEJQeVQ3ZGVsU3I5VkNPdU03eUFabVZFOGJxYjMtejNVbnRNVkZqLVBfWVZ6YVhFZ21EZXFSOW1wbUlkaVRtVTZnalRDSUM3NXZfOE9Yd0tWTEFlbzdGZUl6MEVLRmhNOG5Sb1lleUZJeEZrNzI4QnpkVldkWnF6N1NpVVJ3ZDNsTnE5UjYweDVmektFUTBGYlFTdFJjMTVLaWFDMUVYSGx1N1E?oc=5) | - | 크래프톤 |
| 일반 | 게임 | 크래프톤 | [넥슨 2분기 영업이익 17%↓... 크래프톤, 넥슨 제치고 매출·영업이익 1](https://news.google.com/rss/articles/CBMigwFBVV95cUxPcDR3MGVwVUt1NldlbmpXV0dnbmtlcEJOR3MxUjZrNmRadmtrSzJBZ1BUWEhicUFKNkF5Y2h3WUV5eDVpOFVhLTNTX2ZWdXZ3OTRWQ2JWakx1dkY0VFFkbDBzTlFwcnkyMXVDeDR2Z2JBVDN5SVRnZTVMV0RYT051RzFlcw?oc=5) | - | 조선일보 |
| 일반 | 게임 | 크래프톤 | [펍지 IP 신작 뜬다…크래프톤, 게임스컴 출품작 5종 정보 공개 - 지디넷코](https://news.google.com/rss/articles/CBMiVkFVX3lxTE1TOWJFS2V1cVFDbnQ4WDZ5SlNEalM1bDJwbWhhYXhPMTBZTjg5RWtFLUZQOFJocDJDSW80ZDlBZk9ta0FlSlVBZ2pPb1ZUSXJDVHR3Z2VB?oc=5) | - | 지디넷코리아 |
| 일반 | 게임 | 펄어비스 | [중국인들도 "믿기지 않을 정도"…'한국 대작' 일냈다 - 한국경제](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1PT3l3VUVhUWhnTTYyY0lUdFZnRXF2WHQ0R1VyYUtlLWlkSno0Q1BqZG91UDFoeDJ2cUx2THhfUkdVWlpaUVFuZUl6MVlVaHExT3ZpRjRXUGpnUQ?oc=5) | - | 한국경제 |
| 일반 | 게임 | 펄어비스 | [펄어비스 2분기 매출 247%↑, 영업익 7411%↑… ‘붉은사막’이 견인 ](https://news.google.com/rss/articles/CBMigwFBVV95cUxQN3VidG1oYTQyRUVXdTJjX2ZJeXZoYTREeE5WN3ozRWxGek96aFF6d195U3YtcTNhbmhwRENxQkFOc1FDckdaWXY4X29zYnVhUHpRcVFoVFItX1BBQlNTSFl6MHFYYTU2X2REOUd6UGN1REhEdUE1aHlIZF82aHBMcURRcw?oc=5) | - | 조선일보 |
| 일반 | 게임 | 펄어비스 | [지역사회와 함께하는 펄어비스의 따뜻한 동행​ - Pearl Abyss](https://news.google.com/rss/articles/CBMia0FVX3lxTE1UMExDWmlhSi1GWS1CNHprWHF4MEpZWFoyNEtVQkU5ZVVtUHFIUXV2Sl8zNUY3bllQQy1DZGdJcW1tZXNrczhZMlpVQjdBazd2Uk1yRnBFd0VwUURnWlZ5NmdlT0RJTW1oeXRB?oc=5) | - | Pearl Abyss |
| 일반 | 게임 | 펄어비스 | [펄어비스, ‘붉은사막’ DLC 연내 출시…‘도깨비’는 28년 출시 목표 - ](https://news.google.com/rss/articles/CBMiaEFVX3lxTE5EbTRBQThxVGJVTU85bkJuWU9hZzJaLXBSbVhRVzhzTEFJaTctQ0VXejVRMEVyVmswcUhyTThjMVE4bFBLRGVmaUFySzF5ejFsbDRGNU9MeTdaT0xlQUZuVWhQVkJtaThu?oc=5) | - | 녹색경제신문 |
| 일반 | 게임 | 펄어비스 | [붉은사막 매출인식 지연…'2Q 어닝미스' 펄어비스 13% 급락 - 머니투데이](https://news.google.com/rss/articles/CBMiaEFVX3lxTE9EeTNzMnBnVWJUYlRTVlZaRHFndzBGekFocEtXeWtza21pdksyVUM0WGNMMldsS2ZicGphMTM0OV83bVF0cVZaVzZhcnBnXzZBVXBkU2p4MkoyN2dKRHpDTHdGaVBrSkNi0gFuQVVfeXFMT3RCYVlVdXNoRUdXakYtS1ZVOEQwcEw5TlYwX1hsVE14NDJrWHF5N1RJa1R2bmZOLWZuSjFjYzFMUEJKX1FUbjh3M2JIdVJsSzRUNXBnYkJwUkJtZ0haMnEyaWNqNGN6QXNTT2hnemc?oc=5) | - | 머니투데이 |

### 🏢 회계법인 산업 리포트
**최근 수집된 발간물**

| 법인 | 리포트 |
|---|---|
| 삼정KPMG | [AI가 뒤흔든 콘텐츠 산업의 지형과 성장 전략](https://kpmg.com/kr/ko/insights/eri/2026/issuemonitor-0528.html) |
| EY한영 | [통신사는 어떻게 B2B 성장 전망을 재정의 할 수 있을까요?](https://www.ey.com/ko_kr/insights/telecommunications/reimagining-industry-futures-study-2026) |
| 삼일PwC | [AI 시대 광통신과 국내 기업의 기회](https://www.pwc.com/kr/ko/insights/industry-focus/optical-interconnect.html) |

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
