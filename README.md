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
_최종 갱신: 2026-08-10 09:12 KST_

**수집 현황** — DART 공시 174 · 뉴스 328 · 회계법인 리포트 2

### 📄 DART 공시 (회계 이슈 필터)
_종류별: 실적 75 · 📘정기 54 · 🔴정정 24 · 🟡주요사항 21_

| 종류 | 업종 | 기업 | 일자 | 공시 |
|---|---|---|---|---|
| 🔴정정 | 게임 | 넷마블 | 20260807 | [[기재정정]증권발행실적보고서(합병등)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260807000552) |
| 🔴정정 | 게임 | 더블유게임즈 | 20260724 | [[기재정정]사업보고서 (2025.12)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260724000595) |
| 🔴정정 | 통신 | 에스케이텔레콤 | 20260723 | [[기재정정]타법인주식및출자증권취득결정](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260723801025) |
| 🔴정정 | IT | 엔에이치엔 | 20260710 | [[첨부정정]주요사항보고서(회사합병결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260710000147) |
| 🔴정정 | 게임 | 크래프톤 | 20260630 | [[기재정정]타법인주식및출자증권취득결정](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260630800855) |
| 🔴정정 | 게임 | 위메이드 | 20260630 | [[기재정정]최대주주변경을수반하는주식양수도계약체결](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260630901591) |
| 🔴정정 | 미디어 | 콘텐트리중앙 | 20260630 | [[기재정정]타법인주식및출자증권취득결정](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260630801156) |
| 🔴정정 | 미디어 | 콘텐트리중앙 | 20260630 | [[기재정정]자기전환사채만기전취득결정](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260630801106) |
| 🔴정정 | 미디어 | 콘텐트리중앙 | 20260630 | [[기재정정]주요사항보고서(전환사채권발행결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260630000851) |
| 🔴정정 | 미디어 | 콘텐트리중앙 | 20260615 | [[기재정정]타법인주식및출자증권취득결정](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260615800736) |
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
| 🟡주요사항 | 미디어 | 나스미디어 | 20260806 | [주요사항보고서(자기주식취득신탁계약해지결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260806000438) |
| 🟡주요사항 | 게임 | 크래프톤 | 20260729 | [주요사항보고서(자기주식취득결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260729000354) |
| 🟡주요사항 | 통신 | 엘지유플러스 | 20260729 | [주요사항보고서(자기주식취득신탁계약체결결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260729000479) |
| 🟡주요사항 | IT | 비바리퍼블리카 | 20260728 | [주요사항보고서(회사합병결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260728000491) |
| 🟡주요사항 | IT | 네이버 | 20260727 | [주요사항보고서(유상증자결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260727000001) |
| 🟡주요사항 | 게임 | 위메이드 | 20260721 | [주요사항보고서(자기주식처분결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260721000875) |
| 🟡주요사항 | 통신 | 케이티 | 20260714 | [주요사항보고서(자기주식처분결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260714000371) |
| 🟡주요사항 | 통신 | 케이티 | 20260714 | [주요사항보고서(자기주식취득결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260714000368) |
| 🟡주요사항 | IT | 엔에이치엔 | 20260708 | [주요사항보고서(회사합병결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260708000501) |
| 🟡주요사항 | 게임 | 넷마블 | 20260625 | [주요사항보고서(자기주식취득신탁계약해지결정)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260625000446) |
| 실적 | 게임 | 데브시스터즈 | 20260807 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260807900170) |
| 실적 | 엔터 | 와이지엔터테인먼트 | 20260807 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260807900186) |
| 실적 | 미디어 | 인크로스 | 20260807 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260807900113) |
| 실적 | 미디어 | 인크로스 | 20260807 | [영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260807900112) |
| 실적 | IT | 네이버 | 20260807 | [영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260807800028) |
| 실적 | IT | 네이버 | 20260807 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260807800026) |
| 실적 | 게임 | 웹젠 | 20260806 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260806900270) |
| 실적 | 미디어 | 엘지헬로비전 | 20260806 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260806800075) |
| 실적 | 미디어 | 씨제이이엔엠 | 20260806 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260806900165) |
| 실적 | 미디어 | 스튜디오드래곤 | 20260806 | [연결재무제표기준영업(잠정)실적(공정공시)](https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260806900155) |

### 📰 뉴스 모니터링 (🔴 = 감사·재무제표 신호)
_구분: 🔴회계신호 13 · 🔵회계이슈 12 · 일반 303_

| 구분 | 업종 | 기업 | 기사 | 회계토픽 | 출처 |
|---|---|---|---|---|---|
| 🔴회계신호 | 게임 | 카카오게임즈 | [[재무제표 이야기] 매출은 늘어도, 수익 질 나빠진 카카오..."미래 먹거리](https://news.google.com/rss/articles/CBMibEFVX3lxTE5RZUdDSmVsLXRLOWNKbkowWjdkZkhudUxHaWI2aFNieFF6MDRKOFBaUE5YUGRWVG9HTmZaWVdzbFJVVVN0ZURObGJvWUxaT3NWNkhSM2ZHUjNfdHVJTkRjbzBJOTRRR1lpMjd4cQ?oc=5) | - | 생생비즈플러스 |
| 🔴회계신호 | 엔터 | 에스엠엔터테인먼트 | [매출 73% 폭락·의견거절 속출…팬덤 환호에 가려진 K-엔터 ‘재무 잔혹사’](https://news.google.com/rss/articles/CBMibEFVX3lxTFBNdU5Mck5wR1lkdHBjaU9GV2laZ3EtZHF5eElXWkZ3SDJERVBXUWV5MlRScE0tdWpWMTltRE9kMmpEYmhOeWx6YTJmZUxKWVgyRms4V0w2a29GM0hOZ0F6a0UybVQ3TThtQmlvUQ?oc=5) | - | 한경매거진&북 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권 피해자 대리인단, 금감원에 감리 요청 - 법률신문](https://news.google.com/rss/articles/CBMibkFVX3lxTFB4OEZyLVFxM2lFejNpZm5vRmgwNDAzeWh5TElpVEpxNFhWZ3FJRndLTk5fTF9kWGE0aUdrTjM3S0lCamZ2V3Y4TE03LUNSTmpfTHZsaXROZ1JJeEYzaC1jek9ZRTZudnU2dWRORFdR0gFyQVVfeXFMTlJuUTUzcVYwLTIyMWhZWnFRYVBNc2FPU251QVYyU0V2cXUzU2RvV3RlTS1PMWVXeVNvNElNOTIwWnhXcXRrV1pKdURYZHo5emlVcWR0cC1tc0kxTUlZSVZ0TFBKSGxCUmZDNndnZGg4ZHNR?oc=5) | - | 법률신문 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권투자자들, 금감원에 감리 요구…"회계처리 의문" - 연합뉴스](https://news.google.com/rss/articles/CBMiW0FVX3lxTFB1Ukx0THpTTk1DSVh2VGtQU2hsZTBuZWhlRWhzLUFKNGY0dm1RZkgwdDIxMXdaTzhkTXozUXltRTlOS2VOZ25SdGlfLVY1WVhsYUVfWmMxTERDUmvSAWBBVV95cUxQRDRMM1RQYmYwcGlUY1o2YmZfWTNKQlRDU2JkTmxWNnFlVEs4cTFCOElOR1MyUjhyb0twN18zMkNINldZOE1ZSTNKVVJWdmRDOFZ4S2M2OTVoVHVaWDRHUHo?oc=5) | - | 연합뉴스 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [“돌려막기로 자본잠식 숨겼나”…중앙그룹 채권투자 피해자들, 감리 요구 - 한](https://news.google.com/rss/articles/CBMickFVX3lxTFBDSS1uQk52SXBhb1kycHJkNU5na0w1cmtyUm1hSW5KM2YtQkZWUy1TYlVfT2F5NHhUdElibTdhaExkblFZWExucFBXeVRpM1FkcTNvdm41dHpaODZEVzhScldkQ2FwTnRjZmJWTll0Z3p6dw?oc=5) | - | 한겨레 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 투자자들 “회계처리 의문”… 금감원에 감리 요청 - v.daum.n](https://news.google.com/rss/articles/CBMiT0FVX3lxTE92M3UxRHNaUzJ6dXY0MHhBd2tlZnZfRWJ2V0dCYW5LWWRxTVIzRi1jOVBfc1lseEF5MlVYb2ZBRW9jak1SdWljRHpNUTBoWDQ?oc=5) | - | v.daum.net |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권투자자들, 금감원에 감리 요구…“회계처리 적정성 의문” - v.](https://news.google.com/rss/articles/CBMiRkFVX3lxTE1tWExvbGNFa0wzb21HbDBwUGlNY2pybXhhZlhNYVNlTFoyLWVWekgwbF9ZSjBzTzJ4N3g3RzluY3lUU3RFekE?oc=5) | - | v.daum.net |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권투자자들, 금감원에 중앙그룹 5개사 회계 감리 요청 - 아주경제](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9tSk54eUp3YjcxUGlWM2RTWm5IQnVRcGk4dGdNSTlrMW1fNl9zY2xDdmVHblZRQm1YLVZvVF9HS1Z3bzJVT3BoQ2hzcHVxb3lKc3NhaEVsSml5QdIBWEFVX3lxTE9RY253VjVTSEVGVjJRQ1NkdUZqYUxkSnYyWm1iX3MtbUk0Yk53MTMzWkZaOXdpQ0J0NE1PdHBrNWdaMGU4TlFxUVlVNmplR0VXeGRITUdibWo?oc=5) | - | 아주경제 |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권 투자자 금감원에 감리 요구 - 조선비즈 - Chosunbiz](https://news.google.com/rss/articles/CBMigwFBVV95cUxOZ1BZZWVoNlItVU8zZTdWOTBmWVpncDBDUnMyenNPYUhNbWFDRDRlTjZpbzd6MnFxWHhzeWdmb01Jci1QRnN4UU83M0FmcHNTZ21HQmpxSF80WmxIMWRmcldCYmZhZUd4amk0bUtFazJnMVNOZklrZUp2ZjVPb2dFY2xJUdIBlwFBVV95cUxObmZVWHNYUEZEcU9BUUpKQXl1bmNJblA1ZkVvWlZ6bDExdWZkT2JWdFlnR3B0SGdBMWxQVmZrTUdzSlZiQ3FiV1pHU19FZ3M0WHlVMng2dDdpRW1ZUTRnalV3Ri1keE1rOHJVSkpHVUE3Y29jNzltSFNtZ0pOWUQ0OWJHOV9laHY3X2Z4WkdxZktNaHlzTWhn?oc=5) | - | Chosunbiz |
| 🔴회계신호 | 미디어 | 콘텐트리중앙 | [중앙그룹 채권단, 금감원에 회계감리 요청…“자본 분류 적정성 따져야” - e](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1MdEFiRnVVVW9oOVJ0d0RfYlZ2N0tFcWpFcTllR2s0ZVJ5UDRYOVF6UVRzV0lBR1h5dFNERW1ESC1OTTQ0OUtVTG1peFhKVTZqbUtyUmtmM1drRVBMbTMtZWVPa3BEbkk?oc=5) | - | erountv.com |
| 🔴회계신호 | IT | 카카오 | [토스 재무제표 간단 분석 - 브런치](https://news.google.com/rss/articles/CBMiTkFVX3lxTE5ISHpzQXZzNnJmb1A1ZWlFeGlFYzBBTlRhYXBkeFJ1WU1vamtEemhuVjhvaUpFbHp0R01wN051WnRTWDdiZmRXZ0MxeDNPdw?oc=5) | - | 브런치 |
| 🔴회계신호 | IT | 비바리퍼블리카 | [토스증권, 시각장애인 금융교육 4회 완료…재무제표부터 투자 리스크까지 - E](https://news.google.com/rss/articles/CBMibEFVX3lxTE1TUTREYzVBWGo2eDk2cUdNdU5FUU5oLU0teTBBTTU5V3BFcE1uUWs5X1JJd3pwOGllTXZTc0JWeU9PNVNLZC04elM3QlRxRWRJMmgtZVlzMWJkaGdBeTVMTmttWnVXTU1OUHd6Qw?oc=5) | - | ER 이코노믹리뷰 |
| 🔴회계신호 | IT | 컬리 | [[재무제표 분석 220] 컬리, 정말 재무상황이 좋아지고 있을까? - con](https://news.google.com/rss/articles/CBMihgFBVV95cUxQcmVhZzRtc2tOZFFGZTNSa3I1b25tRHBRb3hXQlBGVGJGbTZoQ3I4cm9iZVJTQ2VVaXZIMGtneVZ0UnlQcTM3RWkzZU44QWh4aTQ5WkVKWjJMR3AyanFkZHA3UlJBNVppTEdVT1M0dklNZi02bUVxOXhyM2xtemp3WG16enZTdw?oc=5) | - | contents.premium.naver.com |
| 🔵회계이슈 | 게임 | 넥슨게임즈 | [[소외된 게임주]⑬ 넥슨게임즈, ‘퍼디’ 효과 사라지고 개발비만 쌓였다 - ](https://news.google.com/rss/articles/CBMiaEFVX3lxTE8zemo1UV9xNW9yNW5RM1FrNlptUnlTNENBSDJfSjZOTVJFdFBSTEZ0aUx6WkJva0h2ajVxZzRQVW9CcXJfdjdQc2c1VHVwN2tTNTNYRF84Snc1dEtpdTNkbm5sUmlPamti0gFsQVVfeXFMTnpXOTQ4SThFWlRGYjJrQ3pRc1BRS3RxSkZQcU91MTdPQ25uRmdlVGRpYkhSNHN3VDVGLUJzaUpZZjBOMlhtd2tjMF9BSE10V3FQaTJfRHNCampybVl4N3N1VTE3aXk1RV9VWmJK?oc=5) | intangible-assets | 블로터 |
| 🔵회계이슈 | 게임 | 위메이드 | [위메이드, 1분기 영업익 85억 '흑자전환'…"라이선스 매출 영향" - 데일](https://news.google.com/rss/articles/CBMigwJBVV95cUxQY2xrQXZUZU44TERLVmg5ZThocWVjNVhSUUFVcDJfaGllU2ZlVzRESy1rU1BJMmJVNFVEeS1SY3d0OFk2U1VHLUtBVlJ3ZnZHUEdQUm9icm41SFRadWpPLTJXVkN0QlBMWVVCeU9rNkw3Z2gza2JTeHZDc09pa1B2YU5pSlVnaTdNWVZ4V2cxS2xxNmt2ZVNBN3UxMl9hRkVRTUJ0TnpDNkx3TVNMWUJmbzdzemEwLXhaOWVZTTZzTWJoS2huRU82c0FxTXVwRUhlal94XzkxanI5WXNUbnotMmhJNkdKQ0daQ3Fra2NwelBua2hUMjFZRGxNTHdySGw1X2pz?oc=5) | intangible-assets | 데일리안 |
| 🔵회계이슈 | 엔터 | 드림어스컴퍼니 | [비마이프렌즈, 2분기 흑자…자회사 시너지 더한 '팬덤 밸류체인' 안착 - 뉴](https://news.google.com/rss/articles/CBMiZkFVX3lxTE9jaTh6aC1uQXlpR1FRcm1IN0pFci1SNmpaUEhMVlpoYl8yZk5vMHNxRGdfbkpvYi1GbFJEMGVyNGwyUVVXdENpS0tfWDFoZGdLUnhLcTVvZVR0M1M1VzQ1VHNybnAwQQ?oc=5) | industry-structure | 뉴스컬처 |
| 🔵회계이슈 | IT | 네이버 | [[네이버 4제] 노크잇 '거래액 급증'·'이지커넥트' 출시·'축구왕 페이펫'](https://news.google.com/rss/articles/CBMib0FVX3lxTE9IWUdDX2d2MHp2bkRhUThRZXd3SkNUcU9VcGxrOFZTMXlYdWEwVkhxb2hTS0Y3MFhHbHAtSXpmODlfaFNWSUgyQklwYmlEZ2JIZzJoTndWTEhmSEl5SlNraVo0RnpaR0R4dGxJWTRMMNIBc0FVX3lxTE5TS1JwblIwWE5mU29QdzdhOW1tTDliYnJoaEk4aFBoXzR3cFRFSC1IcFZmX3FsS1F0TlVPbmNiOEN1NXFRb0QtQlkxUVJYTkhCd0xwU0xTMGtrNVRGb2RDQTFBVEw1ZFZXVzVDQ05NOUIyNzA?oc=5) | platform-cases | 뉴스웍스 |
| 🔵회계이슈 | IT | 네이버 | [[핀포인트] [네이버] '1조 영업권' 시험대 오른 왈라팝 - 네이트](https://news.google.com/rss/articles/CBMiU0FVX3lxTE5wZHgtQy1XclFSak9sTjNsTm9KaVk3QnRUTUVYR2lBUlhNRWwwdE5hM0VVbU1HdWk0Z0xSS3BLbEczc2FoYVl2M2xldW0tR1ZLRnRz?oc=5) | intangible-assets | 네이트 |
| 🔵회계이슈 | IT | 카카오 | [타파스 영업권 '증발'했지만 흑자전환…카카오엔터의 반전 - 블로터](https://news.google.com/rss/articles/CBMiaEFVX3lxTE9xRlNYeExOOHgzSWlGQnlHRHRYQzdKcUZqNEQ5bWlmbzU4OXptYVVGenhsRHJ3VEcxT1RvT19USWx5cWRhNnJKdzhuQlJwSktDT3JrMVlIMXk1WER2MzkxVXVORzZsZ0pN0gFsQVVfeXFMT3IzcGlkYkRHMXVmRVBiX1hKNzF0Nk83VndRZ3Fnc1NsYTQzQTUzS191TVlDSkluMWFJeHJjT25vUHhFd1ZwUkUtV1JyQ25DdnpUTE1WLWh5TXpHelZCNExtdFhlck53NzhRR3JM?oc=5) | intangible-assets | 블로터 |
| 🔵회계이슈 | IT | 카카오 | [업스테이지가 품은 ‘다음’ 평가액…무형자산 1413억 - 서울경제TV](https://news.google.com/rss/articles/CBMiZEFVX3lxTFBfUWJKZUJlbDlMWmxHSjFxZTZhcWJ2UVNkUlltY0tMYVZ5SFZWNF9oRnAzRmNGVlk1eWlaMDJmMmVueEs2SHFHSkZhSXFwVFBWTXA4LTVOYTNZZ3RqQk52a1lic1Q?oc=5) | intangible-assets | 서울경제TV |
| 🔵회계이슈 | IT | 카페24 | [카페24, 2분기 거래액 역대 최대…공격적 투자에 영업익은 27%↓ - 네이](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1SY3RuZjZ0OWprU2VYeWtSbHRSaDUxLV9TTGF5M1VObXBfRTJybjJTRmNGLU5mX2d3VEtWMTdUWXlpelh1UkJyaGtLRF9sV21VX1h3?oc=5) | platform-cases | 네이트 |
| 🔵회계이슈 | IT | 카페24 | [식품·뷰티, D2C 성장 견인…카페24 "상반기 거래액 증가세 지속" - 신](https://news.google.com/rss/articles/CBMicEFVX3lxTE1UNVp6X25IWFFWZHI5cnI5cDNuZkdBLXdQYzVYOUh2QnB0cGkwLVYzM1N6VjFUdTFqZFdtT09tbmlDMEZaaml4X3BJVy1OcVl6NjJtUmtIQUZtZDRpRDFYNGxXTGdZVzVUeHVtT01hRXU?oc=5) | platform-cases | 신아일보 |
| 🔵회계이슈 | IT | 무신사 | [무신사 뷰티, 오프라인 거점 확대로 온라인 거래액 증가 - fetv.co.k](https://news.google.com/rss/articles/CBMiaEFVX3lxTE1rWXN6TW5TMk1Cd1pfQlZHMHNmM1RBRDBFaU84cGM5ZFNwckdtQXUxNjcyVXFVUXRodWo2aXBBbHNkYlMxOFRLZE1iV0tKTk1iZ28wc0hZX1E2czRXS1F3NVBEZmVERmRy?oc=5) | platform-cases | fetv.co.kr |
| 🔵회계이슈 | IT | 무신사 | [무신사, 패션 넘어 화장품도 통했다...상반기 거래액 2.5배↑ - 아주경제](https://news.google.com/rss/articles/CBMiWkFVX3lxTFBTM1hUVWxQUDVBQjNiNWNSVjluRUZFeTlRSXZlazYzR0FXRldWWTltdWNSTFh5b3R3RV9jYy02enBEWE90T2xDeWtkV2x6Z1F3YWd4TGFtS1YyQdIBWEFVX3lxTE5IWkZRYlNuUnd1SEMtcUxHa3N5SUZrRGtsV1cyV1ZZUjc0cFk1SUhfZFRKVHVFM3NrRl9LM0l2dGpzOHZ1azFGQlR0MGxubkRiQTBvbTF4bEY?oc=5) | platform-cases | 아주경제 |
| 🔵회계이슈 | IT | 컬리 | [[프리스탁 건강검진] 컬리, 현금창출력 개선 후 리스부채 부담은! - 프리스](https://news.google.com/rss/articles/CBMib0FVX3lxTFBqc1hSX1o2QUd1QVBVS3Zqd0R0R2N6R3dGRk8xRVU0Z244a1VNT1hqU0QwSVBHaTduZ2VfWWlBT1pCYnZGbHpMSUJiNEJBdTloZXhTeXZMY0ZYRnVYV1JKMU9BbVZDNVE3b1d0T1AwWQ?oc=5) | ifrs16-lease | 프리스탁뉴스 |
| 일반 | 게임 | 넷마블 | [넷마블게임박물관, '한국 게임산업 뿌리' PC게임 상설 전시 - 연합뉴스](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5VaTUzZWlxN3Bmc0NPQko3WXJ1TGIzdzZLemlHV0VSYUxTeHdwMW5ZdUNTQlZhbEljTjBnekduNEFNWWNPWlVNczlOTXpOZEY3cElaTHpEVkw3clnSAWBBVV95cUxQcXIwN0VyM280TGFfc08yYVJRbmR3TzdGUXU5UVpySE9EVTJNbVExdTJoQWxyODlvZmlTZGxPMDF1TnNWRzUtbzZ4b1A3am5ZTnFTMHVHLTFwSzZIYTQtX0s?oc=5) | - | 연합뉴스 |
| 일반 | 게임 | 넷마블 | [넷마블, "다작 전략 수정"...올해 신작 5종에서 3종으로 축소 - 디일렉](https://news.google.com/rss/articles/CBMiZkFVX3lxTE9Kc2xoWC1tSW92QWZoNi1Ed2RyVXp3UXVfNkxKV1YyWEpZMzFyOWpXY2xpS3BWRlM1eUozak00YTlnRGpzcUlVbHRaU1ZQREhPX1E4MU1XWmVTcW9OOW9CSlNja19jdw?oc=5) | - | 디일렉 |
| 일반 | 게임 | 넷마블 | [넷마블, 2분기 영업익 801억원…전년比 21% 감소 - 연합인포맥스](https://news.google.com/rss/articles/CBMicEFVX3lxTE1LSHhmbm5OUk1QTTdLemVSaGF1SGtxXy05Z1NaM3F2VFA2aXdQQU4yZy1fRkhBUXlpSUpuclB2WTVpYjBpRG9mOC1wbG5OLV84MmZfbDBXQUhHaEpBUVhnOUdkdUVoOHhIdURxRzVfMzU?oc=5) | - | 연합인포맥스 |
| 일반 | 게임 | 넷마블 | [넷마블, 신작 힘줬더니…수익성 오히려 악화 - 비즈워치](https://news.google.com/rss/articles/CBMiakFVX3lxTFBFczRsakVaTUp3c0U3dzltTWxEZWk2U2pCeDFMY01iMjZiazY1Nk8tWlJ1T2U4VnEzZUJLblJBcmhWNWstV0I4cm5URGdYWG1uUV9Nc1pURzRkV05PdUl1MFl5bUVLaU5OQVE?oc=5) | - | 비즈워치 |
| 일반 | 게임 | 넷마블 | [넷마블, 2분기 매출 7492억원, 영업이익 801억원 기록 - 전기신문](https://news.google.com/rss/articles/CBMibEFVX3lxTE1XSEIzRVZ3M2RmUUFFTW1NQktOY0tyVXR0bzdvY1g0Mlk3MDRGYll3S3Y3UGM5bl9uMVZlaW9XOWRJVWRGaTFDeFVWYUVxUmlCSDdMb0lyX3JmR1hLUzJQdElfS0dNYjlFZWFwU9IBcEFVX3lxTE5XcDAxaHJmd0c0TDZLaHNSVE9taXlhZzNMdjJUeUtqVE1UTUxINDJWT1o3b2hpQmx0U0p3UjdWeGx3Yl9QeUR5WWM3YjlhOEhxWkkwbDNRakstRFhIS3JYd2RaemdQcU1aWFY2THBwOEY?oc=5) | - | 전기신문 |
| 일반 | 게임 | 엔씨소프트 | [“롬, 리니지W 저작권 침해 아냐”… 엔씨소프트 소송서 패소 - 조선비즈 -](https://news.google.com/rss/articles/CBMiggFBVV95cUxPY2U4Yk1jZXRwZjlXbEF5WXBwTnl4c2w2LTB3M0pwaHZ6Zl9HYWthWkp5SzEzcEFXSEMwczc3VHpDbzVnTF9heU1QY19oS1dSbkhzR2RLZjRraFlkazNyN0VOdHl0Nll1M3h1ZGZ3eWpJNXprblpXSnVxM0hkTGxYb0V30gGWAUFVX3lxTE9KWVBZVjdIRVc1c3pMM2xwTEkzRlJsdDhBd2tpQTlHcDRyVmdJbGZzOVZPRzFselpxajVTTlFXbmR2d1BPamRFdW05NXRtT1lpMkRja2p6djUtWkNEUUFIOFczQmMzMGJqb3lOWDFDNm5tM3VMbVJkemx3SEJzUkh2MWcyZkpKcm55WHdpdkdMRndiYlhZUQ?oc=5) | - | Chosunbiz |
| 일반 | 게임 | 엔씨소프트 | [한때는 100만원이었다 “12만원 역대급 추락” 난리였는데…결국 살아나는 국](https://news.google.com/rss/articles/CBMiVkFVX3lxTE1RcWxWQkJ4bXlfbFo1S3ltWjRkenlfSloxQmJUWGI0ZE9yb1drUFJZT1lRd3ZaYVE5am5keFgzS1dia245aVVUSGxZbzdJcnVSWEJSODRn?oc=5) | - | 헤럴드경제 |
| 일반 | 게임 | 엔씨소프트 | [엔씨소프트 유튜버 '영래기' 형사고소, 경찰 '혐의없음' 결정 - 마일드경제](https://news.google.com/rss/articles/CBMia0FVX3lxTE9OdHBNa0hvZHAxZUhjQTJ2SWVOSWVoNmp5NWxILUpPYUVoeXNsV0RVRFE5MVh4bHN6eHlvT3pfdEhVSnJGcDBYUnZTMlpKTmNtd3RFYTBDODZYVEhDTlFnSDJkT2VNQWFzRkVZ?oc=5) | - | 마일드경제 |
| 일반 | 게임 | 엔씨소프트 | [‘호연’ 접은 엔씨소프트, ‘블루 아카이브’ 개발진과 손잡고 서브컬처 재도전](https://news.google.com/rss/articles/CBMiaEFVX3lxTE5ueldJdHk1RkdCNjRaX1A2WFJVQldTVzNmUjVQeGN5cmNoYUhVT1owQ1lQV0NpMXpWMnZYOGVfTk5LbVJZNGNDUC1hZ21ob2VTUnl3UVEwU1IwU3YzbXdidmpFN2FZSGJ0?oc=5) | - | 디잇플러스 |
| 일반 | 게임 | 엔씨소프트 | [엔씨, ‘아이온’으로 中·美 동시 공략…글로벌 확장 속도 - 문화일보](https://news.google.com/rss/articles/CBMiUEFVX3lxTFBHUmRySU03WVQ3MkVXOGhfZnlMeFpVUU1rTWRnSnRBNE1Zb1RERTJwNnpNNU5Qc2lscmZSTDg0b2NtUnBZbTZjVGFsWVBSUVpm?oc=5) | - | 문화일보 |
| 일반 | 게임 | 크래프톤 | [크래프톤, 게임 결제 인프라 기업 네온커머스에 투자 - 연합뉴스](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9wcFpST1MyN3FVQmp1VEtCc3Rqbk5BbGNvRXR5T2FQMGJNNWl6NU80MFg4aWVrWXI5d0I3eDJZU1VMYU1DbWd5VUg3ME5jd3Fwa3I3UkQ0X3JMUVnSAWBBVV95cUxPYjBsN3BWTl9Ib2hKMV8yTjg0REVvbmI3dFF1by03bjdLbTNGQVB4c282ODJuVDNIellTMUlmSzVtU1Y0ZERBUXRJek5TeEpIS0Q2QWhScUN2NG5sQ0xmeW0?oc=5) | - | 연합뉴스 |
| 일반 | 게임 | 크래프톤 | [실적 호조에도 목마른 크래프톤, '넥스트 배그' 찾을까 - 비즈워치](https://news.google.com/rss/articles/CBMiakFVX3lxTE9FVjZreklaWjNEanhNRmNPRlFoRWtPZk9QMEhiWURIdmY4cHdoTGRWNVk3S2ZqamVvYXRrZVROLWE5T0NxT0E1eFVFVW9CN05HLXViZVdBNjdnYzlzLThUYzNqbTIzLUJfanc?oc=5) | - | 비즈워치 |
| 일반 | 게임 | 크래프톤 | [크래프톤, PUBG·서브노티카2 흥행에 상반기 역대 최고 실적 - 조선일보](https://news.google.com/rss/articles/CBMigwFBVV95cUxQUU52cjFvRTZ1RWxMOENTR1N0MTIxUkJSZnNDR1BZam1KSWRTd2MyYkk4OEp2Q1Jaemw0VkxLMDJQSmFwdE55RTlXMmtjRVJCX0MzeHY4RVlNbUpPWWtlVnlUamxuS2RLaDBvNVFXdzFSbTFOSzlhaWt1Y3pfMTNMS1Fycw?oc=5) | - | 조선일보 |
| 일반 | 게임 | 크래프톤 | [크래프톤, 21B 음성 AI 모델 공개… "30B 이하 한국어 성능 1위" ](https://news.google.com/rss/articles/CBMiakFVX3lxTE1Hb0FIa1RpQzFEYk9TMlhxMlkzUXl5cW43Vmh0Sng1TXNlaTB0VDBFUjFyQXlDNkN5UFBOVnlPUHliTWZFb2RIUFNlMUs5bUpHQkwyWTQ2US13aDE2Ty1sSTB4TkN4Ulh3WUE?oc=5) | - | AI타임스 |
| 일반 | 게임 | 크래프톤 | [크래프톤, 자체개발 음성 AI 모델 ‘K2 라온 스피치’ 공개 - 에너지경제](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9uNzBjanAzLWZNUC0zdWMyNTU2Y3Z6SmI0RkxkTXc0eTJnWUpqQkRBbW1DSmo1TU85RUFxMkJQRDZHclh5LU9QNkpfV1VWNzhDbVUxTldkUUsxR1U?oc=5) | - | 에너지경제신문 |
| 일반 | 게임 | 펄어비스 | [[공지사항] Beyond the Abyss: Community Challen](https://news.google.com/rss/articles/CBMif0FVX3lxTFB3RmxacGlnOWV0OWF2clZIZUlTbTJCTDhNNHRxUG83UG5zWTdUWW0wYzhtNVlpM0hkVTNZVElQUzBQS2JOSTRCek1OQllWZTFpQlJ6VXc0VGdQZ3ZvbHFndUhxb1ZURlc3Qnd3UUtCNXd2bm5EZThpLUY3RFNwNGs?oc=5) | - | Pearl Abyss |
| 일반 | 게임 | 펄어비스 | [중국인들도 "믿기지 않을 정도"…'한국 대작' 일냈다 - 한국경제](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1PT3l3VUVhUWhnTTYyY0lUdFZnRXF2WHQ0R1VyYUtlLWlkSno0Q1BqZG91UDFoeDJ2cUx2THhfUkdVWlpaUVFuZUl6MVlVaHExT3ZpRjRXUGpnUQ?oc=5) | - | 한국경제 |
| 일반 | 게임 | 펄어비스 | ["중국서도 통했다"…펄어비스 '붉은사막' 최고 게임상 - 비즈워치](https://news.google.com/rss/articles/CBMiakFVX3lxTE10RWp0NWhVemlGYUg0OWlxZUIwN0hwLWVhQm9OcW11amdqQ25sRmVZb04zd3dLYVM1aG9jTUpYX185YWZNeURTZW1STEJzcm85QjEwWVNBRzhqekVBYlB5aGdzVVNPdndhZnc?oc=5) | - | 비즈워치 |
| 일반 | 게임 | 펄어비스 | [펄어비스 '붉은사막', PC·콘솔서 게임 이어서 즐긴다 - 연합뉴스](https://news.google.com/rss/articles/CBMiW0FVX3lxTE9YbmctTjN6YXp2VlV0RE9pYWlUVGhPRHNoaWY5WHkwZDhLLWc0ZXdDVWgzOWFDdHdtb1lxR3FDMzJDOGNtaXZFT1MyTXRHNmY5WkJNTmdubkMyN0XSAWBBVV95cUxPUlg4UDJ2MEdpa0h2MDY3T1RkYnZIdVBWN1d2eUVDTEpXWmJ1TW5ZWXdQMVoxNzdTR05GS1JqcjZWWmtKMHZwYmc4QmNoaV9aZFBlem5hV3lGRDFybk04SUk?oc=5) | - | 연합뉴스 |
| 일반 | 게임 | 펄어비스 | [펄어비스, ‘붉은사막’ 올해 신규 IP 중 스팀 매출 1위 - 조선비즈 - ](https://news.google.com/rss/articles/CBMiggFBVV95cUxNdlpudzc0QVFLNEdEaFk2VW9OM1U1OUZGVnpINW9vMzVldFZScjFEbVc3TTA2NWFBZ3IxNnlnSVRxWXktQ0dKaFRVN3JoUWtCcjR1Sk5lOVg4T3JjbV92akpWbDgyT2FyaGhEbXZwZzJkYjNzdjRpWEJpMjd1T0hpLS130gGWAUFVX3lxTE5VY2xEU2JNSEhONlRlSjlFVHd6TU9LZURSSVdmZHNMZmpJSEFOVU5OSHA0TnZrbXVseUMzXy0xRnItUjhFRkJ1U0QtZ2ZJdEg1c0V0MjJ2UU5nS0pza2hWTHBTaGw4VGk1d0lJYTUyczAweUpKR21ja0RCdHN3UTJHbkhsVkxZMXNTYXlNWWFJbWFabVdPQQ?oc=5) | - | Chosunbiz |

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
