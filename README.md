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
_최종 갱신: 2026-11-16 11:44 KST_

**수집 현황** — DART 공시 128 · 뉴스 337 · 회계법인 리포트 2

### 📄 DART 공시 (회계 이슈 필터)
_종류별: 실적 72 · 📘정기 25 · 🔴정정 15 · 🟡주요사항 16_

| 종류 | 업종 | 기업 | 일자 | 공시 |
|---|---|---|---|---|
| 🔴정정 | 게임 | 엔씨소프트 | 20261111 | [[기재정정]연결재무제표기준영업실적등에대한전망(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261111800327) |
| 🔴정정 | IT | 카카오 | 20261105 | [[기재정정]주요사항보고서(회사분할결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261105000098) |
| 🔴정정 | IT | 카카오 | 20261105 | [[기재정정]주요사항보고서(회사합병결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261105000084) |
| 🔴정정 | 미디어 | 엘지헬로비전 | 20261104 | [[첨부정정]연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261104800154) |
| 🔴정정 | IT | 네이버 | 20261103 | [[기재정정]주요사항보고서(유상증자결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261103000311) |
| 🔴정정 | 엔터 | 큐브엔터 | 20261030 | [[기재정정]주요사항보고서(유상증자결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261030000611) |
| 🔴정정 | IT | 네이버 | 20261030 | [[기재정정]주요사항보고서(유상증자결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261030000001) |
| 🔴정정 | IT | 비바리퍼블리카 | 20261030 | [[기재정정]유상증자결정](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261030000628) |
| 🔴정정 | IT | 비바리퍼블리카 | 20261028 | [[기재정정]주요사항보고서(회사합병결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261028000358) |
| 🔴정정 | 미디어 | 에스비에스 | 20261026 | [[기재정정]타법인주식및출자증권취득결정](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261026800689) |
| 📘정기 | 게임 | 펄어비스 | 20261113 | [분기보고서 (2026.09)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261113001084) |
| 📘정기 | 게임 | 카카오게임즈 | 20261113 | [분기보고서 (2026.09)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261113001280) |
| 📘정기 | 게임 | 웹젠 | 20261113 | [분기보고서 (2026.09)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261113001229) |
| 📘정기 | 게임 | 넵튠 | 20261113 | [분기보고서 (2026.09)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261113000977) |
| 📘정기 | 게임 | 위메이드 | 20261113 | [분기보고서 (2026.09)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261113001326) |
| 📘정기 | 게임 | 네오위즈 | 20261113 | [분기보고서 (2026.09)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261113001163) |
| 📘정기 | 게임 | 시프트업 | 20261113 | [분기보고서 (2026.09)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261113001557) |
| 📘정기 | 엔터 | 에스엠엔터테인먼트 | 20261113 | [분기보고서 (2026.09)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261113001370) |
| 📘정기 | 엔터 | 제이와이피엔터테인먼트 | 20261113 | [분기보고서 (2026.09)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261113001566) |
| 📘정기 | 엔터 | 드림어스컴퍼니 | 20261113 | [분기보고서 (2026.09)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261113000220) |
| 🟡주요사항 | 게임 | 더블유게임즈 | 20261110 | [주요사항보고서(타법인주식및출자증권양수결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261110000002) |
| 🟡주요사항 | IT | 카페24 | 20261110 | [주요사항보고서(자기주식취득신탁계약해지결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261110000296) |
| 🟡주요사항 | IT | 카카오 | 20261105 | [주요사항보고서(자기주식취득결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261105000008) |
| 🟡주요사항 | 게임 | 크래프톤 | 20261103 | [주요사항보고서(자기주식취득결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261103000268) |
| 🟡주요사항 | 게임 | 네오위즈 | 20261020 | [주요사항보고서(자기주식처분결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261020000323) |
| 🟡주요사항 | 엔터 | 제이와이피엔터테인먼트 | 20261008 | [주요사항보고서(유형자산양수결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261008000381) |
| 🟡주요사항 | IT | 컬리 | 20261002 | [주요사항보고서(주식교환ㆍ이전결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261002000047) |
| 🟡주요사항 | 미디어 | 제일기획 | 20260930 | [주요사항보고서(자기주식취득결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260930000006) |
| 🟡주요사항 | 엔터 | 디어유 | 20260929 | [주요사항보고서(자기주식취득신탁계약체결결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260929000178) |
| 🟡주요사항 | 게임 | 시프트업 | 20260910 | [주요사항보고서(자기주식취득신탁계약해지결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260910000386) |
| 실적 | 게임 | 펄어비스 | 20261112 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261112900686) |
| 실적 | 게임 | 컴투스 | 20261112 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261112900678) |
| 실적 | 게임 | 더블유게임즈 | 20261112 | [영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261112800030) |
| 실적 | 게임 | 더블유게임즈 | 20261112 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261112800026) |
| 실적 | IT | 네이버 | 20261112 | [영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261112800028) |
| 실적 | IT | 네이버 | 20261112 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261112800027) |
| 실적 | 게임 | 엔씨소프트 | 20261111 | [연결재무제표기준영업실적등에대한전망(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261111800334) |
| 실적 | 게임 | 엔씨소프트 | 20261111 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261111800311) |
| 실적 | 게임 | 위메이드플레이 | 20261111 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261111900470) |
| 실적 | 게임 | 위메이드 | 20261111 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261111900537) |

### 📰 뉴스 모니터링 (🔴 = 감사·재무제표 신호)
_구분: 🔴회계신호 17 · 🔵회계이슈 14 · 일반 306_

| 구분 | 업종 | 기업 | 기사 | 회계토픽 | 출처 |
|---|---|---|---|---|---|
| 🔴회계신호 | 게임 | 넷마블 | [[재무제표 이야기] '정수기 게임' 우려 딛고 넷마블의 ‘황금알’ 된 코웨이](https://news.google.com/rss/articles/CBMibEFVX3lxTE56UWVmcFpXTmhHZm1hanhhWFFjNUljbWpuZndaYUdQckRQTmUzTEtJb3hkU0p2b21jZ1RjSXZhZ0dQc19BRlhkTzFJTlVTM1NtbDB5emxnb1k0MDFQd1JkY3owVVItN3dkZjYzdA?oc=5) | - | 생생비즈플러스 |
| 🔴회계신호 | 엔터 | 하이브 | [의견거절·재무제표 재작성…'암살자(들)' 제작사 하이브미디어코프 회계관리 도](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1Tc1FHRU5CMFp6LUlBcUJkd0FtU195bV9fRGQ2R0NDMjMxWDJ4UW9OTXVRcFRHMzdhSWdiaEVIRkl5WmY5czB3RkJpb0tFdkJHUm5FekFsMzVUdw?oc=5) | - | 블로그 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [유동부채 1.4조 늪…’적정’ 받던 콘텐트리중앙, 5개월 만에 ‘의견거절’ ](https://news.google.com/rss/articles/CBMirAJBVV95cUxNVUpYMW9JNnd4Y0pRNVNyVkttRXZtOERwekxJX2JraWZrdlpIQkRVSU4taktUNHRCOVVvd21GcVAwd0NlVmJEYVN4WnVsOU5GenZnTlhBQVFpZnRqSVR4bUp4dEJyN081UDFzR2Izb1E4aWhqTFhSLUxyT09QUm1fN3pNbkxXa0xHdURhSGdQYkcwUUp5ODBOeEFwQUYtZG5QOGwxUmR0SVZuclNpRkFuQTB0SHY0QmhWaVVyX3BqaFg1OWVyZmsxWU9ybnp3WVM0eTBGRzJrQWpuRWZoUzVqbGV0QnZHOGhrRTZtUlJxeTRhTnpnUjVKeUZKYWdYd1RiVlRMRy1OSFVRdVdBUHhHSGRtQ0JGWVdOMDc0WWVleUh6WHlUX0VCRVQtdTc?oc=5) | - | 뉴스필드 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | ["계열사 전반 재무제표 왜곡 의심"… 중앙그룹 피해자들 검사 확대 요구 - ](https://news.google.com/rss/articles/CBMibkFVX3lxTFAyVVZEV2FCZDdpMW12YURXNWIxVGNIdzE0MWoweUFPYUhlbEFHWVFGV2V4WV9uM2U2WDJ1Ri0xb3U0QTlrTVhIaWo3UWRFMTVJSHNvSzlyUjlPV3d1WWNOODg0NFpZSllKOElOekxB0gFzQVVfeXFMTnMzNmJkaFo0LU15RVNMemVtVUpRSVNlblhEV0w3R3BwWXpZNlNrTDM3Q2twSldRYmZ2RHpiWGlpZnppdzRmdThDVzZyaklMcXBiLUx4MDdzSkE5RERob3M3TzBBUnkwUURIU2hMUVR2V0dZUQ?oc=5) | - | 한국일보 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [반기보고서 무더기 '의견거절'…투자 유의해야 - 아시아경제](https://news.google.com/rss/articles/CBMiYEFVX3lxTE5SaHA3WS14YmJCdkw4blJCSWhaN0tHUXp1OVA4bWREd21McnRkZXFTR05yTEF0VkpSVk5nbXJWN2NKY3FyUnNzUTMzdEhBSVlsVnN1YllUMnFHNGVCZVVVdw?oc=5) | - | 아시아경제 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [[단독] JTBC 등 5곳 회계감리 착수…금감원 칼댄다 - SBS Biz](https://news.google.com/rss/articles/CBMiU0FVX3lxTE5BcmF4YUtlQkF5MlZKVTl3clRKN3ZmaWdjbHVmZm11dmVhdko0dDFycE1EdjJhSmJ1WFJmVWJsa2NQdURBV0JtV0I5OTJmQjVEWXc40gFYQVVfeXFMUGJKUnFuN0FlX2J0UHFiYjU0amtueG80c0w3dHVtRlNaS1FabVFOX2hUSFk3Zk93U216cUkzRTY1bE5SbTBHYlFFR2RCVVhXcFptX29hakgwcA?oc=5) | - | SBS Biz |
| 🔴회계신호 | IT | 네이버 | [제일엠앤에스, 2024년 감사의견 '적정' 정정…상폐 변수 완화 : 네이버 ](https://news.google.com/rss/articles/CBMijwFBVV95cUxNLUpCSXRCd2IzQnpYWVBzWTZPaXdIMTJ4am8yQURBMlZTem44NUh4emZ3cERrMDEzN3N1VkZYbVF1VDZ1eEk3YnIwbjhJTjlJS18xbjBDUjJ5OVdxdW0zcW1ZOXBVWllKR21Ha1FwWVhJaE5HZDBMOWNJbmxEaC16WFBuQ2NZQ20waFp5ekVPYw?oc=5) | - | Naver Blog |
| 🔴회계신호 | IT | 두나무 | [[단독] 두나무, 美 SEC 위원장 면담, 회계기준 전환 완료...나스닥행 ](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPTE5PSW1ya182NWtnSDlMTmFrSkhvVC1xUmhPNG9zb3ZDZWd2RVVGalBvSFdmT0xMYUd3bWIxbkE1TkF3YVpPTWtxdlVZTUszdGExSTBNMFhBdkZaMkV3V2JpT196UXV0aDVFMmczaWpYbU5YVXpWbDd1Q1cxVmtEMWtfdzZ5WHZydGhB?oc=5) | - | 조선일보 |
| 🔴회계신호 | IT | 두나무 | [두나무, 美 회계기준 검토 …“아직 결정된 바 없어” - 전자신문](https://news.google.com/rss/articles/CBMiTkFVX3lxTE5HZTFwRHZlQ19keGRBM3pQYkk2THNlZjNKRzFmRjNnMV83OFRyLUQ4elVxV2M4ZUV5eTJTSFdleEZtZUNORTVpc1NNTU1iZw?oc=5) | - | 전자신문 |
| 🔴회계신호 | IT | 두나무 | [두나무 "美 회계기준 검토…주식교환 마치면 IPO" - 비즈워치](https://news.google.com/rss/articles/CBMiakFVX3lxTE5XdU00TXFrTEJLcHI4RFFYcjVUMlIzV1VuVUVrSzFIcGwtdGVvc2pkQzJDOFgtTzlDZnVLNUxFM01ZNUNZVlNUUWNZV3cyTnYtZ3VqMkFyVEdTaGV4dUZoOGpMNndodC1Zd3c?oc=5) | - | 비즈워치 |
| 🔴회계신호 | IT | 두나무 | [‘美 회계기준 전환’ 나스닥 상장설 솔솔…두나무 “사실 아냐, 상장국가 미정](https://news.google.com/rss/articles/CBMiYkFVX3lxTE1UdlAwTl9kVEhJTm1fdl9QVU5NbjdUVm5VYWVJbnhOQlNBbUM4bk94THdKNmJaa1BDeEtFNDY4UVVEeGZ3YjdaeFdUZTRvOG04dU1aMnl6SWlKLXpMbk5Xc1N3?oc=5) | - | 디지털데일리 |
| 🔴회계신호 | IT | 두나무 | [두나무 "美 회계기준 전환 사실 아냐"…나스닥행도 '미정' - www.ebn](https://news.google.com/rss/articles/CBMiaEFVX3lxTFBJblR6OS1vc3JSNDhlYUctWUE5TVRPQ29uclIwNG04SGpKQTE0Q0pzYWlIWjVsTERpSHlBemR5OXd3RUhya2liQlRRZ1NtWFpnM3BBMUotdXNiS2NHTmhkb1RscnpjYTJO?oc=5) | - | www.ebn.co.kr |
| 🔴회계신호 | IT | 두나무 | [두나무 “美 상장 확정 아냐…회계기준 전환도 사실무근” - 뉴스투데이](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1PZzA0UVNnSERESm1NWDJmMVdLX25MWmFxSkdwZDcxRVZRRlZVM2ZScXhqbHlTM19rQ0x4VFUtUml0SDJDTEhYbmxRSDhqV0NtaENEYVpoYWtxTjg?oc=5) | - | 뉴스투데이 |
| 🔴회계신호 | IT | 두나무 | [두나무, 美 회계기준 검토…주식교환 마치고 IPO 추진 - 데일리안](https://news.google.com/rss/articles/CBMiowJBVV95cUxORkhSRHFOcm5yVWpQS2ZtdDZVeU1nX2VLMmhIVDVDb1B6aHF2YW92a1g2cFNzeVF5OF9tYjdCWHBRandoVlZmd0d1UlpSRUpRTllfWENQcExENE1Ga2hsVVNEb09JUkc5SER0NXUyTTJMYWdIdHFVai1lVmZRemk4RG5zV2Q2aTBzdVpRZTFUbm9TbWxvTy16YVN1eVY3TkpOWk5CNF8tUkZZQkF3WkMxeUVwVjlTWExrSXVVWm9GRWdRNi1rT0x2UTlYN2s2RkFnb2w4N0J0eGtOQ2EzSjVWVVpnVnZvRzV5TG9LWW9neGlDUGZHSXdIb0FNOGtpaUhYUmRpcEduZDZUcG9sVFloQi1Tbm9KN2pWQWxYbHYtRk1Pa3c?oc=5) | - | 데일리안 |
| 🔴회계신호 | IT | 무신사 | [[재무제표 이야기] 무신사, 재무제표는 더없이 훌륭한데...문제는 오너리스크](https://news.google.com/rss/articles/CBMibEFVX3lxTE1jV2NfN21Kc29OVUJ6bk92V01SLS1HaDV1SlFkeUlfOFpqMU8taHFXQUJVT1JYNjBkWVpRenpqMzZwUnZ2OExBbTdaTVRrNm5ZWHhwa2pHZTBwM0xnNnc1c2paZTJjY29XdWR1UA?oc=5) | - | 생생비즈플러스 |
| 🔴회계신호 | IT | 컬리 | [컬리·풀무원 재무제표…좋은 숫자만 믿으면 생기는 일 - 자본시장뉴스](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE96S0pOeklqUjhkWngyNlYtaHJzN1VTREtXcXpzN0JjSTRVTWU2NEFHeEpsUEFwYU16SVA5TXpxM1gycDN6T3o5eE01Q1ozVzl2ekVWbm01Q0o5c0o4bG5pTDdPUlpKVjg?oc=5) | - | 자본시장뉴스 |
| 🔴회계신호 | IT | 컬리 | [[재무제표 이야기] 흑자 전환 컬리...그래도 여전히 '미생(未生)' - 생](https://news.google.com/rss/articles/CBMibEFVX3lxTE1CZHpNRmxVcHB3N3hSazFQYkNJelpma2U0UzVNSjBkcThaNmUxcWlfZGVRWS1STGZzcF9vVVZRb1hfdWdhMEJWRWw4M1RwWjdQM1FGa2tEOXhZdDlaMnZCU0hrV3M0LWd0a0xNcw?oc=5) | - | 생생비즈플러스 |
| 🔵회계이슈 | 게임 | 넷마블 | [[국정감사] "게임판 음원 사재기" 논란에도 정부 조사 없어…김재원, 순위조](https://news.google.com/rss/articles/CBMibkFVX3lxTE1hS2V5dnlPSWVXZkZfOHVGcGxmOWtYNVJQUXR4c3RFdDEzOENvOWZ1dkpqLUJCeUctVUZDSTFUMUhPR2ZPMUQtUVdFOV90bEozUzZnaUhhWjdlcTdSQVUzMFpPR0tGZmxpZnAtVExR?oc=5) | intangible-assets | 에브리뉴스 EveryNews |
| 🔵회계이슈 | 게임 | 펄어비스 | [펄어비스 3분기 영업익 9% 감소…개발비 증가 - SBS Biz](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1QRlZrc2N2U3ItZWxzcmY1Wk5KOXd6b1pKRWY4cm5zVTFJaG9SZ1pFeEk5Q29XRWlJTzBLNU83WFFzZnhWT29jZjAxeWdGRFNCb05F0gFYQVVfeXFMTUpONXQ0TldiOVB0N0IxcDlwYlI5Z2h3X0I2T1hQbDQyQ2lGZ2xUc0RIakxNWXBldFdFd0JfLTFSdXRtR3Y1MWlSdUxIX3ZzQ1JOSFBfelJhbQ?oc=5) | intangible-assets | SBS Biz |
| 🔵회계이슈 | 게임 | 카카오게임즈 | [“영업손실 263억 카카오게임즈, 라이온하트 1.1조 영업권 손상차손 ‘시한](https://news.google.com/rss/articles/CBMib0FVX3lxTFBDeGEzSXN0UXlWUzgtdGVYYUVidm9wa3BScl9UeHo3Nk1OZHVVRVVFak5sb2hGRU9LNnhyZXZaMWlYZGZVZTA4ak5zd0ZYOE1XdmFZcXAzRVN4Ym5mTkVQN1dyRmN2M1hESUNJZFVCWQ?oc=5) | intangible-assets | 뉴스퀘스트 |
| 🔵회계이슈 | 게임 | 위메이드 | [위메이드 3분기 영업이익 264억 원, 흑자 전환 이끈 미르 IP 중국 라이](https://news.google.com/rss/articles/CBMiaEFVX3lxTE1WRk1UU0V1VnN5VHpjUWpOQUg4SW0tVDlCdU1rQUx4UGpIaG1nOUZ5MnBsSDhjTUNhUVptLXREaGhmcjhNV1JTQ0Y3V0E0RzJDa1hKeHlVUjJaenpqQW5zNTBuRlhWRHE3?oc=5) | intangible-assets | 창업일보 |
| 🔵회계이슈 | 게임 | 위메이드 | [위메이드, 미르 中 라이선스 효과 3Q 흑자전환…영업익 264억 - 메가경제](https://news.google.com/rss/articles/CBMickFVX3lxTE0yM3p4UW42RzF3U0JXTjNXWXdOdjdacnVGMWhibE10cXQ5OUFRWmJiYURrcklHWmdxeDVDTzdkSFlDcS1Lb2RWakExdExlNWZrNnBydlRhWU55a1JTbEtnUDJWZ28tUWx5cUxUYjhTVmtLQdIBckFVX3lxTE0yM3p4UW42RzF3U0JXTjNXWXdOdjdacnVGMWhibE10cXQ5OUFRWmJiYURrcklHWmdxeDVDTzdkSFlDcS1Lb2RWakExdExlNWZrNnBydlRhWU55a1JTbEtnUDJWZ28tUWx5cUxUYjhTVmtLQQ?oc=5) | intangible-assets | 메가경제 |
| 🔵회계이슈 | 엔터 | 에스엠엔터테인먼트 | [SM 3분기 연결 영업이익 355억원으로 26.4% 감소, 본사 음반·음원 ](https://news.google.com/rss/articles/CBMicEFVX3lxTE9jS094aFd5XzJERkZpSVlrYWhEWUV4RWM4Rkg2NTdldFFBVWdxWkt5Tmc3ZjY0LVJPWmJrckZmQjBmdTROTURxNlk5aFhkcFViUnNZWC1VNlJsd3pURm9UYWdlMmJXZHN6MFE2b0otVDU?oc=5) | intangible-assets | 이슈인사이트 |
| 🔵회계이슈 | 엔터 | 하이브 | [하이브 디지털, 회계 2분기 순손실 7870만 달러로 확대…채굴 장비 손상차](https://news.google.com/rss/articles/CBMic0FVX3lxTFBtX3hUU1BtYmk4X3liUTFlMUhfQUxGU1NJY25XU0ZhME5ubTVPaWpqT3FVZFRURHlWOTB3Tjdrc1k2SVVzc1pieEZhVE05YUtqQUtZd1RrWUt6a212eDg4M0tua01QQzlZRjduY1hnbnNrRmM?oc=5) | intangible-assets | 데이터투자 |
| 🔵회계이슈 | 엔터 | 와이지엔터테인먼트 | [특징주, 와이지엔터테인먼트-음원/음반 테마 상승세에 6.45% ↑ - 매일경](https://news.google.com/rss/articles/CBMiUkFVX3lxTE5BN3haM0o3WFEzejFQemJTN2c2d08yTExhZkdHaW5tcmlOdlVMc0pHS0JYSllEWXZuVW9rZTNkOWVmSHAxeVlxZFpmZ0NUSy1iMWc?oc=5) | intangible-assets | 매일경제 마켓 |
| 🔵회계이슈 | 엔터 | 큐브엔터 | [[더벨]큐브엔터 소연, 신곡 '퇴사할게여' 주요 음원차트 1위 - 머니투데이](https://news.google.com/rss/articles/CBMiaEFVX3lxTE5vMURKb1JiaGlzRTNyQXpycVZiMjVUTVFxbEM1WFAzVEdfZGtLRGZyTlFSUDZxdkpDZWZ1NklqNnZVVm1qQ3lVNVV3X2NtRDBPbmZZQ2xDbmY1T1ZWLS1sc0Y1SDF1ZjJK0gFuQVVfeXFMTWR5SUNMblBlb0dSUjRfMU1IbWc5OTNxUG1NaHhMTVVVd3dOZ3RxV0JNQUNOREVqLXMzRzV2Y09wNkV3cVI4QWZkSm82TjhqSWtGZk96Z3B6enFERnUxa01IaUFFdzg1UzNLZHR3UVE?oc=5) | intangible-assets | 머니투데이 |
| 🔵회계이슈 | 엔터 | 큐브엔터 | [[더벨]큐브엔터 소연, 국내 주요 음원차트 동시 1위 - 머니투데이 - 머니](https://news.google.com/rss/articles/CBMiaEFVX3lxTE1YUkozVWZZTTZIV3FhZ3N2WG51cTVKeEh3QUZETkpwZDkxTmlzRkZmUW55MjlpQlZRZDA0TElNcS1lN0VKdDFjNllqblUtc1hrcElwMWtRMGxoYWZTTHE2T1lXTUE0LUVy0gFuQVVfeXFMTm85WXQ0VG9sYzZINUt2SUFDMkxPSlFNQWltRzZmZmRzdkRFamtSMHA3WkE4WkJYZ2JNVThsRlFQaVdkcGVtYXFFeV9LVHpEQm9OdlZFVnBsY0c4U0xjN3JCMlBwNDVseDhRT3F5WXc?oc=5) | intangible-assets | 머니투데이 |
| 🔵회계이슈 | 미디어 | 스튜디오드래곤 | [[스튜디오드래곤 톺아보기] 판권 상각기준 전격 변경…'수익·비용 매치' 변동](https://news.google.com/rss/articles/CBMiT0FVX3lxTE9QU0VkMFAzbnhsQnl6amZPVTZYbUtabUVibF9FbmFlNXpLWnRJa0RneFJSNmE5T08xSGtOVFRGS1lpYzRweHdYSGdrUkhYWms?oc=5) | intangible-assets | 딜사이트 |
| 🔵회계이슈 | 미디어 | 스튜디오드래곤 | [[스튜디오드래곤 톺아보기] 판권 상각기준 전격 변경…'수익·비용 매치' 변동](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1ZQ2ZTVFJ3eTNZZ1c0T1AwUjQwNGFULURvV0RIZlpabEhHcnYxYjdkYTZHZTFka2thYy1XRjdKT1MxUUZNR2R1eVB3bUNYU1h4TVlyR0RwMmpGZw?oc=5) | intangible-assets | 블로그 |
| 🔵회계이슈 | IT | 야놀자 | [야놀자, 통합거래액 39조2000억…글로벌 확장 속 수익성 회복 과제 - 한](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBGUjAxQjh5ZDVuNVBhYWFGVm1DcGZIN0dzdk51SEdGVzhjSmpKVEpLRXZoTnl4UFVETnJLRGpwcENlQkhqQXFrUml6QWpSV1JRR0hsVmlmdE0wdw?oc=5) | platform-cases | 한국경제 |
| 🔵회계이슈 | IT | 컬리 | [컬리어스 '파인에비뉴 A동' 매각 자문 완료…누적 거래액 3.2조 돌파 - ](https://news.google.com/rss/articles/CBMickFVX3lxTE5IUlBuUW84Nm5KbnZhbFZBY2ZSMmlReENnR1JhUTZ6c3JIdUhYRVVFSlhWdk1VVVdTQTlPdWRZTVRDandOZnhnTnJGWXAwblBHaG5jUTltcW5aTVF3M3k5RG1UOFZZUUlNY2xvdE0xUVpwQQ?oc=5) | platform-cases | 마켓인 |
| 일반 | 게임 | 넷마블 | [넷마블, 신작 공백에 아쉬운 실적…"내년 13종 이상 출시" - 한국경제](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5uUnpqM3MxdTM2RmtOX2VrcENTUEVQbDNqeFBXWHNNMV9tRjlqOEplRnRjb2xnY25CTE9SMVRVT0MtTzBCY3FaQ1A5cWs3QTNRWjhMTmhSS1hNUQ?oc=5) | - | 한국경제 |
| 일반 | 게임 | 넷마블 | [넷마블, '신의탑: 새로운 세계' 신규 동료 업데이트 - 전기신문](https://news.google.com/rss/articles/CBMicEFVX3lxTE9rb3VXMXFnbUQwSXJTY1N5V0ZLVlJRR012ZndwZGxyM1BOd2o0azVVQmtqMmRMeS16MWM1eW9hbmdnRnNzUWIzT01EZzh6Y3JWSHZxWlNLX3A3bU00alpXRk4wbFMtSjY0YjM3Q1Q2X2fSAXBBVV95cUxPa291VzFxZ21EMElyU2NTeVdGS1ZSUUdNdmZ3cGRscjNQTndqNGs1VUJrajJkTHktejFjNXlvYW5nZ0Zzc1FiM09NRGc4emNyVkh2cVpTS19wN21NNGpaV0ZOMGxTLUo2NGIzN0NUNl9n?oc=5) | - | 전기신문 |
| 일반 | 게임 | 넷마블 | [교보증권, 넷마블 목표주가 16%↓…"신작 성과 확인 필요" - 연합뉴스](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1VVklCVHBIZ3U0V3B6aHVWbW04OUVQSFdWQVFrSnBNRTZZVFZSczVlS3VNLUZpZllRM21ObnU2TnhTUmxqNURrT1d4cnQ0T0k3UmVxYlNweWdIQkHSAWBBVV95cUxOQ1dibkhpMU1qbmhVazItU1VmVGlrWXRGVG5kd3pzMlA1ZVVUXzJCNTkwNXJkMkxrVVFfZWo4ZW9JaUVDdERRby01QmlrNjEtcWZaOHRlMkYxWFpHUmpxRWI?oc=5) | - | 연합뉴스 |
| 일반 | 게임 | 넷마블 | [넷마블, 3분기 영업이익 44.6% 감소…신작 지연에 실적 부진(종합) - ](https://news.google.com/rss/articles/CBMicEFVX3lxTFB0bVplYjYtMzdhek1SLUJIOVd3TllaREN2eHdXSHBIcC01N2dDdTBZNjhuLXQyRHBxeWZZbEs5Si01bXZmS1FESERZMUt5T2czdC1jUmZjUm5oR2RGYXhIUjd3ek5aMnNQbzl6cnFXM3Y?oc=5) | - | 연합인포맥스 |
| 일반 | 게임 | 넷마블 | [넷마블, 'WB 올스타 키우기'·'가디언 테일즈: 디그닷' 신작 2종 공개 ](https://news.google.com/rss/articles/CBMiVkFVX3lxTE5VQVJxWGxsTEFUX0Q3UDllSl91UV9lZUxsamZ3UXdfdW9OcFFiTzFOaW5LZk1PMmNwb2ZWRnBmMEIzLWJBVWp5eW1QSGxqV2F3Yk5wUkxR?oc=5) | - | 지디넷코리아 |
| 일반 | 게임 | 엔씨소프트 | [[기획 | 게임사 AI 전환의 현주소 ③]… 엔씨소프트, 활용 경험·이해도 ](https://news.google.com/rss/articles/CBMibEFVX3lxTE1GMzVTc0t4WWt3dHZFSWtCZC1aWldWbjg4QjJwUkNmSXo3a0l0QkxIYXhySDdLVzlsMHc3VUZmRUhPYl9LYU9LZ1lQVUhmZkQ1b1Y4TkFSTTRYaGVmSnk4RFAtcFVaMWZScVN5SA?oc=5) | - | 이코노미톡뉴스 |
| 일반 | 게임 | 엔씨소프트 | ["게임 생태계 지속 성장 위해"···스타트업과 10년 상생한 엔씨 - 주주경](https://news.google.com/rss/articles/CBMiaEFVX3lxTE1BNDU5LUpuNE53M1B4bFRHYkJCWkFjZGpkbXB1am5UeFZWWGM4U2xwVGRNYmRDNU5lemgxSDlkUkRqTHpNdmpqY1VNZXVQc01TbFZIcnp0ZHpOWVpLVklaWm1GbklVYmdY?oc=5) | - | 주주경제신문 |
| 일반 | 게임 | 엔씨소프트 | [[헷갈리면 손해] 넷마블 영업이익 3525억, 엔씨소프트 161억…같은 게임](https://news.google.com/rss/articles/CBMiYEFVX3lxTE9KbFIxM0pLVDlrVEdkcjdSZ0Mwc2MwRmV3Q3d4XzdNZEpNbnlHMmZ3dW0tSjA1X2pkUHVlZkF3bWY0cEhnRWQtY1pOeFFZeHkxend5aFlCUVZwUkU2aEdJdA?oc=5) | - | https://www.theconnectmoney.com/ |
| 일반 | 게임 | 엔씨소프트 | [미래에셋證 "엔씨소프트, 신성장 준비…목표가 28만원↓" - 이투데이](https://news.google.com/rss/articles/CBMiVEFVX3lxTE16czRpRkxmcklNUWtCNm9aNnNuVEtqT3VOUllBQXVEeHA3TTJieDN4a255MXJCZVVObFF4VE1GUlpfc1dqbElJSHNmNUJ1X2NSVW5zag?oc=5) | - | 이투데이 |
| 일반 | 게임 | 엔씨소프트 | [김택진·박병무 엔씨소프트 대표, AGF 2026 메인 스폰서…최대 150부스](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE05czh6QzJSS2FqZEZCcTJfNThBZ0NpVi0yYktTN1BGYjByWXhqdFdBUkNVaTR3SThuSEpHSWJhMURlOGt1WkVYaEw3aFM3TnZUWDBEQzlNTFZGMFd4TXdIZTRxWnZyNk3SAWtBVV95cUxOMHpBTUx0eVZiT0VqY25KWHA1YlVaRDVzRVhyVVNWN3ZtQUxOSnROeC1laVYwRUdUYVV1SUNfZzdnRGZtMGFzaWVpUWlDM1VUc2t5SW02MmJiVmNvTTY4dkFKZEtDZ3drSGdsSQ?oc=5) | - | CEO저널 |
| 일반 | 게임 | 크래프톤 | [엔씨·크래프톤·컴투스, 3분기 실적 주목 게임사들 - 게임플](https://news.google.com/rss/articles/CBMibEFVX3lxTE5vWGpFTHQydzVGWEpSc1k0ZlI2NWhkX1JyS25FbmpPMVJnNkk1Mm1uaVZhdzdYN284dExOTlFldEg5MFJwbVJLT0tGZmY2VFlpVFpUaUpVY2VBbnZiLU5kQVVtcENqZXhqSDRoaA?oc=5) | - | 게임플 |
| 일반 | 게임 | 크래프톤 | [게임업계에 부는 개발 조직 ‘슬림화’ 바람 - Chosunbiz](https://news.google.com/rss/articles/CBMiggFBVV95cUxNdFh3LU1pdkplMFdrLWNQeGxGcnBrTUVnS3Q1VmlXMVBDeW11Z0tNTzNRazNNRkEtOGNyZVBmVHlqc3Z4WkEweXF6OXFpcjRQTGtmNl9GRXlGM1dYbFh3b2NOeGFNcWIzZVdvbGdBdm9GUjBuM3BGcVk4dXg3bnF1S25n0gGWAUFVX3lxTFBnazduODRPek1Cb1VmQnNFczVRakVPdGlaaG5qNldUSk9Qc0FicC1QSlhkaGI5UF8yN3hPMFBldHNOZVJDT19kZWVOSllNQm5fVTlQb001djJGajYwRkRiMUl6cDJqU0pkaVI5bmZFN19KSmhYV3lOR3F5WUI5WVJIdU5MSm5tU09oOXNkUXRTTi1qN2RoZw?oc=5) | - | Chosunbiz |
| 일반 | 게임 | 크래프톤 | [게임업계 3분기 실적 희비…크래프톤 매출 1조·엔씨 흑자 전망 - 연합뉴스](https://news.google.com/rss/articles/CBMiW0FVX3lxTE41X1poa1VUTmd3ak9fcEZYVmROVW4yeEFQTjhNODNhM09VMUVWMk5aS0VKeVF6V3ZsMW12ZXF0VUU0WWxoTzYyMnZaSFJlVnd6dWNHeTVWN2M2eDDSAWBBVV95cUxOSDBERnVKWUVKaDNEeWpScFUza0tlVlBBUDdMWWtoWkZoMXQ2eG5fV1YtRlZxWHQzbXgycHVJek9MaFNmaVVYWkRCNmVJTV9XTExmR1ExRHFMRXZ0bEhhWjU?oc=5) | - | 연합뉴스 |
| 일반 | 게임 | 크래프톤 | [크래프톤·엔씨 웃고, 넥슨·넷마블·카카오 울고…게임업계 엇갈린 3분기 성적 ](https://news.google.com/rss/articles/CBMicEFVX3lxTFBIXzBfZS1WTTViMEhXUThWTHpkWFFTbzl1SElacHhTV0lrUjNUZ1NsOTRGM0tMZmhabzZxWDRpbUVsTWJWTDhzNEJqVkhZYW1Kcm5BLVJKamtVWmFOU2pudnRPWlBHRnNiUzJaMkNJZW7SAXRBVV95cUxOZ0s1VDZIdFpzc0hRVXlpYkdLVFJqbnhXR1ZaMTc3UjBJbEJ1d3BhSW5aWnhOVGFHejZOTzJWLWZSNW1ZY0k1RHFpc3EtTmVLRTBUdW9ta2lpNTN3emprS2ZvcGVyTWh1Qmw0N0FfQkFhOTl1eg?oc=5) | - | 주간한국 |
| 일반 | 게임 | 크래프톤 | [크래프톤 'PGS 10' 파이널서 한국 3개 팀 출전, 첫 매치부터 고전 -](https://news.google.com/rss/articles/CBMiakFVX3lxTE1SWEV6Q19EZEtGbTIzQ0xMSlNIRHJzSGNGekhoamFIbWdLb09vTVJma3dHU1dwQmg3TmFpOVZHN1FUUE5qWnJvcjQyZFV5X3dUSzRyRld4SWppY24wN2h5dW1VVVNYNlNrMGc?oc=5) | - | 게임뷰 |
| 일반 | 게임 | 펄어비스 | [펄어비스, '붉은사막' 3분기에 68만장 판매…차기작 '도깨비' 내후년 출시](https://news.google.com/rss/articles/CBMiZkFVX3lxTE5hSWxzT3NBLWdJVExITjFlVy01WkxsSTkyWnV0dkU3aG16V2xka3h6VFB1Q252Q0ZWUXMwNFBtMjJpOFBnaGVUWXVxMWJNNjV3VXNReXBoSk12XzZOYlY5Nmt6U2tmZw?oc=5) | - | 디일렉 |
| 일반 | 게임 | 펄어비스 | [펄어비스, 3분기 매출 1015억원…검은사막의 힘 - 비즈워치](https://news.google.com/rss/articles/CBMiakFVX3lxTE1LZndEVnpyZEhjcklUbVRoMmk5Nks0QllPa1NEOW9YVGZoMkxURkQ4X1J2Nk8tSTJWXzJQMVFJSjgyX2RwOHVsUzUweS1WR3J2ZUgyakE0RHRjR09Vb2NfN2l0SzByQjNiYnc?oc=5) | - | 비즈워치 |
| 일반 | 게임 | 펄어비스 | [펄어비스, 2027년 채용 연계형 겨울 인턴십 모집 - 펄어비스 공식 홈페이](https://news.google.com/rss/articles/CBMiZEFVX3lxTFBwN29iT3I4bUhnN1kyUjl1UHROVFZiM1l4bXdJVnZlVW5SN3hHTE5SeWRsVGlXbzhScUtUZU9zY2lvWDF0ODhNS3dLaTdyRVJ2RVE2bjR5N3RCUjV5VU1XbjJJR24?oc=5) | - | 펄어비스 공식 홈페이지 |
| 일반 | 게임 | 펄어비스 | [펄어비스 ‘붉은사막’, ‘2026 대한민국 게임대상’ 기술창작상 ‘정조준’ ](https://news.google.com/rss/articles/CBMiV0FVX3lxTFB0S21qZDJMaWtKa1BnajZ1Nl92WHd4UXVRZlVNSGdYdXJxb2xTazZEVW5HNmFid3htY1pJZHItWUk1ODEzVlFUaUFaMDVQREpOMjd2U0VHaw?oc=5) | - | 브릿지경제 |
| 일반 | 게임 | 펄어비스 | [펄어비스, ‘지스타 G-CON’서 ‘붉은사막’ 오픈월드 개발 노하우 공유 -](https://news.google.com/rss/articles/CBMiVkFVX3lxTE1YXzNVZU96V0ljUzdRbmdQekw4M1c1eFhVV19lQkg5c3NHVzN3dVROZ2lXOTlTOEVaUUJiT3ZCMUlJQi1KR2RFNHNMU21veGZPX1JZU1JR?oc=5) | - | 지디넷코리아 |

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
