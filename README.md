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
_최종 갱신: 2026-11-23 12:38 KST_

**수집 현황** — DART 공시 154 · 뉴스 343 · 회계법인 리포트 1

### 📄 DART 공시 (회계 이슈 필터)
_종류별: 실적 72 · 📘정기 54 · 🔴정정 14 · 🟡주요사항 14_

| 종류 | 업종 | 기업 | 일자 | 공시 |
|---|---|---|---|---|
| 🔴정정 | 게임 | 카카오게임즈 | 20261116 | [[기재정정]타법인주식및출자증권취득결정](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261116901425) |
| 🔴정정 | 게임 | 엔씨소프트 | 20261111 | [[기재정정]연결재무제표기준영업실적등에대한전망(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261111800327) |
| 🔴정정 | IT | 카카오 | 20261105 | [[기재정정]주요사항보고서(회사분할결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261105000098) |
| 🔴정정 | IT | 카카오 | 20261105 | [[기재정정]주요사항보고서(회사합병결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261105000084) |
| 🔴정정 | 미디어 | 엘지헬로비전 | 20261104 | [[첨부정정]연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261104800154) |
| 🔴정정 | IT | 네이버 | 20261103 | [[기재정정]주요사항보고서(유상증자결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261103000311) |
| 🔴정정 | 엔터 | 큐브엔터 | 20261030 | [[기재정정]주요사항보고서(유상증자결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261030000611) |
| 🔴정정 | IT | 네이버 | 20261030 | [[기재정정]주요사항보고서(유상증자결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261030000001) |
| 🔴정정 | IT | 비바리퍼블리카 | 20261030 | [[기재정정]유상증자결정](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261030000628) |
| 🔴정정 | IT | 비바리퍼블리카 | 20261028 | [[기재정정]주요사항보고서(회사합병결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261028000358) |
| 📘정기 | 게임 | 넷마블 | 20261116 | [분기보고서 (2026.09)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261116001002) |
| 📘정기 | 게임 | 엔씨소프트 | 20261116 | [분기보고서 (2026.09)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261116002195) |
| 📘정기 | 게임 | 크래프톤 | 20261116 | [분기보고서 (2026.09)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261116001814) |
| 📘정기 | 게임 | 위메이드플레이 | 20261116 | [분기보고서 (2026.09)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261116001019) |
| 📘정기 | 게임 | 컴투스 | 20261116 | [분기보고서 (2026.09)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261116002172) |
| 📘정기 | 게임 | 더블유게임즈 | 20261116 | [분기보고서 (2026.09)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261116001237) |
| 📘정기 | 게임 | 데브시스터즈 | 20261116 | [분기보고서 (2026.09)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261116001692) |
| 📘정기 | 엔터 | 디어유 | 20261116 | [분기보고서 (2026.09)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261116001157) |
| 📘정기 | 엔터 | 하이브 | 20261116 | [분기보고서 (2026.09)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261116001746) |
| 📘정기 | 엔터 | 와이지엔터테인먼트 | 20261116 | [분기보고서 (2026.09)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261116000477) |
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
_구분: 🔴회계신호 19 · 🔵회계이슈 12 · 일반 312_

| 구분 | 업종 | 기업 | 기사 | 회계토픽 | 출처 |
|---|---|---|---|---|---|
| 🔴회계신호 | 게임 | 넷마블 | [[재무제표 이야기] '정수기 게임' 우려 딛고 넷마블의 ‘황금알’ 된 코웨이](https://news.google.com/rss/articles/CBMibEFVX3lxTE56UWVmcFpXTmhHZm1hanhhWFFjNUljbWpuZndaYUdQckRQTmUzTEtJb3hkU0p2b21jZ1RjSXZhZ0dQc19BRlhkTzFJTlVTM1NtbDB5emxnb1k0MDFQd1JkY3owVVItN3dkZjYzdA?oc=5) | - | 생생비즈플러스 |
| 🔴회계신호 | 게임 | 스마일게이트 | [스마일게이트 'IPO 소송' 2심 돌입…CB 회계처리 공방 - 블로터](https://news.google.com/rss/articles/CBMiaEFVX3lxTE8wR2FkT0VGYmlIWVgxQW1tYW5xQTBFd0ZXMFRsekU5Q0lPRDdLcjF0bVBDd1pITTBxNmllQUtjRmlqVEcyV005d3BKNzl1cDZiVHFSd0U4YmpPazkwNXoxRzQ0Y2F6a3gx0gFsQVVfeXFMTWtiQnFpS1ZBOHVuSWV5amI3VWRFaWdTbUZ4eU1lMWFNVXhFblI1c2U2TkFOV2dWcE5rS0VIQllrc2N1SFRPWjl2eDdOa2hvamhUeWtaVG1vTGw2b2phUWowZndzMXNTNmVBOVFU?oc=5) | - | 블로터 |
| 🔴회계신호 | 게임 | 스마일게이트 | [미래에셋증권·스마일게이트 IPO 소송 2심…‘계약 취지’ vs ‘회계기준’ ](https://news.google.com/rss/articles/CBMia0FVX3lxTE9kVTFRajhxMHdYZ3kwMkczZ3lQa3gxWXlMN0JySnZHbXM1dFlNZVNCN2tyQlRmU1VDdUNhNFA1VjBSYk9zWkhRQmpKNnRmQ0dmdmRRXzY5TUZKNFU1ZnF5TEJHMmw3QlctWHBR?oc=5) | - | 더리브스 |
| 🔴회계신호 | 게임 | 컴투스 | [[재무제표 이야기] 컴투스 명암 엇갈린 10년...미래는 - 생생비즈플러스](https://news.google.com/rss/articles/CBMibEFVX3lxTFBLLTQzb1pZam9pTm5QTXhNc0trU1dDZ25RMnFHQzNqT205STRTbTZ2dDl5TG4zTnhLTy1zczNIcUIwcGtNRm9iUUdNN1YzOXNiTTllXzdFaGRPbndkQkxhb0ZoWjdiMFhBbHloeQ?oc=5) | - | 생생비즈플러스 |
| 🔴회계신호 | 엔터 | 하이브 | [의견거절·재무제표 재작성…'암살자(들)' 제작사 하이브미디어코프 회계관리 도](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1Tc1FHRU5CMFp6LUlBcUJkd0FtU195bV9fRGQ2R0NDMjMxWDJ4UW9OTXVRcFRHMzdhSWdiaEVIRkl5WmY5czB3RkJpb0tFdkJHUm5FekFsMzVUdw?oc=5) | - | 블로그 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | ["계열사 전반 재무제표 왜곡 의심"… 중앙그룹 피해자들 검사 확대 요구 - ](https://news.google.com/rss/articles/CBMibkFVX3lxTFAyVVZEV2FCZDdpMW12YURXNWIxVGNIdzE0MWoweUFPYUhlbEFHWVFGV2V4WV9uM2U2WDJ1Ri0xb3U0QTlrTVhIaWo3UWRFMTVJSHNvSzlyUjlPV3d1WWNOODg0NFpZSllKOElOekxB0gFzQVVfeXFMTnMzNmJkaFo0LU15RVNMemVtVUpRSVNlblhEV0w3R3BwWXpZNlNrTDM3Q2twSldRYmZ2RHpiWGlpZnppdzRmdThDVzZyaklMcXBiLUx4MDdzSkE5RERob3M3TzBBUnkwUURIU2hMUVR2V0dZUQ?oc=5) | - | 한국일보 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [[단독] JTBC 등 5곳 회계감리 착수…금감원 칼댄다 - SBS Biz](https://news.google.com/rss/articles/CBMiU0FVX3lxTE5BcmF4YUtlQkF5MlZKVTl3clRKN3ZmaWdjbHVmZm11dmVhdko0dDFycE1EdjJhSmJ1WFJmVWJsa2NQdURBV0JtV0I5OTJmQjVEWXc40gFYQVVfeXFMUGJKUnFuN0FlX2J0UHFiYjU0amtueG80c0w3dHVtRlNaS1FabVFOX2hUSFk3Zk93U216cUkzRTY1bE5SbTBHYlFFR2RCVVhXcFptX29hakgwcA?oc=5) | - | SBS Biz |
| 🔴회계신호 | IT | 네이버 | [제일엠앤에스, 2024년 감사의견 '적정' 정정…상폐 변수 완화 : 네이버 ](https://news.google.com/rss/articles/CBMijwFBVV95cUxNLUpCSXRCd2IzQnpYWVBzWTZPaXdIMTJ4am8yQURBMlZTem44NUh4emZ3cERrMDEzN3N1VkZYbVF1VDZ1eEk3YnIwbjhJTjlJS18xbjBDUjJ5OVdxdW0zcW1ZOXBVWllKR21Ha1FwWVhJaE5HZDBMOWNJbmxEaC16WFBuQ2NZQ20waFp5ekVPYw?oc=5) | - | Naver Blog |
| 🔴회계신호 | IT | 두나무 | [두나무·빗썸 실적 '희비'…가상자산 평가손실 '회계기준'이 좌우해 - 인더스](https://news.google.com/rss/articles/CBMickFVX3lxTFBfTndtNzZCY2tiYk1BWjdCX1EzSnN0ZkVrX1F5WF9oQVVlcE5QOHVQU19QQVNIZkE0T0k0T2RUM3lfREhHY0VLYk9qbnF3T1FRVl9lMVdJRnBsazltSWlyaUYtcEJVZU80Y0lBenFYZ25UQQ?oc=5) | - | 인더스트리뉴스 |
| 🔴회계신호 | IT | 두나무 | [양대 거래소 두나무 흑자·빗썸 적자…회계기준 차이가 갈랐다 - 서울경제TV](https://news.google.com/rss/articles/CBMiZEFVX3lxTE14YzJVYUVpOU4zZXNOa1pUSVNaWDNLcGhHdUpDOXN4cjlhS2dsUVBQQW5qaDJhS2VOcTJEbWxuelhHaExKVEt6UHVjNjJtSFRRTFF0b2wydm9GUVYxY1lCOTI4bkc?oc=5) | - | 서울경제TV |
| 🔴회계신호 | IT | 두나무 | [두나무 흑자는 회계기준 덕?...보유코인 하락분 평가손실 미반영 - 금융소비](https://news.google.com/rss/articles/CBMiakFVX3lxTE5VMDZCcHJKdEg2cElfV3VMeGltTkdzamhGcXVCYVVnVE1DeGZOc3BoTlZacTVOakRiRTR2dDlaaG5kbXo3RkJUMkM4T0VhWmVPSkpzRDFpOE5QamZxX3JVeG1qemg5Nm9iNWc?oc=5) | - | 금융소비자뉴스 |
| 🔴회계신호 | IT | 두나무 | [올해 두나무 흑자·빗썸 적자…"배경엔 회계기준 차이" - 매일경제 마켓](https://news.google.com/rss/articles/CBMiUkFVX3lxTE9LX2JDMFhsRXJOQThUVDh1OTFTcl82am5FcUJ0NGQzdXZtVE5wRUNudF9qTkZHSFAtdmw3V1VIWXlwWEdZVmI5Y1hwUEx0ZFotV2c?oc=5) | - | 매일경제 마켓 |
| 🔴회계신호 | IT | 두나무 | [두나무 美 상장설 다시 고개…“회계기준·행선지 결정 안 돼” - 이투데이](https://news.google.com/rss/articles/CBMiVEFVX3lxTE5rR0JabEc4RWVrazRoMUIxOWlwb2h6NzI1VjFzWUI3MnFRbThXcnRlbl8yNk13TVBzZXVMLVpNR2hLdWNwWHktYnpQSFNtX3ZqWGFwZw?oc=5) | - | 이투데이 |
| 🔴회계신호 | IT | 두나무 | [두나무, 美 회계기준 검토…상장 국가는 미정 - 아주경제](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5QZmxPY1VoZDBoeVMtNUptQUU0Skkza3I3d1NISVVrWDRNWk84QklUUlFaeGRydWVRNDV2eDFTb1d4elNoRkFEOWQyUGdLbGQwYllhUFZDcm9yZ9IBWEFVX3lxTE5XNHNNNGppTzJzWG5IdjQ2eUF6OHJTT2M0T1JoTGx3ZVNmQ2FiaFY1Q05jTnFQYnl4WjZySnJGTnU3d0sxWEwyZ3l6UzJ3X1gyWFRDUm1qZUE?oc=5) | - | 아주경제 |
| 🔴회계신호 | IT | 두나무 | [두나무 흑자·빗썸 적자 배경엔…업계 회계기준 차이 - SBS Biz](https://news.google.com/rss/articles/CBMiU0FVX3lxTE5SQzNMZUM0ZUszQm52d2lneHpLTzJndC11OUx3MmdZVHFGeVIta1lCcUtkS1IzZU1WUEROR2hyVUxRcTd0Z0lpckNma0ZMdlBHal9J0gFYQVVfeXFMT3luQV9zaXFjc3U1NGtYYmVtbGQzT3BKVllmWjN0clZvY2l1UHowdkhzdHhHS2xVSnVtcTFzZFpIZXVpdzcxU21SYXptVjlvd2xJZ0VxdHI0Rg?oc=5) | - | SBS Biz |
| 🔴회계신호 | IT | 두나무 | [두나무 898억 흑자·빗썸 1102억 적자…가상자산 회계기준 차이가 순손익 ](https://news.google.com/rss/articles/CBMibkFVX3lxTE4xSHVHdlk3dk84N0JydWY3azBtME14WmtRUVprRU5zdWVidGxLYVpneGNZNHZnYlFBT2V6eG9rVS1vX2g3NThNRzZ4cGRuTVVkVks4cHRRa0tqdEk2azNQNTRvUzUtTTZRV2cySERn?oc=5) | - | 폴리뉴스 Polinews |
| 🔴회계신호 | IT | 무신사 | [[재무제표 이야기] 무신사, 재무제표는 더없이 훌륭한데...문제는 오너리스크](https://news.google.com/rss/articles/CBMibEFVX3lxTE1jV2NfN21Kc29OVUJ6bk92V01SLS1HaDV1SlFkeUlfOFpqMU8taHFXQUJVT1JYNjBkWVpRenpqMzZwUnZ2OExBbTdaTVRrNm5ZWHhwa2pHZTBwM0xnNnc1c2paZTJjY29XdWR1UA?oc=5) | - | 생생비즈플러스 |
| 🔴회계신호 | IT | 컬리 | [컬리·풀무원 재무제표…좋은 숫자만 믿으면 생기는 일 - 자본시장뉴스](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE96S0pOeklqUjhkWngyNlYtaHJzN1VTREtXcXpzN0JjSTRVTWU2NEFHeEpsUEFwYU16SVA5TXpxM1gycDN6T3o5eE01Q1ozVzl2ekVWbm01Q0o5c0o4bG5pTDdPUlpKVjg?oc=5) | - | 자본시장뉴스 |
| 🔴회계신호 | IT | 컬리 | [[재무제표 이야기] 흑자 전환 컬리...그래도 여전히 '미생(未生)' - 생](https://news.google.com/rss/articles/CBMibEFVX3lxTE1CZHpNRmxVcHB3N3hSazFQYkNJelpma2U0UzVNSjBkcThaNmUxcWlfZGVRWS1STGZzcF9vVVZRb1hfdWdhMEJWRWw4M1RwWjdQM1FGa2tEOXhZdDlaMnZCU0hrV3M0LWd0a0xNcw?oc=5) | - | 생생비즈플러스 |
| 🔵회계이슈 | 게임 | 넷마블 | [[국정감사] "게임판 음원 사재기" 논란에도 정부 조사 없어…김재원, 순위조](https://news.google.com/rss/articles/CBMibkFVX3lxTE1hS2V5dnlPSWVXZkZfOHVGcGxmOWtYNVJQUXR4c3RFdDEzOENvOWZ1dkpqLUJCeUctVUZDSTFUMUhPR2ZPMUQtUVdFOV90bEozUzZnaUhhWjdlcTdSQVUzMFpPR0tGZmxpZnAtVExR?oc=5) | intangible-assets | 에브리뉴스 EveryNews |
| 🔵회계이슈 | 게임 | 카카오게임즈 | [“영업손실 263억 카카오게임즈, 라이온하트 1.1조 영업권 손상차손 ‘시한](https://news.google.com/rss/articles/CBMib0FVX3lxTFBDeGEzSXN0UXlWUzgtdGVYYUVidm9wa3BScl9UeHo3Nk1OZHVVRVVFak5sb2hGRU9LNnhyZXZaMWlYZGZVZTA4ak5zd0ZYOE1XdmFZcXAzRVN4Ym5mTkVQN1dyRmN2M1hESUNJZFVCWQ?oc=5) | intangible-assets | 뉴스퀘스트 |
| 🔵회계이슈 | 게임 | 위메이드 | [위메이드, 미르 中 라이선스 효과 3Q 흑자전환…영업익 264억 - 메가경제](https://news.google.com/rss/articles/CBMickFVX3lxTE0yM3p4UW42RzF3U0JXTjNXWXdOdjdacnVGMWhibE10cXQ5OUFRWmJiYURrcklHWmdxeDVDTzdkSFlDcS1Lb2RWakExdExlNWZrNnBydlRhWU55a1JTbEtnUDJWZ28tUWx5cUxUYjhTVmtLQdIBckFVX3lxTE0yM3p4UW42RzF3U0JXTjNXWXdOdjdacnVGMWhibE10cXQ5OUFRWmJiYURrcklHWmdxeDVDTzdkSFlDcS1Lb2RWakExdExlNWZrNnBydlRhWU55a1JTbEtnUDJWZ28tUWx5cUxUYjhTVmtLQQ?oc=5) | intangible-assets | 메가경제 |
| 🔵회계이슈 | 엔터 | 드림어스컴퍼니 | [[가요소식] 드림어스컴퍼니, 음원유통사 디에프에스비 콜렉티브 인수 - 스포츠](https://news.google.com/rss/articles/CBMihAFBVV95cUxPVTBBeW9UeUdwdjB5bEpkXzNmZmRvNlJXeW55NjE0WFB0WXhITGpaRE1OanhWU1NQUF9wNXRQLWJwak94VkV0VnVFZURNZHFIV212cXRjc0lzWWwzYURVZzBaR3BDQnR5b1A2LWphU3hSWVdPdUotM0loZVp5d3FVZkx0SlI?oc=5) | intangible-assets | 스포츠조선 |
| 🔵회계이슈 | 엔터 | 드림어스컴퍼니 | [[가요소식] 드림어스컴퍼니, 음원유통사 디에프에스비 콜렉티브 인수 - 연합뉴](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1HXzBrSVdObXBfSzk1MzBjYWhaMVJGWnZsSTlva1hMLW5CY0s4dmV5OEZLNmd1cDE1ZmtzbTZzc0dsUmdwZVlaWDg2SkxRaF9yLTA2ZmRZQkJTTWvSAWBBVV95cUxPYnkxSlZDQXpVOGZpdVM2blc2UVBEcmFMd3dNY1AweWw3ZlRaWlBpMWZkZkNCLTBUNjNzYy13REFZWlc3OEhuMkNCLVk0U09BTnFrTVMydlFsa0VuZ3ZfTlA?oc=5) | intangible-assets | 연합뉴스 |
| 🔵회계이슈 | 엔터 | 드림어스컴퍼니 | [드림어스컴퍼니, 해외 음원 유통사 ‘DFSB 콜렉티브’ 인수 - IT조선](https://news.google.com/rss/articles/CBMicEFVX3lxTFBpVFpTZHFfWFlDZmtZZ2xHYXFVQlRBdFRibUdyNnZLclFNdF9zcXhrMV9LMGlPczZZeG00TElWYmxvLVhFcGVZRlR2aTVrVzRSUll0ckZkWWQyT3BQWVdfS09UR3l5blU5ZEtGRlFIYVjSAXRBVV95cUxPQUtCZGVvaDVfNHNyT1NTY2ZrbHVRRFZmSHpocTFpWlNXd3djQWVVTFdrYzJydUdfZ0ZXMnBQamRRTmZSX2phek9PWkQ2OXRkLU8zU3NzbmVtaVpzNHd3TXBLUWY4U0t3bEhmU0RfNFlKOVNGbQ?oc=5) | intangible-assets | IT조선 |
| 🔵회계이슈 | 엔터 | 큐브엔터 | [[더벨]큐브엔터 소연, 국내 주요 음원차트 동시 1위 - 머니투데이 - 머니](https://news.google.com/rss/articles/CBMiaEFVX3lxTE1YUkozVWZZTTZIV3FhZ3N2WG51cTVKeEh3QUZETkpwZDkxTmlzRkZmUW55MjlpQlZRZDA0TElNcS1lN0VKdDFjNllqblUtc1hrcElwMWtRMGxoYWZTTHE2T1lXTUE0LUVy0gFuQVVfeXFMTm85WXQ0VG9sYzZINUt2SUFDMkxPSlFNQWltRzZmZmRzdkRFamtSMHA3WkE4WkJYZ2JNVThsRlFQaVdkcGVtYXFFeV9LVHpEQm9OdlZFVnBsY0c4U0xjN3JCMlBwNDVseDhRT3F5WXc?oc=5) | intangible-assets | 머니투데이 |
| 🔵회계이슈 | IT | 야놀자 | [야놀자, 3분기 통합거래액 13.8조원 돌파⋯ 조정 EBITDA 26.8% ](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5sT2l6MW41anhnN1p6bHVDYml0cmV0Yk9DUERwa1ZOYWxjT2RBVG9WcDFrQ1dQTnhYUHcxbExyemZlblNwWGtMcDZoclVKRDh5cExvd2pLSlZ4dw?oc=5) | platform-cases | 브릿지경제 |
| 🔵회계이슈 | IT | 야놀자 | [야놀자, 3분기 매출 줄었지만 조정 EBITDA 27% ↑…통합거래액 13조](https://news.google.com/rss/articles/CBMiaEFVX3lxTFByU3A5SWt2ZmZrTjZSekJYdTRNS0JPa2c1VFBheE5Ddnl2TnR2eEpiNk8yTldockQ5eFQ1bDJGQ0hHSHVHeUJpaFRvRVhWZGxzM2FWdjRGd0FjTk9TSlkxZ0luN2piVUtK?oc=5) | platform-cases | www.ebn.co.kr |
| 🔵회계이슈 | IT | 야놀자 | [야놀자, 통합거래액 39조2000억…글로벌 확장 속 수익성 회복 과제 - 한](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBGUjAxQjh5ZDVuNVBhYWFGVm1DcGZIN0dzdk51SEdGVzhjSmpKVEpLRXZoTnl4UFVETnJLRGpwcENlQkhqQXFrUml6QWpSV1JRR0hsVmlmdE0wdw?oc=5) | platform-cases | 한국경제 |
| 🔵회계이슈 | IT | 무신사 | [무신사, 일본 거래액 성장세…내년 도쿄에 첫 오프라인 매장 - 서울경제](https://news.google.com/rss/articles/CBMiUkFVX3lxTFB0RndDVmJQcFMyM1ZaR21jZTg3Qk1oTE82Z19HRlJDMW9TWFZIUnM0VHpXbXhoY01rWG5nazFBRTFiMEhQWG04WUVGeHdjVjZhSFHSAVNBVV95cUxNZExCcFVycEZ4SDRrYzh0Xzl6Z2JXX3N0eENTVlZndmJocEN3LThWYlZrMDJkc0gxZG5oX1d1ck1QMlhHbkhUbTR0dHhKb3UzZWhQbw?oc=5) | platform-cases | 서울경제 |
| 🔵회계이슈 | IT | 컬리 | [컬리어스 '파인에비뉴 A동' 매각 자문 완료…누적 거래액 3.2조 돌파 - ](https://news.google.com/rss/articles/CBMickFVX3lxTE5IUlBuUW84Nm5KbnZhbFZBY2ZSMmlReENnR1JhUTZ6c3JIdUhYRVVFSlhWdk1VVVdTQTlPdWRZTVRDandOZnhnTnJGWXAwblBHaG5jUTltcW5aTVF3M3k5RG1UOFZZUUlNY2xvdE0xUVpwQQ?oc=5) | platform-cases | 마켓인 |
| 일반 | 게임 | 넷마블 | [신작 늦어진 넷마블, 3분기 영업이익 44.6% 감소 - 조선일보](https://news.google.com/rss/articles/CBMigwFBVV95cUxQeWpxdlRqUTFxaUlEQk5SbjNic0tOVDVza2ctRUhCOF82NE1TcHplcEpTdTUxMFI0aUlhbjBKV3B4UjJmRUlzX20wdkUxOW5oVG5fMXVCUkk4Nm9HdVZZR2Q1eDl2ZFU0bkRZMmpiczRWUWthWGVObG05VVpmVW9sbjZCVQ?oc=5) | - | 조선일보 |
| 일반 | 게임 | 넷마블 | [넷마블 '나혼자만레벨업: 어라이즈 오버드라이브', 콘솔 플랫폼 진출 - 지디](https://news.google.com/rss/articles/CBMiVkFVX3lxTE83M1IzUE5nSGNIX0hnWjl1Qkd4VHlOU3RqZnd5RFFtQy02UmhhaUsyU25RV21wOE5xWWtYY1hkNmY1TVpZeW94SUFhblVZZlJrQnUxVHd3?oc=5) | - | 지디넷코리아 |
| 일반 | 게임 | 넷마블 | [내년 신작 13종 쏟아내는 넷마블…"AI로 퍼블리싱 효율화"(종합2보) - ](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBSUk5NZ0tWS2dHLVBjdWpHaUxtTEM3UWg2dTJON3VDdmVSeGEzZGZrcjRqUnJHNWx1R09YaTVQS1E5MzRjMU1TZ1RuS2lUTnBxVXhLajdYbnJPOW_SAWBBVV95cUxQWUgteDVfOGZreVVWYS1JQWRVRW5xWktzNFdQdk5sUzRHYVo4Q2FuMExvalJmLW1wZFJ5WFdUWEtrNXMxa3luVVZfODA4c3p2VDEwNGczcVIyMDJTWksxbUM?oc=5) | - | 연합뉴스 |
| 일반 | 게임 | 넷마블 | [넷마블, 3분기 영업이익 44.6% 감소…신작 지연에 실적 부진(종합) - ](https://news.google.com/rss/articles/CBMicEFVX3lxTFB0bVplYjYtMzdhek1SLUJIOVd3TllaREN2eHdXSHBIcC01N2dDdTBZNjhuLXQyRHBxeWZZbEs5Si01bXZmS1FESERZMUt5T2czdC1jUmZjUm5oR2RGYXhIUjd3ek5aMnNQbzl6cnFXM3Y?oc=5) | - | 연합인포맥스 |
| 일반 | 게임 | 넷마블 | [방준혁 넷마블 의장, 지스타 2026 현장 방문... 대학·스타트업 게임에 ](https://news.google.com/rss/articles/CBMiTkFVX3lxTFB4UkVfLTN4eFY0cGZCY0pjOVlMY2pGQTVMb2g4M1F6YWRkM1RRc2tsc0JJb2cweF9lcTZTRzNmMFpOenlLcFVDTWlNZkN6UQ?oc=5) | - | 전자신문 |
| 일반 | 게임 | 엔씨소프트 | [엔씨소프트 〈리니지2M〉, ‘더블 페이백 월드 신서버 데스나이트' 업데이트 ](https://news.google.com/rss/articles/CBMiaEFVX3lxTE1nWjluYlpmSWFKdmpEbzFhOVh5MHhtdkhJbW52Ul9mXzRFbEswUWQwNXVOM1hTNG95T1RxbV9Uel9scXdESUc4bUxteFRiZVBxSDI5d2hfNVpKaXZSWDNFMEdzTENKMUZ3?oc=5) | - | NC |
| 일반 | 게임 | 엔씨소프트 | [[기획 | 게임사 AI 전환의 현주소 ③]… 엔씨소프트, 활용 경험·이해도 ](https://news.google.com/rss/articles/CBMibEFVX3lxTE1GMzVTc0t4WWt3dHZFSWtCZC1aWldWbjg4QjJwUkNmSXo3a0l0QkxIYXhySDdLVzlsMHc3VUZmRUhPYl9LYU9LZ1lQVUhmZkQ1b1Y4TkFSTTRYaGVmSnk4RFAtcFVaMWZScVN5SA?oc=5) | - | 이코노미톡뉴스 |
| 일반 | 게임 | 엔씨소프트 | [[헷갈리면 손해] 넷마블 영업이익 3525억, 엔씨소프트 161억…같은 게임](https://news.google.com/rss/articles/CBMiYEFVX3lxTE9KbFIxM0pLVDlrVEdkcjdSZ0Mwc2MwRmV3Q3d4XzdNZEpNbnlHMmZ3dW0tSjA1X2pkUHVlZkF3bWY0cEhnRWQtY1pOeFFZeHkxend5aFlCUVZwUkU2aEdJdA?oc=5) | - | https://www.theconnectmoney.com/ |
| 일반 | 게임 | 엔씨소프트 | [엔씨, 지스타 2026서 게임 스타트업 2곳 참가 지원 - 조세금융신문](https://news.google.com/rss/articles/CBMiY0FVX3lxTE9tYzMwT2FFbVlzdERWNlV4ZG5oS3J0ZE1zS2tNTERubUNBdmN4YVl4c3RxM2dHUEZnY2J5VmRUWVBaSE1aX04xNy1qVU9yWGl2emZUQVJqcDduRFJOMkM2Ny1Raw?oc=5) | - | 조세금융신문 |
| 일반 | 게임 | 엔씨소프트 | [미래에셋證 "엔씨소프트, 신성장 준비…목표가 28만원↓" - 이투데이](https://news.google.com/rss/articles/CBMiVEFVX3lxTE16czRpRkxmcklNUWtCNm9aNnNuVEtqT3VOUllBQXVEeHA3TTJieDN4a255MXJCZVVObFF4VE1GUlpfc1dqbElJSHNmNUJ1X2NSVW5zag?oc=5) | - | 이투데이 |
| 일반 | 게임 | 크래프톤 | [엔씨·크래프톤·컴투스, 3분기 실적 주목 게임사들 - 게임플](https://news.google.com/rss/articles/CBMibEFVX3lxTE5vWGpFTHQydzVGWEpSc1k0ZlI2NWhkX1JyS25FbmpPMVJnNkk1Mm1uaVZhdzdYN284dExOTlFldEg5MFJwbVJLT0tGZmY2VFlpVFpUaUpVY2VBbnZiLU5kQVVtcENqZXhqSDRoaA?oc=5) | - | 게임플 |
| 일반 | 게임 | 크래프톤 | [역대 최대 실적에도 웃지 못한 크래프톤 - 비즈워치](https://news.google.com/rss/articles/CBMiakFVX3lxTE5vZ2loSFpmeFhWTzg2N2tnVnZFZVVmR2V6YjVCV2ZaZmhhekFhN01keE1JWTl3THFuc2wwc3dMajB3RDRvUldLYjFSb3pGa2JwOFFXbXVqR3RqX3p1OW81UmVfS3k2ZV9lX2c?oc=5) | - | 비즈워치 |
| 일반 | 게임 | 크래프톤 | [게임업계 3분기 실적 희비…크래프톤 매출 1조·엔씨 흑자 전망 - 연합뉴스](https://news.google.com/rss/articles/CBMiW0FVX3lxTE41X1poa1VUTmd3ak9fcEZYVmROVW4yeEFQTjhNODNhM09VMUVWMk5aS0VKeVF6V3ZsMW12ZXF0VUU0WWxoTzYyMnZaSFJlVnd6dWNHeTVWN2M2eDDSAWBBVV95cUxOSDBERnVKWUVKaDNEeWpScFUza0tlVlBBUDdMWWtoWkZoMXQ2eG5fV1YtRlZxWHQzbXgycHVJek9MaFNmaVVYWkRCNmVJTV9XTExmR1ExRHFMRXZ0bEhhWjU?oc=5) | - | 연합뉴스 |
| 일반 | 게임 | 크래프톤 | [크래프톤 '타래: 언바운드', 개발진이 밝힌 세계관과 액션 - 게임뷰](https://news.google.com/rss/articles/CBMiakFVX3lxTE40SldPRVFjVWFNR0VyOEJ0NXU3enY4TVlNYTdidFN3anZiTEl0Z1hkcGhVVkR1OW5jVUZILUQ5WHc4VEFJcmpqQ3FXZjdRZmZUalJvODd6eWdfSGJmcHQ4UmJabG0tNnNWaVE?oc=5) | - | 게임뷰 |
| 일반 | 게임 | 크래프톤 | [크래프톤·엔씨 웃고, 넥슨·넷마블·카카오 울고…게임업계 엇갈린 3분기 성적 ](https://news.google.com/rss/articles/CBMicEFVX3lxTFBIXzBfZS1WTTViMEhXUThWTHpkWFFTbzl1SElacHhTV0lrUjNUZ1NsOTRGM0tMZmhabzZxWDRpbUVsTWJWTDhzNEJqVkhZYW1Kcm5BLVJKamtVWmFOU2pudnRPWlBHRnNiUzJaMkNJZW7SAXRBVV95cUxOZ0s1VDZIdFpzc0hRVXlpYkdLVFJqbnhXR1ZaMTc3UjBJbEJ1d3BhSW5aWnhOVGFHejZOTzJWLWZSNW1ZY0k1RHFpc3EtTmVLRTBUdW9ta2lpNTN3emprS2ZvcGVyTWh1Qmw0N0FfQkFhOTl1eg?oc=5) | - | 주간한국 |
| 일반 | 게임 | 펄어비스 | ['붉은사막' 역대 최다 8관왕…펄어비스, 8년 만에 대상 - 비즈워치](https://news.google.com/rss/articles/CBMiakFVX3lxTFA4dDZVTnh6ZmY2Q1AyQTBMMUpTVUdSXy1sX2tNZWcwUWQ0VWNmamJ4ZDFlbHdjdkozTlZuMTNTTEk5eHQ4dmwzSEs4S3lLZWdIU3o0cDl6VXBBbThSY21WVGFrVVptRFc2LVE?oc=5) | - | 비즈워치 |
| 일반 | 게임 | 펄어비스 | [펄어비스 붉은사막, '2026 대한민국 게임대상' 대상 수상…8관왕으로 '역](https://news.google.com/rss/articles/CBMiVkFVX3lxTFBrTF92bHRoaWRaTmtjWmQ3bGRCdXpJeEJLOFlDU3RzM05CUEZFYVA3ZjdteVdCT1BtU2tjUmNVbzNBNVFFZjRVRjl0QWtuc3AwZ1dNTkhn?oc=5) | - | 지디넷코리아 |
| 일반 | 게임 | 펄어비스 | [펄어비스 '붉은사막', 게임대상 역대 첫 8관왕…엔씨 '아이온2' 최우수상 ](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBwNmVZd1B2R2N0amVPT1Z3R0N3SkQxcU41OFM2UGlmOEpBallpTWt3eUFqYjEwdGFNS0VPbWFPemJSUkc4QzNIeE1scVViaExqZk9vbGFqZF9HZw?oc=5) | - | 한국경제 |
| 일반 | 게임 | 펄어비스 | [펄어비스, 2027년 채용 연계형 겨울 인턴십 모집 - 펄어비스 공식 홈페이](https://news.google.com/rss/articles/CBMia0FVX3lxTFB4cGFjaEVxVE5BZmdMaXMwMjg0Y1RTS2dzYjhlLUkzY0Z0RHN0aDYwWUlnckpKM1kzUWdMRTJNX3FxR09DTk1pSExUWEMxZW1rYVhydGRRb3RwbFpYWWx3U1FLQ0x5QXVVakZN?oc=5) | - | 펄어비스 공식 홈페이지 |
| 일반 | 게임 | 펄어비스 | [펄어비스 '붉은사막', 대한민국 게임대상 8관왕‥역대 최다 - MBC 뉴스](https://news.google.com/rss/articles/CBMid0FVX3lxTE80TDZENjVfcWozb3lmbk1vS0VPMWw1bS0yZnBYeTBkRk81MjI3Z0ZVaHIyUENHOTJ2dG50WUxUZm9OUU5yZy0wTzN0bWZvNVJSMlJCQ0lrM0t6QzhZbDJwY1c1TnRudS1rOXBPdXB0MW5uS0ZLM1Bn0gF3QVVfeXFMTWZtSFdTaUZGcGJDN0hKVVZla1h0UGxXU01vTGxDUGhsZlQ5Q21VRnNoNFZWTW5wTWZoV3FDSWlqTjZWRGM2RlRxUml4OUlqS0tSTW5HWlVxa2djLVRQVlluanNMbE9JRi16MEFHc3JvUUtTV0hjaEE?oc=5) | - | MBC 뉴스 |

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
