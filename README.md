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
_최종 갱신: 2026-09-21 09:58 KST_

**수집 현황** — DART 공시 160 · 뉴스 339 · 회계법인 리포트 1

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
_구분: 🔴회계신호 17 · 🔵회계이슈 10 · 일반 312_

| 구분 | 업종 | 기업 | 기사 | 회계토픽 | 출처 |
|---|---|---|---|---|---|
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [금감원, 메가박스·콘텐트리중앙 회계심사 돌입…자금 조달·회계처리 점검 - v](https://news.google.com/rss/articles/CBMiVEFVX3lxTE9ta2pGSjBXYnlYS1JhRXZOc1RyUTNxSmI4cXlINVJnNU0xUFgwbnFVS1JIWWF6MDAwc0dzbXhKdTdUNmNIVjNSZ3l1Q3A4UnlMdFRSdw?oc=5) | - | v.daum.net |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권 피해자 대리인단, 금감원에 감리 요청 - 법률신문](https://news.google.com/rss/articles/CBMibkFVX3lxTFB4OEZyLVFxM2lFejNpZm5vRmgwNDAzeWh5TElpVEpxNFhWZ3FJRndLTk5fTF9kWGE0aUdrTjM3S0lCamZ2V3Y4TE03LUNSTmpfTHZsaXROZ1JJeEYzaC1jek9ZRTZudnU2dWRORFdR0gFyQVVfeXFMTlJuUTUzcVYwLTIyMWhZWnFRYVBNc2FPU251QVYyU0V2cXUzU2RvV3RlTS1PMWVXeVNvNElNOTIwWnhXcXRrV1pKdURYZHo5emlVcWR0cC1tc0kxTUlZSVZ0TFBKSGxCUmZDNndnZGg4ZHNR?oc=5) | - | 법률신문 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권투자자들, 금감원에 감리 요구…"회계처리 의문" - 연합뉴스](https://news.google.com/rss/articles/CBMiW0FVX3lxTFB1Ukx0THpTTk1DSVh2VGtQU2hsZTBuZWhlRWhzLUFKNGY0dm1RZkgwdDIxMXdaTzhkTXozUXltRTlOS2VOZ25SdGlfLVY1WVhsYUVfWmMxTERDUmvSAWBBVV95cUxQRDRMM1RQYmYwcGlUY1o2YmZfWTNKQlRDU2JkTmxWNnFlVEs4cTFCOElOR1MyUjhyb0twN18zMkNINldZOE1ZSTNKVVJWdmRDOFZ4S2M2OTVoVHVaWDRHUHo?oc=5) | - | 연합뉴스 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [“돌려막기로 자본잠식 숨겼나”…중앙그룹 채권투자 피해자들, 감리 요구 - h](https://news.google.com/rss/articles/CBMickFVX3lxTFBDSS1uQk52SXBhb1kycHJkNU5na0w1cmtyUm1hSW5KM2YtQkZWUy1TYlVfT2F5NHhUdElibTdhaExkblFZWExucFBXeVRpM1FkcTNvdm41dHpaODZEVzhScldkQ2FwTnRjZmJWTll0Z3p6dw?oc=5) | - | hani.co.kr |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [금감원, 메가박스·콘텐트리중앙 회계심사 돌입…자금 조달·회계처리 점검 - v](https://news.google.com/rss/articles/CBMiT0FVX3lxTE55eHlOanhSb0VrOFJ6MmpaaWhvRVh2SGZKSVJsWktINkNYcGpZRnBRLTUwdFBBWGJoUHFlZm1MUkZTR0tQTzZCanBvWW9xOEk?oc=5) | - | v.daum.net |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | ["계열사 전반 재무제표 왜곡 의심"… 중앙그룹 피해자들 검사 확대 요구 - ](https://news.google.com/rss/articles/CBMibkFVX3lxTFAyVVZEV2FCZDdpMW12YURXNWIxVGNIdzE0MWoweUFPYUhlbEFHWVFGV2V4WV9uM2U2WDJ1Ri0xb3U0QTlrTVhIaWo3UWRFMTVJSHNvSzlyUjlPV3d1WWNOODg0NFpZSllKOElOekxB0gFzQVVfeXFMTnMzNmJkaFo0LU15RVNMemVtVUpRSVNlblhEV0w3R3BwWXpZNlNrTDM3Q2twSldRYmZ2RHpiWGlpZnppdzRmdThDVzZyaklMcXBiLUx4MDdzSkE5RERob3M3TzBBUnkwUURIU2hMUVR2V0dZUQ?oc=5) | - | 한국일보 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권투자자들, 금감원에 감리 요구…"JTBC 등 회계처리 조사" -](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9USmdOS04yVzNFQUhINmFtemVYdjhqYkpJYmN6TnlYMU9mdXQxWGtRQTVmek5kMXpZbjNOZ2kydEJWbFVzaGlZQS1vbUhJUmxDWkc0N3dZLVd1c2VhTURv?oc=5) | - | 조세일보 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 투자자들 “회계처리 의문”… 금감원에 감리 요청 - v.daum.n](https://news.google.com/rss/articles/CBMiVEFVX3lxTE1fS1hlUE9VYWpjdnRpb2JiTGxsVjJpUHNDZV9lQ1hmUVBkUDg3SVpBTjdiVG56R0w1OVlKT1VtVS1mbkZRRkkwSUR1cEpCeHFrSXRKRw?oc=5) | - | v.daum.net |
| 🔴회계신호 | IT | 네이버 | [美 회계기준 문의한 두나무, 나스닥 상장說에 "정해진 바 없어" - v.da](https://news.google.com/rss/articles/CBMiRkFVX3lxTFBuVTZwMGdTUzQycTVOUHBUOWZLR2pKZzBnY2cySDdSaDFsd2xXSHJHT0Q4YmxDQkZCQVRPWmxRSG5TUEtteEE?oc=5) | - | v.daum.net |
| 🔴회계신호 | IT | 네이버 | [두나무 美 상장설 다시 고개…“회계기준·행선지 결정 안 돼” - v.daum](https://news.google.com/rss/articles/CBMiT0FVX3lxTE03dEhZUTVITEEyRjlCMEFLbEx5MWF4NzNJY3FVUTZqWmMzVnIwNmk2NEQzMW9Qb0JaMWlLN08yQlJHdzJic3pGNlZVVW5oWG8?oc=5) | - | v.daum.net |
| 🔴회계신호 | IT | 네이버 | [[단독] 두나무, 美 SEC 위원장 면담, 회계기준 전환 완료...나스닥행 ](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPTE5PSW1ya182NWtnSDlMTmFrSkhvVC1xUmhPNG9zb3ZDZWd2RVVGalBvSFdmT0xMYUd3bWIxbkE1TkF3YVpPTWtxdlVZTUszdGExSTBNMFhBdkZaMkV3V2JpT196UXV0aDVFMmczaWpYbU5YVXpWbDd1Q1cxVmtEMWtfdzZ5WHZydGhB?oc=5) | - | chosun.com |
| 🔴회계신호 | IT | 카카오 | [카카오 노조가 놓친 '새 회계기준 함정'…"내년엔 성과급 0원 될 수도" -](https://news.google.com/rss/articles/CBMiaEFVX3lxTE8yRnFCUUFIUzY3YTR1cDZqdmRVODJWd0pWT3E2SnNFQjBlTlpLZ0ZQQV90cTk3bldhRmdDUm1WVmN6WUZ5aDhrRjlWOXFYZzUwRzJhVktoejFha051VjRCUEVDb2x2UE1u?oc=5) | - | ebn.co.kr |
| 🔴회계신호 | IT | 카카오 | [토스 재무제표 간단 분석 - 브런치](https://news.google.com/rss/articles/CBMiTkFVX3lxTE5ISHpzQXZzNnJmb1A1ZWlFeGlFYzBBTlRhYXBkeFJ1WU1vamtEemhuVjhvaUpFbHp0R01wN051WnRTWDdiZmRXZ0MxeDNPdw?oc=5) | - | 브런치 |
| 🔴회계신호 | IT | 두나무 | [두나무 "美 회계기준 검토…주식교환 마치면 IPO" - 비즈워치](https://news.google.com/rss/articles/CBMiakFVX3lxTE5XdU00TXFrTEJLcHI4RFFYcjVUMlIzV1VuVUVrSzFIcGwtdGVvc2pkQzJDOFgtTzlDZnVLNUxFM01ZNUNZVlNUUWNZV3cyTnYtZ3VqMkFyVEdTaGV4dUZoOGpMNndodC1Zd3c?oc=5) | - | 비즈워치 |
| 🔴회계신호 | IT | 두나무 | [美 회계기준 문의한 두나무, 나스닥 상장說에 "정해진 바 없어" - v.da](https://news.google.com/rss/articles/CBMiS0FVX3lxTFA4VkIydk1iNEwwOVhKSWNYQTVDYkkxcGxEeUJkQUtkWjBVZjZLQjFxcWtUdjBWUnFNVlNRTnZVTWthZzZ4c1I5QzNaaw?oc=5) | - | v.daum.net |
| 🔴회계신호 | IT | 두나무 | [‘445억 해킹’ 두나무 제재 돌입…금감원, 감사의견서 발송 - dailia](https://news.google.com/rss/articles/CBMigwJBVV95cUxQdjlHNElLRGJXMFBlQ2RTM3pDM1FJbTk1LTJrQ3lUbkdMQlI5Y2JNTjQwcmRST3A4RXlPeXlRanJpdFBKbXh4Z3JyWGk3QWxqY2ktLThTRDk3V0pTT3hua1JWV1NoRW4yMUctUXNNT2JMbkF2Tm1qVXl2YkNEeWUwSXhKemkwenhFbWsxbEUwb3pGa0hJR1N3U29JZVhhakFXVkxSRjZta1puN1ZKeTA2VW5ma3Nqa1JCYnhtd00tUXIyRGJGdm5TNGxBaTdaaEhtTFpkczRVSnAtY3hWaDRNNnZvc1RfZVZlZjV4enhvYUtXYkFrZllDZjd3QWVRMWhGYkg4?oc=5) | - | dailian.co.kr |
| 🔴회계신호 | IT | 더존비즈온 | [AI 거래관계망 신용평가 모형, 재무제표 한계 넘는다 - 전자신문](https://news.google.com/rss/articles/CBMiTkFVX3lxTFAyTXpadGpRZkN6M090ZElpTDFqQ1FHZEZnUERfcW43V1JQR2FGX0E0emRyNTFKZjB1V2tPWjJtQXJZa0M4WWFPOTNnTGxiQQ?oc=5) | - | 전자신문 |
| 🔵회계이슈 | 엔터 | 하이브 | [하이브, 역대 최대 실적에도 M&A는 ‘마이너스’… 1조원대 영업권도 부담 ](https://news.google.com/rss/articles/CBMicEFVX3lxTE1EclZkd2RpcVphX0ZoLUh2SHpodTZEZlBUazZxVTVfSWlXcWNQbXJKOHF0MUQ1MVcxc2puQlVOUV9zUjZlZDIzOEg2MmRFSmYyZ0V3cWlLaEtOSlV4QVA4NTRBUEgzVGNzX01BTnBXbW3SAXRBVV95cUxQNFZxR3lGNmx5Z0FHVlVOZjdEd0N2Yk1jaVNLem5zMHJWWmhpcFE0N1F3b3BZTXNyZTRIeU1CS0VNbGJ1cWdQWDZuUzM2cHlNWXRxS3NqYmRWalQ1cTJYM2FOWDVDa0hQNkhvd3lVTkI1alczVg?oc=5) | intangible-assets | IT조선 |
| 🔵회계이슈 | 엔터 | 큐브엔터 | [[더벨]큐브엔터 소연, 신곡 '퇴사할게여' 주요 음원차트 1위 - 머니투데이](https://news.google.com/rss/articles/CBMiaEFVX3lxTE5vMURKb1JiaGlzRTNyQXpycVZiMjVUTVFxbEM1WFAzVEdfZGtLRGZyTlFSUDZxdkpDZWZ1NklqNnZVVm1qQ3lVNVV3X2NtRDBPbmZZQ2xDbmY1T1ZWLS1sc0Y1SDF1ZjJK0gFuQVVfeXFMTWR5SUNMblBlb0dSUjRfMU1IbWc5OTNxUG1NaHhMTVVVd3dOZ3RxV0JNQUNOREVqLXMzRzV2Y09wNkV3cVI4QWZkSm82TjhqSWtGZk96Z3B6enFERnUxa01IaUFFdzg1UzNLZHR3UVE?oc=5) | intangible-assets | 머니투데이 |
| 🔵회계이슈 | 엔터 | 큐브엔터 | [[더벨]큐브엔터 소연, 신곡 '퇴사할게여' 음원차트·SNS서 약진 - sup](https://news.google.com/rss/articles/CBMiXEFVX3lxTFB2cXp4YURwOXRDOUl5ZW1fcnJyODR4cU51dEcwbnQyZldnNE9KOThHSV92eTN5bV94MlFldzVoaVpwcXJVV25CblExMi1MaUJsZl8tM1ZaYkpGaXM2?oc=5) | intangible-assets | supple.kr |
| 🔵회계이슈 | 미디어 | 위지윅스튜디오 | [초상권 라이선스 시대 온다…AI 버추얼 프로덕션의 미래[AI 생존법] - a](https://news.google.com/rss/articles/CBMiYEFVX3lxTE5UNzQzc0UxMVg1QkJuNU9XQWZGa1JtN0o3RFBGNkppVElBcXV0c2VMeXhrekF3ZmN5OXJ4UUZ2cGNGNlhPS3VyT2pNYXZ3Nmp1cXVVcThRblVSMXBhS3kyZA?oc=5) | intangible-assets | asiae.co.kr |
| 🔵회계이슈 | 미디어 | 스튜디오드래곤 | [[스튜디오드래곤 톺아보기] 판권 상각기준 전격 변경…'수익·비용 매치' 변동](https://news.google.com/rss/articles/CBMiT0FVX3lxTE9QU0VkMFAzbnhsQnl6amZPVTZYbUtabUVibF9FbmFlNXpLWnRJa0RneFJSNmE5T08xSGtOVFRGS1lpYzRweHdYSGdrUkhYWms?oc=5) | intangible-assets | 딜사이트 |
| 🔵회계이슈 | 미디어 | 스튜디오드래곤 | [[스튜디오드래곤 톺아보기] 판권 상각기준 전격 변경…'수익·비용 매치' 변동](https://news.google.com/rss/articles/CBMijwFBVV95cUxOeWRaSDJiY0JzY0l6SXlzMGtRVmdaYjZncDdubVBfUjlaNldjS081VlZicUM2UXRsXzVKbTZpdVlnb2xRa1JyNnY1cmxEaFNKQUNuZkZqRXppV2pSYW9iMFVsaFhHcHBzRHNZZmVVNm5hMjNtdTE2a3VsT21qam9YYU5uREpJOG1HQmdLR25Xaw?oc=5) | intangible-assets | Naver Blog |
| 🔵회계이슈 | IT | 카페24 | [카페24 식품·뷰티 거래액 '쑥'…2년 새 44%·38% 증가 - MTN 머](https://news.google.com/rss/articles/CBMiZEFVX3lxTE8wUTBtV2k5ZElfeVIyalB0cmJXYlc5cXdtQTNMUHhlN0FOV0hiVDY2TFNqUWl3TVpoWmZQQk9KZ19vd2pDelN6d3ZIdmZhV2VLU3BCTmlJWFY1Uk1LMGQ0U1FFdWo?oc=5) | platform-cases | MTN 머니투데이방송 |
| 🔵회계이슈 | IT | 카페24 | [카페24, 매치메이킹 상반기 거래액 2배 증가…메가 IP 협업 강화 효과 -](https://news.google.com/rss/articles/CBMiakFVX3lxTE54a0ljYnNwbnNQU2dQOVhNb0tRc1BpSFRROWdIaVBBSkxWaVlhbE1vck1xS1VZUlIyaXRQdXltcnZaV3YyRXNpMUFPNE1iWUtMRXNGU0VVU0V4TlQxc2VTVVByeFFLNUlwaFE?oc=5) | platform-cases | 뉴스포스트 |
| 🔵회계이슈 | IT | 컬리 | [‘떡지순례’ 열풍에 전통간식 거래액 쑥…컬리 6~8월 자체 매출 분석 - 농](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1wVXRvbElEanVWNHJpd2R6bjR2X2ttQkwxeWV2LVRac0NaUzUyWEVDaTFES18yMFlEbGRjSEY3TXRPc0d2VzV4SmVseHl2LVY5NlEwOGxYenVGUQ?oc=5) | platform-cases | 농민신문 |
| 🔵회계이슈 | IT | 컬리 | [네이버 ‘컬리N마트’ 출시 1년 만에 거래액 10배 성장 - chosun.c](https://news.google.com/rss/articles/CBMigwFBVV95cUxPVW51NzZPVE1ySWJCOFJ3Mkk5Y1czbWgwT0stUnlPQnhWVGVfaHpXQVFxa3dFV2p6dWtJRTd3ZTVZSU00TlltT0xVblpmWGtCOHZfWUJYeXFMWW9HQ3FfSG04TE43YjdKMDdVZWpOTFJXOW5ydEsxOWcyNHlMaW0wLVNYdw?oc=5) | platform-cases | chosun.com |
| 일반 | 게임 | 넷마블 | [‘나혼렙’부터 ‘니노쿠니’까지… 넷마블, 도쿄에 IP 4종 깔았다 - v.d](https://news.google.com/rss/articles/CBMiT0FVX3lxTE5KRi1OXzMxcWlFNFRUMXBMOVpja0hiUFB3dEdrQlAybnNINEhRT1FkSDJNN2d6cmhfZEhPaC1fU0FUMW9BdWl5eHBaSjVaRGs?oc=5) | - | v.daum.net |
| 일반 | 게임 | 넷마블 | [넷마블, 신작 3종 들고 日 상륙…'나혼렙' 신화 이어갈까 - 머니투데이 -](https://news.google.com/rss/articles/CBMibEFVX3lxTE9WSXd5MmdMaV9BRzEtZzVWXzFZTl9LYmZaelE1YllPTWFJaDYxTHFOR3h2UUZtLXJmaDhSWFBlLWgtMWE5S0lXTW5Fc0VDUXZzMG1ZRFY3SnF4SjZoRHdkRFNEb2tWLUhWZzFWMdIBbEFVX3lxTE9WSXd5MmdMaV9BRzEtZzVWXzFZTl9LYmZaelE1YllPTWFJaDYxTHFOR3h2UUZtLXJmaDhSWFBlLWgtMWE5S0lXTW5Fc0VDUXZzMG1ZRFY3SnF4SjZoRHdkRFNEb2tWLUhWZzFWMQ?oc=5) | - | 머니투데이 |
| 일반 | 게임 | 넷마블 | [“세금포인트로 아쿠아리움 30% 할인…넷마블게임박물관도 사용” - 세무사신문](https://news.google.com/rss/articles/CBMibkFVX3lxTE5CVG9uUnJfdEdmRFNDWmNqbENEWHVLdElkZzlBMkppUld2SDRDY1JQbWhEWURPb21VX1JEV1FZVlpUelMxYmdRRTZ1anRQb3RsLWRETjRUbkVHaHpOZlBLREhydnZuczNVYUZWVjBn?oc=5) | - | 세무사신문 |
| 일반 | 게임 | 넷마블 | [넷마블 방준혁, 도쿄게임쇼 현장 점검…"유저 목소리 살펴야" - 연합뉴스](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5ZUlhSRG1taEJmV0VzT3VKQ3pqMkw1dE1PQ19GbDJEY2pzSVJHZTZ5bWtlbndlXzZLbVAwdEp0bE5TME9BMUpRUXVKR2o0bGIzdmJGeW5GSG5CM0nSAWBBVV95cUxPUGZvQjVKYUY4bF9Ib3hHWVczU0tNWkgxOVNERWdDZXg2NzZ2cU41MGRvbnM1S3JObnBzOWhISG95SXRkV1FKUmI0VlJmc21LZHhRczl1RWlZUllZUU9Dcmg?oc=5) | - | 연합뉴스 |
| 일반 | 게임 | 넷마블 | [넷마블 '비장의 카드'…"日 인기 IP '샹그릴라 프론티어'로 승부" [TG](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBIaVRkWF9nRFF3RTU4SUZrVkN4aGVOa3p0SzlzUUg5dVV0V0NxYjJKVm9pcU44UC1qUmtPZVI5cC11blMyZHhiZ1d2MEY0MFpvLURSVUJhQ29Kdw?oc=5) | - | 한국경제 |
| 일반 | 게임 | 엔씨소프트 | [매출도 무대도 '글로벌'…엔씨, 포트폴리오 다변화 본궤도 - zdnet.co](https://news.google.com/rss/articles/CBMiVkFVX3lxTFBhbWRtOGxRNGd4UGV2d2IyUTZNQnNEdzFnT1FhemVLcVB2eDNIUmE4d2g2Z1hhWFQxb3hxanhSMTdrc0w3c2VjT19rSm5Md0ViTHFWbHpn?oc=5) | - | zdnet.co.kr |
| 일반 | 게임 | 엔씨소프트 | [네오위즈·엔씨소프트, 엇갈린 2026 전략… IP 확장과 아이온2 승부 - ](https://news.google.com/rss/articles/CBMiVEFVX3lxTE5nODZSOHdVS2NVYXgtWl90V2k5ZmF0Nm9nekxoc3dkaUY5MFd2WXpxTDJOTk5Na09uY25mYjFUR1JILTFmZGo3NTdUNlhkZmNDakZ4ag?oc=5) | - | :: 위즈경제 :: |
| 일반 | 게임 | 엔씨소프트 | [獨 쾰른 달군 K-게임…엔씨·크래프톤·크래프톤 신작 공개[게임스컴 2026]](https://news.google.com/rss/articles/CBMiYEFVX3lxTE1tMHo1TTVCT0twOU5tSFNnejk2M0pYTzR2OEo0bkJKc0ZjOG1UdmduM0hRNUdlWFZfYmlyN0RjeS14bHU5Wkl2ZU96OFk0MEo1U1dqdlB1VTc0VVVQTnFxb9IBeEFVX3lxTE55RGg4bGc5ODdoTzM1Zk15eG81dUppdkVmeE1NV0RkbmlxUEJhSWsxVzJfT0tRZnRNLTVzVndxRUJKZ3hjbkFTTkN6YzJrZDlYQXltT3NPVktKbERKbXlGTThqN3I5aFU5NDFBMWpMeU9xcjBrLVdsMA?oc=5) | - | 뉴시스 |
| 일반 | 게임 | 엔씨소프트 | [[리포트랩] '리니지 의존' 벗는 NC…증권가 목표가 최대 44만원 : 네이](https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBKVHdRTG14OUhBbXVLbmpFVTdYQkt3empJZXhPQjlaTEJmYjJBeHZqQ0QzRUZZX2hQV3AzS2tDWWgzWnd1R2M3eldKbXRORGdRaG1vQkwyaFhkczdZX1NoVnduUDBFd0U?oc=5) | - | Naver Blog |
| 일반 | 게임 | 엔씨소프트 | [게임업계, '신작+라이브서비스+글로벌' 삼각편대… 해외 매출 비중 확대 - ](https://news.google.com/rss/articles/CBMiaEFVX3lxTE5mMlFTa3NyTDlJdl9DU0s5U0Znd2diaTVXTjY2cllsYmxCdDVTNGhBZVFsRjZ2U1JFYzlHMzBKdXZqdjFDYVJaVWlxazA5cmhNRnp0SlNaTkJmWWxvMEFLQzd0TjNTdXlG?oc=5) | - | 녹색경제신문 |
| 일반 | 게임 | 크래프톤 | [CPU에 5070급 GPU 박았다...넥슨ㆍ크래프톤도 줄 섰다 - 게임와이](https://news.google.com/rss/articles/CBMiZkFVX3lxTE9JaW1nclpwbkRWNGNIaWtmWlpjUTEzbjR4cFdnTy1lSkc2V1BJSEJ5b1BQWmNpM1QtVVhfWTlXN3VsNGI1RWIxNllnYU9sMlRHRmhJdlhwOGgxWDdHRzVIUExPWG1sQQ?oc=5) | - | 게임와이 |
| 일반 | 게임 | 크래프톤 | [‘獨 대통령 첫 연설’ 달라진 위상… 크래프톤·엔씨 존재감 - kmib.co](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9tSEpwY05PWXJVVGdtYlVhU3BYS3lpZ1J5U090cVQxUE5seTRGcUhUeVhsSjl1b1VYeHpWSHoyWTYweHdHREQ5MnpXWTY2NzVHRzNmZXZaaHQwSHlRV2xtZ1QxdjdFRDTSAWxBVV95cUxQWm94NU9TYUJIaWJRbzYxUHlQYzM1dWxwR2RCNHJKTy1iZ2s4MW5DdUl6T000VkszVW1HS3pxaFRLeVl3QTNUaVMzTVE3MUFoMXM2aEQyMTFVQUlpdm5ZeDh2N2lkdmF5ZkhjTzI?oc=5) | - | kmib.co.kr |
| 일반 | 게임 | 크래프톤 | [크래프톤, 배그 대회 '외부정보 확인' 사과…마지막 경기 결국 취소 - 뉴시](https://news.google.com/rss/articles/CBMiYEFVX3lxTFBqVnVfYnJHd2tLLTRDc0ZYSjZBLUhlSWhld2xuNjB1MXFDNmFWemR6d1ltQzJ1SV82S3RMVk8teHc1WmViU2hmcGRzbmtRUDYtSTJUZmZIU3lvb2ZTdFhxUdIBeEFVX3lxTE4yeU5oWkIxRWV5dVdnQUd4VXBmNEl1eURoZkN1TlBycXd4dEk4WEZrTjNCWFdkNF91N0ZTTHZnSGlWZWw4cEdUdEtxN1Jjc3VwR2hWdlFtY3RyOTgwWnRKd3p1Y0I3NUJZZmtla2oxLVc0SmtwV2U0Xw?oc=5) | - | 뉴시스 |
| 일반 | 게임 | 크래프톤 | [5민랩, 신작 ‘세계허구관리연맹: WPCA’ 첫 공식 트레일러 공개 - 크래](https://news.google.com/rss/articles/CBMiswJBVV95cUxNejhMcTVvRDAzSkFweGlNVURXaFpvT21iWHM3WnFvdlhOY09aSjJzTERTZktCQnZ3ZjY1VGJXUzlXV1d4Q29wU3k3MzRZSGd6c21lWWxzU3lLdW02aGl4WmFqNnlPeEFYYjA2a0lVcFZNZ2w3UnV5QmdPa1VETHZxT1V5XzlrSWFZdm5uOTVFbVJacW5uR0F5T25HY3hBYlBmWTI5dnYwMkppbWVKd3BfZ2J4Tm9DU29nWEpDdUlrM0FCVWpETWtMQ1JDNE52dEZfd3pFSXUzMUN0Q1Zvc0ZVRUpqakV1a3M3YmV6dWFpS015eU5VVV9RS3BUQmM0X2tGU3RVQ0UyZUFJdUN3Mnl3dF92THEwVE5SLUVTdzFYbllPLXNDTGplZU15NjE2X2EyZ21n?oc=5) | - | 크래프톤 |
| 일반 | 게임 | 크래프톤 | [[단독] 크래프톤-한화에어로 방산 합작법인 설립 사실상 무산 - chosun](https://news.google.com/rss/articles/CBMigwFBVV95cUxQWm5EOFhGcl9pbkE1cVJfTi1Oa29wd0Zta1FnR1U0VExRN29sS0NMeVg0X3NTdkVRNFpOZVpFN0wtcWNHVld6UlBFQm1Jd3dKRUJWLUVERU9RakRNZXFkcUdIQXE4S2FuNVB6ajVzcTd6UHNHT0l1c3JlZUNMODRiQTVfbw?oc=5) | - | chosun.com |
| 일반 | 게임 | 펄어비스 | [600만장 흥행 뒤 찾아온 ‘신작 절벽’…펄어비스 주가 휘청 - 한국경제](https://news.google.com/rss/articles/CBMiWkFVX3lxTE4yUUZjZU1fdnkyNlJ5V2c4Tm1OdUhXM0dIT29OS1Zxd2E5UUswNkhMMWtaajlJRkIxMkVKaWpoX2Z6ZVVrSWl2a1pkTGdSUUpxVjNpNWJSR2JkZw?oc=5) | - | 한국경제 |
| 일반 | 게임 | 펄어비스 | [펄어비스 '붉은사막 인핸스드' 출시, 전 플랫폼 첫 20% 할인 - pear](https://news.google.com/rss/articles/CBMiZEFVX3lxTE5ka1dQVW0tMnE2QWVVT0hlOHp6Ul94OUhxb0VrUmdacXh3aVZlU2F3cEh0TElhdzRpTkl6WFRYVWFxd203eEVpakdhQndLOVNrbjZTVlJwV1lkVklGcE1vU0NPNlA?oc=5) | - | pearlabyss.com |
| 일반 | 게임 | 펄어비스 | [펄어비스 ‘붉은사막’, 게임스컴 어워드 2026 2개 부문 후보 - sent](https://news.google.com/rss/articles/CBMiZEFVX3lxTE1BQUxYbnotY3Rja2htMWo2aFUzUnM0eFM4LWdpRC14X3UxU3pLRTBYcjVWaWlRWVZEQXI5RU1GSHZnVXVsRG1RSXVmRHpObWlwWXl4VURhMUZ3RHYzWEtXcW9kTms?oc=5) | - | sentv.co.kr |
| 일반 | 게임 | 펄어비스 | ["닌텐도·소니도 관심"…펄어비스, '붉은사막' 기술 노하우 공개 - 머니투데](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE53cWFFZ2RkX2Z4bWN6SkNsazV2UVlyTTg2V0pQcnYzMnFLNFY3TDVmeHVfODBRSi05NmNvdk9RTFpvT3RGZ3hKWm9RdWZQV0ZwZWM4Ym5OeFZxOEs2N21YM2hRNTA5ekHSAWxBVV95cUxPeURiTldpR2FnQTJZak1qclJYWG9lQjVHNHZOdXNXNUdaQWVwaHZ1eW45ZlZhUl9mRHJUX3c2R2JHbzhaMy03MnI0Y3hsVk11Z3JOTFNYY2w1YkQyS0xNSndPWGZhRndPQWV3NkU?oc=5) | - | 머니투데이 |
| 일반 | 게임 | 펄어비스 | [3년 적자 단숨에 지운 붉은사막···펄어비스 새 기록 쓴다 - 뉴스웨이](https://news.google.com/rss/articles/CBMiakFVX3lxTE9yZmtDcXZXM1BCd3V5aWdjaUJ6YmFMM2VpMUZfY2tyZUJWaTl6MDU0TVdXdmF6Nm1UdlBRaTgzdDdfRHhWZXozb1g5OGZYQTRkLWp2cFgxcnQ2WVNYajBlTVVXejM2RlBjQlE?oc=5) | - | 뉴스웨이 |

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
