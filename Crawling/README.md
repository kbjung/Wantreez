### 🐈 Crawling [[상세내용]](https://github.com/kbjung/Wantreez/tree/main/Crawling)
#### 💾 2022년 경기도 해외 SNS 게시글 정보 수집 [[폴더]](https://github.com/kbjung/Wantreez/tree/main/Crawling/gyeonggido)
+ To do list 📃[notion](https://www.notion.so/38f59d8d4f474ed4b3a52fad72885683)
+ Blog [code](https://github.com/kbjung/Wantreez/blob/main/Crawling/gyeonggido/blog_crawling.ipynb)
  - 게시글 날짜, 제목, 링크 수집
  - 조회수, 좋아요 수, 공유 수, 댓글 수, 팔로워 수 는 '0' 값으로 채운 특성으로 만듬.(없는 정보)
  - 이슈) 항목별로 수집시 중복되는 게시물 수집 => 항목별로 수집하여 중복 제목의 게시물 자료 제거
+ Facebook [code](https://github.com/kbjung/Wantreez/blob/main/Crawling/gyeonggido/facebook_crawling.ipynb)
  - 로그인X(⁖2단계 로그인 설정)
  - 게시글 날짜, 내용, 좋아요 수, 공유 수, 댓글 수, 게시글 링크 수집
  - 필요없는 샘플 제거(필요없는 단어 들어간 샘플만)
  - 이슈) 게시글 링크가 외부링크 방식으로 종종 수집됨.(이유 확인중..)
  - 이슈) 로그인이 안되어 팔로워 수 파악 불가. 2단계 로그인 설정이 되있어 해결 어려움.
  - 이슈) 1천명이상의 좋아요 수는 정확한 수치 파악 어려움 => 표현상 '1천명'은 문자열로 기록.
+ Instagram [code](https://github.com/kbjung/Wantreez/blob/main/Crawling/gyeonggido/insta_crawling.ipynb)
  - 로그인O(아이디, 비밀번호 입력 방식. 보안상)
  - 게시글 날짜, 내용, 조회수, 좋아요 수, 공유 수, 댓글 수, 팔로워 수, 게시글 링크 수집
  - 이슈) 정확한 "조회수, 좋아요 수, 공유 수, 댓글 수" 정보 얻기 어려움 => 로그인 뒤 "인사이트" 페이지에서 수집.
+ Weibo [code](https://github.com/kbjung/Wantreez/blob/main/Crawling/gyeonggido/weibo_crawling.ipynb)
  - 로그인O(아이디, 비밀번호 입력 방식. 보안상)
  - 게시글 날짜, 내용, 조회수, 좋아요 수, 공유 수, 댓글 수, 팔로워 수, 게시글 링크 수집
  - 이슈) 사이트 접속이 느림 => 사이트 로드 시간 텀을 설정.
+ 경기관광포털 해당 검색어 사진 다운 [code](https://github.com/kbjung/Wantreez/blob/main/Crawling/gyeonggido/crawling_pic(ggtour).ipynb)
  - 경기관광포털 > 포토갤러리 : https://ggtour.or.kr/info/board_photo.php?tsort=1&msort=160
+ 국가문화유산 사진 다운 [code](https://github.com/kbjung/Wantreez/blob/main/Crawling/gyeonggido/crawling_pic(heritage).ipynb)
  - 국가문화유산 : https://www.heritage.go.kr/main/

#### 💾 2022년 음원 사이트 Top100 수집 [[폴더]](https://github.com/kbjung/Wantreez/tree/main/Crawling/music)
+ 내용 정리 ✍[notion](https://www.notion.so/2ca2f19dfdd54028b263e2f41760f602)
+ Melon
  - 실시간 일간 [code](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/live_melon.ipynb)
  - 과거 주간 [code](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/week_melon.ipynb)
  - 과거 월간 [code](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/month_melon.ipynb)
+ Genie
  - 실시간 일간 [code](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/live_genie.ipynb)
  - 과거 일간 [code](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/day_genie.ipynb)
  - 과거 주간 [code](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/week_genie.ipynb)
  - 과거 월간 [code](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/month_genie.ipynb)
+ Flo
  - 실시간 일간 [code](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/live_flo.ipynb)
+ Vibe
  - 실시간 일간 [code](https://github.com/kbjung/Wantreez/blob/main/Crawling/music/live_vibe.ipynb)

#### 💾 인천시 이벤트 댓글 수집 [[폴더]](https://github.com/kbjung/Wantreez/tree/main/Crawling/incheon)
+ 내용 정리 ✍[notion](https://www.notion.so/af8ebd471778439eb7be4b770fda9f94)
+ 네이버 블로그(진행중....⏳)
  - 이벤트 글 테스트 [code](https://github.com/kbjung/Wantreez/blob/main/Crawling/incheon/naver_blog.ipynb)
+ 페이스북(진행중....⏳)
  - 2022.03.29 이벤트 글 테스트[code](https://github.com/kbjung/Wantreez/blob/main/Crawling/incheon/facebook.ipynb)
