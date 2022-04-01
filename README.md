## Wantreez
 원트리즈 뮤직

### Crawling [[상세내용]](https://github.com/kbjung/Wantreez/tree/main/Crawling)
2022년 경기도 해외 SNS 게시글 정보 수집
+ Blog [code](https://github.com/kbjung/Wantreez/blob/main/Crawling/blog_crawling.ipynb)
  - 게시글 날짜, 제목, 링크 수집
  - 조회수, 좋아요 수, 공유 수, 댓글 수, 팔로워 수 는 '0' 값으로 채운 특성으로 만듬.(없는 정보)
  - 항목별로 수집하여 중복되는 게시글 제거
+ Facebook [code](https://github.com/kbjung/Wantreez/blob/main/Crawling/facebook_crawling.ipynb)
  - 로그인X(⁖2단계 로그인 설정)
  - 게시글 날짜, 내용, 좋아요 수, 공유 수, 댓글 수, 게시글 링크 수집
  - 필요없는 샘플 제거(필요없는 단어 들어간 샘플만)
  - 이슈) 게시글 링크가 외부링크 방식으로 종종 수집됨.(이유 확인중..)
+ Instagram [code](https://github.com/kbjung/Wantreez/blob/main/Crawling/insta_crawling.ipynb)
  - 로그인O(아이디, 비밀번호 입력 방식. 보안상)
  - 게시글 날짜, 내용, 조회수, 좋아요 수, 공유 수, 댓글 수, 팔로워 수, 게시글 링크 수집
+ Weibo [code](https://github.com/kbjung/Wantreez/blob/main/Crawling/weibo_crawling.ipynb)
  - 로그인O(아이디, 비밀번호 입력 방식. 보안상)
  - 게시글 날짜, 내용, 조회수, 좋아요 수, 공유 수, 댓글 수, 팔로워 수, 게시글 링크 수집
  - 이슈) 사이트 접속이 느림 => 사이트 로드 시간 텀을 설정.
+ 경기관광포털 해당 검색어 사진 다운 [code](https://github.com/kbjung/Wantreez/blob/main/Crawling/pic_down/crawling_pic(ggtour).ipynb)
  - 경기관광포털>포토갤러리 : https://ggtour.or.kr/info/board_photo.php?tsort=1&msort=160
+ 국가문화유산 사진 다운 [code](https://github.com/kbjung/Wantreez/blob/main/Crawling/pic_down/crawling_pic(heritage).ipynb)
  - 국가문화유산 : https://www.heritage.go.kr/main/
