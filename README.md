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
_최종 갱신: 2026-10-12 11:17 KST_

**수집 현황** — DART 공시 153 · 뉴스 352 · 회계법인 리포트 1

### 📄 DART 공시 (회계 이슈 필터)
_종류별: 실적 71 · 📘정기 54 · 🔴정정 7 · 🟡주요사항 21_

| 종류 | 업종 | 기업 | 일자 | 공시 |
|---|---|---|---|---|
| 🔴정정 | 엔터 | 큐브엔터 | 20260831 | [[기재정정]주요사항보고서(유상증자결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260831001295) |
| 🔴정정 | IT | 카카오 | 20260824 | [[첨부정정]주요사항보고서(회사합병결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260824000219) |
| 🔴정정 | IT | 카카오 | 20260819 | [[기재정정]반기보고서 (2026.06)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260819000055) |
| 🔴정정 | IT | 다우데이타 | 20260811 | [[기재정정]회사합병결정(종속회사의주요경영사항)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260811900833) |
| 🔴정정 | 게임 | 넷마블 | 20260807 | [[기재정정]증권발행실적보고서(합병등)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260807000552) |
| 🔴정정 | 게임 | 더블유게임즈 | 20260724 | [[기재정정]사업보고서 (2025.12)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260724000595) |
| 🔴정정 | 통신 | 에스케이텔레콤 | 20260723 | [[기재정정]타법인주식및출자증권취득결정](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260723801025) |
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
| 🟡주요사항 | 엔터 | 제이와이피엔터테인먼트 | 20261008 | [주요사항보고서(유형자산양수결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261008000381) |
| 🟡주요사항 | IT | 컬리 | 20261002 | [주요사항보고서(주식교환ㆍ이전결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261002000047) |
| 🟡주요사항 | 미디어 | 제일기획 | 20260930 | [주요사항보고서(자기주식취득결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260930000006) |
| 🟡주요사항 | 엔터 | 디어유 | 20260929 | [주요사항보고서(자기주식취득신탁계약체결결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260929000178) |
| 🟡주요사항 | 게임 | 시프트업 | 20260910 | [주요사항보고서(자기주식취득신탁계약해지결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260910000386) |
| 🟡주요사항 | 통신 | 케이티 | 20260909 | [주요사항보고서(자기주식취득신탁계약해지결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260909000349) |
| 🟡주요사항 | 통신 | 에스케이브로드밴드 | 20260827 | [주요사항보고서(회사분할결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260827001001) |
| 🟡주요사항 | 통신 | 에스케이텔레콤 | 20260827 | [주요사항보고서(자기주식처분결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260827000390) |
| 🟡주요사항 | 엔터 | 하이브 | 20260825 | [주요사항보고서(자기주식처분결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260825000350) |
| 🟡주요사항 | IT | 카카오 | 20260821 | [주요사항보고서(회사합병결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260821000052) |
| 실적 | 미디어 | 씨제이이엔엠 | 20261008 | [결산실적공시예고](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261008900389) |
| 실적 | 미디어 | 스튜디오드래곤 | 20261008 | [결산실적공시예고](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261008900270) |
| 실적 | IT | 삼성에스디에스 | 20261006 | [결산실적공시예고(안내공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261006800215) |
| 실적 | 게임 | 위메이드플레이 | 20260812 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260812900504) |
| 실적 | 게임 | 컴투스 | 20260812 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260812900071) |
| 실적 | 게임 | 위메이드 | 20260812 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260812900664) |
| 실적 | 게임 | 네오위즈 | 20260812 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260812900051) |
| 실적 | 게임 | 더블유게임즈 | 20260812 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260812800023) |
| 실적 | 게임 | 더블유게임즈 | 20260812 | [영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260812800020) |
| 실적 | 엔터 | 제이와이피엔터테인먼트 | 20260812 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260812900607) |

### 📰 뉴스 모니터링 (🔴 = 감사·재무제표 신호)
_구분: 🔴회계신호 24 · 🔵회계이슈 22 · 일반 306_

| 구분 | 업종 | 기업 | 기사 | 회계토픽 | 출처 |
|---|---|---|---|---|---|
| 🔴회계신호 | 게임 | 넷마블 | [[재무제표 이야기] '정수기 게임' 우려 딛고 넷마블의 ‘황금알’ 된 코웨이](https://news.google.com/rss/articles/CBMibEFVX3lxTE56UWVmcFpXTmhHZm1hanhhWFFjNUljbWpuZndaYUdQckRQTmUzTEtJb3hkU0p2b21jZ1RjSXZhZ0dQc19BRlhkTzFJTlVTM1NtbDB5emxnb1k0MDFQd1JkY3owVVItN3dkZjYzdA?oc=5) | - | 생생비즈플러스 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [금감원, 메가박스·콘텐트리중앙 회계심사 돌입…자금 조달·회계처리 점검 - K](https://news.google.com/rss/articles/CBMiW0FVX3lxTE54OUVMRE9hMTAyNThval9sRFV5ZDNOeFBHODQ2bmdNQmh5WU41UWtJU2RrZ2ttcEZ0SFhkRm03QjM5R3cxR21pbTJKUFU5ZzFCbEFTSFIwN3hWQUU?oc=5) | - | KBS 뉴스 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [유동부채 1.4조 늪…’적정’ 받던 콘텐트리중앙, 5개월 만에 ‘의견거절’ ](https://news.google.com/rss/articles/CBMirAJBVV95cUxNVUpYMW9JNnd4Y0pRNVNyVkttRXZtOERwekxJX2JraWZrdlpIQkRVSU4taktUNHRCOVVvd21GcVAwd0NlVmJEYVN4WnVsOU5GenZnTlhBQVFpZnRqSVR4bUp4dEJyN081UDFzR2Izb1E4aWhqTFhSLUxyT09QUm1fN3pNbkxXa0xHdURhSGdQYkcwUUp5ODBOeEFwQUYtZG5QOGwxUmR0SVZuclNpRkFuQTB0SHY0QmhWaVVyX3BqaFg1OWVyZmsxWU9ybnp3WVM0eTBGRzJrQWpuRWZoUzVqbGV0QnZHOGhrRTZtUlJxeTRhTnpnUjVKeUZKYWdYd1RiVlRMRy1OSFVRdVdBUHhHSGRtQ0JGWVdOMDc0WWVleUh6WHlUX0VCRVQtdTc?oc=5) | - | 뉴스필드 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권 피해자 대리인단, 금감원에 감리 요청 - 법률신문](https://news.google.com/rss/articles/CBMibkFVX3lxTFB4OEZyLVFxM2lFejNpZm5vRmgwNDAzeWh5TElpVEpxNFhWZ3FJRndLTk5fTF9kWGE0aUdrTjM3S0lCamZ2V3Y4TE03LUNSTmpfTHZsaXROZ1JJeEYzaC1jek9ZRTZudnU2dWRORFdR0gFyQVVfeXFMTlJuUTUzcVYwLTIyMWhZWnFRYVBNc2FPU251QVYyU0V2cXUzU2RvV3RlTS1PMWVXeVNvNElNOTIwWnhXcXRrV1pKdURYZHo5emlVcWR0cC1tc0kxTUlZSVZ0TFBKSGxCUmZDNndnZGg4ZHNR?oc=5) | - | 법률신문 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권투자자들, 금감원에 감리 요구…"회계처리 의문" - 연합뉴스](https://news.google.com/rss/articles/CBMiW0FVX3lxTFB1Ukx0THpTTk1DSVh2VGtQU2hsZTBuZWhlRWhzLUFKNGY0dm1RZkgwdDIxMXdaTzhkTXozUXltRTlOS2VOZ25SdGlfLVY1WVhsYUVfWmMxTERDUmvSAWBBVV95cUxQRDRMM1RQYmYwcGlUY1o2YmZfWTNKQlRDU2JkTmxWNnFlVEs4cTFCOElOR1MyUjhyb0twN18zMkNINldZOE1ZSTNKVVJWdmRDOFZ4S2M2OTVoVHVaWDRHUHo?oc=5) | - | 연합뉴스 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [“돌려막기로 자본잠식 숨겼나”…중앙그룹 채권투자 피해자들, 감리 요구 - 한](https://news.google.com/rss/articles/CBMickFVX3lxTFBDSS1uQk52SXBhb1kycHJkNU5na0w1cmtyUm1hSW5KM2YtQkZWUy1TYlVfT2F5NHhUdElibTdhaExkblFZWExucFBXeVRpM1FkcTNvdm41dHpaODZEVzhScldkQ2FwTnRjZmJWTll0Z3p6dw?oc=5) | - | 한겨레 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권투자자들, 금감원에 감리 요구…"JTBC 등 회계처리 조사" -](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9USmdOS04yVzNFQUhINmFtemVYdjhqYkpJYmN6TnlYMU9mdXQxWGtRQTVmek5kMXpZbjNOZ2kydEJWbFVzaGlZQS1vbUhJUmxDWkc0N3dZLVd1c2VhTURv?oc=5) | - | 조세일보 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [반기보고서 무더기 '의견거절'…투자 유의해야 - 아시아경제](https://news.google.com/rss/articles/CBMiYEFVX3lxTE5SaHA3WS14YmJCdkw4blJCSWhaN0tHUXp1OVA4bWREd21McnRkZXFTR05yTEF0VkpSVk5nbXJWN2NKY3FyUnNzUTMzdEhBSVlsVnN1YllUMnFHNGVCZVVVdw?oc=5) | - | 아시아경제 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권 투자자 금감원에 감리 요구 - 조선비즈 - Chosunbiz](https://news.google.com/rss/articles/CBMigwFBVV95cUxOZ1BZZWVoNlItVU8zZTdWOTBmWVpncDBDUnMyenNPYUhNbWFDRDRlTjZpbzd6MnFxWHhzeWdmb01Jci1QRnN4UU83M0FmcHNTZ21HQmpxSF80WmxIMWRmcldCYmZhZUd4amk0bUtFazJnMVNOZklrZUp2ZjVPb2dFY2xJUdIBlwFBVV95cUxObmZVWHNYUEZEcU9BUUpKQXl1bmNJblA1ZkVvWlZ6bDExdWZkT2JWdFlnR3B0SGdBMWxQVmZrTUdzSlZiQ3FiV1pHU19FZ3M0WHlVMng2dDdpRW1ZUTRnalV3Ri1keE1rOHJVSkpHVUE3Y29jNzltSFNtZ0pOWUQ0OWJHOV9laHY3X2Z4WkdxZktNaHlzTWhn?oc=5) | - | Chosunbiz |
| 🔴회계신호 | IT | 네이버 | [두나무 美 상장설 다시 고개…“회계기준·행선지 결정 안 돼” - 이투데이](https://news.google.com/rss/articles/CBMiVEFVX3lxTE5rR0JabEc4RWVrazRoMUIxOWlwb2h6NzI1VjFzWUI3MnFRbThXcnRlbl8yNk13TVBzZXVMLVpNR2hLdWNwWHktYnpQSFNtX3ZqWGFwZw?oc=5) | - | 이투데이 |
| 🔴회계신호 | IT | 네이버 | [두나무, 美 회계기준 검토 …“아직 결정된 바 없어” - 전자신문](https://news.google.com/rss/articles/CBMiTkFVX3lxTE5HZTFwRHZlQ19keGRBM3pQYkk2THNlZjNKRzFmRjNnMV83OFRyLUQ4elVxV2M4ZUV5eTJTSFdleEZtZUNORTVpc1NNTU1iZw?oc=5) | - | 전자신문 |
| 🔴회계신호 | IT | 네이버 | [두나무 "美 회계기준 검토…주식교환 마치면 IPO" - 비즈워치](https://news.google.com/rss/articles/CBMiakFVX3lxTE5XdU00TXFrTEJLcHI4RFFYcjVUMlIzV1VuVUVrSzFIcGwtdGVvc2pkQzJDOFgtTzlDZnVLNUxFM01ZNUNZVlNUUWNZV3cyTnYtZ3VqMkFyVEdTaGV4dUZoOGpMNndodC1Zd3c?oc=5) | - | 비즈워치 |
| 🔴회계신호 | IT | 네이버 | [[단독] 두나무, 美 SEC 위원장 면담, 회계기준 전환 완료...나스닥행 ](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPTE5PSW1ya182NWtnSDlMTmFrSkhvVC1xUmhPNG9zb3ZDZWd2RVVGalBvSFdmT0xMYUd3bWIxbkE1TkF3YVpPTWtxdlVZTUszdGExSTBNMFhBdkZaMkV3V2JpT196UXV0aDVFMmczaWpYbU5YVXpWbDd1Q1cxVmtEMWtfdzZ5WHZydGhB?oc=5) | - | 조선일보 |
| 🔴회계신호 | IT | 네이버 | [두나무, 美 회계기준 검토…상장 국가는 미정 - 아주경제](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5QZmxPY1VoZDBoeVMtNUptQUU0Skkza3I3d1NISVVrWDRNWk84QklUUlFaeGRydWVRNDV2eDFTb1d4elNoRkFEOWQyUGdLbGQwYllhUFZDcm9yZ9IBWEFVX3lxTE5XNHNNNGppTzJzWG5IdjQ2eUF6OHJTT2M0T1JoTGx3ZVNmQ2FiaFY1Q05jTnFQYnl4WjZySnJGTnU3d0sxWEwyZ3l6UzJ3X1gyWFRDUm1qZUE?oc=5) | - | 아주경제 |
| 🔴회계신호 | IT | 네이버 | [두나무 “美 상장 확정 아냐…회계기준 전환도 사실무근” - 뉴스투데이](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1PZzA0UVNnSERESm1NWDJmMVdLX25MWmFxSkdwZDcxRVZRRlZVM2ZScXhqbHlTM19rQ0x4VFUtUml0SDJDTEhYbmxRSDhqV0NtaENEYVpoYWtxTjg?oc=5) | - | 뉴스투데이 |
| 🔴회계신호 | IT | 두나무 | [두나무, 美 나스닥 상장 준비 추진…US GAAP 재무제표 전환 완료 - 블](https://news.google.com/rss/articles/CBMiUEFVX3lxTE5EN3V6bWdoNE5Ld1VrUDFPeEhKTHdTZFlKbEtmdWw3UkVwYVppeXJCeDJmVE9ER0JtVHBiZXUycktwUjAtRklmNDdJM1VRTjVI?oc=5) | - | 블루밍비트 |
| 🔴회계신호 | IT | 두나무 | [‘美 회계기준 전환’ 나스닥 상장설 솔솔…두나무 “사실 아냐, 상장국가 미정](https://news.google.com/rss/articles/CBMiYkFVX3lxTE1UdlAwTl9kVEhJTm1fdl9QVU5NbjdUVm5VYWVJbnhOQlNBbUM4bk94THdKNmJaa1BDeEtFNDY4UVVEeGZ3YjdaeFdUZTRvOG04dU1aMnl6SWlKLXpMbk5Xc1N3?oc=5) | - | 디지털데일리 |
| 🔴회계신호 | IT | 두나무 | [美 회계기준 문의한 두나무, 나스닥 상장說에 "정해진 바 없어" - 아시아경](https://news.google.com/rss/articles/CBMiYEFVX3lxTFB0MmlXbEZMR0dPcGJEU29yX2tSd2UyeG1zdlNHRWZwOGp6SkdDZWl2eDNBc29rQlZlOEpNMEdPVFI3QWNGNWRBZnpGQTRhQThXRW9NazdHa0VpdlI2Q1UtYg?oc=5) | - | 아시아경제 |
| 🔴회계신호 | IT | 두나무 | [두나무 "美 회계기준 전환 사실 아냐"…나스닥행도 '미정' - www.ebn](https://news.google.com/rss/articles/CBMiaEFVX3lxTFBJblR6OS1vc3JSNDhlYUctWUE5TVRPQ29uclIwNG04SGpKQTE0Q0pzYWlIWjVsTERpSHlBemR5OXd3RUhya2liQlRRZ1NtWFpnM3BBMUotdXNiS2NHTmhkb1RscnpjYTJO?oc=5) | - | www.ebn.co.kr |
| 🔴회계신호 | IT | 두나무 | [美 회계기준 검토에 SEC 접촉까지… 두나무 ‘나스닥행’에 쏠린 눈 - 서울](https://news.google.com/rss/articles/CBMib0FVX3lxTE1MS1Vrc0pBUkhkV2Q0ZWFJSUFMMHdzaWl2c2ZGb215TXZXQkhMbEpjX09RX0JUSk1DX3cyOHBIZ21FSkF3YkJpeFo0cEdpbGVaYm5tLS1tSGJYeXlqVFhXUkNPVXdETWRNZlNQNlJxbw?oc=5) | - | 서울신문 |
| 🔴회계신호 | IT | 두나무 | [두나무, 美 회계기준 검토…주식교환 마치고 IPO 추진 - 데일리안](https://news.google.com/rss/articles/CBMiowJBVV95cUxORkhSRHFOcm5yVWpQS2ZtdDZVeU1nX2VLMmhIVDVDb1B6aHF2YW92a1g2cFNzeVF5OF9tYjdCWHBRandoVlZmd0d1UlpSRUpRTllfWENQcExENE1Ga2hsVVNEb09JUkc5SER0NXUyTTJMYWdIdHFVai1lVmZRemk4RG5zV2Q2aTBzdVpRZTFUbm9TbWxvTy16YVN1eVY3TkpOWk5CNF8tUkZZQkF3WkMxeUVwVjlTWExrSXVVWm9GRWdRNi1rT0x2UTlYN2s2RkFnb2w4N0J0eGtOQ2EzSjVWVVpnVnZvRzV5TG9LWW9neGlDUGZHSXdIb0FNOGtpaUhYUmRpcEduZDZUcG9sVFloQi1Tbm9KN2pWQWxYbHYtRk1Pa3c?oc=5) | - | 데일리안 |
| 🔴회계신호 | IT | 두나무 | [‘445억 해킹’ 두나무 제재 돌입…금감원, 감사의견서 발송 - 데일리안](https://news.google.com/rss/articles/CBMigwJBVV95cUxQdjlHNElLRGJXMFBlQ2RTM3pDM1FJbTk1LTJrQ3lUbkdMQlI5Y2JNTjQwcmRST3A4RXlPeXlRanJpdFBKbXh4Z3JyWGk3QWxqY2ktLThTRDk3V0pTT3hua1JWV1NoRW4yMUctUXNNT2JMbkF2Tm1qVXl2YkNEeWUwSXhKemkwenhFbWsxbEUwb3pGa0hJR1N3U29JZVhhakFXVkxSRjZta1puN1ZKeTA2VW5ma3Nqa1JCYnhtd00tUXIyRGJGdm5TNGxBaTdaaEhtTFpkczRVSnAtY3hWaDRNNnZvc1RfZVZlZjV4enhvYUtXYkFrZllDZjd3QWVRMWhGYkg4?oc=5) | - | 데일리안 |
| 🔴회계신호 | IT | 두나무 | [두나무, 美 회계기준 검토...美 증시 상장 유력 - 생생비즈플러스](https://news.google.com/rss/articles/CBMibEFVX3lxTE5faHRoa0I5NzRIMDYyeGVObHRGczZ0emxfaVR6YjNVdVVvbjh2MTBBckJLQlVaVzd1dEs5QkZTbHJORDRHMzJGaU5DUDJqQzMxVjBUQlhjOEQyNUlfV0YtdFlqRHFHZTd4VFUxag?oc=5) | - | 생생비즈플러스 |
| 🔴회계신호 | IT | 더존비즈온 | [AI 거래관계망 신용평가 모형, 재무제표 한계 넘는다 - 전자신문](https://news.google.com/rss/articles/CBMiTkFVX3lxTFAyTXpadGpRZkN6M090ZElpTDFqQ1FHZEZnUERfcW43V1JQR2FGX0E0emRyNTFKZjB1V2tPWjJtQXJZa0M4WWFPOTNnTGxiQQ?oc=5) | - | 전자신문 |
| 🔵회계이슈 | 게임 | 크래프톤 | [크래프톤, M&A로 무형자산 6562억→1조8628억…성과 시험대 - 마이데](https://news.google.com/rss/articles/CBMiYEFVX3lxTE9EME14WWNpRi1UbFdsOUtHdDNsT2lZZ1hCQVpMZW4zWThESjR4TE1ka0NfNER1V2ZPSnhkbkpsbW95bmhTVjg5WUNBNmpZZVh0NVI3SzJwRzVic00tVFdURA?oc=5) | intangible-assets | 마이데일리 |
| 🔵회계이슈 | 엔터 | 하이브 | [하이브, 역대 최대 실적에도 M&A는 ‘마이너스’… 1조원대 영업권도 부담 ](https://news.google.com/rss/articles/CBMicEFVX3lxTE1EclZkd2RpcVphX0ZoLUh2SHpodTZEZlBUazZxVTVfSWlXcWNQbXJKOHF0MUQ1MVcxc2puQlVOUV9zUjZlZDIzOEg2MmRFSmYyZ0V3cWlLaEtOSlV4QVA4NTRBUEgzVGNzX01BTnBXbW3SAXRBVV95cUxQNFZxR3lGNmx5Z0FHVlVOZjdEd0N2Yk1jaVNLem5zMHJWWmhpcFE0N1F3b3BZTXNyZTRIeU1CS0VNbGJ1cWdQWDZuUzM2cHlNWXRxS3NqYmRWalQ1cTJYM2FOWDVDa0hQNkhvd3lVTkI1alczVg?oc=5) | intangible-assets | IT조선 |
| 🔵회계이슈 | 엔터 | 큐브엔터 | [[더벨]큐브엔터 소연, 신곡 '퇴사할게여' 주요 음원차트 1위 - 머니투데이](https://news.google.com/rss/articles/CBMiaEFVX3lxTE5vMURKb1JiaGlzRTNyQXpycVZiMjVUTVFxbEM1WFAzVEdfZGtLRGZyTlFSUDZxdkpDZWZ1NklqNnZVVm1qQ3lVNVV3X2NtRDBPbmZZQ2xDbmY1T1ZWLS1sc0Y1SDF1ZjJK0gFuQVVfeXFMTWR5SUNMblBlb0dSUjRfMU1IbWc5OTNxUG1NaHhMTVVVd3dOZ3RxV0JNQUNOREVqLXMzRzV2Y09wNkV3cVI4QWZkSm82TjhqSWtGZk96Z3B6enFERnUxa01IaUFFdzg1UzNLZHR3UVE?oc=5) | intangible-assets | 머니투데이 |
| 🔵회계이슈 | 미디어 | 스튜디오드래곤 | [[스튜디오드래곤 톺아보기] 판권 상각기준 전격 변경…'수익·비용 매치' 변동](https://news.google.com/rss/articles/CBMijwFBVV95cUxOeWRaSDJiY0JzY0l6SXlzMGtRVmdaYjZncDdubVBfUjlaNldjS081VlZicUM2UXRsXzVKbTZpdVlnb2xRa1JyNnY1cmxEaFNKQUNuZkZqRXppV2pSYW9iMFVsaFhHcHBzRHNZZmVVNm5hMjNtdTE2a3VsT21qam9YYU5uREpJOG1HQmdLR25Xaw?oc=5) | intangible-assets | Naver Blog |
| 🔵회계이슈 | 미디어 | 스튜디오드래곤 | [[스튜디오드래곤 톺아보기] 판권 상각기준 전격 변경…'수익·비용 매치' 변동](https://news.google.com/rss/articles/CBMiT0FVX3lxTE9QU0VkMFAzbnhsQnl6amZPVTZYbUtabUVibF9FbmFlNXpLWnRJa0RneFJSNmE5T08xSGtOVFRGS1lpYzRweHdYSGdrUkhYWms?oc=5) | intangible-assets | 딜사이트 |
| 🔵회계이슈 | IT | 네이버 | [네이버 혜택 더해지니 100만원 할인…. 갤럭시폰 거래액 20배 '껑충' -](https://news.google.com/rss/articles/CBMiYEFVX3lxTE9wV3BHb2kxX00wa3JBUUI5U3kyLXllSDViMFNaYnJfSzVESmRUeloyOUctdENHSms2Tmp4MWhocmJPb0FKdE03bGRmeGc3VzlVZlBTUzdWMV9LRG5RejRhZtIBeEFVX3lxTE1LV1RUSC1LU0J3UTZSU3ZIczRDM1I1YjlFWlY5d083M3Q5N3JoSEVtWHdzZGxxaXVHSHBDSU5aeVYydTJnWWNLeEl1aDl0M1JMa2NSRzZpN0JvVWNDeVNOWldvVzlTU1I1SWIzTFhtbTBrd1ZjUVV1Tg?oc=5) | platform-cases | 뉴시스 |
| 🔵회계이슈 | IT | 네이버 | [팔지도 못하는 형지엘리트株, 손상차손에 상폐 리스크까지 - 톱데일리](https://news.google.com/rss/articles/CBMiUEFVX3lxTE40ODJ6UDEyUnFqUW5UdWs3SkNabmZmUmc1LVhEU056c1hZS1NNYjltMG9nTnFORklHVTlTWGd0Z1hCbVl4UXVoM2tWdHcxWUxh?oc=5) | intangible-assets | 톱데일리 |
| 🔵회계이슈 | IT | 카페24 | [카페24, 2분기 거래액 역대 최대…공격적 투자에 영업익은 27%↓ - 디지](https://news.google.com/rss/articles/CBMiYkFVX3lxTE9zQllFX284RGRhUFBRMnFWdnc4UVNEUXVVMjJsLUpXMnpLZHlMSUFESHBBX0xrTEJMNUNEUnFlRFR6Nl9ydjJyZVJxSFJkNHV1V0tVY2NlUXVPck1fenQ0OW5B?oc=5) | platform-cases | 디지털데일리 |
| 🔵회계이슈 | IT | 야놀자 | [야놀자 상반기 거래액 21조 원, 매출은 14% 늘어 - 플래텀(Platum](https://news.google.com/rss/articles/CBMiSEFVX3lxTE9oLUxuSEtkVnhuYnVzd19uemVJTmUyUHM3aEZwcjM1WUtad0hfM2dVY0ZPYTh0Q2JUZVNBQS1GMTY5cS0zMzhUSA?oc=5) | platform-cases | 플래텀(Platum) |
| 🔵회계이슈 | IT | 다우데이타 | [[단독] 삼성 초기업노조위원장 최승호 조합카드 마일리지 개인귀속 결제액 5억](https://news.google.com/rss/articles/CBMic0FVX3lxTFBmSGVfcWpLTGI5Q0wzellQWEc2LWRoNF9qUnN0SVVCeDNqRXJMRGcwQ21Deks4MW1CSURZUTliaTIxX2JQMXFFdW9PSHV4dWtCMWw3a3J0eWRfS3NsNTJ5cDZiNk9GSUhZWVNFb1gzdExJSHc?oc=5) | platform-cases | 비즈니스포스트 |
| 🔵회계이슈 | IT | 메가존클라우드 | [제주콘텐츠진흥원, AWS·메가존클라우드와 협력…콘텐츠산업 AX 본격화 - 제](https://news.google.com/rss/articles/CBMib0FVX3lxTFBQU1U5NGxtamZtU3h1WFpPVEpQdmUtMHNmV3dkNzB3NV8yS3ZvXzVqM1dqMFM3dXV5VHBvLUVVbnFtWVNUcEFIUUYtbHREYnJGZ3VLNE13aVJGXzZiV2d0bEExOGJoRkVSODNVRjRvaw?oc=5) | industry-structure | 제주도민일보 |
| 🔵회계이슈 | IT | 무신사 | [[분석] 6년 새 17배 뛴 무신사 계약부채… 급증 구간서 두드러진 ‘선수금](https://news.google.com/rss/articles/CBMibkFVX3lxTFBGSW9pVWhhZlVmU0p5ZjkwSENKYUQxbVBabl9ZNi1CT2ZNUS1zQXBDRHhiUHd5YUJQUXo3bFFnTkNsRW5DWFpyLXpqSWNsNzVFQUEwQTljTFFZc1gyRHYtSUNYMHpPVlFqZ21TbnlB0gFyQVVfeXFMT3FJNmFxLVNraEcxdlFTY1FJWXZjdWd5a3ppZTJLSHppUXhuOEZNVlhHTmhhamRmSFpKN2ZWRUdzWE8wSjRSY0lURGVYTURkdHIzTXFjVVdZck5PdlkwSV9OMnV5Nk5WRmp4OS14MzVVcHpB?oc=5) | ifrs15-revenue | 시사프라임 |
| 🔵회계이슈 | IT | 무신사 | [무신사, 일본 거래액 성장세…내년 도쿄에 첫 오프라인 매장 - 서울경제](https://news.google.com/rss/articles/CBMiUkFVX3lxTFB0RndDVmJQcFMyM1ZaR21jZTg3Qk1oTE82Z19HRlJDMW9TWFZIUnM0VHpXbXhoY01rWG5nazFBRTFiMEhQWG04WUVGeHdjVjZhSFHSAVNBVV95cUxNZExCcFVycEZ4SDRrYzh0Xzl6Z2JXX3N0eENTVlZndmJocEN3LThWYlZrMDJkc0gxZG5oX1d1ck1QMlhHbkhUbTR0dHhKb3UzZWhQbw?oc=5) | platform-cases | 서울경제 |
| 🔵회계이슈 | IT | 컬리 | [컬리어스 '파인에비뉴 A동' 매각 자문 완료…누적 거래액 3.2조 돌파 - ](https://news.google.com/rss/articles/CBMickFVX3lxTE5IUlBuUW84Nm5KbnZhbFZBY2ZSMmlReENnR1JhUTZ6c3JIdUhYRVVFSlhWdk1VVVdTQTlPdWRZTVRDandOZnhnTnJGWXAwblBHaG5jUTltcW5aTVF3M3k5RG1UOFZZUUlNY2xvdE0xUVpwQQ?oc=5) | platform-cases | 마켓인 |
| 🔵회계이슈 | IT | 컬리 | [컬리, 김장철 앞두고 포장김치 인기…최근 3개월 거래액 35%↑ - 뉴스1](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBOTUZmMkhRbGNreEVSUlNIWGkzdGJsdHVfeVloOUpIZ0FvcDE4YXhKSGppRFRTMm9OR3F6ai1LNEl0aWc1WEpFQndfSnJ2dEluUVNhODNyZVdBb3BCRkVz?oc=5) | platform-cases | 뉴스1 |
| 🔵회계이슈 | IT | 컬리 | [컬리 포장김치 거래액 35%↑…소용량 수요 ‘쑥’ - 푸드투데이](https://news.google.com/rss/articles/CBMiZkFVX3lxTE1HTE9kWXlGLTVQZ0xNNnozVmpzamk0TVUyeGNKQlhXazlZVmR2c2xLTVhidEJHMm96Wm5MWV9mS1QySXpQbzY2WnRKd2Fvbm5yMGZ4TWpEVDI4cDdZVURES05fNmRzUQ?oc=5) | platform-cases | 푸드투데이 |
| 🔵회계이슈 | IT | 컬리 | [“김장 대신 사먹는다”…컬리 포장김치 거래액 35%↑ - 이투데이](https://news.google.com/rss/articles/CBMiVEFVX3lxTFBZNXhJelJuRzJfZmRvRjFmNzBVZGUxMTQyRFppMjRqZEs4NTZJWWwyZEN5Rl9HejEyTXpjMFJzZUtwdWdIRXhhYkQ5MVpTMzUxT2w4Vw?oc=5) | platform-cases | 이투데이 |
| 🔵회계이슈 | IT | 컬리 | ["김치도 필요한 만큼만" 컬리, 소용량 포장김치 거래액 39%↑ - 뉴시스](https://news.google.com/rss/articles/CBMiYEFVX3lxTE1RZTg0R1A5OVdQN2JBRWppVTIxeElPdm0zX2NPajNFVld4RGpkS1o1S3RlUW5JLTh3Qlo0YnNpbVQ0czFKS1d3YklfY3FpNUQ3dkE4czRzR2NTSXd4OWFhRtIBeEFVX3lxTE1JbDE5SWZxdzFaTzA4MTFvTjF3T2s1N0lBSXNKdmNwM0owSUhOSXhOU1dFOFZrMnlGLUlWX3R4S25teE0tRXRJZ0xBRTl2a09wMC1fRjhMREJvMnBTbmc1cGlwYzNyVnpPTHE3bmpfSWpsX3pTREtYNw?oc=5) | platform-cases | 뉴시스 |
| 🔵회계이슈 | IT | 컬리 | [컬리, 포장김치 거래액 35% 증가...소용량 제품 성장 두드러져 - 팝콘뉴](https://news.google.com/rss/articles/CBMib0FVX3lxTE9pWWtWLVd6M2FFbkJCeXpnNmRzUUhhQUQ1aERJR2l1dkg0aTh3cDhHQ2wtblNuOXprYTZ6N1N5NjFOVmh4VVR1bnNnR2xSYnVwamQzbFNrZUZoZE9HOHBvdzNQOEpFVkhxSEpnYXk3NNIBckFVX3lxTE5PbzlQek5RMUJVOVlPVjdpc3g1ZVdkR3M3dnM3TTN6R2hQUWs1SjBMd0dNVGdJMElqZFE3U19tbDk0TF9lNHlrMzRtUzFWM09ZVVdqWkZTN2s2QUYxTV9GTDZ1VjRfazVRWXJ6VWRxS3FpZw?oc=5) | platform-cases | 팝콘뉴스 |
| 🔵회계이슈 | IT | 컬리 | [컬리, 포장김치 거래액 35%↑…소용량부터 '미쉐린 김치'까지 - 위키리크스](https://news.google.com/rss/articles/CBMicEFVX3lxTFAtQjIxdDlqOVQ5dEtTemd5RzBsTmtETTYxOGNaUVV2R3VoWEV2dFpxZWpQX2tSZVhJMl9sT2JkZGRSWDZ4bndnQUJ5V1NQRHoxLUl3MVo5VFgzVFVTNkluUVdxb2YtTnZ1bWcwV2tQdnU?oc=5) | platform-cases | 위키리크스한국 |
| 일반 | 게임 | 넷마블 | [넷마블넥서스의 AI 코딩 도구 도입기 – 게임 개발팀의 Kiro 도입 및 활](https://news.google.com/rss/articles/CBMid0FVX3lxTE9KSVd3RHZXMTlSV3Z4Q1VDMi1iRVJyUWtxaWRmQ0J1WkdKVkdNaG5oTTZxQnpWcnc1ZkJUWnBhMl9yTGwxRkkxc0s5TlV0UDR0cHF4WUdYLVQ3ZjJVLVBJVDN6TnJhWUpWS000cXpHVFl2Q0Y1cVk4?oc=5) | - | Amazon Web Services (AWS) |
| 일반 | 게임 | 넷마블 | [도쿄게임쇼 찾은 넷마블 방준혁 “지스타 참가, 당연”... 내년 복귀 시사[](https://news.google.com/rss/articles/CBMiTkFVX3lxTE5MV1pXS1RJYjhDSmIydU5KUDVEdUptQmJWNGVYYTFSZUh4TDhzaGoyNkhIRGxocUV5VkNBaGM4aEMxdWkyTkRlMzFuMUhwZw?oc=5) | - | 전자신문 |
| 일반 | 게임 | 넷마블 | [상법 개정 타고 거세진 행동주의… 넷마블 vs 얼라인, 코웨이 지분 매입 경](https://news.google.com/rss/articles/CBMigwFBVV95cUxQZFd3dmVDOUJkSHFJOGx0aG00WTVKeEZzcks0d1JOY3p2TUNxNjAzcHlXT1hLMzBVZ2dfQ29WdnpVSDZKb3h0cXNWSHBCRHZGdUI0YXp4eHN0RnJoZnV6ZWhkdDIyLVA4WWMwNjZhdFoxY2NYNDFWdXVJNkZ3bHZBWF9oYw?oc=5) | - | 조선일보 |
| 일반 | 게임 | 넷마블 | [[클릭! e 게임]넷마블 ‘세븐나이츠 리버스’, 日 애니 ‘귀멸의 칼날’ 협](https://news.google.com/rss/articles/CBMiUEFVX3lxTE9WS2REc2Zjc3JEcEgxd0t4NWVUMmFuRERqcEphZDV1Y2JOQ3RGUUJwaDlmcFdVQVBaeHFmNUEwSGtIVTNNeVVMQnQzT1dxckVR?oc=5) | - | 문화일보 |
| 일반 | 게임 | 넷마블 | [넷마블 방준혁 "지스타 패스 없다…준비 중인 게임이 일본향인 것뿐" - 머니](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE5fY2t1SVBtMnU3dXVmMXdoMmFVN1BRTmJQWUwxWEZLbDUyeGdXU19ERERudjZzZHloWU1ZcV8zUGNtSUlzSkg5aXVnWUZzZHFUMUU5cHg3d1YzVWdYS0dLbjJHeFU0T3PSAWxBVV95cUxOQnFkT045Q0xuTFlnak5tZmlla3M4SlU1d0pSTzM4cmxhejhWNERkQ0dzQzJ4eGFNclNyc0Vkc0JpQjFlamVfTDNIZ1lTMFhYNG5CM05tY0pkbVBpdmwxTGQ2UndmT1Q0bnRRR1o?oc=5) | - | 머니투데이 |
| 일반 | 게임 | 엔씨소프트 | [엔씨소프트, ‘아이온2 글로벌’ 초반 흥행…게임주 재평가 신호탄 되나 - 조](https://news.google.com/rss/articles/CBMiY0FVX3lxTE9lbUwxWUhsWkp3OHBpSHV1WFNrMThRaGpGS3lXcndEMUsxb2VtY2NqLS1TZ0NaS1I3Y0dLVnhRbzlzSFJlUHpfUklScFlEcXl4cVVHc2JnX21ubzcwR0VncE9HWQ?oc=5) | - | 조세금융신문 |
| 일반 | 게임 | 엔씨소프트 | [TGS 시연부터 연내 글로벌 CBT까지… 엔씨 신작 ‘아스오라’, 완성도 높](https://news.google.com/rss/articles/CBMiT0FVX3lxTE9fUEs0UURKem5PMC1IRlBYZWxBNHZXakRKalpnS0MtTGdzZFdoZVpZUEE3eWJqc0QtZHQ5RXFxN0tRRXNiMVVoVmhIU1BGSDg?oc=5) | - | Daum |
| 일반 | 게임 | 엔씨소프트 | [엔씨-MS 맞손, ‘아이온2’ 글로벌 흥행 정조준 - 미주중앙일보](https://news.google.com/rss/articles/CBMiYkFVX3lxTE9hRXhJazhzbUxkQ0dkeHhJZkM3amN3eGhreW5qRVplTFJsY3BiTEhvdFNqNDlTc2VaeWxaQ3BYRUJqMzlKaEhmSmtScG5FNDBuVmNQOW9vMHdWcjRUcDNJdEt3?oc=5) | - | 미주중앙일보 |
| 일반 | 게임 | 엔씨소프트 | [‘아이온2’ 5일 글로벌 출시 … 엔씨 주가 힘받나 - 조선일보](https://news.google.com/rss/articles/CBMigwFBVV95cUxOODZyOGpsRDNsdXpOTF91NExKYzN1WGIyM0wxLVhlbHlobHIxV2JJWmI4bDJORnpCYnBVZlhzbHdOdnRQbjc0OGpvMlhLSGRrSC1TTGpwY0RNUzl0UzR3eEltTXBLX3JtZGU0OFVDb296MUF3UHdKeUV6Z3JVRlhLMzI2VQ?oc=5) | - | 조선일보 |
| 일반 | 게임 | 엔씨소프트 | [‘아이온2’ 글로벌 동접 40만…게임은 긍정, 과금엔 불만 - 디일렉](https://news.google.com/rss/articles/CBMiZkFVX3lxTE5PRnVZRW4wazQ3ODA2U00xaEFMOXFUZTBZQ2RQc1BOSmI4NmxqdWJyNk5FV1VieEI2Z3gyRGpMaE5vOWlSaDlLeGhkUjNFcFZXZGl5TGEtUzYybUtNUEtWNlo2VjJtQQ?oc=5) | - | 디일렉 |
| 일반 | 게임 | 크래프톤 | [한국 게임 매출 1위 넥슨서 크래프톤으로 18년 만에 바뀌나, 이정헌 김창한](https://news.google.com/rss/articles/CBMic0FVX3lxTFBZQkZFTUx3TnpjOEE0TW13R294WHBlbDBBWjNBYml0T1FvWmJmeG1nWnQxbWZfaGhvbEtxREM0UWhKWEVHZjY1MksyRkVYRndHVU4zNFZDdE41MlFoRVdpbUFjNG00UVJNendTVnBNdUxPX0U?oc=5) | - | 비즈니스포스트 |
| 일반 | 게임 | 크래프톤 | [리그 멈추고 SNS 닫혔지만…크래프톤, 베트남 사업 향방은 - 뉴스핌](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBHWTNfNkNxTGJvVGQ1S3RxSl92NU9Od0o1ZHh4dlZQdDN6V3UxRE5mWVNseVBxV2FJdk1KeGJjVGxGay10clhNeGlraFJXZmo3WlZKQThiWEU5bjhI?oc=5) | - | 뉴스핌 |
| 일반 | 게임 | 크래프톤 | [크래프톤 배그 대회 파행 '후폭풍'…주요시장 베트남서 퍼지는 이상기류 - 한](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1ZUDM0c2ctUHlVNUFYMXhObGFJR2E3Z2gyRDFKMVJLX2RPc3ZpeDFrYlV3N05fcW80S1lHc1RNdU9QWGhyZm9OSDN1R2ZxVW5oYU9vb1EyV2VtZw?oc=5) | - | 한국경제 |
| 일반 | 게임 | 크래프톤 | [신작 ‘PUBG: 데드넷’ 첫 클로즈드 베타 테스트 진행 | KRAFTON ](https://news.google.com/rss/articles/CBMiswJBVV95cUxQaGpJMVc4MndsSVBpcVBfSjdONnIzWi02NDRXM1NpVjlHM2s4VUVtdzl3Ri1OTkt3UnY4VkxBMlF4YVRJbFFYejVyOWpzZWM1Yllob29rc2RxVHcyczh2YWhEaTRfNDJmWmZQX0FoWkdaNGNObWZaM2RENUVFRlZUMVlySUxuTHV4S1NSQk44OXdYdENobEpuX0tEM3JjUVZsODl1OEd3MHBpS2l0a2JtRGZCaHVpVFY1NF9nb0k2c3VlYWU0eTdnU0JEdmtpbGJMcVlkOTJlSEVmQWFHSTlPMVMwYzZPWmZ6N3JsVXpJN21WRV9FQldpa0I3OU0tRTdjTlpmZXpyLUtZU1VZVkJwaUFjMmRNY2E2anF2RGhyb3JuSkw3elRPU1pmQ2ExcUY2TWZj?oc=5) | - | 크래프톤 |
| 일반 | 게임 | 크래프톤 | [베트남 선수 '방플' 논란에 PUBG 대회 취소…"재발 방지책 마련"(종합)](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBMS254c0YwZ0c3bFZjOEc3cUJzMExVWU9XUWFlRmlZekxOOVNUNjZVLUh3TkpkUkw0UDJJTmxEWElGcUFGbUh6b05qWklURU9JMjZDUl9kaDZONFHSAWBBVV95cUxQRFRCMGs5TkJ0RXVhNzlab013cTdheHRJeVdrT29HQi13enI4MWhuckRDUEVIRTgyVFV3bWVkTlRaamRSdEF6UUhLb1NZNzc5V25aWnVBenQxXzlqbWpJZUg?oc=5) | - | 연합뉴스 |
| 일반 | 게임 | 펄어비스 | [인턴십 지원자와 함께한 펄어비스 사옥 초청 행사 - Pearl Abyss](https://news.google.com/rss/articles/CBMiZEFVX3lxTE5pbmJ1dkw0dzh4bnplVG8zQ1lNb0dXMnpTV2NjamU5TElyZ1BaanZZbEJDX2EzMjl2dFZzNFNjZXBlQnhGVU8wSXNOUFNIU003LVI1Tm1oRWJtWjBjYTV4LXdkQXg?oc=5) | - | Pearl Abyss |
| 일반 | 게임 | 펄어비스 | [펄어비스 '붉은사막' DLC, 출시일 10월 30일로 조정 - 연합뉴스](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1qMFhqVV9KTXVVTFBkSGlZU3FOdW5QdEhfZDJienRrams1dG9sQjFPazlpSDAzQWJSam5Demo3QnlOdF85MXFTdENXTEdKWnVvcWJQeHVRQU1xX3fSAWBBVV95cUxPREdFbFY2dEROT1pYd0Z2YzFMNG4xUERya1hkX3RXSlU4UTk2WjRUTlFvem5nSGtsU1pXNGJxaEtXRkc5TFVpdjFSTVBpSTBmUDNCbmJWVVZscE81b2ZIeko?oc=5) | - | 연합뉴스 |
| 일반 | 게임 | 펄어비스 | [펄어비스, ‘검은사막’으로 네덜란드서 K-게임 우수성 전파 - 문화일보](https://news.google.com/rss/articles/CBMiUEFVX3lxTE5qYk1lMl9JakxHYmh6a3pxSUZfNVVkazBWV2w1eER5c09VdUdDMWZGTTQ3Yzk0OFAzbkRwZGhrY05CWi1IWEdPcm45X1ZYV0Nw?oc=5) | - | 문화일보 |
| 일반 | 게임 | 펄어비스 | [펄어비스 신규입사자 온보딩 여정 - '첫날의 설렘부터, 2년차의 성장을 향해](https://news.google.com/rss/articles/CBMia0FVX3lxTE1oYlNUcGdSSmg4cFZLRENXMWlPRkoxdFYteDB1YlJRUG1RTGdWeXFxVGhjTVcxcld5c3MxZFk5b3c3a3NQcXNFVjZUc0NQbURSeWNnMWZwbi1RREd4eXo2ZTBBN3hWVWpIenVJ?oc=5) | - | Pearl Abyss |
| 일반 | 게임 | 펄어비스 | [지역사회와 함께하는 펄어비스의 따뜻한 동행​ - Pearl Abyss](https://news.google.com/rss/articles/CBMia0FVX3lxTE1UMExDWmlhSi1GWS1CNHprWHF4MEpZWFoyNEtVQkU5ZVVtUHFIUXV2Sl8zNUY3bllQQy1DZGdJcW1tZXNrczhZMlpVQjdBazd2Uk1yRnBFd0VwUURnWlZ5NmdlT0RJTW1oeXRB?oc=5) | - | Pearl Abyss |

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
