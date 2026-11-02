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
_최종 갱신: 2026-11-02 11:18 KST_

**수집 현황** — DART 공시 150 · 뉴스 335 · 회계법인 리포트 2

### 📄 DART 공시 (회계 이슈 필터)
_종류별: 실적 69 · 📘정기 54 · 🔴정정 12 · 🟡주요사항 15_

| 종류 | 업종 | 기업 | 일자 | 공시 |
|---|---|---|---|---|
| 🔴정정 | 엔터 | 큐브엔터 | 20261030 | [[기재정정]주요사항보고서(유상증자결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261030000611) |
| 🔴정정 | IT | 네이버 | 20261030 | [[기재정정]주요사항보고서(유상증자결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261030000001) |
| 🔴정정 | IT | 비바리퍼블리카 | 20261030 | [[기재정정]유상증자결정](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261030000628) |
| 🔴정정 | IT | 비바리퍼블리카 | 20261028 | [[기재정정]주요사항보고서(회사합병결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261028000358) |
| 🔴정정 | 미디어 | 에스비에스 | 20261026 | [[기재정정]타법인주식및출자증권취득결정](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261026800689) |
| 🔴정정 | 통신 | 엘지유플러스 | 20261015 | [[기재정정]증권신고서(채무증권)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261015000362) |
| 🔴정정 | 게임 | 위메이드 | 20261014 | [[기재정정]최대주주변경을수반하는주식양수도계약체결](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261014900192) |
| 🔴정정 | 엔터 | 큐브엔터 | 20260831 | [[기재정정]주요사항보고서(유상증자결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260831001295) |
| 🔴정정 | IT | 카카오 | 20260824 | [[첨부정정]주요사항보고서(회사합병결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260824000219) |
| 🔴정정 | IT | 카카오 | 20260819 | [[기재정정]반기보고서 (2026.06)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260819000055) |
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
| 🟡주요사항 | 게임 | 네오위즈 | 20261020 | [주요사항보고서(자기주식처분결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261020000323) |
| 🟡주요사항 | 엔터 | 제이와이피엔터테인먼트 | 20261008 | [주요사항보고서(유형자산양수결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261008000381) |
| 🟡주요사항 | IT | 컬리 | 20261002 | [주요사항보고서(주식교환ㆍ이전결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261002000047) |
| 🟡주요사항 | 미디어 | 제일기획 | 20260930 | [주요사항보고서(자기주식취득결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260930000006) |
| 🟡주요사항 | 엔터 | 디어유 | 20260929 | [주요사항보고서(자기주식취득신탁계약체결결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260929000178) |
| 🟡주요사항 | 게임 | 시프트업 | 20260910 | [주요사항보고서(자기주식취득신탁계약해지결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260910000386) |
| 🟡주요사항 | 통신 | 케이티 | 20260909 | [주요사항보고서(자기주식취득신탁계약해지결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260909000349) |
| 🟡주요사항 | 통신 | 에스케이브로드밴드 | 20260827 | [주요사항보고서(회사분할결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260827001001) |
| 🟡주요사항 | 통신 | 에스케이텔레콤 | 20260827 | [주요사항보고서(자기주식처분결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260827000390) |
| 🟡주요사항 | 엔터 | 하이브 | 20260825 | [주요사항보고서(자기주식처분결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260825000350) |
| 실적 | 게임 | 위메이드플레이 | 20261030 | [결산실적공시예고](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261030900859) |
| 실적 | 미디어 | 제일기획 | 20261030 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261030800459) |
| 실적 | IT | 엘지씨엔에스 | 20261030 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261030800194) |
| 실적 | 게임 | 데브시스터즈 | 20261029 | [결산실적공시예고](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261029900176) |
| 실적 | IT | 슈프리마 | 20261029 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261029900465) |
| 실적 | IT | 삼성에스디에스 | 20261029 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261029800090) |
| 실적 | 게임 | 넷마블 | 20261028 | [결산실적공시예고(안내공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261028800498) |
| 실적 | 게임 | 웹젠 | 20261028 | [결산실적공시예고](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261028900427) |
| 실적 | 미디어 | 이노션 | 20261028 | [결산실적공시예고(안내공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261028800369) |
| 실적 | 미디어 | 엘지헬로비전 | 20261028 | [결산실적공시예고(안내공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261028800505) |

### 📰 뉴스 모니터링 (🔴 = 감사·재무제표 신호)
_구분: 🔴회계신호 17 · 🔵회계이슈 8 · 일반 310_

| 구분 | 업종 | 기업 | 기사 | 회계토픽 | 출처 |
|---|---|---|---|---|---|
| 🔴회계신호 | 게임 | 넷마블 | [[재무제표 이야기] '정수기 게임' 우려 딛고 넷마블의 ‘황금알’ 된 코웨이](https://news.google.com/rss/articles/CBMibEFVX3lxTE56UWVmcFpXTmhHZm1hanhhWFFjNUljbWpuZndaYUdQckRQTmUzTEtJb3hkU0p2b21jZ1RjSXZhZ0dQc19BRlhkTzFJTlVTM1NtbDB5emxnb1k0MDFQd1JkY3owVVItN3dkZjYzdA?oc=5) | - | 생생비즈플러스 |
| 🔴회계신호 | 엔터 | 하이브 | [의견거절·재무제표 재작성…'암살자(들)' 제작사 하이브미디어코프 회계관리 도](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1Tc1FHRU5CMFp6LUlBcUJkd0FtU195bV9fRGQ2R0NDMjMxWDJ4UW9OTXVRcFRHMzdhSWdiaEVIRkl5WmY5czB3RkJpb0tFdkJHUm5FekFsMzVUdw?oc=5) | - | 블로그 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [금감원, 메가박스·콘텐트리중앙 회계심사 돌입…자금 조달·회계처리 점검 - K](https://news.google.com/rss/articles/CBMiW0FVX3lxTE54OUVMRE9hMTAyNThval9sRFV5ZDNOeFBHODQ2bmdNQmh5WU41UWtJU2RrZ2ttcEZ0SFhkRm03QjM5R3cxR21pbTJKUFU5ZzFCbEFTSFIwN3hWQUU?oc=5) | - | KBS 뉴스 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [유동부채 1.4조 늪…’적정’ 받던 콘텐트리중앙, 5개월 만에 ‘의견거절’ ](https://news.google.com/rss/articles/CBMirAJBVV95cUxNVUpYMW9JNnd4Y0pRNVNyVkttRXZtOERwekxJX2JraWZrdlpIQkRVSU4taktUNHRCOVVvd21GcVAwd0NlVmJEYVN4WnVsOU5GenZnTlhBQVFpZnRqSVR4bUp4dEJyN081UDFzR2Izb1E4aWhqTFhSLUxyT09QUm1fN3pNbkxXa0xHdURhSGdQYkcwUUp5ODBOeEFwQUYtZG5QOGwxUmR0SVZuclNpRkFuQTB0SHY0QmhWaVVyX3BqaFg1OWVyZmsxWU9ybnp3WVM0eTBGRzJrQWpuRWZoUzVqbGV0QnZHOGhrRTZtUlJxeTRhTnpnUjVKeUZKYWdYd1RiVlRMRy1OSFVRdVdBUHhHSGRtQ0JGWVdOMDc0WWVleUh6WHlUX0VCRVQtdTc?oc=5) | - | 뉴스필드 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [반기보고서 무더기 '의견거절'…투자 유의해야 - 아시아경제](https://news.google.com/rss/articles/CBMiYEFVX3lxTE5SaHA3WS14YmJCdkw4blJCSWhaN0tHUXp1OVA4bWREd21McnRkZXFTR05yTEF0VkpSVk5nbXJWN2NKY3FyUnNzUTMzdEhBSVlsVnN1YllUMnFHNGVCZVVVdw?oc=5) | - | 아시아경제 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [장 끝나자 ‘의견거절’ 우수수…반기보고서 마감일 또 ‘올빼미 공시’ - 마켓](https://news.google.com/rss/articles/CBMic0FVX3lxTFBsZlhILU5kVWM2dEc0UDhLcFhIUnlIbWhVcVd5V05RenRldXZtaldBWnhObmdKTVFFcHN5dmxwTVpmdWJLbVR1ZG1ReWF4T2dEMGdsQ05IdkoyVlRVbTNRVEVTNE5JdDF4dDZaZkViMVNlckk?oc=5) | - | 마켓인 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | ["계열사 전반 재무제표 왜곡 의심"… 중앙그룹 피해자들 검사 확대 요구 - ](https://news.google.com/rss/articles/CBMibkFVX3lxTFAyVVZEV2FCZDdpMW12YURXNWIxVGNIdzE0MWoweUFPYUhlbEFHWVFGV2V4WV9uM2U2WDJ1Ri0xb3U0QTlrTVhIaWo3UWRFMTVJSHNvSzlyUjlPV3d1WWNOODg0NFpZSllKOElOekxB0gFzQVVfeXFMTnMzNmJkaFo0LU15RVNMemVtVUpRSVNlblhEV0w3R3BwWXpZNlNrTDM3Q2twSldRYmZ2RHpiWGlpZnppdzRmdThDVzZyaklMcXBiLUx4MDdzSkE5RERob3M3TzBBUnkwUURIU2hMUVR2V0dZUQ?oc=5) | - | 한국일보 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [[단독] JTBC 등 5곳 회계감리 착수…금감원 칼댄다 - SBS Biz](https://news.google.com/rss/articles/CBMiU0FVX3lxTE5BcmF4YUtlQkF5MlZKVTl3clRKN3ZmaWdjbHVmZm11dmVhdko0dDFycE1EdjJhSmJ1WFJmVWJsa2NQdURBV0JtV0I5OTJmQjVEWXc40gFYQVVfeXFMUGJKUnFuN0FlX2J0UHFiYjU0amtueG80c0w3dHVtRlNaS1FabVFOX2hUSFk3Zk93U216cUkzRTY1bE5SbTBHYlFFR2RCVVhXcFptX29hakgwcA?oc=5) | - | SBS Biz |
| 🔴회계신호 | IT | 두나무 | [[단독] 두나무, 美 SEC 위원장 면담, 회계기준 전환 완료...나스닥행 ](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPTE5PSW1ya182NWtnSDlMTmFrSkhvVC1xUmhPNG9zb3ZDZWd2RVVGalBvSFdmT0xMYUd3bWIxbkE1TkF3YVpPTWtxdlVZTUszdGExSTBNMFhBdkZaMkV3V2JpT196UXV0aDVFMmczaWpYbU5YVXpWbDd1Q1cxVmtEMWtfdzZ5WHZydGhB?oc=5) | - | 조선일보 |
| 🔴회계신호 | IT | 두나무 | [두나무, 美 회계기준 검토 …“아직 결정된 바 없어” - 전자신문](https://news.google.com/rss/articles/CBMiTkFVX3lxTE5HZTFwRHZlQ19keGRBM3pQYkk2THNlZjNKRzFmRjNnMV83OFRyLUQ4elVxV2M4ZUV5eTJTSFdleEZtZUNORTVpc1NNTU1iZw?oc=5) | - | 전자신문 |
| 🔴회계신호 | IT | 두나무 | [두나무, 美 나스닥 상장 준비 추진…US GAAP 재무제표 전환 완료 - 블](https://news.google.com/rss/articles/CBMiUEFVX3lxTE5EN3V6bWdoNE5Ld1VrUDFPeEhKTHdTZFlKbEtmdWw3UkVwYVppeXJCeDJmVE9ER0JtVHBiZXUycktwUjAtRklmNDdJM1VRTjVI?oc=5) | - | 블루밍비트 |
| 🔴회계신호 | IT | 두나무 | [두나무 "美 회계기준 검토…주식교환 마치면 IPO" - 비즈워치](https://news.google.com/rss/articles/CBMiakFVX3lxTE5XdU00TXFrTEJLcHI4RFFYcjVUMlIzV1VuVUVrSzFIcGwtdGVvc2pkQzJDOFgtTzlDZnVLNUxFM01ZNUNZVlNUUWNZV3cyTnYtZ3VqMkFyVEdTaGV4dUZoOGpMNndodC1Zd3c?oc=5) | - | 비즈워치 |
| 🔴회계신호 | IT | 두나무 | [‘美 회계기준 전환’ 나스닥 상장설 솔솔…두나무 “사실 아냐, 상장국가 미정](https://news.google.com/rss/articles/CBMiYkFVX3lxTE1UdlAwTl9kVEhJTm1fdl9QVU5NbjdUVm5VYWVJbnhOQlNBbUM4bk94THdKNmJaa1BDeEtFNDY4UVVEeGZ3YjdaeFdUZTRvOG04dU1aMnl6SWlKLXpMbk5Xc1N3?oc=5) | - | 디지털데일리 |
| 🔴회계신호 | IT | 두나무 | [美 회계기준 문의한 두나무, 나스닥 상장說에 "정해진 바 없어" - 아시아경](https://news.google.com/rss/articles/CBMiYEFVX3lxTFB0MmlXbEZMR0dPcGJEU29yX2tSd2UyeG1zdlNHRWZwOGp6SkdDZWl2eDNBc29rQlZlOEpNMEdPVFI3QWNGNWRBZnpGQTRhQThXRW9NazdHa0VpdlI2Q1UtYg?oc=5) | - | 아시아경제 |
| 🔴회계신호 | IT | 두나무 | [두나무 "美 회계기준 전환 사실 아냐"…나스닥행도 '미정' - www.ebn](https://news.google.com/rss/articles/CBMiaEFVX3lxTFBJblR6OS1vc3JSNDhlYUctWUE5TVRPQ29uclIwNG04SGpKQTE0Q0pzYWlIWjVsTERpSHlBemR5OXd3RUhya2liQlRRZ1NtWFpnM3BBMUotdXNiS2NHTmhkb1RscnpjYTJO?oc=5) | - | www.ebn.co.kr |
| 🔴회계신호 | IT | 두나무 | [美 회계기준 검토에 SEC 접촉까지… 두나무 ‘나스닥행’에 쏠린 눈 - 서울](https://news.google.com/rss/articles/CBMib0FVX3lxTE1MS1Vrc0pBUkhkV2Q0ZWFJSUFMMHdzaWl2c2ZGb215TXZXQkhMbEpjX09RX0JUSk1DX3cyOHBIZ21FSkF3YkJpeFo0cEdpbGVaYm5tLS1tSGJYeXlqVFhXUkNPVXdETWRNZlNQNlJxbw?oc=5) | - | 서울신문 |
| 🔴회계신호 | IT | 무신사 | [[재무제표 이야기] 무신사, 재무제표는 더없이 훌륭한데...문제는 오너리스크](https://news.google.com/rss/articles/CBMibEFVX3lxTE1jV2NfN21Kc29OVUJ6bk92V01SLS1HaDV1SlFkeUlfOFpqMU8taHFXQUJVT1JYNjBkWVpRenpqMzZwUnZ2OExBbTdaTVRrNm5ZWHhwa2pHZTBwM0xnNnc1c2paZTJjY29XdWR1UA?oc=5) | - | 생생비즈플러스 |
| 🔵회계이슈 | 게임 | 넷마블 | [[국정감사] "게임판 음원 사재기" 논란에도 정부 조사 없어…김재원, 순위조](https://news.google.com/rss/articles/CBMibkFVX3lxTE1hS2V5dnlPSWVXZkZfOHVGcGxmOWtYNVJQUXR4c3RFdDEzOENvOWZ1dkpqLUJCeUctVUZDSTFUMUhPR2ZPMUQtUVdFOV90bEozUzZnaUhhWjdlcTdSQVUzMFpPR0tGZmxpZnAtVExR?oc=5) | intangible-assets | 에브리뉴스 EveryNews |
| 🔵회계이슈 | 엔터 | 큐브엔터 | [[더벨]큐브엔터 소연, 신곡 '퇴사할게여' 주요 음원차트 1위 - 머니투데이](https://news.google.com/rss/articles/CBMiaEFVX3lxTE5vMURKb1JiaGlzRTNyQXpycVZiMjVUTVFxbEM1WFAzVEdfZGtLRGZyTlFSUDZxdkpDZWZ1NklqNnZVVm1qQ3lVNVV3X2NtRDBPbmZZQ2xDbmY1T1ZWLS1sc0Y1SDF1ZjJK0gFuQVVfeXFMTWR5SUNMblBlb0dSUjRfMU1IbWc5OTNxUG1NaHhMTVVVd3dOZ3RxV0JNQUNOREVqLXMzRzV2Y09wNkV3cVI4QWZkSm82TjhqSWtGZk96Z3B6enFERnUxa01IaUFFdzg1UzNLZHR3UVE?oc=5) | intangible-assets | 머니투데이 |
| 🔵회계이슈 | 미디어 | 스튜디오드래곤 | [[스튜디오드래곤 톺아보기] 판권 상각기준 전격 변경…'수익·비용 매치' 변동](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1ZQ2ZTVFJ3eTNZZ1c0T1AwUjQwNGFULURvV0RIZlpabEhHcnYxYjdkYTZHZTFka2thYy1XRjdKT1MxUUZNR2R1eVB3bUNYU1h4TVlyR0RwMmpGZw?oc=5) | intangible-assets | 블로그 |
| 🔵회계이슈 | 미디어 | 스튜디오드래곤 | [[스튜디오드래곤 톺아보기] 판권 상각기준 전격 변경…'수익·비용 매치' 변동](https://news.google.com/rss/articles/CBMiT0FVX3lxTE9QU0VkMFAzbnhsQnl6amZPVTZYbUtabUVibF9FbmFlNXpLWnRJa0RneFJSNmE5T08xSGtOVFRGS1lpYzRweHdYSGdrUkhYWms?oc=5) | intangible-assets | 딜사이트 |
| 🔵회계이슈 | IT | 카카오 | [[단독] 카카오, 웹툰·음원·카카오T에 스테이블코인 결제 연동…소설 원작 A](https://news.google.com/rss/articles/CBMiTkFVX3lxTE9iLTNtamhiMk54R29YamVpcW8xeDBHOVZpLW5DMWNiNUEyMFRZRVAtUG1MeXVNQ3M1XzhaY3RqZ05wVFQ3bmY1b2xGUGd6dw?oc=5) | intangible-assets | 전자신문 |
| 🔵회계이슈 | IT | 카페24 | [카페24, 2분기 거래액 역대 최대…공격적 투자에 영업익은 27%↓ - 디지](https://news.google.com/rss/articles/CBMiYkFVX3lxTE9zQllFX284RGRhUFBRMnFWdnc4UVNEUXVVMjJsLUpXMnpLZHlMSUFESHBBX0xrTEJMNUNEUnFlRFR6Nl9ydjJyZVJxSFJkNHV1V0tVY2NlUXVPck1fenQ0OW5B?oc=5) | platform-cases | 디지털데일리 |
| 🔵회계이슈 | IT | 컬리 | [컬리어스 '파인에비뉴 A동' 매각 자문 완료…누적 거래액 3.2조 돌파 - ](https://news.google.com/rss/articles/CBMickFVX3lxTE5IUlBuUW84Nm5KbnZhbFZBY2ZSMmlReENnR1JhUTZ6c3JIdUhYRVVFSlhWdk1VVVdTQTlPdWRZTVRDandOZnhnTnJGWXAwblBHaG5jUTltcW5aTVF3M3k5RG1UOFZZUUlNY2xvdE0xUVpwQQ?oc=5) | platform-cases | 마켓인 |
| 🔵회계이슈 | IT | 컬리 | [컬리 김치 거래액 35% 늘어…김장 대신 사 먹는다 - 자본시장뉴스](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9WenJqUGlXNHl4NGFqaU1nRGJPeFBQWHZkbXJ4bE91OTUzVzFiUVA3aUZ6TkFNTVo3TFd1THFwdlU3cFZ3amUxMzdQd0F0STBLdTBPUURwY05kdi1VMkNXZlpuRi1rbFE?oc=5) | platform-cases | 자본시장뉴스 |
| 일반 | 게임 | 넷마블 | [넷마블 '솔' 1200억 · 컴투스 '제우스' 한 달 470억 벌었다 - 디](https://news.google.com/rss/articles/CBMiZkFVX3lxTFBNblRuc1JUc0FqQjhBaVNiaGdqVTJzSGFXRHQxaGV3OG9YbFlsZzdjNklFTkx2cDJMaGxkUHplZm1WWHBzVm1PR29pZURETzdKa1lwQ29TVEhhS0xwd2J3eG82NEhaZw?oc=5) | - | 디일렉 |
| 일반 | 게임 | 넷마블 | [넷마블넥서스의 AI 코딩 도구 도입기 – 게임 개발팀의 Kiro 도입 및 활](https://news.google.com/rss/articles/CBMid0FVX3lxTE9KSVd3RHZXMTlSV3Z4Q1VDMi1iRVJyUWtxaWRmQ0J1WkdKVkdNaG5oTTZxQnpWcnc1ZkJUWnBhMl9yTGwxRkkxc0s5TlV0UDR0cHF4WUdYLVQ3ZjJVLVBJVDN6TnJhWUpWS000cXpHVFl2Q0Y1cVk4?oc=5) | - | Amazon Web Services (AWS) |
| 일반 | 게임 | 넷마블 | [[게임프리뷰] 넷마블이 선사하는 차세대 4인 액션 〈이블베인〉 - 글로벌E](https://news.google.com/rss/articles/CBMia0FVX3lxTFAtOGNpVXpOM3hneXZYbGIyZWpmVWdkbU5zLXJUYjFUbWZYV096bG00b25RcFA5TzctU0FQSGxsUHExcVlBOFBXUGdKT2ZLaTJVTTdSSDdEWkpSVEdrdDB4eVBNQk9ETm41cnMw0gFvQVVfeXFMT3lXZWhjVlB5M3h1UmF1WUxmcE02dHhpNTVwZWl1dnJxbnhPV3pxVWdJZzFCSzJWeGYwZUZFUlR3VUxrZDNuTlpzNWY1SHpIcVZLY09JVjMzRVpSNjZUSmFfTzYyakdYRVVTbFNiM1Zj?oc=5) | - | 글로벌E |
| 일반 | 게임 | 넷마블 | [‘텐센트 리스크’ 떨친 넷마블, 4000억 자사주 소각으로 밸류업 [자사주 ](https://news.google.com/rss/articles/CBMifEFVX3lxTFBmZE9md3dhUW54ZG9ieGV5c1RpeTltYzR2REs2Qnc0LWxuazQ1Z3B3a21hZDV3QmdGWUpCM2tpZVVhLVdqVV9SN2x4dWYzbHpWczB1LWRjNGxsLU5nSkhGTnl4QVE4SVN4WG03UzN5YTZiaEQ2YXhpWmd4TjM?oc=5) | - | 금융신문 |
| 일반 | 게임 | 넷마블 | [[N2 포커스] 넷마블, 코웨이 지분에 1500억 투입…추진 배경은 - 뉴스](https://news.google.com/rss/articles/CBMiXkFVX3lxTE9Bb2pNWXdKUmRiUmNZcWprTlpaRWJnQXBqT0dUZDhiS053X1RtWHpRQkNGMU92Y3V0RGdsNksybExCZWl3NnJyQ1NLbEZiR1lFS3AzTV9vWjNBTXJYTWc?oc=5) | - | 뉴스투데이 |
| 일반 | 게임 | 엔씨소프트 | [NC, 아이온2 흥행 기대엔 못 미쳐…목표가↓-NH By 인포스탁데일리 - ](https://news.google.com/rss/articles/CBMicEFVX3lxTE1wRk9LQVlCcmt4alh0MlFfbEgyY2NiWktpQ25RM3pNd0FMM2ZkbVNlNFNvcXJteFlvaE1Uc2FIMVRIVGlObEJuSmVOTnZBUjZIdm9RUG1kVFVyUkVEcEtHMVMxZk9MTW9fVU81VEY5X2I?oc=5) | - | Investing.com 한국어 |
| 일반 | 게임 | 엔씨소프트 | [엔씨소프트, ‘아이온2 글로벌’ 초반 흥행…4분기 실적 기대감↑ - 조세금융](https://news.google.com/rss/articles/CBMiZkFVX3lxTE5MbmVyT1pmUXd3Y1ZpV0JjVjIzdXhPRVQwcVY3ZDFFT2J4ZE9tT0V5dF9xSlJNQnY5a3cxYUZNQXNHTXJONWp4WFpIM011cnV5YTQxdFlUNjl6Z2ZPOFpjekpCMXBidw?oc=5) | - | 조세금융신문 |
| 일반 | 게임 | 엔씨소프트 | [‘아이온2’ 5일 글로벌 출시 … 엔씨 주가 힘받나 - 조선일보](https://news.google.com/rss/articles/CBMigwFBVV95cUxOODZyOGpsRDNsdXpOTF91NExKYzN1WGIyM0wxLVhlbHlobHIxV2JJWmI4bDJORnpCYnBVZlhzbHdOdnRQbjc0OGpvMlhLSGRrSC1TTGpwY0RNUzl0UzR3eEltTXBLX3JtZGU0OFVDb296MUF3UHdKeUV6Z3JVRlhLMzI2VQ?oc=5) | - | 조선일보 |
| 일반 | 게임 | 엔씨소프트 | [김택진 동생 김택헌, 엔씨 주식 전량 매도…퇴임 2년 만에 지분 정리 - 연](https://news.google.com/rss/articles/CBMicEFVX3lxTE5NZUlBRzVjWkpaY3F1MXdkelJpS0RPNFN2b1psRmViUGVhVHZiM3ZqRndiMXFMOFpCQzJLXzdXQ1Zab0daYndJcWN4ZHlPbTlqYVB6S192UGZNSC1oSzhrV2dPcVdaeXQxSWtVaHY3bTI?oc=5) | - | 연합인포맥스 |
| 일반 | 게임 | 엔씨소프트 | [엔씨, 리니지2 ‘BASIC’ 업데이트 예고 - 스마트투데이](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBScUhzdEtJcGZEVFh3bWxDcnlCVWxXbXJFcG1CdTZfa3JFVFBfRG4xWkZPWFFSN013aUtONVZWblV0c1daUXpWZXZ0ZlhZQWRxbHZhalRXa0FkZ1FzcW5j?oc=5) | - | 스마트투데이 |
| 일반 | 게임 | 크래프톤 | [게임업계 3분기 실적 희비…크래프톤 매출 1조·엔씨 흑자 전망 - 연합뉴스](https://news.google.com/rss/articles/CBMiW0FVX3lxTE41X1poa1VUTmd3ak9fcEZYVmROVW4yeEFQTjhNODNhM09VMUVWMk5aS0VKeVF6V3ZsMW12ZXF0VUU0WWxoTzYyMnZaSFJlVnd6dWNHeTVWN2M2eDDSAWBBVV95cUxOSDBERnVKWUVKaDNEeWpScFUza0tlVlBBUDdMWWtoWkZoMXQ2eG5fV1YtRlZxWHQzbXgycHVJek9MaFNmaVVYWkRCNmVJTV9XTExmR1ExRHFMRXZ0bEhhWjU?oc=5) | - | 연합뉴스 |
| 일반 | 게임 | 크래프톤 | [크래프톤, 브라질에 첫 남미 거점…K게임 신시장 공략 본격화 - 한국경제](https://news.google.com/rss/articles/CBMiWkFVX3lxTE05cFFFQUprNHNLMl9va2JYMlUxOHhVenFNUWdIcGYwZXRLZm9kTTAxdHJGSG5hTjM5eTRBbDFoZEtPSjFhZzZCWmNpT1NfenljNGVmMG9UemRVQQ?oc=5) | - | 한국경제 |
| 일반 | 게임 | 크래프톤 | [크래프톤, 넷플릭스와 'PUBG' 실사 시리즈 제작 발표 - 지디넷코리아](https://news.google.com/rss/articles/CBMiVkFVX3lxTFB1dnVNSmhtYTBUUmMwWm1QbjA5U0ptT2lsMF83S2kwWXU0VWhza1ptYWk4d3VvemZKV3R0YVZpRmlrVmdmV1U3NGRSZ05neGVJQThFUElB?oc=5) | - | 지디넷코리아 |
| 일반 | 게임 | 크래프톤 | [장병규 크래프톤 의장 “익숙한 길 벗어나야 새로운 기회 열린다” - Chos](https://news.google.com/rss/articles/CBMiggFBVV95cUxPX1NZcW84aDhWWVJ5ZzFSX056YjdtLVR0eE15cHowWGJqSzZoSEZFR0pBVVBkQm9EV0lza1dfNXhQbVplblBXRUFyencyVmFST0M2aEllYk4zNExuR3ZlWXBDUEFRcDlxdW9hVllBTlc3aGtfNWtNVWxNUzZLaVQtcFBR0gGWAUFVX3lxTE5qZUhEaElKTExuX19ubDBvQVBCV2FYVGtCN1BWTnNXaUNxLU5qaDJfYVMyaGRPZ2VhUGEtVVlsQ3pSRW1Ba2U1RW1EWkR6emtVMGVUdGZkaVBmVkhJUFA2TVpYWmhYVl9OcXJVc0VzNkNsOWRJRWdfaEs1MUNHWldLWGg2RHNXRVRmXzZKOU05UE1pdXduUQ?oc=5) | - | Chosunbiz |
| 일반 | 게임 | 크래프톤 | [크래프톤, 실적 좋아도 '흐림'...삼중고 넘어설까 - 글로벌이코노믹](https://news.google.com/rss/articles/CBMif0FVX3lxTE5SeEYzZjg0dkJZa2stVzN6UldUQjYzeVFkaDl5T2VkTDVfVC1DbVBJanpNM19PZnhQUmt5SU56ZWNMQWxqOXVmaWNBTWZOSU9KX29DWFBxUVZ5bktzU1dfQ2NjZUdwM3JvQ3Z0N0psMm9rS3R5b3lXUVAzVXh6MGs?oc=5) | - | 글로벌이코노믹 |
| 일반 | 게임 | 펄어비스 | [AMD 경영진, 펄어비스 방문... '붉은사막' 기술 협력 확대 논의 - 전](https://news.google.com/rss/articles/CBMiTkFVX3lxTE1sS3h3aFQ5RDlIWWpHRUE0RHU3alFrMjdnOVl6MktadXNmOGRVNWppc3FBOGhyc3pqRV94M1pPN3hpemZBTnNsZEc0bmRuUQ?oc=5) | - | 전자신문 |
| 일반 | 게임 | 펄어비스 | ['붉은사막' 흥행에도···펄어비스, 내년엔 66% 역성장 전망 왜? - 뉴스](https://news.google.com/rss/articles/CBMiakFVX3lxTFBlUFQtMm1Nc1picHIzdERxbXRYWFFzekU4ZmludWRZT2xRSUlRZGtQV005X0FwR2ZhUVp2QTVod2VkOEcxbDNNMUxQOWdUYnZlUUJ6c2U3RWxsd0tka293NlM3dEpYUGtSRXc?oc=5) | - | 뉴스웨이 |
| 일반 | 게임 | 펄어비스 | [펄어비스, '붉은사막 인핸스드' 첫 DLC 출시 - MTN 머니투데이방송](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9ZdVFlb3dMM29FRzNKZEFESU1BX1FXNVdSVEpmUUVDWXVra0Y2OVNBUEZPVF8tejZLd1R4dUQ2dC1FV1FmWV82Y0RZaXBZcFV3ak9OOTBvQ2tabDBkTlpj?oc=5) | - | MTN 머니투데이방송 |
| 일반 | 게임 | 펄어비스 | [펄어비스 3분기 영업익 둔화…4분기 DLC 출시로 반등 모색 - 디일렉](https://news.google.com/rss/articles/CBMiZkFVX3lxTFBOLUF5QjJaYVZmbmpoOUo1SURQdXhmaXRTWktJX1VfN3ZzZklmMlpnVlpJbFF5Qm51ODJqVzFNVlg4SU5vYU5hRy1FUFFEUjZMbkpPMHQ5Ry1XbnU4V2p6MFQ1SG5QZw?oc=5) | - | 디일렉 |
| 일반 | 게임 | 펄어비스 | [[클릭! e 게임]“영상만으로 ‘잠재력’ 확신”…펄어비스 ‘붉은사막’ 그래픽](https://news.google.com/rss/articles/CBMiUEFVX3lxTFBqWXFCbVBDTGVOOVI4VkNtb2lHRC15b3ZKcGlIVFBEZHdPMkhGUkhCSm1qZnhsUENsbUFzMVlvekd6U05lSzdFaTBqTXgzN0Rk?oc=5) | - | 문화일보 |

### 🏢 회계법인 산업 리포트
**최근 수집된 발간물**

| 법인 | 리포트 |
|---|---|
| EY한영 | [지정학적 리스크 상시화, 한국 기업의 공급망은 어떻게 달라져야 할까요?](https://www.ey.com/ko_kr/insights/geostrategy/geopolitical-risks-and-korean-supply-chains) |
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
