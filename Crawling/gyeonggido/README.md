# 💾 경기도 해외 SNS 게시글 데이터 수집  [[상세설명]](https://github.com/kbjung/Wantreez/tree/main/Crawling/gyeonggido#readme)

## 🏆 성과
- 구글 블로그, 페이스북, 인스타그램, 웨이보 게시글 데이터 수집 및 가공 프로그램 완성
- 보고서 작성 시간 1/3로 절약 및 데이터 업데이트 효율 향상
- 게시글용 사진 자동 다운 프로그램 작성으로 업무 효율성 비약적 향상

## 📃 과업 정보
+ 주요 업무 : 업로드 게시글 데이터 수집
+ 기간 : 매주
  - 수행 : 2022.03 ~ 2022.04(약 2개월)
  
## 📌 수행 업무 내용
+ 내용 정리 ✍ [[notion]](https://www.notion.so/SNS-da3d2d48a900455bbd0270df0b338b41)
+ 코드 설명서 📃 [[notion]](https://www.notion.so/5f7b9484d2b14e54b0e4111e6a047ffd)
+ 데이터 수집 및 백업
  - 경기도 공식 해외 소셜 미디어(Google blog, Facebook, Instagram, Weibo) 게시글 데이터 수집
  - 수집한 데이터 xlsx, csv 파일로 저장 및 제공
  - 홍보용 사진 다운
+ 사이트
  - 구글 블로그 [링크](https://www.gyeonggido-korea.com/)
  - 페이스북 [링크](https://www.facebook.com/GyeonggiKorea.en)
  - 인스타그램 [링크](https://www.instagram.com/gyeonggi_korea/)
  - 웨이보 [링크](https://weibo.com/p/1001066011831795/home?from=page_100106&mod=TAB#place)

## 🔧 활용 기술
- 언어 : Python
- IDE : VSCode, Jupyter Notebook
- 라이브러리 : BeautifulSoup, Selenium, Pandas 등

## ⚙ 코드
+ Blog [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/gyeonggido/blog_crawling.ipynb)
  - 게시글 날짜, 제목, 링크 수집
  - 조회수, 좋아요 수, 공유 수, 댓글 수, 팔로워 수 는 '0' 값으로 채운 특성으로 만듬.(없는 정보)
  - 이슈) 항목별로 수집시 중복되는 게시물 수집 => 항목별로 수집하여 중복 제목의 게시물 자료 제거
+ Facebook [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/gyeonggido/facebook_crawling.ipynb)
  - 로그인X(⁖2단계 로그인 설정)
  - 게시글 날짜, 내용, 좋아요 수, 공유 수, 댓글 수, 게시글 링크 수집
  - 필요없는 샘플 제거(필요없는 단어 들어간 샘플만)
  - 이슈) 게시글 링크가 외부링크 방식으로 종종 수집됨.
  - 이슈) 로그인이 안되어 팔로워 수 파악 불가. 2단계 로그인 설정이 되있어 해결 어려움.
  - 이슈) 1천명이상의 좋아요 수는 정확한 수치 파악 어려움 => 표현상 '1천명'은 문자열로 기록.
+ Instagram [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/gyeonggido/insta_crawling.ipynb)
  - 로그인O(아이디, 비밀번호 입력 방식. 보안상)
  - 게시글 날짜, 내용, 조회수, 좋아요 수, 공유 수, 댓글 수, 팔로워 수, 게시글 링크 수집
  - 이슈) 정확한 "조회수, 좋아요 수, 공유 수, 댓글 수" 정보 얻기 어려움 => 로그인 뒤 "인사이트" 페이지에서 수집.
+ Weibo [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/gyeonggido/weibo_crawling.ipynb)
  - 로그인O(아이디, 비밀번호 입력 방식. 보안상)
  - 게시글 날짜, 내용, 조회수, 좋아요 수, 공유 수, 댓글 수, 팔로워 수, 게시글 링크 수집
  - 이슈) 사이트 접속이 느림 => 사이트 로드 시간 텀을 설정.
+ 경기관광포털 사진 다운 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/gyeonggido/crawling_pic(ggtour).ipynb)
  - 경기관광포털 > 포토갤러리(url) : https://ggtour.or.kr/info/board_photo.php?tsort=1&msort=160
  - 검색어 설정하면 해당 검색어 결과 사진 자동 다운
+ 국가문화유산 사진 다운 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/gyeonggido/crawling_pic(heritage).ipynb)
  - 국가문화유산(url) : https://www.heritage.go.kr/main/
  - 검색어 설정하면 해당 검색어 결과 사진 자동 다운
