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
_최종 갱신: 2026-08-31 10:19 KST_

**수집 현황** — DART 공시 169 · 뉴스 341 · 회계법인 리포트 2

### 📄 DART 공시 (회계 이슈 필터)
_종류별: 실적 73 · 📘정기 54 · 🔴정정 16 · 🟡주요사항 26_

| 종류 | 업종 | 기업 | 일자 | 공시 |
|---|---|---|---|---|
| 🔴정정 | IT | 카카오 | 20260824 | [[첨부정정]주요사항보고서(회사합병결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260824000219) |
| 🔴정정 | IT | 카카오 | 20260819 | [[기재정정]반기보고서 (2026.06)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260819000055) |
| 🔴정정 | IT | 다우데이타 | 20260811 | [[기재정정]회사합병결정(종속회사의주요경영사항)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260811900833) |
| 🔴정정 | 게임 | 넷마블 | 20260807 | [[기재정정]증권발행실적보고서(합병등)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260807000552) |
| 🔴정정 | 게임 | 더블유게임즈 | 20260724 | [[기재정정]사업보고서 (2025.12)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260724000595) |
| 🔴정정 | 통신 | 에스케이텔레콤 | 20260723 | [[기재정정]타법인주식및출자증권취득결정](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260723801025) |
| 🔴정정 | IT | 엔에이치엔 | 20260710 | [[첨부정정]주요사항보고서(회사합병결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260710000147) |
| 🔴정정 | 게임 | 크래프톤 | 20260630 | [[기재정정]타법인주식및출자증권취득결정](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260630800855) |
| 🔴정정 | 게임 | 위메이드 | 20260630 | [[기재정정]최대주주변경을수반하는주식양수도계약체결](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260630901591) |
| 🔴정정 | 미디어 | 콘텐트리중앙 | 20260630 | [[기재정정]타법인주식및출자증권취득결정](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260630801156) |
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
_구분: 🔴회계신호 22 · 🔵회계이슈 12 · 일반 307_

| 구분 | 업종 | 기업 | 기사 | 회계토픽 | 출처 |
|---|---|---|---|---|---|
| 🔴회계신호 | 게임 | 카카오게임즈 | [[재무제표 이야기] 매출은 늘어도, 수익 질 나빠진 카카오..."미래 먹거리](https://news.google.com/rss/articles/CBMibEFVX3lxTE5RZUdDSmVsLXRLOWNKbkowWjdkZkhudUxHaWI2aFNieFF6MDRKOFBaUE5YUGRWVG9HTmZaWVdzbFJVVVN0ZURObGJvWUxaT3NWNkhSM2ZHUjNfdHVJTkRjbzBJOTRRR1lpMjd4cQ?oc=5) | - | 생생비즈플러스 |
| 🔴회계신호 | 엔터 | 에스엠엔터테인먼트 | [매출 73% 폭락·의견거절 속출…팬덤 환호에 가려진 K-엔터 ‘재무 잔혹사’](https://news.google.com/rss/articles/CBMibEFVX3lxTFBNdU5Mck5wR1lkdHBjaU9GV2laZ3EtZHF5eElXWkZ3SDJERVBXUWV5MlRScE0tdWpWMTltRE9kMmpEYmhOeWx6YTJmZUxKWVgyRms4V0w2a29GM0hOZ0F6a0UybVQ3TThtQmlvUQ?oc=5) | - | 한경매거진&북 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [금감원, 메가박스·콘텐트리중앙 회계심사 돌입…자금 조달·회계처리 점검 - v](https://news.google.com/rss/articles/CBMiVEFVX3lxTE9ta2pGSjBXYnlYS1JhRXZOc1RyUTNxSmI4cXlINVJnNU0xUFgwbnFVS1JIWWF6MDAwc0dzbXhKdTdUNmNIVjNSZ3l1Q3A4UnlMdFRSdw?oc=5) | - | v.daum.net |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권 피해자 대리인단, 금감원에 감리 요청 - 법률신문](https://news.google.com/rss/articles/CBMibkFVX3lxTFB4OEZyLVFxM2lFejNpZm5vRmgwNDAzeWh5TElpVEpxNFhWZ3FJRndLTk5fTF9kWGE0aUdrTjM3S0lCamZ2V3Y4TE03LUNSTmpfTHZsaXROZ1JJeEYzaC1jek9ZRTZudnU2dWRORFdR0gFyQVVfeXFMTlJuUTUzcVYwLTIyMWhZWnFRYVBNc2FPU251QVYyU0V2cXUzU2RvV3RlTS1PMWVXeVNvNElNOTIwWnhXcXRrV1pKdURYZHo5emlVcWR0cC1tc0kxTUlZSVZ0TFBKSGxCUmZDNndnZGg4ZHNR?oc=5) | - | 법률신문 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권투자자들, 금감원에 감리 요구…"회계처리 의문" - 연합뉴스](https://news.google.com/rss/articles/CBMiW0FVX3lxTFB1Ukx0THpTTk1DSVh2VGtQU2hsZTBuZWhlRWhzLUFKNGY0dm1RZkgwdDIxMXdaTzhkTXozUXltRTlOS2VOZ25SdGlfLVY1WVhsYUVfWmMxTERDUmvSAWBBVV95cUxQRDRMM1RQYmYwcGlUY1o2YmZfWTNKQlRDU2JkTmxWNnFlVEs4cTFCOElOR1MyUjhyb0twN18zMkNINldZOE1ZSTNKVVJWdmRDOFZ4S2M2OTVoVHVaWDRHUHo?oc=5) | - | 연합뉴스 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [“돌려막기로 자본잠식 숨겼나”…중앙그룹 채권투자 피해자들, 감리 요구 - 한](https://news.google.com/rss/articles/CBMickFVX3lxTFBDSS1uQk52SXBhb1kycHJkNU5na0w1cmtyUm1hSW5KM2YtQkZWUy1TYlVfT2F5NHhUdElibTdhaExkblFZWExucFBXeVRpM1FkcTNvdm41dHpaODZEVzhScldkQ2FwTnRjZmJWTll0Z3p6dw?oc=5) | - | 한겨레 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [금감원, 메가박스·콘텐트리중앙 회계심사 돌입…자금 조달·회계처리 점검 - v](https://news.google.com/rss/articles/CBMiT0FVX3lxTE55eHlOanhSb0VrOFJ6MmpaaWhvRVh2SGZKSVJsWktINkNYcGpZRnBRLTUwdFBBWGJoUHFlZm1MUkZTR0tQTzZCanBvWW9xOEk?oc=5) | - | v.daum.net |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [금감원, 메가박스·콘텐트리중앙 회계심사 돌입…자금 조달·회계처리 점검 - K](https://news.google.com/rss/articles/CBMiW0FVX3lxTE54OUVMRE9hMTAyNThval9sRFV5ZDNOeFBHODQ2bmdNQmh5WU41UWtJU2RrZ2ttcEZ0SFhkRm03QjM5R3cxR21pbTJKUFU5ZzFCbEFTSFIwN3hWQUU?oc=5) | - | KBS 뉴스 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 투자자들 “회계처리 의문”… 금감원에 감리 요청 - v.daum.n](https://news.google.com/rss/articles/CBMiT0FVX3lxTE92M3UxRHNaUzJ6dXY0MHhBd2tlZnZfRWJ2V0dCYW5LWWRxTVIzRi1jOVBfc1lseEF5MlVYb2ZBRW9jak1SdWljRHpNUTBoWDQ?oc=5) | - | v.daum.net |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권 투자자 금감원에 감리 요구 - 조선비즈 - Chosunbiz](https://news.google.com/rss/articles/CBMigwFBVV95cUxOZ1BZZWVoNlItVU8zZTdWOTBmWVpncDBDUnMyenNPYUhNbWFDRDRlTjZpbzd6MnFxWHhzeWdmb01Jci1QRnN4UU83M0FmcHNTZ21HQmpxSF80WmxIMWRmcldCYmZhZUd4amk0bUtFazJnMVNOZklrZUp2ZjVPb2dFY2xJUdIBlwFBVV95cUxObmZVWHNYUEZEcU9BUUpKQXl1bmNJblA1ZkVvWlZ6bDExdWZkT2JWdFlnR3B0SGdBMWxQVmZrTUdzSlZiQ3FiV1pHU19FZ3M0WHlVMng2dDdpRW1ZUTRnalV3Ri1keE1rOHJVSkpHVUE3Y29jNzltSFNtZ0pOWUQ0OWJHOV9laHY3X2Z4WkdxZktNaHlzTWhn?oc=5) | - | Chosunbiz |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [콘텐트리중앙, 관리종목 지정사유 반기검토의견 의견거절로 변경 - 톱스타뉴스](https://news.google.com/rss/articles/CBMickFVX3lxTE03Ui10WThDS1ljYnBHOXI3MXhHb19Td3gwRkRxSG1qek5HcDR5TTc3cWFUd0dERXhJUzFveGNBOWJRYkF3VHJaV2VpbTRZWDRndHE2UU1mUG8tN1g5VmZTTmhwOWpsRWFTdnY5RmFKdTRudw?oc=5) | - | 톱스타뉴스 |
| 🔴회계신호 | IT | 네이버 | [[단독] 두나무, 美 SEC 위원장 면담, 회계기준 전환 완료...나스닥행 ](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPTE5PSW1ya182NWtnSDlMTmFrSkhvVC1xUmhPNG9zb3ZDZWd2RVVGalBvSFdmT0xMYUd3bWIxbkE1TkF3YVpPTWtxdlVZTUszdGExSTBNMFhBdkZaMkV3V2JpT196UXV0aDVFMmczaWpYbU5YVXpWbDd1Q1cxVmtEMWtfdzZ5WHZydGhB?oc=5) | - | 조선일보 |
| 🔴회계신호 | IT | 카카오 | [카카오 노조가 놓친 '새 회계기준 함정'…"내년엔 성과급 0원 될 수도" -](https://news.google.com/rss/articles/CBMiaEFVX3lxTE8yRnFCUUFIUzY3YTR1cDZqdmRVODJWd0pWT3E2SnNFQjBlTlpLZ0ZQQV90cTk3bldhRmdDUm1WVmN6WUZ5aDhrRjlWOXFYZzUwRzJhVktoejFha051VjRCUEVDb2x2UE1u?oc=5) | - | ebn.co.kr |
| 🔴회계신호 | IT | 카카오 | [토스 재무제표 간단 분석 - 브런치](https://news.google.com/rss/articles/CBMiTkFVX3lxTE5ISHpzQXZzNnJmb1A1ZWlFeGlFYzBBTlRhYXBkeFJ1WU1vamtEemhuVjhvaUpFbHp0R01wN051WnRTWDdiZmRXZ0MxeDNPdw?oc=5) | - | 브런치 |
| 🔴회계신호 | IT | 두나무 | [두나무 "美 회계기준 검토…주식교환 마치면 IPO" - 비즈워치](https://news.google.com/rss/articles/CBMiakFVX3lxTE5XdU00TXFrTEJLcHI4RFFYcjVUMlIzV1VuVUVrSzFIcGwtdGVvc2pkQzJDOFgtTzlDZnVLNUxFM01ZNUNZVlNUUWNZV3cyTnYtZ3VqMkFyVEdTaGV4dUZoOGpMNndodC1Zd3c?oc=5) | - | 비즈워치 |
| 🔴회계신호 | IT | 두나무 | [두나무, 美 회계기준 검토 …“아직 결정된 바 없어” - 전자신문](https://news.google.com/rss/articles/CBMiTkFVX3lxTE5HZTFwRHZlQ19keGRBM3pQYkk2THNlZjNKRzFmRjNnMV83OFRyLUQ4elVxV2M4ZUV5eTJTSFdleEZtZUNORTVpc1NNTU1iZw?oc=5) | - | 전자신문 |
| 🔴회계신호 | IT | 두나무 | [美 회계기준 문의한 두나무, 나스닥 상장說에 "정해진 바 없어" - 아시아경](https://news.google.com/rss/articles/CBMiYEFVX3lxTFB0MmlXbEZMR0dPcGJEU29yX2tSd2UyeG1zdlNHRWZwOGp6SkdDZWl2eDNBc29rQlZlOEpNMEdPVFI3QWNGNWRBZnpGQTRhQThXRW9NazdHa0VpdlI2Q1UtYg?oc=5) | - | 아시아경제 |
| 🔴회계신호 | IT | 두나무 | [두나무 "美 회계기준 전환 사실 아냐"…나스닥행도 '미정' - ebn.co.](https://news.google.com/rss/articles/CBMiaEFVX3lxTFBJblR6OS1vc3JSNDhlYUctWUE5TVRPQ29uclIwNG04SGpKQTE0Q0pzYWlIWjVsTERpSHlBemR5OXd3RUhya2liQlRRZ1NtWFpnM3BBMUotdXNiS2NHTmhkb1RscnpjYTJO?oc=5) | - | ebn.co.kr |
| 🔴회계신호 | IT | 두나무 | [두나무 “美 상장 확정 아냐…회계기준 전환도 사실무근” - 뉴스투데이](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1VLU5XbGN2eTYwNFI4eU9JOFBjOVZTZXd5V3dMOVBtNmFWVEJWanRXdXJLTFhCbnVDOWpfZklkcWRoY1diejE3X0ljWXA4NW9qSGNSTXh0MVpwTzhCbWc?oc=5) | - | 뉴스투데이 |
| 🔴회계신호 | IT | 두나무 | [두나무, 美 회계기준 검토…상장 국가는 미정 - 아주경제](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5QZmxPY1VoZDBoeVMtNUptQUU0Skkza3I3d1NISVVrWDRNWk84QklUUlFaeGRydWVRNDV2eDFTb1d4elNoRkFEOWQyUGdLbGQwYllhUFZDcm9yZ9IBWEFVX3lxTE5XNHNNNGppTzJzWG5IdjQ2eUF6OHJTT2M0T1JoTGx3ZVNmQ2FiaFY1Q05jTnFQYnl4WjZySnJGTnU3d0sxWEwyZ3l6UzJ3X1gyWFRDUm1qZUE?oc=5) | - | 아주경제 |
| 🔴회계신호 | IT | 두나무 | [美 회계기준 검토에 SEC 접촉까지… 두나무 ‘나스닥행’에 쏠린 눈 - 서울](https://news.google.com/rss/articles/CBMib0FVX3lxTE1MS1Vrc0pBUkhkV2Q0ZWFJSUFMMHdzaWl2c2ZGb215TXZXQkhMbEpjX09RX0JUSk1DX3cyOHBIZ21FSkF3YkJpeFo0cEdpbGVaYm5tLS1tSGJYeXlqVFhXUkNPVXdETWRNZlNQNlJxbw?oc=5) | - | 서울신문 |
| 🔴회계신호 | IT | 두나무 | [두나무 美 상장설 다시 고개…“회계기준·행선지 결정 안 돼” - 이투데이](https://news.google.com/rss/articles/CBMiVEFVX3lxTE5rR0JabEc4RWVrazRoMUIxOWlwb2h6NzI1VjFzWUI3MnFRbThXcnRlbl8yNk13TVBzZXVMLVpNR2hLdWNwWHktYnpQSFNtX3ZqWGFwZw?oc=5) | - | 이투데이 |
| 🔵회계이슈 | 게임 | 크래프톤 | [크래프톤, M&A로 무형자산 6562억→1조8628억…성과 시험대 - 마이데](https://news.google.com/rss/articles/CBMiYEFVX3lxTE9EME14WWNpRi1UbFdsOUtHdDNsT2lZZ1hCQVpMZW4zWThESjR4TE1ka0NfNER1V2ZPSnhkbkpsbW95bmhTVjg5WUNBNmpZZVh0NVI3SzJwRzVic00tVFdURA?oc=5) | intangible-assets | 마이데일리 |
| 🔵회계이슈 | 게임 | 넵튠 | [크래프톤, M&A로 무형자산 6562억→1조8628억…성과 시험대 - 네이트](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1EMFZ6UkYtMVRmV0YwZGtoWXNjVEx6ZVRmQ0lNRmtfMnZTSDk1OEZZV2xSLVhhWWh5VGdpNVl5ZndyZHpwLXRqbWFQaUliY0tCWUU4?oc=5) | intangible-assets | 네이트 |
| 🔵회계이슈 | 엔터 | 와이지엔터테인먼트 | [빅뱅, 데뷔 20주년 신곡 'BiiiG' 음원 차트 석권… 월드투어 포문 -](https://news.google.com/rss/articles/CBMidkFVX3lxTE5kX0w2YTdVUFVxUFZQSUtDdEJCdXhXMGN6SnZnS0wzY1AxMDR0dHFHV0pqbXdXMTNWdXBuRzlHTFBzUDVQM2JvWllfQmhQWThmYUI1QnNrVThLNENGR1ZYZXV0bVZTY3cxbnlCYV9nZEsyLTVCSWfSAXtBVV95cUxNazVmWXZmS1lSX2lqVW9EYlN0WVZzajM5YXo2ZlhvLXJTMHlEbVVoMFFQSm4wVmFjY183bktsTG1MUnJwNHlUMFZ0MzdWZVppcndDdDhQeGpkYUxPR05pY3lNWXpGeEZIZjVaUW8wN1M4dlZwbFdtWVVtNFU?oc=5) | intangible-assets | 머니투데이 |
| 🔵회계이슈 | 미디어 | 스튜디오드래곤 | [[스튜디오드래곤 톺아보기] 판권 상각기준 전격 변경…'수익·비용 매치' 변동](https://news.google.com/rss/articles/CBMiT0FVX3lxTE9QU0VkMFAzbnhsQnl6amZPVTZYbUtabUVibF9FbmFlNXpLWnRJa0RneFJSNmE5T08xSGtOVFRGS1lpYzRweHdYSGdrUkhYWms?oc=5) | intangible-assets | 딜사이트 |
| 🔵회계이슈 | 미디어 | 스튜디오드래곤 | [[스튜디오드래곤 톺아보기] 판권 상각기준 전격 변경…'수익·비용 매치' 변동](https://news.google.com/rss/articles/CBMijwFBVV95cUxOeWRaSDJiY0JzY0l6SXlzMGtRVmdaYjZncDdubVBfUjlaNldjS081VlZicUM2UXRsXzVKbTZpdVlnb2xRa1JyNnY1cmxEaFNKQUNuZkZqRXppV2pSYW9iMFVsaFhHcHBzRHNZZmVVNm5hMjNtdTE2a3VsT21qam9YYU5uREpJOG1HQmdLR25Xaw?oc=5) | intangible-assets | Naver Blog |
| 🔵회계이슈 | IT | 네이버 | [[핀포인트] [네이버] '1조 영업권' 시험대 오른 왈라팝 - 네이트](https://news.google.com/rss/articles/CBMiU0FVX3lxTE5wZHgtQy1XclFSak9sTjNsTm9KaVk3QnRUTUVYR2lBUlhNRWwwdE5hM0VVbU1HdWk0Z0xSS3BLbEczc2FoYVl2M2xldW0tR1ZLRnRz?oc=5) | intangible-assets | 네이트 |
| 🔵회계이슈 | IT | 카카오 | [[IB토마토]차바이오그룹, 카카오헬스 품었지만…CB·영업권 부담 '먼저' -](https://news.google.com/rss/articles/CBMiYEFVX3lxTE5oR2RicWlCR1pLcWtHNVVpY3Q2SGV0aERvc09adlVyajl2WkhibUNRMFVZV3FnUUZOUFJCTzFrS0JzZ2R0S2RpSHJLMUg3UEM1SVZXanh2V0dhYkhKSjE4RQ?oc=5) | intangible-assets | 뉴스토마토 |
| 🔵회계이슈 | IT | 카카오 | [업스테이지가 품은 ‘다음’ 평가액…무형자산 1413억 - 서울경제TV](https://news.google.com/rss/articles/CBMiZEFVX3lxTFBfUWJKZUJlbDlMWmxHSjFxZTZhcWJ2UVNkUlltY0tMYVZ5SFZWNF9oRnAzRmNGVlk1eWlaMDJmMmVueEs2SHFHSkZhSXFwVFBWTXA4LTVOYTNZZ3RqQk52a1lic1Q?oc=5) | intangible-assets | 서울경제TV |
| 🔵회계이슈 | IT | 카페24 | ['거래액 역대 최대' 카페24, 투자 확대로 수익성 주춤 - 딜사이트](https://news.google.com/rss/articles/CBMiT0FVX3lxTE1uLXNOMEtFLW1CVmZmcjVWYUswckYwYmxaRDlfczdxMFRxSUJLaFVFTV8yMm9NakR1bnFLdDBjRWZadXlMOXJyWWNCb0JUX3c?oc=5) | platform-cases | 딜사이트 |
| 🔵회계이슈 | IT | 야놀자 | [야놀자 상반기 거래액 21조 원, 매출은 14% 늘어 - 플래텀(Platum](https://news.google.com/rss/articles/CBMiSEFVX3lxTE9oLUxuSEtkVnhuYnVzd19uemVJTmUyUHM3aEZwcjM1WUtad0hfM2dVY0ZPYTh0Q2JUZVNBQS1GMTY5cS0zMzhUSA?oc=5) | platform-cases | 플래텀(Platum) |
| 🔵회계이슈 | IT | 컬리 | [[프리스탁 건강검진] 컬리, 현금창출력 개선 후 리스부채 부담은! - 프리스](https://news.google.com/rss/articles/CBMib0FVX3lxTFBqc1hSX1o2QUd1QVBVS3Zqd0R0R2N6R3dGRk8xRVU0Z244a1VNT1hqU0QwSVBHaTduZ2VfWWlBT1pCYnZGbHpMSUJiNEJBdTloZXhTeXZMY0ZYRnVYV1JKMU9BbVZDNVE3b1d0T1AwWQ?oc=5) | ifrs16-lease | 프리스탁뉴스 |
| 🔵회계이슈 | IT | 컬리 | [컬리N마트, 오픈 1년 만에 월 거래액 10배 성장 - 푸드투데이](https://news.google.com/rss/articles/CBMiZkFVX3lxTE1kMUhrS2lDOVJlWW9jWTFETDR0WTVUSVYyTDV4TVY5WDc4RmhBVkhVSFlZeUR2M0RsajlDbF92bUNrT2phbGFaa2JxQWFrN2FETkViNHp4T3lwNzZRM2lJdHlfU01kZw?oc=5) | platform-cases | 푸드투데이 |
| 일반 | 게임 | 넷마블 | [넷마블 게임즈 컨설턴트를 위한 친환경 에너지 권위 있는 가이드 - Plate](https://news.google.com/rss/articles/CBMiZEFVX3lxTFBkZjJ4eHNUZlV6SUFTNXV0RFlfTmZzT2dxcUdvanNpRTNpNE5DeFJieVJ3M29FbmxZUlFMVFFRcFpuWDEtR3RKa3VqX2dhX3Q2VWVJRzgtcnZnT3VGOUF1NGd4dTg?oc=5) | - | Platea Magazine |
| 일반 | 게임 | 넷마블 | [방준혁, 텐센트 보유 넷마블 지분 13.4% 인수 - 비즈워치](https://news.google.com/rss/articles/CBMiakFVX3lxTE5RNFV3RnJRaWwtWU15LVlSSHdJc3JWalp4cmd2Y2ljVENRb0xBbkxGc1lkMjFPN1REd0hlRVpSeUtYVV9VSThRQUx4Wl9KUXJ1ODdWdDd1Q2RZcjJzdXpMNjBibE5qU05uT0E?oc=5) | - | 비즈워치 |
| 일반 | 게임 | 넷마블 | [넷마블몬스터 "中 물량 공세 맞설 K-서브컬처 무기는 캐릭터" - v.dau](https://news.google.com/rss/articles/CBMiRkFVX3lxTE53ZlpxNG85Z19SVmNrd24zYVlrTEpSQjVPVjBTVEYxLVJrNFAtMENobXcxam1FdnB5Z0ZxYndXbU0xUnlQdkE?oc=5) | - | v.daum.net |
| 일반 | 게임 | 넷마블 | [넷마블, TGS서 '펄 인 블루' 첫 공개…日 시장 정조준 : 네이버 블로그](https://news.google.com/rss/articles/CBMijwFBVV95cUxQVEd2VE41QTNsdlFMeElubU84clVaRjdWZU41dGRFMXJLRmRWU2EwRElkc1Z1OTJ3d3dCMEZ2MHdRekJyV19aSUp1WlQ4a19ieDNtVVIyR2tjU1BCYTY4WXcwX1VCWEVJZGI0TmtWMkNUakFyYzJ2aXJUUFB4b19wbEhiZUhENllCSjM4bk5aNA?oc=5) | - | Naver Blog |
| 일반 | 게임 | 넷마블 | [[게임리뷰] 넷마블 '아스달 연대기', 뉴월드 시즌2 업데이트 사전등록 실시](https://news.google.com/rss/articles/CBMiY0FVX3lxTFAtZnVPWUZnVHZKLXV4ZVF2c09taC1acjA0Q2RzOVItOVI3RFFYdENPallDdFBhTEVXRGtFajA4bHc5cU1ab19DT2VYQ0lrYlplZXVxRGdBaWxRd1RBa2MtczdHZw?oc=5) | - | 더구루 |
| 일반 | 게임 | 엔씨소프트 | [토토 3플3 비타임|폴드4 카메라 성능 - Platea Magazine](https://news.google.com/rss/articles/CBMiZEFVX3lxTE5ZM0ZiQnZVSUJkcDVvcFhqRURjeHBIcHVQV3g5QnU4N0ZfQWFuVTRBMU9ocXZxNGUxVFVWemRJZXNSZzl0NkxiMmJIMWE4X3BXdUEzMXZiODNHOWQ3bkllQjVGRkY?oc=5) | - | Platea Magazine |
| 일반 | 게임 | 엔씨소프트 | [김택진 엔씨소프트 대표, 아이온2로 중국 공략…IP 확장 본격화 - 피플투데](https://news.google.com/rss/articles/CBMib0FVX3lxTFBPdVQ3TGt0THdwVW8xbHBkV3BmZ0U1UkNMbl9HdnVnZnY0VXdjaW5talptc3pxLVZlMTFlY1BBbUFKOFlYek9pdElCQjQ1M3YwaVYzRzRtc1ZTZlNtYmV4X1hZa01IVkhMVy1ydXFaMA?oc=5) | - | 피플투데이 |
| 일반 | 게임 | 엔씨소프트 | [엔씨소프트 노조 “그룹 통합교섭, 기업 경험과 기술 지키는 경쟁력” - 로리](https://news.google.com/rss/articles/CBMibEFVX3lxTE13Q1BjWGVwaUpSMmpuTkZLaXVPSURKR3VBTWNMTXRRMVRjbUVTMkl4OGF6bTlkMEk3aEVra1pGazBZRV9sVnJRS0J6dEFNUklIX2R2cW5LR1FDZjRLdlppcnVEWXBqTzJoMUJaNQ?oc=5) | - | 로리더 |
| 일반 | 게임 | 엔씨소프트 | [엔씨소프트, 타임 테이커즈 글로벌 테스트 실시 - 2news.co.kr](https://news.google.com/rss/articles/CBMiaEFVX3lxTE1YOV9oYk9aX1BXcENxbW1Pd2ZITVREM0MzZWM3bV9CVzZESHVYaFB3TDZtRlM0bDl5c0VCTnA4WW5ZZ29ZUWpyQlpKdGhodmtMRTM4eF9seDJjSkRDeENkQUs5VUpWR3JJ?oc=5) | - | 2news.co.kr |
| 일반 | 게임 | 엔씨소프트 | [엔씨, 2분기 실적 앞두고 '모바일 캐주얼' 주목…새 성장축 자리잡나 - v](https://news.google.com/rss/articles/CBMiRkFVX3lxTE9XdnE5aXFFMUF0V3RHNzh6a05mMXRST2FQb3ZTVkN0VW5rRF9wNVJFanZ0bjFRb2p6SkJhbVNwVHlDNlVOY1E?oc=5) | - | v.daum.net |
| 일반 | 게임 | 크래프톤 | [크래프톤 '타래: 언바운드' 해보니…한국적 세계관에 액션 손맛 - 연합뉴스](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBMc01rYVNJbmZjVjUwZXJnRDhidEFDb0ptWVhhWm1Ta0JfTVk5OWQ2S3E3S3JxU0VVTDZ0a3pfb1ctdEtGT2R6Q3V0UGl4eTZKSE5Pa1QzOEVvYzDSAWBBVV95cUxNZW50MVF3MGZuUzBHTUJpNnVSN3B5SWd0ak1QVkExMzFLVjJSWjJpTE9DZDRYZUNySEJMZ0JjX2I0bmNnQy1fbzdNQkVBbzY0S3FwU2wyTDZGNDNYVHJtbkY?oc=5) | - | 연합뉴스 |
| 일반 | 게임 | 크래프톤 | [크래프톤·엔씨 신작, 게임스컴서 베일 벗었다 - 비즈워치](https://news.google.com/rss/articles/CBMiakFVX3lxTE5taHdRN2RxNnlrQnR6SE83YzRyWTIzbWJDaUQ3cGk4dmkyQmE3Vm5lSkZOZC0xR29jbXZFeVA1MVdla0VYVkRuYjF4NXVrZXNJUjNkNm5ZMDRkLVpfY0ZCMHduZ203SU5fcnc?oc=5) | - | 비즈워치 |
| 일반 | 게임 | 크래프톤 | [크래프톤, '배틀그라운드 다음' 찾는다... 신작 5종으로 IP 확장 승부수](https://news.google.com/rss/articles/CBMiTkFVX3lxTE5pbDBTaU4zdTlkTVB4ci1ja0RBMXk4a0hqMmY2cWFhZnNiQzZtdnhwSkRWdGlDWHBpbzBxUmlNWEh2LXNhMDhLTW9UYTRYUQ?oc=5) | - | 전자신문 |
| 일반 | 게임 | 크래프톤 | [크래프톤, 신작 5종 공개…‘넥스트 배그’ 찾는다 - 디일렉](https://news.google.com/rss/articles/CBMiZkFVX3lxTFBhZjZYX0lZZHhWLTVDZmxGZV8tQ2E2NVdEU3pwTm9aYzk0S19ibGpURmVzdEVHTWxyZ1d4anByT2E0UDBWNExUOVZGS0hQQ3RiR1ExeXNHRUlsTjJPTlFzMkIyemVndw?oc=5) | - | 디일렉 |
| 일반 | 게임 | 크래프톤 | [[게임스컴 2026] 크래프톤, `배그` IP 신작 베일 벗었다…ONL서 신](https://news.google.com/rss/articles/CBMiZEFVX3lxTE1WYTVxcDY4Y3dnWGxLR1VmM0VZNF9CdzRPRTF4eW1lZU1WVzcwRzd1OVJZeDAxR0htR0N6bTdXa0RJNGhVRzNfd0REUWRWNy0xaGxNUFZ6RXdTZnYzTlo5WDRnR18?oc=5) | - | 디지털데일리 |
| 일반 | 게임 | 펄어비스 | [‘어닝쇼크’ 펄어비스에 日 노무라 “목표가 59% 하향” - 매일경제](https://news.google.com/rss/articles/CBMiUkFVX3lxTE5tbWNRV1NySjNCWHpxTVo1eTFsNlR4N2pVY0szUWgyOVpzbXc3UDFSaGhrQ0hTdGRTamc2VWNRVjZZU04wUFNsV0pCcXZGYV95aXc?oc=5) | - | 매일경제 |
| 일반 | 게임 | 펄어비스 | [펄어비스 '검은사막' 하반기 콘텐츠 확장으로 흥행 이어간다 - v.daum.](https://news.google.com/rss/articles/CBMiRkFVX3lxTFBkYUFzSjBFNm9ua3kyY1JjdjlTWnF2NDZXdnhWVDNVY3gtMzVsNlpWSmNYelFrNDhhWjVNWE5ySzhySVZ4TFE?oc=5) | - | v.daum.net |
| 일반 | 게임 | 펄어비스 | [펄어비스 붉은사막, ‘게임스컴 어워드 2026’ – ‘에픽’, ‘최고의 PC](https://news.google.com/rss/articles/CBMiZEFVX3lxTE5mSG14ZENKZ1dHZW1DYU8zWWJiVTFFcHNZZkhGdHRjczQ4ZGtkbnZoZzRzay1vUWpDMG9abXU0LUJNNWNlcTIySVA0RTd6cmdjTjBPNnJfLUppbkx5dVRJMW1lcFI?oc=5) | - | Pearl Abyss |
| 일반 | 게임 | 펄어비스 | [펄어비스, '어닝 쇼크'에 장중 14%대 급락 - 한국경제](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9lZ3dkSjY3NTdWOV80SnhybFV6a0pLY2pGMTFpdXhrN01oSE4wZGFMcVg5blRTRWhGbHJYLWhaLV9QaEN6SHdlVTV6eW5XRGhjR0xXa1dscUZnQQ?oc=5) | - | 한국경제 |
| 일반 | 게임 | 펄어비스 | [펄어비스 2분기 매출 247%↑, 영업익 7411%↑… ‘붉은사막’이 견인 ](https://news.google.com/rss/articles/CBMigwFBVV95cUxQN3VidG1oYTQyRUVXdTJjX2ZJeXZoYTREeE5WN3ozRWxGek96aFF6d195U3YtcTNhbmhwRENxQkFOc1FDckdaWXY4X29zYnVhUHpRcVFoVFItX1BBQlNTSFl6MHFYYTU2X2REOUd6UGN1REhEdUE1aHlIZF82aHBMcURRcw?oc=5) | - | 조선일보 |

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
