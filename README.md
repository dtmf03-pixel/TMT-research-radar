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
_최종 갱신: 2026-08-17 08:47 KST_

**수집 현황** — DART 공시 167 · 뉴스 331 · 회계법인 리포트 3

### 📄 DART 공시 (회계 이슈 필터)
_종류별: 실적 73 · 📘정기 54 · 🔴정정 17 · 🟡주요사항 23_

| 종류 | 업종 | 기업 | 일자 | 공시 |
|---|---|---|---|---|
| 🔴정정 | IT | 다우데이타 | 20260811 | [[기재정정]회사합병결정(종속회사의주요경영사항)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260811900833) |
| 🔴정정 | 게임 | 넷마블 | 20260807 | [[기재정정]증권발행실적보고서(합병등)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260807000552) |
| 🔴정정 | 게임 | 더블유게임즈 | 20260724 | [[기재정정]사업보고서 (2025.12)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260724000595) |
| 🔴정정 | 통신 | 에스케이텔레콤 | 20260723 | [[기재정정]타법인주식및출자증권취득결정](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260723801025) |
| 🔴정정 | IT | 엔에이치엔 | 20260710 | [[첨부정정]주요사항보고서(회사합병결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260710000147) |
| 🔴정정 | 게임 | 크래프톤 | 20260630 | [[기재정정]타법인주식및출자증권취득결정](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260630800855) |
| 🔴정정 | 게임 | 위메이드 | 20260630 | [[기재정정]최대주주변경을수반하는주식양수도계약체결](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260630901591) |
| 🔴정정 | 미디어 | 콘텐트리중앙 | 20260630 | [[기재정정]타법인주식및출자증권취득결정](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260630801156) |
| 🔴정정 | 미디어 | 콘텐트리중앙 | 20260630 | [[기재정정]자기전환사채만기전취득결정](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260630801106) |
| 🔴정정 | 미디어 | 콘텐트리중앙 | 20260630 | [[기재정정]주요사항보고서(전환사채권발행결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260630000851) |
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
| 🟡주요사항 | IT | 무신사 | 20260813 | [주요사항보고서(자기주식처분결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260813001369) |
| 🟡주요사항 | 게임 | 네오위즈 | 20260812 | [주요사항보고서(자기주식취득신탁계약체결결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260812000035) |
| 🟡주요사항 | 미디어 | 나스미디어 | 20260806 | [주요사항보고서(자기주식취득신탁계약해지결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260806000438) |
| 🟡주요사항 | 게임 | 크래프톤 | 20260729 | [주요사항보고서(자기주식취득결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260729000354) |
| 🟡주요사항 | 통신 | 엘지유플러스 | 20260729 | [주요사항보고서(자기주식취득신탁계약체결결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260729000479) |
| 🟡주요사항 | IT | 비바리퍼블리카 | 20260728 | [주요사항보고서(회사합병결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260728000491) |
| 🟡주요사항 | IT | 네이버 | 20260727 | [주요사항보고서(유상증자결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260727000001) |
| 🟡주요사항 | 게임 | 위메이드 | 20260721 | [주요사항보고서(자기주식처분결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260721000875) |
| 🟡주요사항 | 통신 | 케이티 | 20260714 | [주요사항보고서(자기주식처분결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260714000371) |
| 🟡주요사항 | 통신 | 케이티 | 20260714 | [주요사항보고서(자기주식취득결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260714000368) |
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
_구분: 🔴회계신호 12 · 🔵회계이슈 10 · 일반 309_

| 구분 | 업종 | 기업 | 기사 | 회계토픽 | 출처 |
|---|---|---|---|---|---|
| 🔴회계신호 | 게임 | 카카오게임즈 | [[재무제표 이야기] 매출은 늘어도, 수익 질 나빠진 카카오..."미래 먹거리](https://news.google.com/rss/articles/CBMibEFVX3lxTE5RZUdDSmVsLXRLOWNKbkowWjdkZkhudUxHaWI2aFNieFF6MDRKOFBaUE5YUGRWVG9HTmZaWVdzbFJVVVN0ZURObGJvWUxaT3NWNkhSM2ZHUjNfdHVJTkRjbzBJOTRRR1lpMjd4cQ?oc=5) | - | 생생비즈플러스 |
| 🔴회계신호 | 엔터 | 에스엠엔터테인먼트 | [매출 73% 폭락·의견거절 속출…팬덤 환호에 가려진 K-엔터 ‘재무 잔혹사’](https://news.google.com/rss/articles/CBMibEFVX3lxTFBNdU5Mck5wR1lkdHBjaU9GV2laZ3EtZHF5eElXWkZ3SDJERVBXUWV5MlRScE0tdWpWMTltRE9kMmpEYmhOeWx6YTJmZUxKWVgyRms4V0w2a29GM0hOZ0F6a0UybVQ3TThtQmlvUQ?oc=5) | - | 한경매거진&북 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [금감원, 메가박스·콘텐트리중앙 회계심사 돌입…자금 조달·회계처리 점검 - v](https://news.google.com/rss/articles/CBMiS0FVX3lxTE01b28xT1lOWGJZQXBtZFJaY1FhLXpobXA5Mm5QQzJ4VFQyUmRmeE5QMm5obnhocnN1cGtSd0dON2NBcnpWTXFBRV9BTQ?oc=5) | - | v.daum.net |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권투자자들, 금감원에 감리 요구…"회계처리 의문" - 연합뉴스](https://news.google.com/rss/articles/CBMiW0FVX3lxTFB1Ukx0THpTTk1DSVh2VGtQU2hsZTBuZWhlRWhzLUFKNGY0dm1RZkgwdDIxMXdaTzhkTXozUXltRTlOS2VOZ25SdGlfLVY1WVhsYUVfWmMxTERDUmvSAWBBVV95cUxQRDRMM1RQYmYwcGlUY1o2YmZfWTNKQlRDU2JkTmxWNnFlVEs4cTFCOElOR1MyUjhyb0twN18zMkNINldZOE1ZSTNKVVJWdmRDOFZ4S2M2OTVoVHVaWDRHUHo?oc=5) | - | 연합뉴스 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 투자자들 “회계처리 의문”… 금감원에 감리 요청 - v.daum.n](https://news.google.com/rss/articles/CBMiT0FVX3lxTE92M3UxRHNaUzJ6dXY0MHhBd2tlZnZfRWJ2V0dCYW5LWWRxTVIzRi1jOVBfc1lseEF5MlVYb2ZBRW9jak1SdWljRHpNUTBoWDQ?oc=5) | - | v.daum.net |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권투자자들, 금감원에 중앙그룹 5개사 회계 감리 요청 - 아주경제](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9tSk54eUp3YjcxUGlWM2RTWm5IQnVRcGk4dGdNSTlrMW1fNl9zY2xDdmVHblZRQm1YLVZvVF9HS1Z3bzJVT3BoQ2hzcHVxb3lKc3NhaEVsSml5QdIBWEFVX3lxTE9RY253VjVTSEVGVjJRQ1NkdUZqYUxkSnYyWm1iX3MtbUk0Yk53MTMzWkZaOXdpQ0J0NE1PdHBrNWdaMGU4TlFxUVlVNmplR0VXeGRITUdibWo?oc=5) | - | 아주경제 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권 투자자 금감원에 감리 요구 - 조선비즈 - Chosunbiz](https://news.google.com/rss/articles/CBMigwFBVV95cUxOZ1BZZWVoNlItVU8zZTdWOTBmWVpncDBDUnMyenNPYUhNbWFDRDRlTjZpbzd6MnFxWHhzeWdmb01Jci1QRnN4UU83M0FmcHNTZ21HQmpxSF80WmxIMWRmcldCYmZhZUd4amk0bUtFazJnMVNOZklrZUp2ZjVPb2dFY2xJUdIBlwFBVV95cUxObmZVWHNYUEZEcU9BUUpKQXl1bmNJblA1ZkVvWlZ6bDExdWZkT2JWdFlnR3B0SGdBMWxQVmZrTUdzSlZiQ3FiV1pHU19FZ3M0WHlVMng2dDdpRW1ZUTRnalV3Ri1keE1rOHJVSkpHVUE3Y29jNzltSFNtZ0pOWUQ0OWJHOV9laHY3X2Z4WkdxZktNaHlzTWhn?oc=5) | - | Chosunbiz |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권투자자들, 금감원에 감리 요구…“회계처리 적정성 의문” - v.](https://news.google.com/rss/articles/CBMiVEFVX3lxTFBld1FWTEQxRF95ZnZxMFV3cE5idVNhellBd2VmRVo1cWI4VFVOQjR0SHNJQThLZUVLNFk0RzhFTXplQ2hUdk9CSTA0ajM3N3AxR19zZA?oc=5) | - | v.daum.net |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [“돌려막기로 자본잠식 숨겼나”…중앙그룹 채권투자 피해자들, 감리 요구 - 한](https://news.google.com/rss/articles/CBMickFVX3lxTFBDSS1uQk52SXBhb1kycHJkNU5na0w1cmtyUm1hSW5KM2YtQkZWUy1TYlVfT2F5NHhUdElibTdhaExkblFZWExucFBXeVRpM1FkcTNvdm41dHpaODZEVzhScldkQ2FwTnRjZmJWTll0Z3p6dw?oc=5) | - | 한겨레 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙 채권투자자 측, 금감원에 감리 요구…"회계처리 조사해야" - 뉴시스](https://news.google.com/rss/articles/CBMiYEFVX3lxTE9YNWhyTGpIeFlmZ0I3dnhBeDdlQmVpcXIxNFZsQ0szVUxNZm1IS1d2eEYxNjRpN2Y3aW5TMVdQNlNjRkV0V0dtTnpqcVpPU1FWbEJrb1p4d3pLb2lvN1NzUNIBeEFVX3lxTE10WFpPbS14UFFRcHdRTzJKalZRQmFkdnVNSnlrNVU0TllhbFl6REF6RzRBQkJXZS1hcmlYT1l2LXk4aFk5anpLSVVhd3hYc2UzWG95Q3M5czV3V3JMS2xId3JqMU1weEt6UlJGS0lZYW9OWFBOLTYycw?oc=5) | - | 뉴시스 |
| 🔴회계신호 | IT | 카카오 | [카카오 노조가 놓친 '새 회계기준 함정'…"내년엔 성과급 0원 될 수도" -](https://news.google.com/rss/articles/CBMiaEFVX3lxTE8yRnFCUUFIUzY3YTR1cDZqdmRVODJWd0pWT3E2SnNFQjBlTlpLZ0ZQQV90cTk3bldhRmdDUm1WVmN6WUZ5aDhrRjlWOXFYZzUwRzJhVktoejFha051VjRCUEVDb2x2UE1u?oc=5) | - | ebn.co.kr |
| 🔴회계신호 | IT | 카카오 | [토스 재무제표 간단 분석 - 브런치](https://news.google.com/rss/articles/CBMiTkFVX3lxTE5ISHpzQXZzNnJmb1A1ZWlFeGlFYzBBTlRhYXBkeFJ1WU1vamtEemhuVjhvaUpFbHp0R01wN051WnRTWDdiZmRXZ0MxeDNPdw?oc=5) | - | 브런치 |
| 🔵회계이슈 | 게임 | 넥슨게임즈 | [[소외된 게임주]⑬ 넥슨게임즈, ‘퍼디’ 효과 사라지고 개발비만 쌓였다 - ](https://news.google.com/rss/articles/CBMiaEFVX3lxTE8zemo1UV9xNW9yNW5RM1FrNlptUnlTNENBSDJfSjZOTVJFdFBSTEZ0aUx6WkJva0h2ajVxZzRQVW9CcXJfdjdQc2c1VHVwN2tTNTNYRF84Snc1dEtpdTNkbm5sUmlPamti0gFsQVVfeXFMTnpXOTQ4SThFWlRGYjJrQ3pRc1BRS3RxSkZQcU91MTdPQ25uRmdlVGRpYkhSNHN3VDVGLUJzaUpZZjBOMlhtd2tjMF9BSE10V3FQaTJfRHNCampybVl4N3N1VTE3aXk1RV9VWmJK?oc=5) | intangible-assets | 블로터 |
| 🔵회계이슈 | 게임 | 위메이드 | [위메이드 2분기 영업손실 210억 원... 라이선스 매출 제외로 적자 전환 ](https://news.google.com/rss/articles/CBMiaEFVX3lxTE1nZHF1TXVhVUNLRnVZVnpTUzdSZlBnZjhZRHZIU3owYl9RQjNUQkY2aDBicjFQa3hmLVlGbmlNaGJhVVEyRkVxa2NYeE1CZ0Nsc2hkWFJtTkVqcjI1c1kwU1djVXV4a3dM?oc=5) | intangible-assets | ipnn.co.kr |
| 🔵회계이슈 | 엔터 | 하이브 | [하이브, 역대 최대 실적에도 M&A는 ‘마이너스’… 1조원대 영업권도 부담 ](https://news.google.com/rss/articles/CBMicEFVX3lxTE1EclZkd2RpcVphX0ZoLUh2SHpodTZEZlBUazZxVTVfSWlXcWNQbXJKOHF0MUQ1MVcxc2puQlVOUV9zUjZlZDIzOEg2MmRFSmYyZ0V3cWlLaEtOSlV4QVA4NTRBUEgzVGNzX01BTnBXbW3SAXRBVV95cUxQNFZxR3lGNmx5Z0FHVlVOZjdEd0N2Yk1jaVNLem5zMHJWWmhpcFE0N1F3b3BZTXNyZTRIeU1CS0VNbGJ1cWdQWDZuUzM2cHlNWXRxS3NqYmRWalQ1cTJYM2FOWDVDa0hQNkhvd3lVTkI1alczVg?oc=5) | intangible-assets | it.chosun.com |
| 🔵회계이슈 | 미디어 | 씨제이이엔엠 | [CJ온스타일, 3년 만에 100억 브랜드 속출… 거래액 16배 뛰었다 - 패](https://news.google.com/rss/articles/CBMiUEFVX3lxTE1jZTR0eUFhRF9KTWVUcG93OXNPV01XXzluWlg0aVVRLUNLdUY1YWpzMzZmNDdCRTU3T2RYQ1k0dVYycEU5djRLQVkyYjJTaUpw?oc=5) | platform-cases | 패션비즈 |
| 🔵회계이슈 | IT | 네이버 | [[핀포인트] [네이버] '1조 영업권' 시험대 오른 왈라팝 - 네이트](https://news.google.com/rss/articles/CBMiU0FVX3lxTE5wZHgtQy1XclFSak9sTjNsTm9KaVk3QnRUTUVYR2lBUlhNRWwwdE5hM0VVbU1HdWk0Z0xSS3BLbEczc2FoYVl2M2xldW0tR1ZLRnRz?oc=5) | intangible-assets | 네이트 |
| 🔵회계이슈 | IT | 카카오 | [업스테이지가 품은 ‘다음’ 평가액…무형자산 1413억 - 서울경제TV](https://news.google.com/rss/articles/CBMiZEFVX3lxTFBfUWJKZUJlbDlMWmxHSjFxZTZhcWJ2UVNkUlltY0tMYVZ5SFZWNF9oRnAzRmNGVlk1eWlaMDJmMmVueEs2SHFHSkZhSXFwVFBWTXA4LTVOYTNZZ3RqQk52a1lic1Q?oc=5) | intangible-assets | 서울경제TV |
| 🔵회계이슈 | IT | 카페24 | [카페24 "최근 2년간 식품·뷰티 자사몰 거래액 43.8%·38%↑" - 지](https://news.google.com/rss/articles/CBMiVkFVX3lxTFBXZ2hmaWpULWJzaWxzZ2dRb0Z5Wkx0cWxKSlhxNUlDY0RiUWhwa3VyeTVXbEhyS1pwaW1jcVpqbTRGb1Z4RDNYcHpTWDJCRFZTazdzMlNB?oc=5) | platform-cases | 지디넷코리아 |
| 🔵회계이슈 | IT | 야놀자 | [야놀자 상반기 거래액 21조 원, 매출은 14% 늘어 - 플래텀(Platum](https://news.google.com/rss/articles/CBMiSEFVX3lxTE9oLUxuSEtkVnhuYnVzd19uemVJTmUyUHM3aEZwcjM1WUtad0hfM2dVY0ZPYTh0Q2JUZVNBQS1GMTY5cS0zMzhUSA?oc=5) | platform-cases | 플래텀(Platum) |
| 🔵회계이슈 | IT | 무신사 | [무신사 뷰티, 오프라인 거점 확대로 온라인 거래액 증가 - fetv.co.k](https://news.google.com/rss/articles/CBMiaEFVX3lxTE1rWXN6TW5TMk1Cd1pfQlZHMHNmM1RBRDBFaU84cGM5ZFNwckdtQXUxNjcyVXFVUXRodWo2aXBBbHNkYlMxOFRLZE1iV0tKTk1iZ28wc0hZX1E2czRXS1F3NVBEZmVERmRy?oc=5) | platform-cases | fetv.co.kr |
| 🔵회계이슈 | IT | 컬리 | [[프리스탁 건강검진] 컬리, 현금창출력 개선 후 리스부채 부담은! - 프리스](https://news.google.com/rss/articles/CBMib0FVX3lxTFBqc1hSX1o2QUd1QVBVS3Zqd0R0R2N6R3dGRk8xRVU0Z244a1VNT1hqU0QwSVBHaTduZ2VfWWlBT1pCYnZGbHpMSUJiNEJBdTloZXhTeXZMY0ZYRnVYV1JKMU9BbVZDNVE3b1d0T1AwWQ?oc=5) | ifrs16-lease | 프리스탁뉴스 |
| 일반 | 게임 | 넷마블 | [“다작王 타이틀 어디로?”…넷마블에 물었더니 - 에너지경제신문](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5lOHRvX0RTYjNxTm9hR0FlWmJyUVlxd2ZJdUp2TXAzNmJMVk9YaHYwSXVzZVRwT2Q0RzVBZVNlWUlBU1BfOHU4Nk5WVDhINU1sQ1Q1OHZBN0tNa1U?oc=5) | - | 에너지경제신문 |
| 일반 | 게임 | 넷마블 | [넷마블, "다작 전략 수정"...올해 신작 5종에서 3종으로 축소 - 디일렉](https://news.google.com/rss/articles/CBMiZkFVX3lxTE9Kc2xoWC1tSW92QWZoNi1Ed2RyVXp3UXVfNkxKV1YyWEpZMzFyOWpXY2xpS3BWRlM1eUozak00YTlnRGpzcUlVbHRaU1ZQREhPX1E4MU1XWmVTcW9OOW9CSlNja19jdw?oc=5) | - | 디일렉 |
| 일반 | 게임 | 넷마블 | [넷마블 골드 작업장 비교 팀 협업 체계적 방법 - Gwara Media](https://news.google.com/rss/articles/CBMi2wFBVV95cUxQVXJfUTJRMzFsaFQtaGpyTnlhaVkzZm1Nb1BJTjkyOFZRYzdXa0xaSWotRGRlREJCRW0zU3BYRk56b3o4VHpyZThyY1c0YXVndmNObVMxMEtreWhLUXQzNllCUHRTanBuMWFxRkF2S1ZfeXI0eG1seTUwR1dhVkpTYzBzSzNVOFp3aHkwUGwwY2ZpVk94TDFVRVM2LWlWVnFucTV2cDNsXzNzUlhTeVE0OEp6cFRzR193UzFnbTFCNHhSN2s4NXN4Rjdkam1pWmJvcDlzOV9oU0ZHR1U?oc=5) | - | Gwara Media |
| 일반 | 게임 | 넷마블 | ["게임 밖으로 나온 스톤에이지"···넷마블이 하나은행과 손잡은 이유 - 여성](https://news.google.com/rss/articles/CBMic0FVX3lxTE5uSkxJTHNEQ05ZZmtzSXQ2aHE4ZTFqNmY1d0lrNFB5WXROYzBvNlFCNXZEZERHSmZ2VGMwQi1OcXh0dWhWYmNQcFRrcWNoYlI2NS02MU8yQjlGbHcxYUZCQ0RNTWlJblNCaVBYOXZKZUJ4TVE?oc=5) | - | 여성경제신문 |
| 일반 | 게임 | 넷마블 | [넷마블, ‘다작’ 대신 ‘장수게임’ 키운다…하반기 전략 선회 - 문화일보](https://news.google.com/rss/articles/CBMiUEFVX3lxTE5OREFVS3I4bC03dXc4d2QwQ1N4WW1qYWg2VldsZHFIR3ZkYUdIZzlNWS1vdW5hc1g4QjBaN2VWaVdVeGtsVU4yN2lPcWpVVkNi?oc=5) | - | 문화일보 |
| 일반 | 게임 | 엔씨소프트 | [김택진 엔씨소프트 대표, 아이온2로 중국 공략…IP 확장 본격화 - 피플투데](https://news.google.com/rss/articles/CBMib0FVX3lxTFBPdVQ3TGt0THdwVW8xbHBkV3BmZ0U1UkNMbl9HdnVnZnY0VXdjaW5talptc3pxLVZlMTFlY1BBbUFKOFlYek9pdElCQjQ1M3YwaVYzRzRtc1ZTZlNtYmV4X1hZa01IVkhMVy1ydXFaMA?oc=5) | - | 피플투데이 |
| 일반 | 게임 | 엔씨소프트 | [엔씨소프트 2분기 영업이익 1739억…해외 매출 비중 52%로 첫 추월 - ](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE5zaHlhT1hORUc5NDVJWnpBWFlhaVAteDBfZS0xU2pyU0RFN3JkZDlPRHVhcHdzRXJCRUlJNmR3ZnRBOTZlb0VvTnliNFBHa1FIamxQQXdUai15SS14U2kxc21vYVVjUmc?oc=5) | - | jabon.co.kr |
| 일반 | 게임 | 엔씨소프트 | [엔씨소프트 노조 “그룹 통합교섭, 기업 경험과 기술 지키는 경쟁력” - 로리](https://news.google.com/rss/articles/CBMibEFVX3lxTE13Q1BjWGVwaUpSMmpuTkZLaXVPSURKR3VBTWNMTXRRMVRjbUVTMkl4OGF6bTlkMEk3aEVra1pGazBZRV9sVnJRS0J6dEFNUklIX2R2cW5LR1FDZjRLdlppcnVEWXBqTzJoMUJaNdIBcEFVX3lxTE9pR0c1LWNqNU1tVkJvTG9Jcl9xUGJmdHBEbkxkS0tYYzNwV1JXSGhkU1d5aFRPZE5IZEhVUEFtbDE2Y3k1OWFWWDRoMnNKTU84dXcwNEI0R0FpM1A5QzdzNWVSVmpfTzBJRTRmN3RBenQ?oc=5) | - | 로리더 |
| 일반 | 게임 | 엔씨소프트 | [[Q2 분석] “해외 매출 52%·클래식 IP 폭발" 엔씨소프트…"리니지 원](https://news.google.com/rss/articles/CBMibEFVX3lxTE9KVFZwbmtsM3FjdGw3blNGaDEyY1lQcW1FTTJLdjB2dUJfd2NIZG5Za29LakRJTThraFh6elZaUFd3S0dad2lfY0lJOEZpaGVrSUh3VnFzRFdKV3B2ZVVrLXQzdTNzUzNkS3BCZA?oc=5) | - | 이코노미톡뉴스 |
| 일반 | 게임 | 엔씨소프트 | [엔씨, 2분기 실적 앞두고 '모바일 캐주얼' 주목…새 성장축 자리잡나 - v](https://news.google.com/rss/articles/CBMiT0FVX3lxTE5SN1ZheGNWOXdrVmZNd2tlbTF1SUNWTHAzdnRweE5fSnlTNEJQREhhN3ozRkNPaHVhN254NXk3czNrZnIxa3RYNC11ZHRSUm8?oc=5) | - | v.daum.net |
| 일반 | 게임 | 크래프톤 | [[크래프톤 M&A 잔혹사] 8447억 베팅의 대가…크래프톤, 언노운월즈 가치](https://news.google.com/rss/articles/CBMiT0FVX3lxTE90VzJCQlVMVTM1QWFpNS1faWF3NzFMcWhUOG5ocVc3d2wzdDEwMDZ4NWFfWWN6dUlFOWx2UEMwSmVSQUJsQVNXRUpQQTJDSkE?oc=5) | - | 딜사이트 |
| 일반 | 게임 | 크래프톤 | [게임업계 2분기 실적 전망 엇갈려…크래프톤 독주 예상 - 연합뉴스](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1fXzlTRUZmMGM0OUJ6Nno2YVZfektQbGw3ZEt6bVNlS3FydmhYbmdUdWwya2FfS08waWlzNUQ2S01zRTNOMXhsR0dkLTVJWnBHbXpqTXF1VXljQUnSAWBBVV95cUxOV3c5X2M5Y2t3djBDVnNQN2Rsd1lCdE1xb0lhZGlzNlJaTm1MLV9ObXlmRE9XQ2ZRYlJncTUwU0RZN2NTX0Vhd09ORXlkcXBfSmZSdjh0MVJOTXhaRzF4SkY?oc=5) | - | 연합뉴스 |
| 일반 | 게임 | 크래프톤 | [장태석 크래프톤 총괄, 게임업계 연봉 1위 등극 - 조선일보](https://news.google.com/rss/articles/CBMigwFBVV95cUxQaDZDY01sc1VoLXdFQmp2bEpZU2NfRWxLX2NJTDdVTlJGUUZMTkk3Z2o0MkI5VEdDbVBDdHM2TjN4MEJhUnBNeVV0NUh0YTU4SUtQblJOVVdlREZxeHhPVW5NV2dUZWJwZWh0SmloRllhd1ViZ0dUcFdSNWxtNnFOQVFfWQ?oc=5) | - | 조선일보 |
| 일반 | 게임 | 크래프톤 | [크래프톤·엔씨·펄어비스, 나란히 ‘실적 점프’…성장 전략은 달랐다 - 디일렉](https://news.google.com/rss/articles/CBMiZkFVX3lxTE1HWUMwQmxneHU1NlZ3dUl0aVpKcTdUck1YSHZ2SE1pRldYcmQ0MFRUVFZQQUdoNjc1Z3NqblNqeldTQlFnUDhNelV0RE5EcVlwUHplRlg2bkZxVmdaQU82SjRqa3hsdw?oc=5) | - | 디일렉 |
| 일반 | 게임 | 크래프톤 | [크래프톤, 자체개발 음성 AI 모델 ‘K2 라온 스피치’ 공개 - 에너지경제](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9uNzBjanAzLWZNUC0zdWMyNTU2Y3Z6SmI0RkxkTXc0eTJnWUpqQkRBbW1DSmo1TU85RUFxMkJQRDZHclh5LU9QNkpfV1VWNzhDbVUxTldkUUsxR1U?oc=5) | - | 에너지경제신문 |
| 일반 | 게임 | 펄어비스 | [펄어비스 2분기 매출 247%↑, 영업익 7411%↑… ‘붉은사막’이 견인 ](https://news.google.com/rss/articles/CBMigwFBVV95cUxQN3VidG1oYTQyRUVXdTJjX2ZJeXZoYTREeE5WN3ozRWxGek96aFF6d195U3YtcTNhbmhwRENxQkFOc1FDckdaWXY4X29zYnVhUHpRcVFoVFItX1BBQlNTSFl6MHFYYTU2X2REOUd6UGN1REhEdUE1aHlIZF82aHBMcURRcw?oc=5) | - | 조선일보 |
| 일반 | 게임 | 펄어비스 | [펄어비스, '어닝 쇼크'에 장중 14%대 급락 - 한국경제](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9lZ3dkSjY3NTdWOV80SnhybFV6a0pLY2pGMTFpdXhrN01oSE4wZGFMcVg5blRTRWhGbHJYLWhaLV9QaEN6SHdlVTV6eW5XRGhjR0xXa1dscUZnQQ?oc=5) | - | 한국경제 |
| 일반 | 게임 | 펄어비스 | [‘붉은사막’ 효과 펄어비스, 2분기 영업익 676억원…스위치2 출시 준비 -](https://news.google.com/rss/articles/CBMiZkFVX3lxTFBUb19YR1ZkbWF1NkthQTdTdG04UFB1dUNsNWU1bEo1MS1TUENXNWxhUmxOYUxMUUtkd2ViODFSTnpCR0djZkxzclR1ZGJBSVo1VmZMcXh6c1lCdVNfakNKLWQ4NTRXQQ?oc=5) | - | 디일렉 |
| 일반 | 게임 | 펄어비스 | [펄어비스, '붉은사막' 글로벌 이용자 콘텐츠 확대 - 팍스경제TV](https://news.google.com/rss/articles/CBMiaEFVX3lxTE5oV1JpejFzTTI1UWREWVFtR1Njck4tR3VYZjN2RENSMDdQSzhzQ1FqdVhhbkVXLU8yTkQxMmNLSm5iVXlKbUtmSW9yNHgtalg1ckVmM083U1Jha25KaHZ1NDFPZ3pOWlot?oc=5) | - | 팍스경제TV |
| 일반 | 게임 | 펄어비스 | [펄어비스 '붉은사막', 중국서 '최고의 인터내셔널 게임' 선정 - 연합뉴스](https://news.google.com/rss/articles/CBMiW0FVX3lxTE0yaXVOTXljbDY2MU0zMzVEQTFXdUtmRnFoTVVQRDI5dnBJbWFBVlQzMGZQSGlXaW9mNlk0LUFXTVNmTTZfQUlnMUxLNjMyT2RDek1BWFlWVXpZbW_SAWBBVV95cUxPcmk2NjJQQ2ZlX2tOU0JiMXhwTzdEODJRSWJLbVBzVkdqdjAyOEZ1bWZOSXJ3N3ZaLTItNEZkaVJrejhiYjFZaUlXNXp5LTcydk9pTkowZjdTT0dpSXUxZHQ?oc=5) | - | 연합뉴스 |

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
