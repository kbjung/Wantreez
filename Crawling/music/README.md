## 💾 2022년 음원 사이트 Top100 & 소셜 미디어 데이터 수집, 분석, 시각화 [[폴더]](https://github.com/kbjung/Wantreez/tree/main/Crawling/music)
+ 내용 정리 ✍ [[notion]](https://www.notion.so/9b207b18803c4d6ea36e9906ca4777e4)

### 음원 데이터 수집
+ 6개 음원 사이트
  - 실시간 자동(매일 1번 자동 실행) [py](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/00-01.live_music_rank.py)
+ Melon : 실시간 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/live_melon.ipynb) / 실시간 자동 [py](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/live_melon.py) / 과거 주간 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/week_melon.ipynb) / 과거 월간 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/month_melon.ipynb)
+ Genie : 실시간 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/live_genie.ipynb) / 실시간 자동 [py](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/live_genie.py) / 과거 일간 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/day_genie.ipynb) / 과거 주간 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/week_genie.ipynb) / 과거 월간 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/month_genie.ipynb)
+ Flo : 실시간 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/live_flo.ipynb) / 실시간 자동 [py](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/live_flo.py)
+ Vibe : 실시간 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/live_vibe.ipynb) / 실시간 자동 [py](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/live_vibe.py) 
+ Bugs : 실시간 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/live_bugs.ipynb) / 실시간 자동 [py](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/live_bugs.py) / 과거 일간 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/day_bugs.ipynb) / 과거 주간 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/week_bugs.ipynb)
+ Soribada : 실시간 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/live_soribada.ipynb) / 실시간 자동 [py](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/live_soribada.py) / 과거 일간 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/day_soribada.ipynb) / 과거 주간 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/week_soribada.ipynb) / 과거 월간 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/month_soribada.ipynb)

### 리포트 작성 코드(분석, 시각화)
+ 설명서 📃 [[notion]](https://www.notion.so/debe145a50054ac088fb83d767a2ccaa)
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
