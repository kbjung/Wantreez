import pandas as pd
from bs4 import BeautifulSoup as bs
import chromedriver_autoinstaller as ca
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from datetime import datetime
import time, os, schedule, ctypes, random

# Flo
def flo_crawling():
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

# Genie
def genie_crawling():
    # 현재 경로 확인
    code_path = os.path.dirname(__file__).replace('\\', '/')

    # 수집한 파일 저장할 폴더 생성
    crawled_folder_path = code_path + '/crawled_data/live_genie'
    os.makedirs(crawled_folder_path, exist_ok=True)

    # make link
    today_date = str(datetime.today().strftime("%Y%m%d"))

    today_hour = str(datetime.today().strftime("%H"))

    link_list = []
    first_link = f'https://www.genie.co.kr/chart/top200?ditc=D&ymd={today_date}&hh={today_hour}&rtm=Y&pg=1'
    second_link = f'https://www.genie.co.kr/chart/top200?ditc=D&ymd={today_date}&hh={today_hour}&rtm=Y&pg=2'
    link_list.append(first_link)
    link_list.append(second_link)

    # 순위 날짜
    today_rank_date = str(datetime.today().strftime("%Y-%m-%d"))

    repeat_rank_date_list = []
    for i in range(100):
        repeat_rank_date_list.append(today_rank_date)

    # rank
    rank_list = []
    for i in range(1, 101):
        rank_list.append(i)

    title_list = []
    artist_list = []
    album_list = []

    for link in link_list:
            
        # 페이지 접속
        headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
        # 지니뮤직 url
        data = requests.get(link, headers=headers)
        # soup : html형식
        soup = bs(data.text, 'lxml')

        # 곡 제목
        song_info = soup.find_all('td', 'info')
        for one in song_info:
            temp = one.find('a', 'title ellipsis').text.strip()
            if '19금' in temp:
                temp = temp[3:].strip()
            title_list.append(temp)

        # 가수
        for one in song_info:
            temp = one.find('a', 'artist ellipsis').text
            artist_list.append(temp)

        # 앨범
        for one in song_info:
            temp = one.find('a', 'albumtitle ellipsis').text
            album_list.append(temp)

        time.sleep( random.uniform(0.5, 0.9) )

    # 데이터 셋으로 만들기
    dict = {'날짜':repeat_rank_date_list, '순위':rank_list, '곡':title_list, '가수':artist_list, '앨범':album_list}
    df = pd.DataFrame(dict)

    # excel 파일로 출력
    today_date = str(datetime.today().strftime("%Y%m%d_%H%M%S"))
    file_name = f'live_genie_{today_date}.xlsx'
    path = crawled_folder_path + '/'
    df.to_excel(path + file_name, index=False, encoding='utf-8')

    print(f"{file_name} 파일 생성 완료")

    msg = ctypes.windll.user32.MessageBoxW(None, f'Genie 순위 자료 스크래핑 완료.\n{file_name} 생성완료', '알림', 0)

# Melon
def melon_crawling():
    # 파일 경로 확인
    code_path = os.path.dirname(__file__).replace('\\', '/')

    # 수집한 파일 저장할 폴더 생성
    crawled_folder_path = code_path + '/crawled_data/live_melon'
    os.makedirs(crawled_folder_path, exist_ok=True)

    # 페이지 접속
    url = 'https://www.melon.com/chart/index.htm'
    headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
    # 지니뮤직 url
    data = requests.get(url, headers=headers)
    # soup : html형식
    soup = bs(data.text, 'lxml')

    # 순위 날짜
    raw_date = soup.find('div', 'calendar_prid mt12')
    rank_date = raw_date.find('span', 'year').text.replace('.', '-')

    repeat_rank_date_list = []
    for i in range(100):
        repeat_rank_date_list.append(rank_date)

    # rank
    rank_list = []
    for i in range(1, 101):
        rank_list.append(i)

    # song title
    titles = soup.find_all('div', 'ellipsis rank01')

    title_list = []
    for one in titles:
        temp = one.find('a').text
        title_list.append(temp)

    # artist
    artists = soup.find_all('div','ellipsis rank02')

    artist_list = []
    for one in artists:
        temp = one.find('a').text
        artist_list.append(temp)

    # album
    albums = soup.find_all('div', 'ellipsis rank03')

    album_list = []
    for one in albums:
        temp = one.find('a').text
        album_list.append(temp)

    # make df
    dict = {'날짜':repeat_rank_date_list, '순위':rank_list, '곡':title_list, '가수':artist_list, '앨범':album_list}
    df = pd.DataFrame(dict)

    # make file
    today_date = datetime.today().strftime("%Y%m%d_%H%M%S")
    file_name = f'live_melon_{today_date}.xlsx'
    path = crawled_folder_path + '/'
    df.to_excel(path + file_name, index=False, encoding='utf-8')

    print(f"{file_name} 파일 생성 완료")
    
    msg = ctypes.windll.user32.MessageBoxW(None, f'Melon 순위 자료 스크래핑 완료.\n{file_name} 생성완료', '알림', 0)

# Vibe
def vibe_crawling():
    # 현재 경로 확인
    code_path = os.path.dirname(__file__).replace('\\', '/')

    # 수집한 파일 저장할 폴더 생성
    crawled_folder_path = code_path + '/crawled_data/live_vibe'
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
    url = 'https://vibe.naver.com/chart/total'
    driver.get(url)
    driver.implicitly_wait(3)
    driver.maximize_window()

    # 정보 수프에 담기
    soup = bs(driver.page_source, 'lxml')

    # driver quit
    driver.quit()

    # 순위 날짜
    rank_date = datetime.today().strftime('%Y-%m-%d')

    repeat_rank_date_list = []
    for i in range(100):
        repeat_rank_date_list.append(rank_date)

    # rank
    rank_list = []
    for i in range(1, 101):
        rank_list.append(i)

    # song_title
    titles = soup.find_all('div', 'title_badge_wrap')

    title_list = []
    for one in titles:
        temp = one.find('a', 'link_text').text
        title_list.append(temp)

    # artist
    artists = soup.find_all('td', 'artist')

    artist_list = []
    for one in artists:
        temp = one.find('a', 'link_artist').text
        artist_list.append(temp)

    # album
    albums = soup.find_all('td', 'album')

    album_list = []
    for one in albums:
        temp = one.find('a', 'link').text
        album_list.append(temp)

    # make df
    dict = {'날짜':repeat_rank_date_list, '순위':rank_list, '곡':title_list, '가수':artist_list, '앨범':album_list}
    df = pd.DataFrame(dict)

    # make excel
    today_date = datetime.today().strftime("%Y%m%d_%H%M%S")
    file_name = f'live_vibe_{today_date}.xlsx'
    path = crawled_folder_path + '/'
    df.to_excel(path + file_name, index=False)

    print(f"{file_name} 파일 생성 완료")

    msg = ctypes.windll.user32.MessageBoxW(None, f'Vibe 순위 자료 스크래핑 완료.\n{file_name} 생성완료', '알림', 0)

# 일정 시간마다 반복
job1 = schedule.every().day.at("11:00").do( flo_crawling )
job2 = schedule.every().day.at("11:02").do( genie_crawling )
job3 = schedule.every().day.at("11:04").do( melon_crawling )
job4 = schedule.every().day.at("11:06").do( vibe_crawling )

count = 0

# 7번만 반복하도록 설정
while True:
    schedule.run_pending()
    time.sleep(60)

    if count > 7:
        schedule.cancel_job(job1)
        schedule.cancel_job(job2)
        schedule.cancel_job(job3)
        schedule.cancel_job(job4)