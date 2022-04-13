from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
from datetime import datetime
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller as ca
import time, os, schedule, time, ctypes

def crawling():
    # 현재 경로 확인
    code_path = os.path.dirname(__file__).replace('\\', '/')

    # 수집한 파일 저장할 폴더 생성
    crawled_folder_path = code_path + '/crawled_data/live_flo'
    os.makedirs(crawled_folder_path, exist_ok=True)

    # 현재 크롬 버전 확인
    chrome_ver = ca.get_chrome_version().split('.')[0]
    # 크롬 드라이버 확인 및 설치
    try:
        driver = webdriver.Chrome(code_path + f'/{chrome_ver}/' +'chromedriver.exe')
    except:
        ca.install(True)
        driver = webdriver.Chrome(code_path + f'/{chrome_ver}/' +'chromedriver.exe')

    # 페이지 접속
    url = 'https://www.music-flo.com/browse'
    driver.get(url)
    driver.implicitly_wait(3)
    driver.maximize_window()

    # 페이지 스크롤 다운
    # 더보기 버튼 화면상 보여야 클릭 동작 작동함. 화면상에서 페이지 다운으로 더보기 버튼이 보이게 함.
    body = driver.find_element_by_css_selector('body')
    body.send_keys(Keys.PAGE_DOWN)
    driver.implicitly_wait(1)
    time.sleep(2)

    # 더보기 버튼
    more_view_button = driver.find_element_by_xpath('//*[@id="browseRank"]/div[2]/div/button')
    more_view_button.click()
    time.sleep(3)

    # 수프에 담기
    soup = bs(driver.page_source, 'lxml')

    # webdriver quit
    driver.quit()

    # 순위 날짜
    rank_date = datetime.today().strftime('%Y-%m-%d')

    repeat_rank_date_list = []
    for i in range(100):
        repeat_rank_date_list.append(rank_date)

    # song_title
    song_titles = soup.find_all('strong', 'tit__text')

    title_list = []
    for one in song_titles:
        temp = one.text
        title_list.append(temp)

    # artist
    artists = soup.find_all('a', 'last')

    artist_list = []
    for one in artists:
        # temp = eval(one.attrs['data-rake'])['artistId'] # eval : str -> dict 변환 함수
        temp = one.text
        artist_list.append(temp)

    # album
    albums = soup.find_all('p', 'album')

    album_list = []
    for one in albums:
        temp = one.text
        album_list.append(temp)

    # rank
    rank_list = []
    for i in range(1, 101):
        rank_list.append(i)

    # make df
    dict = {'날짜':repeat_rank_date_list, '순위':rank_list, '곡':title_list, '가수': artist_list, '앨범':album_list}
    df = pd.DataFrame(dict)

    # make excel
    today_date = datetime.today().strftime("%Y%m%d_%H%M%S")
    file_name = f'live_flo_{today_date}.xlsx'
    path = crawled_folder_path + '/'
    df.to_excel(path + file_name, index=False, encoding='utf-8')

    print(f"{file_name} 파일 생성 완료")

    msg = ctypes.windll.user32.MessageBoxW(None, f'Flo 순위 자료 스크래핑 완료.\n{file_name} 생성완료', '알림', 0)

# 일정 시간마다 반복
job = schedule.every().day.at("11:00").do( crawling )

count = 0

# 7번만 반복하도록 설정
while True:
    schedule.run_pending()
    time.sleep(60)

    if count > 7:
        schedule.cancel_job(job)