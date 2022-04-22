from bs4 import BeautifulSoup as bs
import pandas as pd
import os, ctypes
from datetime import datetime
from selenium import webdriver
import chromedriver_autoinstaller as ca

def soribada_crawling():
    # 현재 경로 확인
    code_path = os.getcwd().replace('\\', '/')

    # 파일 저장할 폴더 생성
    crawled_folder_path = code_path + '/crawled_data/live_soribada/'
    os.makedirs(crawled_folder_path, exist_ok=True)

    # 현재 크롬 버전 확인
    chrome_ver = ca.get_chrome_version().split('.')[0]

    # 크롬 드라이버 확인 및 설치
    try:
        driver = webdriver.Chrome(code_path + f'/{chrome_ver}/' + 'chromedriver.exe')
    except:
        ca.install(True)
        driver = webdriver.Chrome(code_path + f'/{chrome_ver}/' + 'chromedriver.exe')

    # 페이지 접속
    url = 'https://www.soribada.com/music/chart'
    driver.get(url)
    driver.implicitly_wait(3)
    driver.maximize_window()

    # 수프 담기
    soup = bs(driver.page_source, 'lxml')

    # 리스트
    li_soup = soup.find_all('li', 'listen')
    len(li_soup)

    # 날짜
    rank_date = soup.find('span', 'nowText').text
    rank_date = rank_date.replace('년 ', '-')
    rank_date = rank_date.replace('월 ', '-')
    rank_date = rank_date.replace('일 ', '_')
    rank_date = rank_date.replace('시 ', ':')
    rank_date = rank_date.replace('분', '')

    repeat_rank_date_list = []
    for i in range(100):
        repeat_rank_date_list.append(rank_date)

    # rank
    rank_list = []
    for i in range(1, 101):
        rank_list.append(i)

    song_title_list = []
    for one in li_soup:
        song_title = one.find('span', 'song-title').text
        song_title_list.append(song_title)

    # artist
    artist_list = []
    for one in li_soup:
        try:
            artist = one.find('span', 'link-type2-name artist').find('a').text.strip()
        except:
            artist = one.find('span', 'link-type2-name artist detail_artist').text.strip()
        artist_list.append(artist)


    # album
    album_list = []
    for one in li_soup:
        album = one.find('span', 'link-type2 album-title').text
        album_list.append(album)

    # df
    dict = {'날짜':repeat_rank_date_list, '순위':rank_list, '곡':song_title_list, '가수':artist_list, '앨범':album_list}
    df = pd.DataFrame(dict)

    # make excel
    today_date = datetime.today().strftime("%Y%m%d_%H%M%S")
    date = rank_date.split('_')[0].replace('-', '')
    file_name = f'live_soribada_{date}_{today_date}.xlsx'
    df.to_excel(crawled_folder_path + file_name, index=False)

    print(f"{file_name} 파일 생성 완료")

    msg = ctypes.windll.user32.MessageBoxW(None, f'Soribada 순위 자료 스크래핑 완료.\n{file_name} 생성완료', '알림', 0)

# 일정 시간마다 반복
job = schedule.every().day.at("11:10").do( soribada_crawling )