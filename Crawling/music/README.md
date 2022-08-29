# 💾 음원사재기 모니터링 [[상세설명]](https://github.com/kbjung/Wantreez/tree/main/Crawling/music#readme)

## 📃 과업 정보
+ 발주처 : 한국콘텐츠진흥원
+ 주요 업무 : 국내 음원 사재기 방지를 위한 데이터 수집 및 분석
+ 기간
  - 과업 : 7개월(2022.05~2022.12)
  - 수행 : 2개월(2022.04~2022.05)
+ 보고서
  - 주간 보고서 : 매주 금요일 제출
  - 월간 보고서 : 매주 3주 금요일 제출
  - 중간 보고 : 발주처와 일정 조율
  - 최종 보고서 : 과업 종료일 제출

## 📌 수행 업무 내용
+ 수행 내용 정리 ✍ [[notion]](https://www.notion.so/ff85b4ade1b94280819a4ebfbd9a6abf#9b207b18803c4d6ea36e9906ca4777e4)
+ 수행 팀 리더 📢
  - 일정 배분, 데이터 수집&분석 수행 및 검토, 보고서 작성 및 검토
  - 의사소통 및 의견 조율
+ 데이터 수집 & 분석 주요 항목
  - 국내 6개(Bugs, Flo, Genie, Melon, Soribada, Vibe), 해외 1개(Youtube Music), 노래방 사이트 2개(금영, TJ) Top100 음원 데이터 수집.
  - 순위 데이터 자동 수집 프로그램 작성 및 활용
  - 수집한 데이터 백업
  - 음원 순위 변동 분석을 통한 급상승 음원 추출
  - 급상승 음원의 소셜 미디어 관심도 시각화
  - 급상승 음원의 순위 변동과 소셜 미디어 관심도 비교를 통한 순위 급상승 타당성 평가
  - Top100 음원 순위 변동 시각화
  - 신규 진입 음원 데이터 수집 & 기록
  - 노래방 신규 진입 음원의 소셜 미디어 관심도 시각화
+ 보고서
  - 목차 수정 및 작성
  - 수집한 데이터 종합 및 수정
  - 분석 내용 종합 및 작성

## 🏆 성과
- 업무 프로세스 구축
- 국내외 음원 사이트 순위 데이터 자동 수집 프로그램 완성
- 데이터 분석 및 보고서 내용 출력 체계화

## 🔧 활용 기술
+ 언어 : Python
+ IDE : VSCode, Jupyter Notebook
+ 데이터 수집 : Pandas, Selenium, BeutifulSoup, Request 등
+ 분석 및 시각화 : Matplotlib.pyplot, Seaborn 등
+ 실행 파일 제작 : Pyinstaller

## 음원 데이터 수집
+ 6개 음원 사이트
  - 실시간 자동(매일 1번 자동 실행) [py](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/00-01.live_music_rank.py)
+ Melon : 실시간 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/live_melon.ipynb) / 실시간 자동 [py](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/live_melon.py) / 과거 주간 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/week_melon.ipynb) / 과거 월간 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/month_melon.ipynb)
+ Genie : 실시간 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/live_genie.ipynb) / 실시간 자동 [py](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/live_genie.py) / 과거 일간 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/day_genie.ipynb) / 과거 주간 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/week_genie.ipynb) / 과거 월간 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/month_genie.ipynb)
+ Flo : 실시간 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/live_flo.ipynb) / 실시간 자동 [py](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/live_flo.py)
+ Vibe : 실시간 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/live_vibe.ipynb) / 실시간 자동 [py](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/live_vibe.py) 
+ Bugs : 실시간 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/live_bugs.ipynb) / 실시간 자동 [py](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/live_bugs.py) / 과거 일간 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/day_bugs.ipynb) / 과거 주간 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/week_bugs.ipynb)
+ Soribada : 실시간 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/live_soribada.ipynb) / 실시간 자동 [py](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/live_soribada.py) / 과거 일간 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/day_soribada.ipynb) / 과거 주간 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/week_soribada.ipynb) / 과거 월간 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/month_soribada.ipynb)

## 리포트 작성 코드(분석, 시각화)
+ 코드 설명서 📃 [[notion]](https://www.notion.so/debe145a50054ac088fb83d767a2ccaa)
+ 데이터 전처리
  - 01\. 추가된 가수 확인 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/01.new_artist.ipynb)
  - 02\. 수집 데이터에 소속사 추가 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/02.add_agency.ipynb)
  - 03\. 소속사 입력되지않은 음원 확인 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/03.check_agency.ipynb)
+ 분석 및 시각화
  - 04\. 음원 순위 그래프, 급상승 음원, 기획사/소속사별 진입 음원 데이터 저장[ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/04.report.ipynb)
  - 05\. 50위 진입/이탈, 10위 음원 데이터 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/05.Top10%2C50_music.ipynb)
  - 06\. 신규 음원 데이터 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/06.new_title.ipynb)
  - 07\. 노래방 신규 음원 데이터 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/07.new_title_ky%2Ctj.ipynb)
  - 08\. 노래방 신규 음원. 네이버 데이터 랩, 카카오 트랜드, 구글 트랜드 데이터 저장 및 시각화 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/08.karaoke_social_search.ipynb)
  - 09-01\. 급상승음원 네이버 데이터 랩 데이터 저장 및 시각화 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/09-01.outlier_naver_search.ipynb)
  - 09-02\. 급상승음원 카카오 트랜드 데이터 저장 및 시각화 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/09-02.outlier_kakao_search.ipynb)
  - 09-03\. 급상승음원 구글 트랜드 데이터 저장 및 시각화 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/09-03.outlier_google_search.ipynb)
+ 2022년 1-3월
  - 음원 순위 그래프, 급상승음원 데이터 저장 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/month1_3.ipynb)
