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
_최종 갱신: 2026-10-05 10:51 KST_

**수집 현황** — DART 공시 154 · 뉴스 338 · 회계법인 리포트 1

### 📄 DART 공시 (회계 이슈 필터)
_종류별: 실적 71 · 📘정기 54 · 🔴정정 8 · 🟡주요사항 21_

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
| 🟡주요사항 | IT | 컬리 | 20261002 | [주요사항보고서(주식교환ㆍ이전결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261002000047) |
| 🟡주요사항 | 미디어 | 제일기획 | 20260930 | [주요사항보고서(자기주식취득결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260930000006) |
| 🟡주요사항 | 엔터 | 디어유 | 20260929 | [주요사항보고서(자기주식취득신탁계약체결결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260929000178) |
| 🟡주요사항 | 게임 | 시프트업 | 20260910 | [주요사항보고서(자기주식취득신탁계약해지결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260910000386) |
| 🟡주요사항 | 통신 | 케이티 | 20260909 | [주요사항보고서(자기주식취득신탁계약해지결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260909000349) |
| 🟡주요사항 | 통신 | 에스케이브로드밴드 | 20260827 | [주요사항보고서(회사분할결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260827001001) |
| 🟡주요사항 | 통신 | 에스케이텔레콤 | 20260827 | [주요사항보고서(자기주식처분결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260827000390) |
| 🟡주요사항 | 엔터 | 하이브 | 20260825 | [주요사항보고서(자기주식처분결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260825000350) |
| 🟡주요사항 | IT | 카카오 | 20260821 | [주요사항보고서(회사합병결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260821000052) |
| 🟡주요사항 | IT | 카카오 | 20260821 | [주요사항보고서(회사분할결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260821000047) |
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
_구분: 🔴회계신호 23 · 🔵회계이슈 12 · 일반 303_

| 구분 | 업종 | 기업 | 기사 | 회계토픽 | 출처 |
|---|---|---|---|---|---|
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [금감원, 메가박스·콘텐트리중앙 회계심사 돌입…자금 조달·회계처리 점검 - K](https://news.google.com/rss/articles/CBMiW0FVX3lxTE54OUVMRE9hMTAyNThval9sRFV5ZDNOeFBHODQ2bmdNQmh5WU41UWtJU2RrZ2ttcEZ0SFhkRm03QjM5R3cxR21pbTJKUFU5ZzFCbEFTSFIwN3hWQUU?oc=5) | - | KBS 뉴스 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [유동부채 1.4조 늪…’적정’ 받던 콘텐트리중앙, 5개월 만에 ‘의견거절’ ](https://news.google.com/rss/articles/CBMirAJBVV95cUxNVUpYMW9JNnd4Y0pRNVNyVkttRXZtOERwekxJX2JraWZrdlpIQkRVSU4taktUNHRCOVVvd21GcVAwd0NlVmJEYVN4WnVsOU5GenZnTlhBQVFpZnRqSVR4bUp4dEJyN081UDFzR2Izb1E4aWhqTFhSLUxyT09QUm1fN3pNbkxXa0xHdURhSGdQYkcwUUp5ODBOeEFwQUYtZG5QOGwxUmR0SVZuclNpRkFuQTB0SHY0QmhWaVVyX3BqaFg1OWVyZmsxWU9ybnp3WVM0eTBGRzJrQWpuRWZoUzVqbGV0QnZHOGhrRTZtUlJxeTRhTnpnUjVKeUZKYWdYd1RiVlRMRy1OSFVRdVdBUHhHSGRtQ0JGWVdOMDc0WWVleUh6WHlUX0VCRVQtdTc?oc=5) | - | 뉴스필드 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [금감원, 메가박스·콘텐트리중앙 회계심사 돌입…자금 조달·회계처리 점검 - v](https://news.google.com/rss/articles/CBMiRkFVX3lxTE80LURCejkydGZMLWJjaVZjYncwZWZaSkZPZmZtYTRNU0F0TFNEN29RSG5RYlRNcFlTY3VkVGNET2p4RXZFTWc?oc=5) | - | v.daum.net |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권 피해자 대리인단, 금감원에 감리 요청 - 법률신문](https://news.google.com/rss/articles/CBMibkFVX3lxTFB4OEZyLVFxM2lFejNpZm5vRmgwNDAzeWh5TElpVEpxNFhWZ3FJRndLTk5fTF9kWGE0aUdrTjM3S0lCamZ2V3Y4TE03LUNSTmpfTHZsaXROZ1JJeEYzaC1jek9ZRTZudnU2dWRORFdR0gFyQVVfeXFMTlJuUTUzcVYwLTIyMWhZWnFRYVBNc2FPU251QVYyU0V2cXUzU2RvV3RlTS1PMWVXeVNvNElNOTIwWnhXcXRrV1pKdURYZHo5emlVcWR0cC1tc0kxTUlZSVZ0TFBKSGxCUmZDNndnZGg4ZHNR?oc=5) | - | 법률신문 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권투자자들, 금감원에 감리 요구…"회계처리 의문" - 연합뉴스](https://news.google.com/rss/articles/CBMiW0FVX3lxTFB1Ukx0THpTTk1DSVh2VGtQU2hsZTBuZWhlRWhzLUFKNGY0dm1RZkgwdDIxMXdaTzhkTXozUXltRTlOS2VOZ25SdGlfLVY1WVhsYUVfWmMxTERDUmvSAWBBVV95cUxQRDRMM1RQYmYwcGlUY1o2YmZfWTNKQlRDU2JkTmxWNnFlVEs4cTFCOElOR1MyUjhyb0twN18zMkNINldZOE1ZSTNKVVJWdmRDOFZ4S2M2OTVoVHVaWDRHUHo?oc=5) | - | 연합뉴스 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [“돌려막기로 자본잠식 숨겼나”…중앙그룹 채권투자 피해자들, 감리 요구 - 한](https://news.google.com/rss/articles/CBMickFVX3lxTFBDSS1uQk52SXBhb1kycHJkNU5na0w1cmtyUm1hSW5KM2YtQkZWUy1TYlVfT2F5NHhUdElibTdhaExkblFZWExucFBXeVRpM1FkcTNvdm41dHpaODZEVzhScldkQ2FwTnRjZmJWTll0Z3p6dw?oc=5) | - | 한겨레 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권투자자들, 금감원에 감리 요구…"JTBC 등 회계처리 조사" -](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9USmdOS04yVzNFQUhINmFtemVYdjhqYkpJYmN6TnlYMU9mdXQxWGtRQTVmek5kMXpZbjNOZ2kydEJWbFVzaGlZQS1vbUhJUmxDWkc0N3dZLVd1c2VhTURv?oc=5) | - | 조세일보 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권 투자자 금감원에 감리 요구 - 조선비즈 - Chosunbiz](https://news.google.com/rss/articles/CBMigwFBVV95cUxOZ1BZZWVoNlItVU8zZTdWOTBmWVpncDBDUnMyenNPYUhNbWFDRDRlTjZpbzd6MnFxWHhzeWdmb01Jci1QRnN4UU83M0FmcHNTZ21HQmpxSF80WmxIMWRmcldCYmZhZUd4amk0bUtFazJnMVNOZklrZUp2ZjVPb2dFY2xJUdIBlwFBVV95cUxObmZVWHNYUEZEcU9BUUpKQXl1bmNJblA1ZkVvWlZ6bDExdWZkT2JWdFlnR3B0SGdBMWxQVmZrTUdzSlZiQ3FiV1pHU19FZ3M0WHlVMng2dDdpRW1ZUTRnalV3Ri1keE1rOHJVSkpHVUE3Y29jNzltSFNtZ0pOWUQ0OWJHOV9laHY3X2Z4WkdxZktNaHlzTWhn?oc=5) | - | Chosunbiz |
| 🔴회계신호 | IT | 네이버 | [두나무 "美 회계기준 검토…주식교환 마치면 IPO" - 비즈워치](https://news.google.com/rss/articles/CBMiakFVX3lxTE5XdU00TXFrTEJLcHI4RFFYcjVUMlIzV1VuVUVrSzFIcGwtdGVvc2pkQzJDOFgtTzlDZnVLNUxFM01ZNUNZVlNUUWNZV3cyTnYtZ3VqMkFyVEdTaGV4dUZoOGpMNndodC1Zd3c?oc=5) | - | 비즈워치 |
| 🔴회계신호 | IT | 네이버 | [두나무, 美 회계기준 검토 …“아직 결정된 바 없어” - 전자신문](https://news.google.com/rss/articles/CBMiTkFVX3lxTE5HZTFwRHZlQ19keGRBM3pQYkk2THNlZjNKRzFmRjNnMV83OFRyLUQ4elVxV2M4ZUV5eTJTSFdleEZtZUNORTVpc1NNTU1iZw?oc=5) | - | 전자신문 |
| 🔴회계신호 | IT | 네이버 | [[단독] 두나무, 美 SEC 위원장 면담, 회계기준 전환 완료...나스닥행 ](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPTE5PSW1ya182NWtnSDlMTmFrSkhvVC1xUmhPNG9zb3ZDZWd2RVVGalBvSFdmT0xMYUd3bWIxbkE1TkF3YVpPTWtxdlVZTUszdGExSTBNMFhBdkZaMkV3V2JpT196UXV0aDVFMmczaWpYbU5YVXpWbDd1Q1cxVmtEMWtfdzZ5WHZydGhB?oc=5) | - | 조선일보 |
| 🔴회계신호 | IT | 네이버 | [두나무 "美 회계기준 전환 사실 아냐"…나스닥행도 '미정' - ebn.co.](https://news.google.com/rss/articles/CBMiaEFVX3lxTFBJblR6OS1vc3JSNDhlYUctWUE5TVRPQ29uclIwNG04SGpKQTE0Q0pzYWlIWjVsTERpSHlBemR5OXd3RUhya2liQlRRZ1NtWFpnM3BBMUotdXNiS2NHTmhkb1RscnpjYTJO?oc=5) | - | ebn.co.kr |
| 🔴회계신호 | IT | 네이버 | [두나무, 美 회계기준 검토…상장 국가는 미정 - 아주경제](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5QZmxPY1VoZDBoeVMtNUptQUU0Skkza3I3d1NISVVrWDRNWk84QklUUlFaeGRydWVRNDV2eDFTb1d4elNoRkFEOWQyUGdLbGQwYllhUFZDcm9yZ9IBWEFVX3lxTE5XNHNNNGppTzJzWG5IdjQ2eUF6OHJTT2M0T1JoTGx3ZVNmQ2FiaFY1Q05jTnFQYnl4WjZySnJGTnU3d0sxWEwyZ3l6UzJ3X1gyWFRDUm1qZUE?oc=5) | - | 아주경제 |
| 🔴회계신호 | IT | 카카오 | [토스 재무제표 간단 분석 - brunch.co.kr](https://news.google.com/rss/articles/CBMiTkFVX3lxTE5ISHpzQXZzNnJmb1A1ZWlFeGlFYzBBTlRhYXBkeFJ1WU1vamtEemhuVjhvaUpFbHp0R01wN051WnRTWDdiZmRXZ0MxeDNPdw?oc=5) | - | brunch.co.kr |
| 🔴회계신호 | IT | 두나무 | [두나무, 美 나스닥 상장 준비 추진…US GAAP 재무제표 전환 완료 - 블](https://news.google.com/rss/articles/CBMiUEFVX3lxTE5EN3V6bWdoNE5Ld1VrUDFPeEhKTHdTZFlKbEtmdWw3UkVwYVppeXJCeDJmVE9ER0JtVHBiZXUycktwUjAtRklmNDdJM1VRTjVI?oc=5) | - | 블루밍비트 |
| 🔴회계신호 | IT | 두나무 | [‘美 회계기준 전환’ 나스닥 상장설 솔솔…두나무 “사실 아냐, 상장국가 미정](https://news.google.com/rss/articles/CBMiYkFVX3lxTE1UdlAwTl9kVEhJTm1fdl9QVU5NbjdUVm5VYWVJbnhOQlNBbUM4bk94THdKNmJaa1BDeEtFNDY4UVVEeGZ3YjdaeFdUZTRvOG04dU1aMnl6SWlKLXpMbk5Xc1N3?oc=5) | - | 디지털데일리 |
| 🔴회계신호 | IT | 두나무 | [美 회계기준 검토에 SEC 접촉까지… 두나무 ‘나스닥행’에 쏠린 눈 - 서울](https://news.google.com/rss/articles/CBMib0FVX3lxTE1MS1Vrc0pBUkhkV2Q0ZWFJSUFMMHdzaWl2c2ZGb215TXZXQkhMbEpjX09RX0JUSk1DX3cyOHBIZ21FSkF3YkJpeFo0cEdpbGVaYm5tLS1tSGJYeXlqVFhXUkNPVXdETWRNZlNQNlJxbw?oc=5) | - | 서울신문 |
| 🔴회계신호 | IT | 두나무 | [두나무, 美 회계기준 검토…주식교환 마치고 IPO 추진 - 데일리안](https://news.google.com/rss/articles/CBMiowJBVV95cUxORkhSRHFOcm5yVWpQS2ZtdDZVeU1nX2VLMmhIVDVDb1B6aHF2YW92a1g2cFNzeVF5OF9tYjdCWHBRandoVlZmd0d1UlpSRUpRTllfWENQcExENE1Ga2hsVVNEb09JUkc5SER0NXUyTTJMYWdIdHFVai1lVmZRemk4RG5zV2Q2aTBzdVpRZTFUbm9TbWxvTy16YVN1eVY3TkpOWk5CNF8tUkZZQkF3WkMxeUVwVjlTWExrSXVVWm9GRWdRNi1rT0x2UTlYN2s2RkFnb2w4N0J0eGtOQ2EzSjVWVVpnVnZvRzV5TG9LWW9neGlDUGZHSXdIb0FNOGtpaUhYUmRpcEduZDZUcG9sVFloQi1Tbm9KN2pWQWxYbHYtRk1Pa3c?oc=5) | - | 데일리안 |
| 🔴회계신호 | IT | 두나무 | [美 회계기준 문의한 두나무, 나스닥 상장說에 "정해진 바 없어" - 아시아경](https://news.google.com/rss/articles/CBMiYkFVX3lxTFBianJSX3pLc1hBSWdwTlhTMXdNNEJfXzItZ3JIX3dNRGJZQVZMX0swNTEzbFl2WThNbWdHV21jNV9XV0lsY25idnRXTjEyUHp3VF9yVHVPRVpGd3NfYmZMVHd3?oc=5) | - | 아시아경제 |
| 🔴회계신호 | IT | 두나무 | [‘445억 해킹’ 두나무 제재 돌입…금감원, 감사의견서 발송 - 데일리안](https://news.google.com/rss/articles/CBMigwJBVV95cUxQdjlHNElLRGJXMFBlQ2RTM3pDM1FJbTk1LTJrQ3lUbkdMQlI5Y2JNTjQwcmRST3A4RXlPeXlRanJpdFBKbXh4Z3JyWGk3QWxqY2ktLThTRDk3V0pTT3hua1JWV1NoRW4yMUctUXNNT2JMbkF2Tm1qVXl2YkNEeWUwSXhKemkwenhFbWsxbEUwb3pGa0hJR1N3U29JZVhhakFXVkxSRjZta1puN1ZKeTA2VW5ma3Nqa1JCYnhtd00tUXIyRGJGdm5TNGxBaTdaaEhtTFpkczRVSnAtY3hWaDRNNnZvc1RfZVZlZjV4enhvYUtXYkFrZllDZjd3QWVRMWhGYkg4?oc=5) | - | 데일리안 |
| 🔴회계신호 | IT | 두나무 | [두나무 美 상장설 다시 고개…“회계기준·행선지 결정 안 돼” - v.daum](https://news.google.com/rss/articles/CBMiT0FVX3lxTE03dEhZUTVITEEyRjlCMEFLbEx5MWF4NzNJY3FVUTZqWmMzVnIwNmk2NEQzMW9Qb0JaMWlLN08yQlJHdzJic3pGNlZVVW5oWG8?oc=5) | - | v.daum.net |
| 🔴회계신호 | IT | 두나무 | [美 회계기준 검토에 SEC 접촉까지… 두나무 ‘나스닥행’에 쏠린 눈 - tw](https://news.google.com/rss/articles/CBMieEFVX3lxTE9yMXZ0VFVsc2gyWk1NanJTUkl0U18zZ0VIVURLbWQzeXBSYkR2RFhVUUZhWWNZTnBOemdFcE9MaElZTm02ZjRic1NGckNaS0hlRDE1N0RiU29rVXJxUVhiNjRKT3p0WnBrUmw3X0VHRHQwdWpnYmY2eQ?oc=5) | - | twig24.com |
| 🔴회계신호 | IT | 더존비즈온 | [AI 거래관계망 신용평가 모형, 재무제표 한계 넘는다 - 전자신문](https://news.google.com/rss/articles/CBMiTkFVX3lxTFAyTXpadGpRZkN6M090ZElpTDFqQ1FHZEZnUERfcW43V1JQR2FGX0E0emRyNTFKZjB1V2tPWjJtQXJZa0M4WWFPOTNnTGxiQQ?oc=5) | - | 전자신문 |
| 🔵회계이슈 | 게임 | 위메이드 | [위메이드 2분기 영업손실 210억 원... 라이선스 매출 제외로 적자 전환 ](https://news.google.com/rss/articles/CBMiaEFVX3lxTE1nZHF1TXVhVUNLRnVZVnpTUzdSZlBnZjhZRHZIU3owYl9RQjNUQkY2aDBicjFQa3hmLVlGbmlNaGJhVVEyRkVxa2NYeE1CZ0Nsc2hkWFJtTkVqcjI1c1kwU1djVXV4a3dM?oc=5) | intangible-assets | ipnn.co.kr |
| 🔵회계이슈 | 엔터 | 하이브 | [하이브, 역대 최대 실적에도 M&A는 ‘마이너스’… 1조원대 영업권도 부담 ](https://news.google.com/rss/articles/CBMicEFVX3lxTE1EclZkd2RpcVphX0ZoLUh2SHpodTZEZlBUazZxVTVfSWlXcWNQbXJKOHF0MUQ1MVcxc2puQlVOUV9zUjZlZDIzOEg2MmRFSmYyZ0V3cWlLaEtOSlV4QVA4NTRBUEgzVGNzX01BTnBXbW3SAXRBVV95cUxQNFZxR3lGNmx5Z0FHVlVOZjdEd0N2Yk1jaVNLem5zMHJWWmhpcFE0N1F3b3BZTXNyZTRIeU1CS0VNbGJ1cWdQWDZuUzM2cHlNWXRxS3NqYmRWalQ1cTJYM2FOWDVDa0hQNkhvd3lVTkI1alczVg?oc=5) | intangible-assets | IT조선 |
| 🔵회계이슈 | 엔터 | 큐브엔터 | [[더벨]큐브엔터 소연, 신곡 '퇴사할게여' 주요 음원차트 1위 - 머니투데이](https://news.google.com/rss/articles/CBMiaEFVX3lxTE5vMURKb1JiaGlzRTNyQXpycVZiMjVUTVFxbEM1WFAzVEdfZGtLRGZyTlFSUDZxdkpDZWZ1NklqNnZVVm1qQ3lVNVV3X2NtRDBPbmZZQ2xDbmY1T1ZWLS1sc0Y1SDF1ZjJK0gFuQVVfeXFMTWR5SUNMblBlb0dSUjRfMU1IbWc5OTNxUG1NaHhMTVVVd3dOZ3RxV0JNQUNOREVqLXMzRzV2Y09wNkV3cVI4QWZkSm82TjhqSWtGZk96Z3B6enFERnUxa01IaUFFdzg1UzNLZHR3UVE?oc=5) | intangible-assets | 머니투데이 |
| 🔵회계이슈 | 미디어 | 스튜디오드래곤 | [[스튜디오드래곤 톺아보기] 판권 상각기준 전격 변경…'수익·비용 매치' 변동](https://news.google.com/rss/articles/CBMijwFBVV95cUxOeWRaSDJiY0JzY0l6SXlzMGtRVmdaYjZncDdubVBfUjlaNldjS081VlZicUM2UXRsXzVKbTZpdVlnb2xRa1JyNnY1cmxEaFNKQUNuZkZqRXppV2pSYW9iMFVsaFhHcHBzRHNZZmVVNm5hMjNtdTE2a3VsT21qam9YYU5uREpJOG1HQmdLR25Xaw?oc=5) | intangible-assets | Naver Blog |
| 🔵회계이슈 | 미디어 | 스튜디오드래곤 | [[스튜디오드래곤 톺아보기] 판권 상각기준 전격 변경…'수익·비용 매치' 변동](https://news.google.com/rss/articles/CBMiT0FVX3lxTE9QU0VkMFAzbnhsQnl6amZPVTZYbUtabUVibF9FbmFlNXpLWnRJa0RneFJSNmE5T08xSGtOVFRGS1lpYzRweHdYSGdrUkhYWms?oc=5) | intangible-assets | 딜사이트 |
| 🔵회계이슈 | IT | 카페24 | [카페24, 2분기 거래액 역대 최대…공격적 투자에 영업익은 27%↓ - 디지](https://news.google.com/rss/articles/CBMiYkFVX3lxTE9zQllFX284RGRhUFBRMnFWdnc4UVNEUXVVMjJsLUpXMnpLZHlMSUFESHBBX0xrTEJMNUNEUnFlRFR6Nl9ydjJyZVJxSFJkNHV1V0tVY2NlUXVPck1fenQ0OW5B?oc=5) | platform-cases | 디지털데일리 |
| 🔵회계이슈 | IT | 야놀자 | [야놀자 상반기 거래액 21조 원, 매출은 14% 늘어 - 플래텀(Platum](https://news.google.com/rss/articles/CBMiSEFVX3lxTE9oLUxuSEtkVnhuYnVzd19uemVJTmUyUHM3aEZwcjM1WUtad0hfM2dVY0ZPYTh0Q2JUZVNBQS1GMTY5cS0zMzhUSA?oc=5) | platform-cases | 플래텀(Platum) |
| 🔵회계이슈 | IT | 다우데이타 | [[단독] 삼성 초기업노조위원장 최승호 조합카드 마일리지 개인귀속 결제액 5억](https://news.google.com/rss/articles/CBMic0FVX3lxTFBmSGVfcWpLTGI5Q0wzellQWEc2LWRoNF9qUnN0SVVCeDNqRXJMRGcwQ21Deks4MW1CSURZUTliaTIxX2JQMXFFdW9PSHV4dWtCMWw3a3J0eWRfS3NsNTJ5cDZiNk9GSUhZWVNFb1gzdExJSHc?oc=5) | platform-cases | 비즈니스포스트 |
| 🔵회계이슈 | IT | 메가존클라우드 | [제주콘텐츠진흥원, AWS·메가존클라우드와 협력…콘텐츠산업 AX 본격화 - 제](https://news.google.com/rss/articles/CBMib0FVX3lxTFBQU1U5NGxtamZtU3h1WFpPVEpQdmUtMHNmV3dkNzB3NV8yS3ZvXzVqM1dqMFM3dXV5VHBvLUVVbnFtWVNUcEFIUUYtbHREYnJGZ3VLNE13aVJGXzZiV2d0bEExOGJoRkVSODNVRjRvaw?oc=5) | industry-structure | 제주도민일보 |
| 🔵회계이슈 | IT | 무신사 | [[분석] 6년 새 17배 뛴 무신사 계약부채… 급증 구간서 두드러진 ‘선수금](https://news.google.com/rss/articles/CBMibkFVX3lxTFBGSW9pVWhhZlVmU0p5ZjkwSENKYUQxbVBabl9ZNi1CT2ZNUS1zQXBDRHhiUHd5YUJQUXo3bFFnTkNsRW5DWFpyLXpqSWNsNzVFQUEwQTljTFFZc1gyRHYtSUNYMHpPVlFqZ21TbnlB0gFyQVVfeXFMT3FJNmFxLVNraEcxdlFTY1FJWXZjdWd5a3ppZTJLSHppUXhuOEZNVlhHTmhhamRmSFpKN2ZWRUdzWE8wSjRSY0lURGVYTURkdHIzTXFjVVdZck5PdlkwSV9OMnV5Nk5WRmp4OS14MzVVcHpB?oc=5) | ifrs15-revenue | 시사프라임 |
| 🔵회계이슈 | IT | 컬리 | [컬리어스 '파인에비뉴 A동' 매각 자문 완료…누적 거래액 3.2조 돌파 - ](https://news.google.com/rss/articles/CBMigAFBVV95cUxObnp3cHV6Q3owZl9USWgxTGFiN3hpWmVtdTItandyQlNBSHJBMUtVRXF1ZmgwamRER3A2bzl3ZWNHY1J1UlhBdWRLd3ZuWjg5Mkt6SkY2WFZPQXo2R3l4QjVGdVBwOThVYWxsNFlNYXhTcW42MEpyS3VNSFU2N1c4Zw?oc=5) | platform-cases | edaily.co.kr |
| 🔵회계이슈 | IT | 컬리 | [‘쿠팡 겨냥’ 네이버·컬리 장보기 동맹 1년… 거래액 10배·이용자 2배로 ](https://news.google.com/rss/articles/CBMiigFBVV95cUxPQlFpRHZValFLNlNtTnJobG50SkxodEdfS2RPangyLVFMaWxtaU5ZanlwemtKcy00djczYjI0SjQ4aFpIZDVwSnZPVWY5OEVObFMtMjJVblQ2anVKWTNfazRiN1dJakdGSkdMaEdycTVZc2Y3NFdpQVVFcGxXVkU4bmRBMWRoYmUtRmfSAZ4BQVVfeXFMT1Zlc2VrQ1RmdERwclUyQ0VyMm1lVWJIRC1wbldZRWVDVnNyT0JtVHRwRk5mMzV3UmJLTFdOZHJJUms4Q21tNjAxMDJMcnhUYzFHa2tUeXFWMW5PRkkxOFA2YS1RNUo4TWp5bmYzWlVhVzdGYi15WThJa3g1RzBDc1ZqLU84cmhkMTBMZFJ1TmNxYlA4d2tTcG80X2UxeWc?oc=5) | platform-cases | Chosunbiz |
| 일반 | 게임 | 넷마블 | [넷마블 '몬길: 스타 다이브' 등 게임 3종…'올해의 우수게임' 수상 - 머](https://news.google.com/rss/articles/CBMiZ0FVX3lxTFA2ZmNJcV95N09UWERxSlNLQ0ZiVm8yNGlMTEpWWFBQeHNsbGRUNlJSR1EwTDl0em1UWGRYV3FIMzljVlBuM25vWGo3LXA3azNpVjdaU2ZRdXJISU50M3QxM0NnR2kycHfSAWxBVV95cUxONFFKU28zMTVmXzZzSGhySGluSlBmUmttakdhMnQtQjhWNkdYRU11dXJqTElHaDJiU095YnNIV1VWNURVblE2LU5OSjc2SlRxRGNmX0N3b2h5MDlscExyS3JQbVJsMVVMNy1Cb3M?oc=5) | - | 머니투데이 |
| 일반 | 게임 | 넷마블 | [상법 개정 타고 거세진 행동주의… 넷마블 vs 얼라인, 코웨이 지분 매입 경](https://news.google.com/rss/articles/CBMigwFBVV95cUxQZFd3dmVDOUJkSHFJOGx0aG00WTVKeEZzcks0d1JOY3p2TUNxNjAzcHlXT1hLMzBVZ2dfQ29WdnpVSDZKb3h0cXNWSHBCRHZGdUI0YXp4eHN0RnJoZnV6ZWhkdDIyLVA4WWMwNjZhdFoxY2NYNDFWdXVJNkZ3bHZBWF9oYw?oc=5) | - | 조선일보 |
| 일반 | 게임 | 넷마블 | [[클릭! e 게임]넷마블 ‘세븐나이츠 리버스’, 日 애니 ‘귀멸의 칼날’ 협](https://news.google.com/rss/articles/CBMiUEFVX3lxTE9WS2REc2Zjc3JEcEgxd0t4NWVUMmFuRERqcEphZDV1Y2JOQ3RGUUJwaDlmcFdVQVBaeHFmNUEwSGtIVTNNeVVMQnQzT1dxckVR?oc=5) | - | 문화일보 |
| 일반 | 게임 | 넷마블 | [넷마블, 신작 3종 앞세워 도쿄게임쇼 공략…일본 시장 접점 확대 - v.da](https://news.google.com/rss/articles/CBMiT0FVX3lxTE1ZVGxLTGFqcFJXRUk0ME0yTXF4cEQzVWl2MFBqbjlISE1lWFVFZzZtQktkSUZoZTRjQnJZZjYybVZ4Z1hEMzFnYWhqcUhIcUU?oc=5) | - | v.daum.net |
| 일반 | 게임 | 넷마블 | [넷마블, 구로구 '제1회 G밸리 퇴근길 락' 공식 후원 및 참여 - 지디넷코](https://news.google.com/rss/articles/CBMiVkFVX3lxTFBRUFFaTlcybzFDQ2Mwa2hvSjR3dWdOLUNqY3JGbTc1NmxrYUtrWjEtVDBuNW9PRFYyV09hS0I3TGNUX18zc3Fyck9SckQ3UnNYXzV0cUxR?oc=5) | - | 지디넷코리아 |
| 일반 | 게임 | 엔씨소프트 | [엔씨소프트, ‘아스트라에 오라티오’ 글로벌 CBT 돌입…6일까지 진행 - t](https://news.google.com/rss/articles/CBMiYEFVX3lxTE5zR2QxVDdBbkl2Z1JZRXNaZGdOYnNoWkJSYWRKVDFrajhyVWFOZ193Vmw4ODU5a2ozVVR2NXhSdVlFN08wZmlfRkJHOEliQjAyelVDWDN3aWpycl8zS3AxTg?oc=5) | - | tfmedia.co.kr |
| 일반 | 게임 | 엔씨소프트 | [네오위즈·엔씨소프트, 엇갈린 2026 전략… IP 확장과 아이온2 승부 - ](https://news.google.com/rss/articles/CBMiVEFVX3lxTE5nODZSOHdVS2NVYXgtWl90V2k5ZmF0Nm9nekxoc3dkaUY5MFd2WXpxTDJOTk5Na09uY25mYjFUR1JILTFmZGo3NTdUNlhkZmNDakZ4ag?oc=5) | - | wikyung.com |
| 일반 | 게임 | 엔씨소프트 | [엔씨, TGS 2026서 '아스트라에 오라티오' 시연 빌드 및 부스 구성 공](https://news.google.com/rss/articles/CBMiVkFVX3lxTE45LUR4dUVxa1pfN3NPQ0RRdGFSc3h3WVhRZ05VU0ZkUlByN2ZPMUI3WjJrblhIdXREMWlCQ29GRnlRVlNCV1I1QTBZSnBIT2ZYajhKdGln?oc=5) | - | 지디넷코리아 |
| 일반 | 게임 | 엔씨소프트 | [3D로 만나는 '아스트라에 오라티오'…엔씨·삼성전자, ‘TGS 2026’ 부](https://news.google.com/rss/articles/CBMiRkFVX3lxTE5nYWpjRTJlUjVaQUpMdmF2bUFMQzBsVlozaEljNnp3SXVXWk1mR2xSeU9MZ2hDcXBqNC1wNlI2ZmdLOFlZb1E?oc=5) | - | v.daum.net |
| 일반 | 게임 | 엔씨소프트 | [엔씨-MS 맞손, ‘아이온2’ 글로벌 흥행 정조준 - 미주중앙일보](https://news.google.com/rss/articles/CBMiYkFVX3lxTE9hRXhJazhzbUxkQ0dkeHhJZkM3amN3eGhreW5qRVplTFJsY3BiTEhvdFNqNDlTc2VaeWxaQ3BYRUJqMzlKaEhmSmtScG5FNDBuVmNQOW9vMHdWcjRUcDNJdEt3?oc=5) | - | 미주중앙일보 |
| 일반 | 게임 | 크래프톤 | ['방플' 논란 지속에 백기 든 크래프톤… "전적으로 잘못" - 뉴스1](https://news.google.com/rss/articles/CBMiYEFVX3lxTE5rUUgzQ0Z1TlJMUXlLRXpseDVyLUliTFpWdEp3Sm9DLXVrOXNibDVhSWliNWJ6ZmFGeU5mczlIbEh6d05BYU1iaTVmLXFmWXN0al9kOFl6REp0ckExQjlVMNIBZkFVX3lxTE1yM3ByNE1JN0h5Sm1wNjJNVDdlSHNLRXl3ZmY2LUF0cjA4TzQ4OWwzNnpCU2dkU2tOU1ZzOUJzUlRuOGh4Z3BPa2xvekxwQ2xYZjJzMXZkWW5rdzZ1M05VdnJQekFhdw?oc=5) | - | 뉴스1 |
| 일반 | 게임 | 크래프톤 | [크래프톤, 뒤늦게 ‘방플’ 확인 “운영과 소통 실패” - 조선일보](https://news.google.com/rss/articles/CBMigwFBVV95cUxNdUxGOHR6YVpsUy1lT3JOZDJmUkl0YUNDNVFkN19BRE4tdUIxUzhldE85NkZzcmxXSmdQWml1S28yejhLbHBSSmRsSDdSblBGa3l0YlpPM0hMakVMWEFWUnVfUE5IczZ1aXkxWWxvV1RZMnNqR0d2eE14SlFMNFhIVDJiWQ?oc=5) | - | 조선일보 |
| 일반 | 게임 | 크래프톤 | [경기 파행에 스폰서 줄줄이 발 뺐다…크래프톤 'PUBG' 무슨 일이 - 한국](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBuOVdncEJjWE1KQUxsbkhRd1hnTG5iVG5renBuODBKOTZ0NFdrT2YySjBjRkl1UGVtUEo3YklwOENvYXBERm5RcXJETzBIZDlLX2FvSzdSV1M2QQ?oc=5) | - | 한국경제 |
| 일반 | 게임 | 크래프톤 | [크래프톤, ‘방플’ 논란에 배그 대회 조기종료 ‘엔딩’…미숙한 대응이 키운 ](https://news.google.com/rss/articles/CBMibEFVX3lxTE9ES2xtaEJodkJMSXRQUEs2cVhCRWpRWmNmSjFtNWdFb1ItSk9GaVYzMjhmZndhekFLczU3TWlINmJXcF9iSUxGMkVXWWNUMXJxWEZhQXNUT0NybklSNUhlYkhlWHNmQlMzSkJzTA?oc=5) | - | 인사이드비나 |
| 일반 | 게임 | 크래프톤 | [크래프톤, 베트남 선수 부정행위 징계…"운영 실패 사과" - 연합뉴스](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5ZRHU3SzVFOE1WMDBuU0dJa1lVbEd6OHJyOXFpNDJEdE4yWGp3Z1lUbjF5dVNlN1pubEZKcTFKc0FEa3dwbGwxZV9qaE92QTlSWW1nU0RXSm1aemfSAWBBVV95cUxNUDNMZm8zT09xV1dVaVR2TlYzeFQ3UFVXTjRMSWFvdHo4dXFaOEJIeE82dHgtbWdQQXFfY0tRdzdaVkNXUTRlODlWdTlUTmU0M0s1NFE2VWpwNGFwajlTLVA?oc=5) | - | 연합뉴스 |
| 일반 | 게임 | 펄어비스 | [펄어비스 신규입사자 온보딩 여정 - '첫날의 설렘부터, 2년차의 성장을 향해](https://news.google.com/rss/articles/CBMia0FVX3lxTE0xZ0pqZVBvbUl3TVFSRjBiRzRNb29zSDFDam1KT3pLeTRVYlZmNmptR3JWWEhpQ1BWTWpYMFFHa2ZEd0V6LWpqZDJvdmlmY1Z3Nkxkdy03dGdlanFpWTViMU9TOHBWenhIV1Vv?oc=5) | - | Pearl Abyss |
| 일반 | 게임 | 펄어비스 | [김대일 펄어비스 의장, '2026 대한민국 콘텐츠대상' 정부포상 후보 올라 ](https://news.google.com/rss/articles/CBMiVkFVX3lxTE1VS2xSMzFCUWlqSkttWmlLLTZXeTVUbUI5cGg2Qi1XZG10c21FWGpsV3dBejVWQTRlSnd5MmF5WnNpNDl3ZmtINXZDMEVRVGJkM0l0UTdn?oc=5) | - | 지디넷코리아 |
| 일반 | 게임 | 펄어비스 | [펄어비스 '붉은사막', 英 GJA 이어 美 TGA 유력 후보…K-게임 최초 ](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1veVFVemZVeXFxaVN6WjRFajVYMFBZZjNaQUVPQ2Z1SksxZzhSTTNPc1dyVWc2ZUZ2R25icDVlVWlBdkswd3ZHLVJXWmtiUUNHWGZWWVVlbXFmQlJjVnc?oc=5) | - | 더구루 |
| 일반 | 게임 | 펄어비스 | [12년간 매주 업데이트…펄어비스 '검은사막' 장수 비결 - 머니투데이 - 머](https://news.google.com/rss/articles/CBMiZ0FVX3lxTFA3YXhHTkY5bDhFbjVic0xpXzVaU0t1b0ZoWkdlaVhicW9WSWlTSUNXalRBZ29LQjVCSnVkV2d6R1VfeDFnU002Y1pjdzQtTmNKYkk4blFuNmdOMzNjR0ZWcE14YzUzd2fSAWxBVV95cUxQak9zSndzTnNaUjZtTkFjaHlwZ0pxemdETXVwYTA4aFpMWlNveUE2N3g2THJ2QUtRdFRBNEMxMkZOWnJuUTJLV0NJWUI4ZHdiT1N5VjFHRzFuUndTLTdTTWNwYkQtbU1kd0kzR1E?oc=5) | - | 머니투데이 |
| 일반 | 게임 | 펄어비스 | ['붉은사막' 4000억 원 흥행… 펄어비스, 과천 지정타 '대장 기업' 등극](https://news.google.com/rss/articles/CBMiVEFVX3lxTE5QNHF2Mm51TGpSLWRzUDd3TGlVUzRvSWxNZXpnRUd1anFDSUlfLTBXNzBkVkxjQ1hrZWtYdF9MV1UzNXZBbS1LeUoxMlI1V2xQRFNxOQ?oc=5) | - | v.daum.net |

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
