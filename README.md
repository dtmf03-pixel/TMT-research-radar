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
_최종 갱신: 2026-08-06 10:21 KST_

**수집 현황** — DART 공시 169 · 뉴스 328 · 회계법인 리포트 2

### 📄 DART 공시 (회계 이슈 필터)
_종류별: 실적 69 · 📘정기 55 · 🔴정정 23 · 🟡주요사항 22_

| 종류 | 업종 | 기업 | 일자 | 공시 |
|---|---|---|---|---|
| 🔴정정 | 게임 | 더블유게임즈 | 20260724 | [[기재정정]사업보고서 (2025.12)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260724000595) |
| 🔴정정 | 통신 | 에스케이텔레콤 | 20260723 | [[기재정정]타법인주식및출자증권취득결정](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260723801025) |
| 🔴정정 | IT | 엔에이치엔 | 20260710 | [[첨부정정]주요사항보고서(회사합병결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260710000147) |
| 🔴정정 | 게임 | 크래프톤 | 20260630 | [[기재정정]타법인주식및출자증권취득결정](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260630800855) |
| 🔴정정 | 게임 | 위메이드 | 20260630 | [[기재정정]최대주주변경을수반하는주식양수도계약체결](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260630901591) |
| 🔴정정 | 미디어 | 콘텐트리중앙 | 20260630 | [[기재정정]타법인주식및출자증권취득결정](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260630801156) |
| 🔴정정 | 미디어 | 콘텐트리중앙 | 20260630 | [[기재정정]자기전환사채만기전취득결정](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260630801106) |
| 🔴정정 | 미디어 | 콘텐트리중앙 | 20260630 | [[기재정정]주요사항보고서(전환사채권발행결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260630000851) |
| 🔴정정 | 미디어 | 콘텐트리중앙 | 20260615 | [[기재정정]타법인주식및출자증권취득결정](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260615800736) |
| 🔴정정 | 게임 | 네오위즈 | 20260612 | [[첨부정정]주요사항보고서(회사합병결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260612000289) |
| 📘정기 | IT | 당근마켓 | 20260529 | [분기보고서 (2026.03)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260529000128) |
| 📘정기 | IT | 무신사 | 20260527 | [분기보고서 (2026.03)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260527000075) |
| 📘정기 | 게임 | 엔씨소프트 | 20260515 | [분기보고서 (2026.03)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260515002636) |
| 📘정기 | 게임 | 크래프톤 | 20260515 | [분기보고서 (2026.03)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260515002756) |
| 📘정기 | 게임 | 펄어비스 | 20260515 | [분기보고서 (2026.03)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260515002684) |
| 📘정기 | 게임 | 카카오게임즈 | 20260515 | [분기보고서 (2026.03)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260515002470) |
| 📘정기 | 게임 | 웹젠 | 20260515 | [분기보고서 (2026.03)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260515000594) |
| 📘정기 | 게임 | 넵튠 | 20260515 | [분기보고서 (2026.03)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260515000649) |
| 📘정기 | 게임 | 위메이드플레이 | 20260515 | [분기보고서 (2026.03)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260515001430) |
| 📘정기 | 게임 | 컴투스 | 20260515 | [분기보고서 (2026.03)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260515002977) |
| 🟡주요사항 | 게임 | 크래프톤 | 20260729 | [주요사항보고서(자기주식취득결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260729000354) |
| 🟡주요사항 | 통신 | 엘지유플러스 | 20260729 | [주요사항보고서(자기주식취득신탁계약체결결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260729000479) |
| 🟡주요사항 | IT | 비바리퍼블리카 | 20260728 | [주요사항보고서(회사합병결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260728000491) |
| 🟡주요사항 | IT | 네이버 | 20260727 | [주요사항보고서(유상증자결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260727000001) |
| 🟡주요사항 | 게임 | 위메이드 | 20260721 | [주요사항보고서(자기주식처분결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260721000875) |
| 🟡주요사항 | 통신 | 케이티 | 20260714 | [주요사항보고서(자기주식처분결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260714000371) |
| 🟡주요사항 | 통신 | 케이티 | 20260714 | [주요사항보고서(자기주식취득결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260714000368) |
| 🟡주요사항 | IT | 엔에이치엔 | 20260708 | [주요사항보고서(회사합병결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260708000501) |
| 🟡주요사항 | 게임 | 넷마블 | 20260625 | [주요사항보고서(자기주식취득신탁계약해지결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260625000446) |
| 🟡주요사항 | IT | 이스트소프트 | 20260625 | [주요사항보고서(자기주식취득신탁계약체결결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260625000245) |
| 실적 | 미디어 | 엘지헬로비전 | 20260806 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260806800075) |
| 실적 | 통신 | 엘지유플러스 | 20260806 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260806800073) |
| 실적 | 통신 | 엘지유플러스 | 20260806 | [영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260806800069) |
| 실적 | IT | 카카오 | 20260806 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260806800010) |
| 실적 | IT | 카카오 | 20260806 | [영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260806800011) |
| 실적 | 게임 | 넷마블 | 20260805 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260805800477) |
| 실적 | 게임 | 카카오게임즈 | 20260805 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260805900059) |
| 실적 | 엔터 | 에스엠엔터테인먼트 | 20260805 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260805900312) |
| 실적 | 엔터 | 에스엠엔터테인먼트 | 20260805 | [영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260805900311) |
| 실적 | 엔터 | 제이와이피엔터테인먼트 | 20260805 | [결산실적공시예고](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260805900573) |

### 📰 뉴스 모니터링 (🔴 = 감사·재무제표 신호)
_구분: 🔴회계신호 13 · 🔵회계이슈 12 · 일반 303_

| 구분 | 업종 | 기업 | 기사 | 회계토픽 | 출처 |
|---|---|---|---|---|---|
| 🔴회계신호 | 엔터 | 에스엠엔터테인먼트 | [매출 73% 폭락·의견거절 속출…팬덤 환호에 가려진 K-엔터 ‘재무 잔혹사’](https://news.google.com/rss/articles/CBMibEFVX3lxTFBNdU5Mck5wR1lkdHBjaU9GV2laZ3EtZHF5eElXWkZ3SDJERVBXUWV5MlRScE0tdWpWMTltRE9kMmpEYmhOeWx6YTJmZUxKWVgyRms4V0w2a29GM0hOZ0F6a0UybVQ3TThtQmlvUQ?oc=5) | - | 한경매거진&북 |
| 🔴회계신호 | 엔터 | 에스엠엔터테인먼트 | [[재무제표 이야기] 매출은 늘어도, 수익 질 나빠진 카카오..."미래 먹거리](https://news.google.com/rss/articles/CBMibEFVX3lxTE5RZUdDSmVsLXRLOWNKbkowWjdkZkhudUxHaWI2aFNieFF6MDRKOFBaUE5YUGRWVG9HTmZaWVdzbFJVVVN0ZURObGJvWUxaT3NWNkhSM2ZHUjNfdHVJTkRjbzBJOTRRR1lpMjd4cQ?oc=5) | - | 생생비즈플러스 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권투자자들, 금감원에 감리 요구…"회계처리 의문" - 연합뉴스](https://news.google.com/rss/articles/CBMiW0FVX3lxTFB1Ukx0THpTTk1DSVh2VGtQU2hsZTBuZWhlRWhzLUFKNGY0dm1RZkgwdDIxMXdaTzhkTXozUXltRTlOS2VOZ25SdGlfLVY1WVhsYUVfWmMxTERDUmvSAWBBVV95cUxQRDRMM1RQYmYwcGlUY1o2YmZfWTNKQlRDU2JkTmxWNnFlVEs4cTFCOElOR1MyUjhyb0twN18zMkNINldZOE1ZSTNKVVJWdmRDOFZ4S2M2OTVoVHVaWDRHUHo?oc=5) | - | 연합뉴스 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [“돌려막기로 자본잠식 숨겼나”…중앙그룹 채권투자 피해자들, 감리 요구 - 한](https://news.google.com/rss/articles/CBMickFVX3lxTFBDSS1uQk52SXBhb1kycHJkNU5na0w1cmtyUm1hSW5KM2YtQkZWUy1TYlVfT2F5NHhUdElibTdhaExkblFZWExucFBXeVRpM1FkcTNvdm41dHpaODZEVzhScldkQ2FwTnRjZmJWTll0Z3p6dw?oc=5) | - | 한겨레 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권 피해자 대리인단, 금감원에 감리 요청 - 법률신문](https://news.google.com/rss/articles/CBMibkFVX3lxTFB4OEZyLVFxM2lFejNpZm5vRmgwNDAzeWh5TElpVEpxNFhWZ3FJRndLTk5fTF9kWGE0aUdrTjM3S0lCamZ2V3Y4TE03LUNSTmpfTHZsaXROZ1JJeEYzaC1jek9ZRTZudnU2dWRORFdR0gFyQVVfeXFMTlJuUTUzcVYwLTIyMWhZWnFRYVBNc2FPU251QVYyU0V2cXUzU2RvV3RlTS1PMWVXeVNvNElNOTIwWnhXcXRrV1pKdURYZHo5emlVcWR0cC1tc0kxTUlZSVZ0TFBKSGxCUmZDNndnZGg4ZHNR?oc=5) | - | 법률신문 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 투자자들 “회계처리 의문”… 금감원에 감리 요청 - v.daum.n](https://news.google.com/rss/articles/CBMiVEFVX3lxTE1fS1hlUE9VYWpjdnRpb2JiTGxsVjJpUHNDZV9lQ1hmUVBkUDg3SVpBTjdiVG56R0w1OVlKT1VtVS1mbkZRRkkwSUR1cEpCeHFrSXRKRw?oc=5) | - | v.daum.net |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권 투자자 금감원에 감리 요구 - 조선비즈 - biz.chosun](https://news.google.com/rss/articles/CBMigwFBVV95cUxOZ1BZZWVoNlItVU8zZTdWOTBmWVpncDBDUnMyenNPYUhNbWFDRDRlTjZpbzd6MnFxWHhzeWdmb01Jci1QRnN4UU83M0FmcHNTZ21HQmpxSF80WmxIMWRmcldCYmZhZUd4amk0bUtFazJnMVNOZklrZUp2ZjVPb2dFY2xJUdIBlwFBVV95cUxObmZVWHNYUEZEcU9BUUpKQXl1bmNJblA1ZkVvWlZ6bDExdWZkT2JWdFlnR3B0SGdBMWxQVmZrTUdzSlZiQ3FiV1pHU19FZ3M0WHlVMng2dDdpRW1ZUTRnalV3Ri1keE1rOHJVSkpHVUE3Y29jNzltSFNtZ0pOWUQ0OWJHOV9laHY3X2Z4WkdxZktNaHlzTWhn?oc=5) | - | biz.chosun.com |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권투자자들, 금감원에 감리 요구…“회계처리 적정성 의문” - v.](https://news.google.com/rss/articles/CBMiT0FVX3lxTFA3QmJMNkRza3lRTS1HUTd1Yk1MMURqeFVraTVqUHFqTXNOQjk3S1dUMlFPanJ0MTEzNjVZVm0zN0hWY1JuSnA0NmhROTNaNmc?oc=5) | - | v.daum.net |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권투자자들, 금감원에 중앙그룹 5개사 회계 감리 요청 - 아주경제](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9tSk54eUp3YjcxUGlWM2RTWm5IQnVRcGk4dGdNSTlrMW1fNl9zY2xDdmVHblZRQm1YLVZvVF9HS1Z3bzJVT3BoQ2hzcHVxb3lKc3NhaEVsSml5QdIBWEFVX3lxTE9RY253VjVTSEVGVjJRQ1NkdUZqYUxkSnYyWm1iX3MtbUk0Yk53MTMzWkZaOXdpQ0J0NE1PdHBrNWdaMGU4TlFxUVlVNmplR0VXeGRITUdibWo?oc=5) | - | 아주경제 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권투자자 금감원에 회계감리 요구 - 서울경제](https://news.google.com/rss/articles/CBMiUkFVX3lxTE9KeElKUjk1Z0tsTmw2aVdLRXhfZWZmVnY3cUJpT1RfQTItWWxGRjRzcDhMdnhfMVVaYm9GMnE2NVFfZ21oeXZ4VHZqMGVxNUt5THfSAVNBVV95cUxQa0EzYnhRMU15d05Fa2tmSXlQSVY5Zk9wamRSMDMtR1lSTnlhN0Zza2Y2bWtkRWktak1hNzQ2eHFMc2R3LXlqckNlTTdmZER3RWg1Zw?oc=5) | - | 서울경제 |
| 🔴회계신호 | IT | 카카오 | [카카오 노조가 놓친 '새 회계기준 함정'…"내년엔 성과급 0원 될 수도" -](https://news.google.com/rss/articles/CBMiaEFVX3lxTE8yRnFCUUFIUzY3YTR1cDZqdmRVODJWd0pWT3E2SnNFQjBlTlpLZ0ZQQV90cTk3bldhRmdDUm1WVmN6WUZ5aDhrRjlWOXFYZzUwRzJhVktoejFha051VjRCUEVDb2x2UE1u?oc=5) | - | ebn.co.kr |
| 🔴회계신호 | IT | 비바리퍼블리카 | [토스증권, 시각장애인 금융교육 4회 완료…재무제표부터 투자 리스크까지 - E](https://news.google.com/rss/articles/CBMibEFVX3lxTE1TUTREYzVBWGo2eDk2cUdNdU5FUU5oLU0teTBBTTU5V3BFcE1uUWs5X1JJd3pwOGllTXZTc0JWeU9PNVNLZC04elM3QlRxRWRJMmgtZVlzMWJkaGdBeTVMTmttWnVXTU1OUHd6Qw?oc=5) | - | ER 이코노믹리뷰 |
| 🔴회계신호 | IT | 컬리 | [[재무제표 분석 220] 컬리, 정말 재무상황이 좋아지고 있을까? - 네이버](https://news.google.com/rss/articles/CBMihgFBVV95cUxQcmVhZzRtc2tOZFFGZTNSa3I1b25tRHBRb3hXQlBGVGJGbTZoQ3I4cm9iZVJTQ2VVaXZIMGtneVZ0UnlQcTM3RWkzZU44QWh4aTQ5WkVKWjJMR3AyanFkZHA3UlJBNVppTEdVT1M0dklNZi02bUVxOXhyM2xtemp3WG16enZTdw?oc=5) | - | 네이버 프리미엄콘텐츠 |
| 🔵회계이슈 | 게임 | 크래프톤 | [크래프톤, '배그' 의존도 심각…손상차손 7배 급증[더시그널] - 한스경제](https://news.google.com/rss/articles/CBMia0FVX3lxTE9OWUd5cDQ5UkhWUVdNZ3JnaGtjU19sQmkyOGE4TFd0Yi01NWxTQXNQV2sxb0hGN04zNno2b2JsSWJfMlFuUkpEUEg3WWlMT3pHUEY0cXlvckZFeWlkUGJqb195WkRiTUxXcDgw0gFvQVVfeXFMT3VWME1neTMxSElzNGdFRDZxMml6NGVOMVhJU2FxcGNNeTluT1M0Rmc1VzJHX1h4ZVJaaXd6cmRXQ1lvLWxBcG9HUTQwcGRpSjg0OVdDdW5mZEdScGJTNG02WGxEQ0t3UkhEeWVOdWY0?oc=5) | intangible-assets | 한스경제 |
| 🔵회계이슈 | 게임 | 넥슨게임즈 | [[소외된 게임주]⑬ 넥슨게임즈, ‘퍼디’ 효과 사라지고 개발비만 쌓였다 - ](https://news.google.com/rss/articles/CBMiaEFVX3lxTE8zemo1UV9xNW9yNW5RM1FrNlptUnlTNENBSDJfSjZOTVJFdFBSTEZ0aUx6WkJva0h2ajVxZzRQVW9CcXJfdjdQc2c1VHVwN2tTNTNYRF84Snc1dEtpdTNkbm5sUmlPamti0gFsQVVfeXFMTnpXOTQ4SThFWlRGYjJrQ3pRc1BRS3RxSkZQcU91MTdPQ25uRmdlVGRpYkhSNHN3VDVGLUJzaUpZZjBOMlhtd2tjMF9BSE10V3FQaTJfRHNCampybVl4N3N1VTE3aXk1RV9VWmJK?oc=5) | intangible-assets | 블로터 |
| 🔵회계이슈 | 게임 | 위메이드 | ['라이선스 매출' 위메이드, 3개 분기 연속 흑자 달성...1분기 매출 약 ](https://news.google.com/rss/articles/CBMiYkFVX3lxTE9TTV82ekJFb1J1VGpOVE5JYXJBZDA2OE5qLXJFdlBCMW95S1lFZXdzVEpXNWw2Mm4tQlEwanVTRDhyS2xHU1gzLWpxRDY3ZzNfWEJjX2ZqMWx2LTdQUXNfdkhn?oc=5) | intangible-assets | 미주중앙일보 |
| 🔵회계이슈 | 게임 | 시프트업 | [신작 개발비 증가, 시프트업 1분기 영업익 18.1% 감소 - 게임메카](https://news.google.com/rss/articles/CBMiWEFVX3lxTE1FTlBDcHdMSzFLSDdOS09QUGF6MzkyaThmMDJGTjJjLW9DRDFhUVNUWS1QcDNkSFN4aUluZUZ5TzlXMGQ2cE5KM05kWnhwOHZtZDdNTzU3MDbSAVtBVV95cUxNWXI3Yktybld1MlZXeENJcmlmek9LX2lvQWw2ZURXNGZ4ZzJlcktTaDNINXR4RV8xcEx2TE1Hb282cVRVVUxWZ3ExU3Z0eE04elBkbUZRUjEzWXFB?oc=5) | intangible-assets | 게임메카 |
| 🔵회계이슈 | IT | 네이버 | ['1조 영업권' 시험대 오른 왈라팝 - DealSite경제TV](https://news.google.com/rss/articles/CBMiVkFVX3lxTE5YRGpJZnptbVIwOHBNWVRmbmUwR29QQmxIVlltNkFsT1dLdkZYNTBzZFo0bjI2U1dCMWR3UGktckFZM2ZZVFhtaFg0SExUVnoxdUZMLUNn?oc=5) | intangible-assets | DealSite경제TV |
| 🔵회계이슈 | IT | 네이버 | [[네이버 4제] 노크잇 '거래액 급증'·'이지커넥트' 출시·'축구왕 페이펫'](https://news.google.com/rss/articles/CBMib0FVX3lxTE9IWUdDX2d2MHp2bkRhUThRZXd3SkNUcU9VcGxrOFZTMXlYdWEwVkhxb2hTS0Y3MFhHbHAtSXpmODlfaFNWSUgyQklwYmlEZ2JIZzJoTndWTEhmSEl5SlNraVo0RnpaR0R4dGxJWTRMMNIBc0FVX3lxTE5TS1JwblIwWE5mU29QdzdhOW1tTDliYnJoaEk4aFBoXzR3cFRFSC1IcFZmX3FsS1F0TlVPbmNiOEN1NXFRb0QtQlkxUVJYTkhCd0xwU0xTMGtrNVRGb2RDQTFBVEw1ZFZXVzVDQ05NOUIyNzA?oc=5) | platform-cases | 뉴스웍스 |
| 🔵회계이슈 | IT | 카카오 | [업스테이지가 품은 ‘다음’ 평가액…무형자산 1413억 - 서울경제TV](https://news.google.com/rss/articles/CBMiZEFVX3lxTFBfUWJKZUJlbDlMWmxHSjFxZTZhcWJ2UVNkUlltY0tMYVZ5SFZWNF9oRnAzRmNGVlk1eWlaMDJmMmVueEs2SHFHSkZhSXFwVFBWTXA4LTVOYTNZZ3RqQk52a1lic1Q?oc=5) | intangible-assets | 서울경제TV |
| 🔵회계이슈 | IT | 야놀자 | [거래액 9.5조의 ‘그늘’…야놀자, 나스닥 문턱 넘을까 - edaily.co](https://news.google.com/rss/articles/CBMigAFBVV95cUxONjkxaERZU0ZsUGhFYzYydzJ0LWpmZzNvcENPM1N6QjJFU2tUWnlpbkJGb3BQTlZTcW1JdUNFZ1RsNXhkeU9nTkJnTHlvTURQS1kzTDI2MFhwdk9fY05OaE9vbmJNemZBUS1Tc1JtZ3o0b0NLRzNhdU1WX0NqTmNYXw?oc=5) | platform-cases | edaily.co.kr |
| 🔵회계이슈 | IT | 무신사 | [무신사 뷰티, 오프라인 거점 확대로 온라인 거래액 증가 - fetv.co.k](https://news.google.com/rss/articles/CBMiaEFVX3lxTE1rWXN6TW5TMk1Cd1pfQlZHMHNmM1RBRDBFaU84cGM5ZFNwckdtQXUxNjcyVXFVUXRodWo2aXBBbHNkYlMxOFRLZE1iV0tKTk1iZ28wc0hZX1E2czRXS1F3NVBEZmVERmRy?oc=5) | platform-cases | fetv.co.kr |
| 🔵회계이슈 | IT | 무신사 | [무신사 스탠다드 뷰티, 상반기 거래액 2.5배로 '껑충' - 연합뉴스](https://news.google.com/rss/articles/CBMiYEFVX3lxTFBSNC1jb0MxcnFNdTQtNER4bHZhd09UT1pldFR5YXV6bUREenZyM3J5YXFHb2lSdGp6Q1lyTWxoVW8wSlZWclFGZUFMWkZqTTBwb0VHNURDZEZhMmhrSnphSNIBYEFVX3lxTFBSNC1jb0MxcnFNdTQtNER4bHZhd09UT1pldFR5YXV6bUREenZyM3J5YXFHb2lSdGp6Q1lyTWxoVW8wSlZWclFGZUFMWkZqTTBwb0VHNURDZEZhMmhrSnphSA?oc=5) | platform-cases | 연합뉴스 |
| 🔵회계이슈 | IT | 무신사 | [무신사 스탠다드 뷰티, 상반기 거래액 2.5배 급증…“연내 中 시장 진출” ](https://news.google.com/rss/articles/CBMiZEFVX3lxTE1QNjQ3Z2NyekRQQ2VSUGpIRzFCay1YbFNIMnFJTzRxN1FyN2tfRFJSVlVRaFFheGhTUDIwbmtWZHF0WEJRWi1vdFE4cl82OC04bDJxZkRDZ3NxUTFJSTJ4d0VoaTU?oc=5) | platform-cases | 서울경제TV |
| 🔵회계이슈 | IT | 컬리 | [[프리스탁 건강검진] 컬리, 현금창출력 개선 후 리스부채 부담은! - 프리스](https://news.google.com/rss/articles/CBMib0FVX3lxTFBqc1hSX1o2QUd1QVBVS3Zqd0R0R2N6R3dGRk8xRVU0Z244a1VNT1hqU0QwSVBHaTduZ2VfWWlBT1pCYnZGbHpMSUJiNEJBdTloZXhTeXZMY0ZYRnVYV1JKMU9BbVZDNVE3b1d0T1AwWQ?oc=5) | ifrs16-lease | 프리스탁뉴스 |
| 일반 | 게임 | 넷마블 | [넷마블게임박물관, '한국 게임산업 뿌리' PC게임 상설 전시 - 연합뉴스](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5VaTUzZWlxN3Bmc0NPQko3WXJ1TGIzdzZLemlHV0VSYUxTeHdwMW5ZdUNTQlZhbEljTjBnekduNEFNWWNPWlVNczlOTXpOZEY3cElaTHpEVkw3clnSAWBBVV95cUxQcXIwN0VyM280TGFfc08yYVJRbmR3TzdGUXU5UVpySE9EVTJNbVExdTJoQWxyODlvZmlTZGxPMDF1TnNWRzUtbzZ4b1A3am5ZTnFTMHVHLTFwSzZIYTQtX0s?oc=5) | - | 연합뉴스 |
| 일반 | 게임 | 넷마블 | [넷마블, 2분기 영업익 801억원…전년比 21% 감소 | - 연합인포맥스](https://news.google.com/rss/articles/CBMidEFVX3lxTE9nSWNmV0prbFZOOUkxUFNKa1RHWUVUZUNpY2djTzctd3FQUmN5TkhUY0g4aUh4N2lxMnlwUk5tS0Y0YXV3bU5vU2VQN3JjX0xEUTFCVXU2T0ZqS2VEOGNxb09Td3p3VVFIZVdMbXNRdHVGMGUt?oc=5) | - | 연합인포맥스 |
| 일반 | 게임 | 넷마블 | [넷마블, "다작 전략 수정"...올해 신작 5종에서 3종으로 축소 - 디일렉](https://news.google.com/rss/articles/CBMiZkFVX3lxTE9Kc2xoWC1tSW92QWZoNi1Ed2RyVXp3UXVfNkxKV1YyWEpZMzFyOWpXY2xpS3BWRlM1eUozak00YTlnRGpzcUlVbHRaU1ZQREhPX1E4MU1XWmVTcW9OOW9CSlNja19jdw?oc=5) | - | 디일렉 |
| 일반 | 게임 | 넷마블 | [“다작王 타이틀 어디로?”…넷마블에 물었더니 - 에너지경제신문](https://news.google.com/rss/articles/CBMiY0FVX3lxTE53ZkNzaEt5MHVwM2R6TFZreWNXQTA3QU10MW1WUWcxUEc5cTA5NEtnZERmTVc2dThYanZtYy1rOHkxQm5LRVdjZjg3LWZpRFFsemJvTmZyVTdJQ2oxdm9SdDNXTQ?oc=5) | - | 에너지경제신문 |
| 일반 | 게임 | 넷마블 | [“패키지 게임 추억 한눈에”…넷마블게임박물관, PC게임 전시 상설화 - 서울](https://news.google.com/rss/articles/CBMiZEFVX3lxTE9pQXlPdXNHOXpMbENtX2kwOU40dWV4UnJXZkhXcVBMdDA1ZG53bDE0T2xGbkxualZWM0g4RzR0OFJrXzM4RVg0NXpaMEtkUUtwd0pPUlpoT1RiTnM2Y3pUNnFiRGk?oc=5) | - | 서울경제TV |
| 일반 | 게임 | 엔씨소프트 | ["롬, 리니지W 저작권 침해 안해"…엔씨소프트 패소 - v.daum.net](https://news.google.com/rss/articles/CBMiT0FVX3lxTE14Ym9WWjRGR1c2RHhpUENiR3R4SjNoWERMUGFqQmtCdHJoZzByTFRLSEtnZzBSZUg5WTJHUmJyVGJXUV95cmtsSm4wWlhfdkE?oc=5) | - | v.daum.net |
| 일반 | 게임 | 엔씨소프트 | [[단독] 엔씨, 또 명의도용 논란…‘리니지 사태’ 재조명 - 뉴시안](https://news.google.com/rss/articles/CBMiakFVX3lxTE1CTjNnVEd3Snl4TGZlck5PeHg4T3RmTHVnUW1mZDFqUDF5SU8yT25Bc3RObzBNaGNFRVJaNmJpaGpnallwVHBORGNLSVNEcjk2cjdlV1NYZV92alZBUlJ6VmdIQldGdkIwSVHSAW5BVV95cUxQRjJjZ0JtWDhQRURVcDZYYnNray1NTWdVaEI4eDZHUjFFT2ZvalFmeVpqMWhwOW9pVkk4Ml9jU2xPNDU4dFItX1FyVHQzSWZldXc4WUcyTFgyNGlpVDJIaWRwbEFxcEFKV2ZVTlQ5dw?oc=5) | - | 뉴시안 |
| 일반 | 게임 | 엔씨소프트 | [‘호연’ 접은 엔씨소프트, ‘블루 아카이브’ 개발진과 손잡고 서브컬처 재도전](https://news.google.com/rss/articles/CBMiaEFVX3lxTE5ueldJdHk1RkdCNjRaX1A2WFJVQldTVzNmUjVQeGN5cmNoYUhVT1owQ1lQV0NpMXpWMnZYOGVfTk5LbVJZNGNDUC1hZ21ob2VTUnl3UVEwU1IwU3YzbXdidmpFN2FZSGJ0?oc=5) | - | 디잇플러스 |
| 일반 | 게임 | 엔씨소프트 | ['리니지' 제작사 엔씨소프트에 고소당한 유명 게임 유튜버 '영래기', 경찰은](https://news.google.com/rss/articles/CBMia0FVX3lxTE84cjBGbGlrM05KcHJqWFRPNjZIaExNcnZGX0ZPVkRNSkVvOUFVRGgwYzZ1M3UzNWtpSTJvZVZUQnpiT3J3V0o2ZVZpZ0JPS1VmYUkyaFBpNFpWTTlQbU1ySTlyU0d2OTRuWThR0gFvQVVfeXFMTnN6Z0dUUnFoWHZveG5yNDZHcllETDVlVS1iZlphWHY2bzBxZnRRN1JjamFjMXV4Slo4VmRnMlU2dTdrRkRvcXoxV3dMZkxlcjBoS0I4QXUxU1liQnNKdlNSa3NtMC1iN2lNeC1oT05B?oc=5) | - | 펜앤마이크 |
| 일반 | 게임 | 엔씨소프트 | [엔씨소프트, 주요 게임서 여름 테마 이벤트 진행 - 뉴스후플러스](https://news.google.com/rss/articles/CBMibkFVX3lxTE1uZmZsWkl1NkhJLTF0ZmlrMko3aWJvLXFLeVAtRWRWN2FoSFJVT19iRnRtTVh4b1NCS2JQTWtodFR4T09CX2NQT0hsbmpoZWtrbkZ0LXlQZkJ3ODl6Y1F3d1RRb1V6UmY0c3pPVk9R?oc=5) | - | 뉴스후플러스 |
| 일반 | 게임 | 크래프톤 | [넥스트 배그' 찾은 크래프톤…역대 최대 실적 썼다(종합2보) - 연합뉴스](https://news.google.com/rss/articles/CBMiW0FVX3lxTE4xY1ZJdkZFRlcxekJSa2pKM0F2VFdEOVV3WGdlTEZUZkNCTGg5cmFWRWtrdGV0bkczaWFqaUczQ0VUVFIteHQtZEJtM1hDQUgtU1g1S2lteDBkMDTSAWBBVV95cUxPQWxGM3JZWVZSeGs4dm5xSnMwajUwQktWMENkTFhMQUlNVnZIMGN0VmVOUTVqeTBoWlZnVjF4UzNZektRMlJzRW1NbW5nQlZHcmNHM2NLV09pU3JfUXZsTWk?oc=5) | - | 연합뉴스 |
| 일반 | 게임 | 크래프톤 | [크래프톤, 21B 음성 AI 모델 공개… "30B 이하 한국어 성능 1위" ](https://news.google.com/rss/articles/CBMiakFVX3lxTE1Hb0FIa1RpQzFEYk9TMlhxMlkzUXl5cW43Vmh0Sng1TXNlaTB0VDBFUjFyQXlDNkN5UFBOVnlPUHliTWZFb2RIUFNlMUs5bUpHQkwyWTQ2US13aDE2Ty1sSTB4TkN4Ulh3WUE?oc=5) | - | aitimes.com |
| 일반 | 게임 | 크래프톤 | [배틀그라운드 모바일, 한일 대항전 ‘PUBG MOBILE RIVALS CUP](https://news.google.com/rss/articles/CBMitwJBVV95cUxObDR4ajh0cHQwQTFJOXBfaERsdndQZUFSUW1WYkpOcVh6YlJRVVZNS3QxSFBGNFJDd0M4OThScWdKYTRnbzlyMU1UdU5tSkFjQmNjMFlhVG02bHcxejdCNV80Wk8yREdXT0NRdWZzWUVQV0Y2NHd6NEVOcFZYQS0tbWptWjZjOWNDTDVsN2tsMkQybldmdEpua2RCelRQR01NUVdjc0xXZDVOR09oNVQ4M1RDX2hWWGtjelpOckx2OFcxbG5tdVN1Qmw2UUZudTJoMGhkQWctNEV4U0ZLbFFjMVNYdllmU2E3ZTdXd0NIeGFURG5qSDh4UHF5VjJQUjJoT0w0QTVwOFR3eFc1U3J5QjFrOEhmUTZqT0NXVjN4MzRLUUFiQ2ZFbFdla2tWVUd6RkJEa3JzTQ?oc=5) | - | 크래프톤 |
| 일반 | 게임 | 크래프톤 | [크래프톤 배틀그라운드, 커스포지와 글로벌 UGC 콘테스트 개최 - 디일렉](https://news.google.com/rss/articles/CBMiZkFVX3lxTE1WeUI3dnhHYUdzWjRmSFRqTHo2VGpJQUxsWFF4SVRDWXlFUnlLaVBUMWZUUThkLUVhWGVNU1hfOGpKNEd6NEtpRGZ1VllpWVBoQmw5WDhFYld4MVk0VzFvblRFeU1Kdw?oc=5) | - | 디일렉 |
| 일반 | 게임 | 크래프톤 | [‘펍지’ 이어 ‘서브노티카 2’…크래프톤, 게임업계 맏형자리 꿰차나 - 에너](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBhZHpPWTBWaDRSZWFOM3dOUDBXUklYWXZsMDNmM01RQ204TFl4ckk4a3JBTFphdF95VzhoMTdKVk9BYjhLQmd2WUdKU1BoMEEtR2ZzeWJtMzRRdzg?oc=5) | - | 에너지경제신문 |
| 일반 | 게임 | 펄어비스 | [펄어비스 검은사막 모바일, 7월 11일 하이델 연회 앞두고 특별 이벤트 진행](https://news.google.com/rss/articles/CBMiZEFVX3lxTE9DZUJkQVUzUzFUanlSaEtlZ0k4TUNJZTFxMkdoeW1MdjJ0eHpMTi1MaU0yMmNxQ202QXhrM2pGVnFXb3JaazJQcDkyYy1mMXdqRlQ1TEh5LXkySFZkY3dreHdfM3M?oc=5) | - | 펄어비스 공식 홈페이지 |
| 일반 | 게임 | 펄어비스 | [중국인들도 "믿기지 않을 정도"…'한국 대작' 일냈다 - 한국경제](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1PT3l3VUVhUWhnTTYyY0lUdFZnRXF2WHQ0R1VyYUtlLWlkSno0Q1BqZG91UDFoeDJ2cUx2THhfUkdVWlpaUVFuZUl6MVlVaHExT3ZpRjRXUGpnUQ?oc=5) | - | 한국경제 |
| 일반 | 게임 | 펄어비스 | ["중국서도 통했다"…펄어비스 '붉은사막' 최고 게임상 - 비즈워치](https://news.google.com/rss/articles/CBMiakFVX3lxTE10RWp0NWhVemlGYUg0OWlxZUIwN0hwLWVhQm9OcW11amdqQ25sRmVZb04zd3dLYVM1aG9jTUpYX185YWZNeURTZW1STEJzcm85QjEwWVNBRzhqekVBYlB5aGdzVVNPdndhZnc?oc=5) | - | 비즈워치 |
| 일반 | 게임 | 펄어비스 | [펄어비스 '붉은사막', PC·콘솔서 게임 이어서 즐긴다 - 연합뉴스](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9YbmctTjN6YXp2VlV0RE9pYWlUVGhPRHNoaWY5WHkwZDhLLWc0ZXdDVWgzOWFDdHdtb1lxR3FDMzJDOGNtaXZFT1MyTXRHNmY5WkJNTmdubkMyN0XSAWBBVV95cUxPUlg4UDJ2MEdpa0h2MDY3T1RkYnZIdVBWN1d2eUVDTEpXWmJ1TW5ZWXdQMVoxNzdTR05GS1JqcjZWWmtKMHZwYmc4QmNoaV9aZFBlem5hV3lGRDFybk04SUk?oc=5) | - | 연합뉴스 |
| 일반 | 게임 | 펄어비스 | [[주말엔게임]매출 1兆 이어간 크래프톤…엔씨·펄어비스도 '맑음' 기대 - v](https://news.google.com/rss/articles/CBMiT0FVX3lxTE54RVJBYV9pV0ZYSUlLd3dIZHgyTVRoZVpNTE1sekRzbjBhYjFxdi05cTZjWDNUOEg4NEVHQXFsUk1NdHFOczU2QmNBR0dTWFE?oc=5) | - | v.daum.net |

### 🏢 회계법인 산업 리포트
| 법인 | 리포트 |
|---|---|
| 삼정KPMG | [AI가 뒤흔든 콘텐츠 산업의 지형과 성장 전략](https://kpmg.com/kr/ko/insights/eri/2026/issuemonitor-0528.html) |
| EY한영 | [통신사는 어떻게 B2B 성장 전망을 재정의 할 수 있을까요?](https://www.ey.com/ko_kr/insights/telecommunications/reimagining-industry-futures-study-2026) |

<!--RADAR:END-->

---
_본 리포지토리는 학습·포트폴리오 목적의 공개 정보 정리이며, 투자 자문이나 감사 의견이 아닙니다._
