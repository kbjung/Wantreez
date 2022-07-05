## 💾 인천시 이벤트 댓글 데이터 수집 [[폴더]](https://github.com/kbjung/Wantreez/tree/main/Crawling/incheon)

### 📃 과업 정보
+ 주제 : 이벤트 게시글 댓글 정보 수집
+ 기간 : 비정기적
  - 수행 : 약 2개월(2022.04 ~ 05)
  
### 📌 수행 업무 내용
+ 내용 정리 ✍ [[notion]](https://www.notion.so/3936885a648a4134b5edac352eeb1ad4)
+ 코드 설명서 📃 [[notion]](https://www.notion.so/7aa007e411a64978938757ef4905f3f8)
+ 데이터 수집 및 제공
  - 3개 소셜 미디어(Naver blog, Facebook, Instagram) 이벤트 게시글의 댓글 정보 수집
  - 수집한 데이터 xlsx 파일로 저장 및 제공
+ 사이트
- 네이버 블로그 [링크](https://blog.naver.com/PostList.nhn?blogId=icouncil103&categoryNo=9&from=postList&parentCategoryNo=9)
- 페이스북 [링크](https://www.facebook.com/incheoncouncil/?ref=page_internal)
- 인스타그램 [링크](https://www.instagram.com/icouncil103/)

### 🔧 활용 기술
- 언어 : Python
- IDE : VSCode, Jupyter Notebook
- 라이브러리 : BeautifulSoup, Selenium, Pandas 등

 ### 코드
+ 네이버 블로그
  - 테스트 코드 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/incheon/test_naver_blog.ipynb)
  - 이벤트 글 테스트 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/incheon/naver_blog.ipynb)
+ 페이스북
  - 테스트 코드 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/incheon/test_insta.ipynb)
  - 2022.03.29 이벤트 글 테스트 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/incheon/facebook.ipynb)
+ 인스타그램
  - 테스트 코드 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/incheon/test_naver_blog.ipynb)
  - 2022.02.25 이벤트 글 테스트 [ipynb](https://github.com/kbjung/Wantreez/blob/main/Crawling/incheon/insta.ipynb)
+ ~엑셀 파일 너비 조정~
