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
_최종 갱신: 2026-10-26 10:06 KST_

**수집 현황** — DART 공시 151 · 뉴스 352 · 회계법인 리포트 2

### 📄 DART 공시 (회계 이슈 필터)
_종류별: 실적 72 · 📘정기 54 · 🔴정정 7 · 🟡주요사항 18_

| 종류 | 업종 | 기업 | 일자 | 공시 |
|---|---|---|---|---|
| 🔴정정 | 통신 | 엘지유플러스 | 20261015 | [[기재정정]증권신고서(채무증권)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261015000362) |
| 🔴정정 | 게임 | 위메이드 | 20261014 | [[기재정정]최대주주변경을수반하는주식양수도계약체결](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261014900192) |
| 🔴정정 | 엔터 | 큐브엔터 | 20260831 | [[기재정정]주요사항보고서(유상증자결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260831001295) |
| 🔴정정 | IT | 카카오 | 20260824 | [[첨부정정]주요사항보고서(회사합병결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260824000219) |
| 🔴정정 | IT | 카카오 | 20260819 | [[기재정정]반기보고서 (2026.06)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260819000055) |
| 🔴정정 | IT | 다우데이타 | 20260811 | [[기재정정]회사합병결정(종속회사의주요경영사항)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260811900833) |
| 🔴정정 | 게임 | 넷마블 | 20260807 | [[기재정정]증권발행실적보고서(합병등)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260807000552) |
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
| 실적 | 게임 | 컴투스 | 20261023 | [결산실적공시예고](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261023900628) |
| 실적 | IT | 안랩 | 20261023 | [결산실적공시예고](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261023900438) |
| 실적 | 통신 | 엘지유플러스 | 20261021 | [증권발행실적보고서](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261021000340) |
| 실적 | 게임 | 크래프톤 | 20261020 | [결산실적공시예고(안내공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261020800466) |
| 실적 | 게임 | 위메이드 | 20261020 | [결산실적공시예고](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261020900344) |
| 실적 | 게임 | 네오위즈 | 20261020 | [결산실적공시예고](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261020900613) |
| 실적 | 엔터 | 에스엠엔터테인먼트 | 20261020 | [결산실적공시예고](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261020900545) |
| 실적 | 미디어 | 제일기획 | 20261020 | [결산실적공시예고(안내공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261020800589) |
| 실적 | IT | 엔에이치엔 | 20261019 | [결산실적공시예고(안내공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261019800530) |
| 실적 | 게임 | 펄어비스 | 20261016 | [결산실적공시예고](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261016900906) |

### 📰 뉴스 모니터링 (🔴 = 감사·재무제표 신호)
_구분: 🔴회계신호 23 · 🔵회계이슈 19 · 일반 310_

| 구분 | 업종 | 기업 | 기사 | 회계토픽 | 출처 |
|---|---|---|---|---|---|
| 🔴회계신호 | 게임 | 넷마블 | [[재무제표 이야기] '정수기 게임' 우려 딛고 넷마블의 ‘황금알’ 된 코웨이](https://news.google.com/rss/articles/CBMibEFVX3lxTE56UWVmcFpXTmhHZm1hanhhWFFjNUljbWpuZndaYUdQckRQTmUzTEtJb3hkU0p2b21jZ1RjSXZhZ0dQc19BRlhkTzFJTlVTM1NtbDB5emxnb1k0MDFQd1JkY3owVVItN3dkZjYzdA?oc=5) | - | 생생비즈플러스 |
| 🔴회계신호 | 게임 | 펄어비스 | [경실련, 국세청·금감원에 5개 게임사 신고… GVP 계약 회계처리 검증 요구](https://news.google.com/rss/articles/CBMia0FVX3lxTFB0Vm1ub053ekhzd2lQRzhwOHFSYWgwQS1rMWpOQnpRQlpiMm5tREp1ME0xalBJMUtKMTk1TEJhMnc4YWI0QU9lUnRuWFVGS3VkcG5TMXE3UVpCY2FjeHE4d2J4VXlSWWlPUVA40gFvQVVfeXFMTlNmd2dmOG5XSGNUVXdzbjgxMmJCR0ZKTXZqSDJvMTNWTnhyOXRWeXRESnZyWlAwMnAyT3ExQ3ZVSXNjSHZ6LUZUbngyT1BPZW5fcGJTLVlaX19Tcm5UM3N5RnJ6S0V3X01OMjZMS0F3?oc=5) | - | 시사위크 |
| 🔴회계신호 | 엔터 | 하이브 | [의견거절·재무제표 재작성…'암살자(들)' 제작사 하이브미디어코프 회계관리 도](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1Tc1FHRU5CMFp6LUlBcUJkd0FtU195bV9fRGQ2R0NDMjMxWDJ4UW9OTXVRcFRHMzdhSWdiaEVIRkl5WmY5czB3RkJpb0tFdkJHUm5FekFsMzVUdw?oc=5) | - | 블로그 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [금감원, 메가박스·콘텐트리중앙 회계심사 돌입…자금 조달·회계처리 점검 - K](https://news.google.com/rss/articles/CBMiW0FVX3lxTE54OUVMRE9hMTAyNThval9sRFV5ZDNOeFBHODQ2bmdNQmh5WU41UWtJU2RrZ2ttcEZ0SFhkRm03QjM5R3cxR21pbTJKUFU5ZzFCbEFTSFIwN3hWQUU?oc=5) | - | KBS 뉴스 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [유동부채 1.4조 늪…’적정’ 받던 콘텐트리중앙, 5개월 만에 ‘의견거절’ ](https://news.google.com/rss/articles/CBMirAJBVV95cUxNVUpYMW9JNnd4Y0pRNVNyVkttRXZtOERwekxJX2JraWZrdlpIQkRVSU4taktUNHRCOVVvd21GcVAwd0NlVmJEYVN4WnVsOU5GenZnTlhBQVFpZnRqSVR4bUp4dEJyN081UDFzR2Izb1E4aWhqTFhSLUxyT09QUm1fN3pNbkxXa0xHdURhSGdQYkcwUUp5ODBOeEFwQUYtZG5QOGwxUmR0SVZuclNpRkFuQTB0SHY0QmhWaVVyX3BqaFg1OWVyZmsxWU9ybnp3WVM0eTBGRzJrQWpuRWZoUzVqbGV0QnZHOGhrRTZtUlJxeTRhTnpnUjVKeUZKYWdYd1RiVlRMRy1OSFVRdVdBUHhHSGRtQ0JGWVdOMDc0WWVleUh6WHlUX0VCRVQtdTc?oc=5) | - | 뉴스필드 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [금감원, 메가박스·콘텐트리중앙 회계심사 돌입…자금 조달·회계처리 점검 - D](https://news.google.com/rss/articles/CBMiRkFVX3lxTE80LURCejkydGZMLWJjaVZjYncwZWZaSkZPZmZtYTRNU0F0TFNEN29RSG5RYlRNcFlTY3VkVGNET2p4RXZFTWc?oc=5) | - | Daum |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [장 끝나자 ‘의견거절’ 우수수…반기보고서 마감일 또 ‘올빼미 공시’ - 마켓](https://news.google.com/rss/articles/CBMic0FVX3lxTFBsZlhILU5kVWM2dEc0UDhLcFhIUnlIbWhVcVd5V05RenRldXZtaldBWnhObmdKTVFFcHN5dmxwTVpmdWJLbVR1ZG1ReWF4T2dEMGdsQ05IdkoyVlRVbTNRVEVTNE5JdDF4dDZaZkViMVNlckk?oc=5) | - | 마켓인 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [반기보고서 무더기 '의견거절'…투자 유의해야 - 아시아경제](https://news.google.com/rss/articles/CBMiYEFVX3lxTE5SaHA3WS14YmJCdkw4blJCSWhaN0tHUXp1OVA4bWREd21McnRkZXFTR05yTEF0VkpSVk5nbXJWN2NKY3FyUnNzUTMzdEhBSVlsVnN1YllUMnFHNGVCZVVVdw?oc=5) | - | 아시아경제 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권 피해자들, 금감원에 회계법인 감리 요구..."돌려막기 규명" ](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5wdTRtX0dLQU5xZENjanI3OVRkUTlaZlllQ1JhMEQ2NXVhZ0lxcmdzcXNGN2lmM3BTYUE3bFAwLUQ5QVQyQnZYY090TnRRT3FsWE1wNS14MVRLMGRTWDlB?oc=5) | - | 조세일보 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | ["계열사 전반 재무제표 왜곡 의심"… 중앙그룹 피해자들 검사 확대 요구 - ](https://news.google.com/rss/articles/CBMibkFVX3lxTFAyVVZEV2FCZDdpMW12YURXNWIxVGNIdzE0MWoweUFPYUhlbEFHWVFGV2V4WV9uM2U2WDJ1Ri0xb3U0QTlrTVhIaWo3UWRFMTVJSHNvSzlyUjlPV3d1WWNOODg0NFpZSllKOElOekxB0gFzQVVfeXFMTnMzNmJkaFo0LU15RVNMemVtVUpRSVNlblhEV0w3R3BwWXpZNlNrTDM3Q2twSldRYmZ2RHpiWGlpZnppdzRmdThDVzZyaklMcXBiLUx4MDdzSkE5RERob3M3TzBBUnkwUURIU2hMUVR2V0dZUQ?oc=5) | - | 한국일보 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권 투자자들 "7405억 충당금 미설정"…금감원 감리 요청 - 뉴](https://news.google.com/rss/articles/CBMiX0FVX3lxTE90QkpoNk1ucVpmMVRSTkhPQUdiZFMtUFJfYTJ3WmFwVDZsZFl5Zk9IX1RnSlQ0X2I0T0Nod09yLWNqTlhta0JneWpyMHpwbG9qZl9uUndnMDFIdDI4bzI4?oc=5) | - | 뉴스1 |
| 🔴회계신호 | IT | 네이버 | [[단독] 두나무, 美 SEC 위원장 면담, 회계기준 전환 완료...나스닥행 ](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPTE5PSW1ya182NWtnSDlMTmFrSkhvVC1xUmhPNG9zb3ZDZWd2RVVGalBvSFdmT0xMYUd3bWIxbkE1TkF3YVpPTWtxdlVZTUszdGExSTBNMFhBdkZaMkV3V2JpT196UXV0aDVFMmczaWpYbU5YVXpWbDd1Q1cxVmtEMWtfdzZ5WHZydGhB?oc=5) | - | 조선일보 |
| 🔴회계신호 | IT | 네이버 | [두나무 "美 회계기준 검토…주식교환 마치면 IPO" - 비즈워치](https://news.google.com/rss/articles/CBMiakFVX3lxTE5XdU00TXFrTEJLcHI4RFFYcjVUMlIzV1VuVUVrSzFIcGwtdGVvc2pkQzJDOFgtTzlDZnVLNUxFM01ZNUNZVlNUUWNZV3cyTnYtZ3VqMkFyVEdTaGV4dUZoOGpMNndodC1Zd3c?oc=5) | - | 비즈워치 |
| 🔴회계신호 | IT | 두나무 | [두나무, 美 회계기준 검토 …“아직 결정된 바 없어” - 전자신문](https://news.google.com/rss/articles/CBMiTkFVX3lxTE5HZTFwRHZlQ19keGRBM3pQYkk2THNlZjNKRzFmRjNnMV83OFRyLUQ4elVxV2M4ZUV5eTJTSFdleEZtZUNORTVpc1NNTU1iZw?oc=5) | - | 전자신문 |
| 🔴회계신호 | IT | 두나무 | [두나무, 美 나스닥 상장 준비 추진…US GAAP 재무제표 전환 완료 - 블](https://news.google.com/rss/articles/CBMiUEFVX3lxTE5EN3V6bWdoNE5Ld1VrUDFPeEhKTHdTZFlKbEtmdWw3UkVwYVppeXJCeDJmVE9ER0JtVHBiZXUycktwUjAtRklmNDdJM1VRTjVI?oc=5) | - | 블루밍비트 |
| 🔴회계신호 | IT | 두나무 | [‘美 회계기준 전환’ 나스닥 상장설 솔솔…두나무 “사실 아냐, 상장국가 미정](https://news.google.com/rss/articles/CBMiYkFVX3lxTE1UdlAwTl9kVEhJTm1fdl9QVU5NbjdUVm5VYWVJbnhOQlNBbUM4bk94THdKNmJaa1BDeEtFNDY4UVVEeGZ3YjdaeFdUZTRvOG04dU1aMnl6SWlKLXpMbk5Xc1N3?oc=5) | - | 디지털데일리 |
| 🔴회계신호 | IT | 두나무 | [두나무 "美 회계기준 전환 사실 아냐"…나스닥행도 '미정' - www.ebn](https://news.google.com/rss/articles/CBMiaEFVX3lxTFBJblR6OS1vc3JSNDhlYUctWUE5TVRPQ29uclIwNG04SGpKQTE0Q0pzYWlIWjVsTERpSHlBemR5OXd3RUhya2liQlRRZ1NtWFpnM3BBMUotdXNiS2NHTmhkb1RscnpjYTJO?oc=5) | - | www.ebn.co.kr |
| 🔴회계신호 | IT | 두나무 | [美 회계기준 문의한 두나무, 나스닥 상장說에 "정해진 바 없어" - 아시아경](https://news.google.com/rss/articles/CBMiYEFVX3lxTFB0MmlXbEZMR0dPcGJEU29yX2tSd2UyeG1zdlNHRWZwOGp6SkdDZWl2eDNBc29rQlZlOEpNMEdPVFI3QWNGNWRBZnpGQTRhQThXRW9NazdHa0VpdlI2Q1UtYg?oc=5) | - | 아시아경제 |
| 🔴회계신호 | IT | 두나무 | [美 회계기준 검토에 SEC 접촉까지… 두나무 ‘나스닥행’에 쏠린 눈 - 서울](https://news.google.com/rss/articles/CBMib0FVX3lxTE1MS1Vrc0pBUkhkV2Q0ZWFJSUFMMHdzaWl2c2ZGb215TXZXQkhMbEpjX09RX0JUSk1DX3cyOHBIZ21FSkF3YkJpeFo0cEdpbGVaYm5tLS1tSGJYeXlqVFhXUkNPVXdETWRNZlNQNlJxbw?oc=5) | - | 서울신문 |
| 🔴회계신호 | IT | 두나무 | [두나무, 美 회계기준 검토…상장 국가는 미정 - 아주경제](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5QZmxPY1VoZDBoeVMtNUptQUU0Skkza3I3d1NISVVrWDRNWk84QklUUlFaeGRydWVRNDV2eDFTb1d4elNoRkFEOWQyUGdLbGQwYllhUFZDcm9yZ9IBWEFVX3lxTE5XNHNNNGppTzJzWG5IdjQ2eUF6OHJTT2M0T1JoTGx3ZVNmQ2FiaFY1Q05jTnFQYnl4WjZySnJGTnU3d0sxWEwyZ3l6UzJ3X1gyWFRDUm1qZUE?oc=5) | - | 아주경제 |
| 🔴회계신호 | IT | 두나무 | [두나무 “美 상장 확정 아냐…회계기준 전환도 사실무근” - 뉴스투데이](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1PZzA0UVNnSERESm1NWDJmMVdLX25MWmFxSkdwZDcxRVZRRlZVM2ZScXhqbHlTM19rQ0x4VFUtUml0SDJDTEhYbmxRSDhqV0NtaENEYVpoYWtxTjg?oc=5) | - | 뉴스투데이 |
| 🔴회계신호 | IT | 다우기술 | [‘몸값 6000억원?’…중앙일보 진짜 가격표는 [재무제표 AI 독해] - 한](https://news.google.com/rss/articles/CBMibEFVX3lxTE1MbUtmTVBIS3ptTXgzUzNIRHZ2eXc3NnUzSXVlSEhxU0ZOcVI1VTZ1MENuVUFCNTFmMlJaMXE0SHlaSGU1WVVhZnk4S3dFWWwtRWx1aGY3cml2VDlyQVowVXdORnhJWlZwTERtRA?oc=5) | - | 한경매거진 |
| 🔴회계신호 | IT | 무신사 | [[재무제표 이야기] 무신사, 재무제표는 더없이 훌륭한데...문제는 오너리스크](https://news.google.com/rss/articles/CBMibEFVX3lxTE1jV2NfN21Kc29OVUJ6bk92V01SLS1HaDV1SlFkeUlfOFpqMU8taHFXQUJVT1JYNjBkWVpRenpqMzZwUnZ2OExBbTdaTVRrNm5ZWHhwa2pHZTBwM0xnNnc1c2paZTJjY29XdWR1UA?oc=5) | - | 생생비즈플러스 |
| 🔵회계이슈 | 게임 | 넷마블 | [[국정감사] "게임판 음원 사재기" 논란에도 정부 조사 없어…김재원, 순위조](https://news.google.com/rss/articles/CBMibkFVX3lxTE1hS2V5dnlPSWVXZkZfOHVGcGxmOWtYNVJQUXR4c3RFdDEzOENvOWZ1dkpqLUJCeUctVUZDSTFUMUhPR2ZPMUQtUVdFOV90bEozUzZnaUhhWjdlcTdSQVUzMFpPR0tGZmxpZnAtVExR?oc=5) | intangible-assets | 에브리뉴스 EveryNews |
| 🔵회계이슈 | 게임 | 위메이드 | [[IB토마토]위메이드, 매출 기반 해외로 이동…라이선스 변동성은 부담 - 뉴](https://news.google.com/rss/articles/CBMiYEFVX3lxTE5YUjdvYjNraTkxUlBnRDdVM3ZBaVl2S21ZdFRtWVFPRE1GY0Yyc3NTOWdjZkw0QjBkb1F5eWMtcFVzbUMtTzg3Z1NCWmd5TlBOSm91ejlfYzBYQVdHR3RmXw?oc=5) | intangible-assets | 뉴스토마토 |
| 🔵회계이슈 | 엔터 | 하이브 | [하이브, 역대 최대 실적에도 M&A는 ‘마이너스’… 1조원대 영업권도 부담 ](https://news.google.com/rss/articles/CBMicEFVX3lxTE1EclZkd2RpcVphX0ZoLUh2SHpodTZEZlBUazZxVTVfSWlXcWNQbXJKOHF0MUQ1MVcxc2puQlVOUV9zUjZlZDIzOEg2MmRFSmYyZ0V3cWlLaEtOSlV4QVA4NTRBUEgzVGNzX01BTnBXbW3SAXRBVV95cUxQNFZxR3lGNmx5Z0FHVlVOZjdEd0N2Yk1jaVNLem5zMHJWWmhpcFE0N1F3b3BZTXNyZTRIeU1CS0VNbGJ1cWdQWDZuUzM2cHlNWXRxS3NqYmRWalQ1cTJYM2FOWDVDa0hQNkhvd3lVTkI1alczVg?oc=5) | intangible-assets | IT조선 |
| 🔵회계이슈 | 엔터 | 큐브엔터 | [[더벨]큐브엔터 소연, 신곡 '퇴사할게여' 주요 음원차트 1위 - 머니투데이](https://news.google.com/rss/articles/CBMiaEFVX3lxTE5vMURKb1JiaGlzRTNyQXpycVZiMjVUTVFxbEM1WFAzVEdfZGtLRGZyTlFSUDZxdkpDZWZ1NklqNnZVVm1qQ3lVNVV3X2NtRDBPbmZZQ2xDbmY1T1ZWLS1sc0Y1SDF1ZjJK0gFuQVVfeXFMTWR5SUNMblBlb0dSUjRfMU1IbWc5OTNxUG1NaHhMTVVVd3dOZ3RxV0JNQUNOREVqLXMzRzV2Y09wNkV3cVI4QWZkSm82TjhqSWtGZk96Z3B6enFERnUxa01IaUFFdzg1UzNLZHR3UVE?oc=5) | intangible-assets | 머니투데이 |
| 🔵회계이슈 | 미디어 | 위지윅스튜디오 | [컴투스, 레드아이스와 ‘IP 동맹’…게임 넘어 콘텐츠 밸류체인 넓힌다 - 팝](https://news.google.com/rss/articles/CBMibkFVX3lxTE9PcjNoMEJnNkFabGc0dkNMRDZCVkJpS3p4Zm16aVVSQ0tWQWNDajJzcHNiOWdxVEQxVTdpVkZaandMbkROaVBXNXdULVZxQVRQa00tcWVCUlZhUE5ZaDNlczM1ZzZObGlZQmZ0UDVn0gFyQVVfeXFMT3lFXzZ1RGlpRGxNQ09BVDdxaEh3ZWdhMDJhdWdtV3BGT3FTNmNEN2tPZ2JMczAwZEtsWnU5eGloU0c1WE10MDlFenFYcXRnM2J0MV8tMkV2UENqQk5PY0VVbEtMSnBQbDRGT1BsVWZJQzdn?oc=5) | industry-structure | 팝콘뉴스 |
| 🔵회계이슈 | 미디어 | 스튜디오드래곤 | [[스튜디오드래곤 톺아보기] 판권 상각기준 전격 변경…'수익·비용 매치' 변동](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1ZQ2ZTVFJ3eTNZZ1c0T1AwUjQwNGFULURvV0RIZlpabEhHcnYxYjdkYTZHZTFka2thYy1XRjdKT1MxUUZNR2R1eVB3bUNYU1h4TVlyR0RwMmpGZw?oc=5) | intangible-assets | 블로그 |
| 🔵회계이슈 | IT | 카카오 | [[단독] 카카오, 웹툰·음원·카카오T에 스테이블코인 결제 연동…소설 원작 A](https://news.google.com/rss/articles/CBMiTkFVX3lxTE9iLTNtamhiMk54R29YamVpcW8xeDBHOVZpLW5DMWNiNUEyMFRZRVAtUG1MeXVNQ3M1XzhaY3RqZ05wVFQ3bmY1b2xGUGd6dw?oc=5) | intangible-assets | 전자신문 |
| 🔵회계이슈 | IT | 카페24 | [카페24, 2분기 거래액 역대 최대…공격적 투자에 영업익은 27%↓ - 디지](https://news.google.com/rss/articles/CBMiYkFVX3lxTE9zQllFX284RGRhUFBRMnFWdnc4UVNEUXVVMjJsLUpXMnpLZHlMSUFESHBBX0xrTEJMNUNEUnFlRFR6Nl9ydjJyZVJxSFJkNHV1V0tVY2NlUXVPck1fenQ0OW5B?oc=5) | platform-cases | 디지털데일리 |
| 🔵회계이슈 | IT | 메가존클라우드 | [제주콘텐츠진흥원, AWS·메가존클라우드와 협력…콘텐츠산업 AX 본격화 - 제](https://news.google.com/rss/articles/CBMib0FVX3lxTFBQU1U5NGxtamZtU3h1WFpPVEpQdmUtMHNmV3dkNzB3NV8yS3ZvXzVqM1dqMFM3dXV5VHBvLUVVbnFtWVNUcEFIUUYtbHREYnJGZ3VLNE13aVJGXzZiV2d0bEExOGJoRkVSODNVRjRvaw?oc=5) | industry-structure | 제주도민일보 |
| 🔵회계이슈 | IT | 쿠팡 | [쿠팡풀필먼트서비스, 리스부채 1.7조원..3084억 상환에도 7629억 증가](https://news.google.com/rss/articles/CBMiUkFVX3lxTE9WYjhtT0xRcFBBT0tiQUVFMUdSQjhOMWJsWFRmQ19vMExodnFjZnNxWFk5dWdEaTIzN01vTHJUS1JQcWZVVkN1M0hkdmZSdUhfOHc?oc=5) | ifrs16-lease | 한국정경신문 |
| 🔵회계이슈 | IT | 무신사 | [무신사, 코스피 상장 예심 청구…글로벌 거래액 3조 목표 - FETV](https://news.google.com/rss/articles/CBMiaEFVX3lxTE1UVklJWVBfMlJMYjhCV2ZHLTgxeThycmVKdURrRndORzFoQmRGdGFCemFDRXdTZVB3VjRBd2NrUTFOX29hdnByQk1raXFpQ005YTkxWEw3SDFkSmdPbDhCQ2kzT3RrVHpZ?oc=5) | platform-cases | FETV |
| 🔵회계이슈 | IT | 컬리 | [컬리어스 '파인에비뉴 A동' 매각 자문 완료…누적 거래액 3.2조 돌파 - ](https://news.google.com/rss/articles/CBMickFVX3lxTE5IUlBuUW84Nm5KbnZhbFZBY2ZSMmlReENnR1JhUTZ6c3JIdUhYRVVFSlhWdk1VVVdTQTlPdWRZTVRDandOZnhnTnJGWXAwblBHaG5jUTltcW5aTVF3M3k5RG1UOFZZUUlNY2xvdE0xUVpwQQ?oc=5) | platform-cases | 마켓인 |
| 🔵회계이슈 | IT | 컬리 | [컬리, “김장 대신 완제품 구매”…포장김치 거래액 전년 比 35% 증가 - ](https://news.google.com/rss/articles/CBMiTkFVX3lxTE9yaWR3TnhwdTdDdFJvSjg0cDhCazMtOU5ibjlCeWtmd3pxU2VWOElYTDY5bHVtTlFUbjNaSktHNm1KYUdJV0MzelBJYlZCdw?oc=5) | platform-cases | 전자신문 |
| 🔵회계이슈 | IT | 컬리 | [컬리 포장김치 거래액 35%↑…소용량 수요 ‘쑥’ - 푸드투데이](https://news.google.com/rss/articles/CBMiZkFVX3lxTE1HTE9kWXlGLTVQZ0xNNnozVmpzamk0TVUyeGNKQlhXazlZVmR2c2xLTVhidEJHMm96Wm5MWV9mS1QySXpQbzY2WnRKd2Fvbm5yMGZ4TWpEVDI4cDdZVURES05fNmRzUQ?oc=5) | platform-cases | 푸드투데이 |
| 🔵회계이슈 | IT | 컬리 | [네이버와 장보기 ‘시너지’…컬리N마트 거래액, 1년 새 10배 성장 - 서울](https://news.google.com/rss/articles/CBMiUkFVX3lxTE9mdXJkQnNOZloydUFqMXVOSWluZXM4UVNDcUNiczJhNXc1bjRTclZObDZCYTdHdExfY2Jwc0FQUUNySFFlZnoyalNtLTdUd3lCV2fSAVNBVV95cUxOQmxjN0t1a1FkbFJWZHM0RXdCaGdZSGh0eEx2TXZQckRlZndibnlqXzZxSlUtZDdSNHFTNlpnWTM5NmlKaHM4QkhpM0VWanctdGJGUQ?oc=5) | platform-cases | 서울경제 |
| 🔵회계이슈 | IT | 컬리 | [김치도 ‘소용량’이 대세···컬리 포장김치 거래액 35%↑ - 스마트비즈](https://news.google.com/rss/articles/CBMibEFVX3lxTE83R2pRUmlsNlNHSU9GcWNSSHQxYlpEQU0zUV8yRlRiQjd3LUxTUDdvSGt0VURhampQMmZtcUktaVQwWHlxMEtnTi03R1lLZHhSWU9FZ3A4N1NkSmNGb3Y4ODNoOGhvMDRKZTVwTw?oc=5) | platform-cases | 스마트비즈 |
| 🔵회계이슈 | IT | 컬리 | ["김치도 필요한 만큼만" 컬리, 소용량 포장김치 거래액 39%↑ - 뉴시스](https://news.google.com/rss/articles/CBMiYEFVX3lxTE1RZTg0R1A5OVdQN2JBRWppVTIxeElPdm0zX2NPajNFVld4RGpkS1o1S3RlUW5JLTh3Qlo0YnNpbVQ0czFKS1d3YklfY3FpNUQ3dkE4czRzR2NTSXd4OWFhRtIBeEFVX3lxTE1JbDE5SWZxdzFaTzA4MTFvTjF3T2s1N0lBSXNKdmNwM0owSUhOSXhOU1dFOFZrMnlGLUlWX3R4S25teE0tRXRJZ0xBRTl2a09wMC1fRjhMREJvMnBTbmc1cGlwYzNyVnpPTHE3bmpfSWpsX3pTREtYNw?oc=5) | platform-cases | 뉴시스 |
| 🔵회계이슈 | IT | 컬리 | [김장 대신 사 먹는다…컬리 포장김치 거래액 35% 증가 - 뉴스저널리즘](https://news.google.com/rss/articles/CBMia0FVX3lxTE4wbkc4Z1dTS3pCQTJ2S3o2NVQ0REg4TWNfTmFicXdnSy1HMVBJa05ZMmlXUFJlWVFubkQ4N3pfX0hxbDZzdVRfaW9RcUFiSzNyOTlTb0w0WkREYm1LMFJzaVZDbnd4ZVhHLTFj?oc=5) | platform-cases | 뉴스저널리즘 |
| 🔵회계이슈 | IT | 컬리 | [컬리, 포장김치 거래액 35%↑···소용량 제품 증가폭 가장 커 - 뉴스프리](https://news.google.com/rss/articles/CBMic0FVX3lxTE1DdkZMbjhRYWE5V1hVQzh5NVQ0MlBIdkxsWF9fRzd4bUhrSllnS0J1R055TjFkcHlWWkFYeFJ3U2lOUXdqc1pBV3pmREo1cmFob0ZsZUluT3EyMFJONmEtZmNBLUozS0NybHhBeGt6N0tmT1XSAXdBVV95cUxNVkp2bk14RXg1MFltRm84ZjlPOVBrMEU2ZnF6Z3pjZlV6R3dCblJRZVZ1Y205WnBYSG94SUlLdkVreFNsa0s3T0FtbF9sS3pCNWJ5dHl3c2ZGUE1pd0dCSl9XeXZGNmVwQkpweHlHSUdCVmNnREctRQ?oc=5) | platform-cases | 뉴스프리존 |
| 일반 | 게임 | 넷마블 | [넷마블 '솔' 1200억 · 컴투스 '제우스' 한 달 470억 벌었다 - 디](https://news.google.com/rss/articles/CBMiZkFVX3lxTFBNblRuc1JUc0FqQjhBaVNiaGdqVTJzSGFXRHQxaGV3OG9YbFlsZzdjNklFTkx2cDJMaGxkUHplZm1WWHBzVm1PR29pZURETzdKa1lwQ29TVEhhS0xwd2J3eG82NEhaZw?oc=5) | - | 디일렉 |
| 일반 | 게임 | 넷마블 | [넷마블넥서스의 AI 코딩 도구 도입기 – 게임 개발팀의 Kiro 도입 및 활](https://news.google.com/rss/articles/CBMid0FVX3lxTE9KSVd3RHZXMTlSV3Z4Q1VDMi1iRVJyUWtxaWRmQ0J1WkdKVkdNaG5oTTZxQnpWcnc1ZkJUWnBhMl9yTGwxRkkxc0s5TlV0UDR0cHF4WUdYLVQ3ZjJVLVBJVDN6TnJhWUpWS000cXpHVFl2Q0Y1cVk4?oc=5) | - | Amazon Web Services (AWS) |
| 일반 | 게임 | 넷마블 | [넷마블, 구로구 '제1회 G밸리 퇴근길 락' 공식 후원 및 참여 - 지디넷코](https://news.google.com/rss/articles/CBMiVkFVX3lxTFBRUFFaTlcybzFDQ2Mwa2hvSjR3dWdOLUNqY3JGbTc1NmxrYUtrWjEtVDBuNW9PRFYyV09hS0I3TGNUX18zc3Fyck9SckQ3UnNYXzV0cUxR?oc=5) | - | 지디넷코리아 |
| 일반 | 게임 | 넷마블 | [[핀포인트] [넷마블] 6년 전 M&A 승부수…막대한 배당수익 거둬 - De](https://news.google.com/rss/articles/CBMiVkFVX3lxTE9jTWpPWGQ0OXd0TVZrQ1psOEtPRVBqNHFwUUxEMmRldkNRTmZYVUdTSVREMGJDcjFmay1oVl8xQkk1VU90WV9DLTVqeWdiZXVkWEw4ZUxn?oc=5) | - | DealSite경제TV |
| 일반 | 게임 | 넷마블 | [넷마블 '나 혼자만 레벨업:어라이즈' 글로벌 인기 입증···7000만 다운로](https://news.google.com/rss/articles/CBMiaEFVX3lxTE5peVhlLWJBbDlNTGVVQk9md1Q4NFJCZTB3WEJKNUctR2VXWW8wMWxfYm5oTmJDWUZvTm1pNXM4b3R0MXNyWXJsNWtqeUVISF9pOXRWMV92SEkxNzRZakVvV3hCLWhRUEZP?oc=5) | - | 한국NGO신문 |
| 일반 | 게임 | 엔씨소프트 | [NC, 아이온2 흥행 기대엔 못 미쳐…목표가↓-NH By 인포스탁데일리 - ](https://news.google.com/rss/articles/CBMicEFVX3lxTE1wRk9LQVlCcmt4alh0MlFfbEgyY2NiWktpQ25RM3pNd0FMM2ZkbVNlNFNvcXJteFlvaE1Uc2FIMVRIVGlObEJuSmVOTnZBUjZIdm9RUG1kVFVyUkVEcEtHMVMxZk9MTW9fVU81VEY5X2I?oc=5) | - | Investing.com 한국어 |
| 일반 | 게임 | 엔씨소프트 | [엔씨소프트, ‘아이온2 글로벌’ 초반 흥행…게임주 재평가 신호탄 되나 - 조](https://news.google.com/rss/articles/CBMiY0FVX3lxTE9lbUwxWUhsWkp3OHBpSHV1WFNrMThRaGpGS3lXcndEMUsxb2VtY2NqLS1TZ0NaS1I3Y0dLVnhRbzlzSFJlUHpfUklScFlEcXl4cVVHc2JnX21ubzcwR0VncE9HWQ?oc=5) | - | 조세금융신문 |
| 일반 | 게임 | 엔씨소프트 | [손익분기점에서 5000억원 이익으로…엔씨소프트 턴어라운드 기대 - 핀포인트뉴](https://news.google.com/rss/articles/CBMid0FVX3lxTE9uaXV3dDhrY09NUVR3cGJFX1drN2czcmZTTGFabFgzWGVFSWh5OUlTdHJIQWMwX2xtMExGQWJYOTBkYllvYW1UVE8yX0FRT05TOExNc3ZONFRGb2FEMWtfNEJpVFdUbVFtdzNwd2Z2bUdxVm1KWnNN0gF3QVVfeXFMT25pdXd0OGtjT01RVHdwYkVfV2s3ZzNyZlNMYVpsWDNYZUVJaHk5SVN0ckhBYzBfbG0wTEZBYlg5MGRiWW9hbVRUTzJfQVFPTlM4TE1zdk40VEZvYUQxa180QmlUV1RtUW13M3B3ZnZtR3FWbUpac00?oc=5) | - | 핀포인트뉴스 |
| 일반 | 게임 | 엔씨소프트 | [지스타 인디 106곳 참가…넥슨 넷마블 엔씨 불참 - 자본시장뉴스](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1UaE9UcFNrczN5OGxCWS15UnpxaHNHTkZEblVTb1ZWU3VmeHJuZ0laeVhlMUtlcDZiTDlwdVphZXdDSTNlQXdYaWNtX2dmWmhXQWpfM0o0cTlKR0NHVlFMT2NUejdQWlU?oc=5) | - | 자본시장뉴스 |
| 일반 | 게임 | 엔씨소프트 | [7만명 몰린 ‘아이온2’…엔씨표 MMORPG 해외서 또 먹힐까? - 디일렉](https://news.google.com/rss/articles/CBMiZkFVX3lxTFBMX28ybHVhRVJKTVhVNDVackhMVmtucW8tanZRUklJSFNRS21BWDk0NHdUaXY3VUhCOEtGRDBrdkwzeHd4WmxfSFE0dk1mdy1qYzUwWUxHNldDclF3M1RkZkRfSjFOUQ?oc=5) | - | 디일렉 |
| 일반 | 게임 | 크래프톤 | [PUBG 과의존한 크래프톤…잇단 악재에 주가도 ‘뚝’ [재계톡톡] - 매일경](https://news.google.com/rss/articles/CBMiVkFVX3lxTE5Ba2FEWGQteDFNQTZXMVlEdDNyazdoNEMyS2NPaTF1alNEOG1vamZCVlZ1OUVNSVllNHFuWU9VVzQxT2lQT1RZd1d1Mi1XdEFjeGpCaVJn?oc=5) | - | 매일경제 |
| 일반 | 게임 | 크래프톤 | [게임업계에 부는 개발 조직 ‘슬림화’ 바람 - 조선비즈 - Chosunbiz](https://news.google.com/rss/articles/CBMiggFBVV95cUxNdFh3LU1pdkplMFdrLWNQeGxGcnBrTUVnS3Q1VmlXMVBDeW11Z0tNTzNRazNNRkEtOGNyZVBmVHlqc3Z4WkEweXF6OXFpcjRQTGtmNl9GRXlGM1dYbFh3b2NOeGFNcWIzZVdvbGdBdm9GUjBuM3BGcVk4dXg3bnF1S25n0gGWAUFVX3lxTFBnazduODRPek1Cb1VmQnNFczVRakVPdGlaaG5qNldUSk9Qc0FicC1QSlhkaGI5UF8yN3hPMFBldHNOZVJDT19kZWVOSllNQm5fVTlQb001djJGajYwRkRiMUl6cDJqU0pkaVI5bmZFN19KSmhYV3lOR3F5WUI5WVJIdU5MSm5tU09oOXNkUXRTTi1qN2RoZw?oc=5) | - | Chosunbiz |
| 일반 | 게임 | 크래프톤 | [크래프톤 'PGS 10' 파이널서 한국 3개 팀 출전, 첫 매치부터 고전 -](https://news.google.com/rss/articles/CBMiakFVX3lxTE1SWEV6Q19EZEtGbTIzQ0xMSlNIRHJzSGNGekhoamFIbWdLb09vTVJma3dHU1dwQmg3TmFpOVZHN1FUUE5qWnJvcjQyZFV5X3dUSzRyRld4SWppY24wN2h5dW1VVVNYNlNrMGc?oc=5) | - | 게임뷰 |
| 일반 | 게임 | 크래프톤 | [역대 최대 규모 ‘AI Native’ 신입채용 실시 | KRAFTON - 크](https://news.google.com/rss/articles/CBMioAJBVV95cUxNNWp4LV9PeUtIa1M0MVRxWDNPVkJHelF1OWtMYjdqZmJMSDdGSW1OTDJEOWZOMlJWSDFncU5fUnFjV0JDU0hCR2VCMHdCcjJLdHI4TWhnWEU4Vl9KNGZwZGM4LVBuektMc0lzcUlYYmtkYnprTjJlREh5N0tFS3M3ZWV1bkZ1VzRHV2VkaDZhZWcwUmZYXzBoSERUNDZpQVl1bWNNNi1wcmhzZ3NuUmlBNkJnXzhtTDJtSnJPNjA5RlNHLW1fbkhPczVHMVktY3VoSWdKSWg1U2o5aGR3UjFVOVhJS0RPa0VNVWdSTTktOGJNTU8wMUJYOUxmdXNmNFp2TU5yZ2g0Z1pxUHJNdWZLNXdyZFNqaXUyT3pWODVUeEY?oc=5) | - | 크래프톤 |
| 일반 | 게임 | 크래프톤 | [크래프톤, 자체개발 LLM '라온-1 미니' 프리뷰 공개 - 연합뉴스](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBFaGxkejRCRWtLaldlQ0E0WmJlVERVa01wZFFxdXhTZDlvU2FEYk14cWdWbVhyV0dyajdCcU1rc0V5NWQtbnBpeFZid0VidDlSemQwamhpbUczdEXSAWBBVV95cUxNVmU4S3E1eFBmQjYxZG10VnN1dEVWbE56dnRpTVk4alNkZ0FmVXQxTy1ZSFRZSDFIMG91clB6elFiY294b0RERWdkNTBRX3ZVVmJsaVloMXh1VHBSZlBQczI?oc=5) | - | 연합뉴스 |
| 일반 | 게임 | 펄어비스 | ['붉은사막' 흥행에도···펄어비스, 내년엔 66% 역성장 전망 왜? - 뉴스](https://news.google.com/rss/articles/CBMiakFVX3lxTFBlUFQtMm1Nc1picHIzdERxbXRYWFFzekU4ZmludWRZT2xRSUlRZGtQV005X0FwR2ZhUVp2QTVod2VkOEcxbDNNMUxQOWdUYnZlUUJ6c2U3RWxsd0tka293NlM3dEpYUGtSRXc?oc=5) | - | 뉴스웨이 |
| 일반 | 게임 | 펄어비스 | [[Oh!쎈 초점] '붉은사막' 4000억 원 흥행… 펄어비스, 과천 지정타 ](https://news.google.com/rss/articles/CBMiVEFVX3lxTFBpd2lscTl1ZnFlWU9iV3dxVUxXSXh2eHJLcmFMOER5ZEY3ZldSYnJaaHp6d2VNV2RGUjBoUDg0NHg4RGJCMWR4N1QwMmd2LWpjOUdBSQ?oc=5) | - | OSEN |
| 일반 | 게임 | 펄어비스 | [펄어비스, 차기작까지 2년 공백…검·붉은사막이 채운다 - 대한경제](https://news.google.com/rss/articles/CBMic0FVX3lxTE9WRmE4VzR4VnpUQnVwdXB5U2RHU1NJSExVMWotZHlJaGp6YTdLNXdsS3hBUHNsSHZpNzVKTnBHbFUtcndTYVU0T0dPYnNSRl8yaWVSeWdRa0U2TmhlMGd0WGlWR0VDRnY5SjFacjhKWUN2NFE?oc=5) | - | 대한경제 |
| 일반 | 게임 | 펄어비스 | [펄어비스 '붉은사막' DLC, 출시일 10월 30일로 조정 - 연합뉴스](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1qMFhqVV9KTXVVTFBkSGlZU3FOdW5QdEhfZDJienRrams1dG9sQjFPazlpSDAzQWJSam5Demo3QnlOdF85MXFTdENXTEdKWnVvcWJQeHVRQU1xX3fSAWBBVV95cUxPREdFbFY2dEROT1pYd0Z2YzFMNG4xUERya1hkX3RXSlU4UTk2WjRUTlFvem5nSGtsU1pXNGJxaEtXRkc5TFVpdjFSTVBpSTBmUDNCbmJWVVZscE81b2ZIeko?oc=5) | - | 연합뉴스 |
| 일반 | 게임 | 펄어비스 | [펄어비스 붉은사막, 글로벌 누적 판매량 600만 장 달성 - 펄어비스 공식 ](https://news.google.com/rss/articles/CBMia0FVX3lxTE5XZmJDZy0yQ01STmh2OS1USzgyRXlJU3dIeWdSMDN6cU9zTU1EUUFNTmpuZmZmYmViVkd0M2lYa19ndUdDdEJfTUFNNnNDV0prVm9PLUd0eEZRMWpLUEpFWHl1QTlLUEltbWl3?oc=5) | - | 펄어비스 공식 홈페이지 |

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
