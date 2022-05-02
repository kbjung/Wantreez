from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
from datetime import datetime
import os, schedule, time, ctypes
import chromedriver_autoinstaller as ca


def crawling():
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

    df.to_excel(f'\\\\192.168.100.178/d/용역/2022/2022년 음원사재기 관련 모니터링 위탁용역/음원순위_크롤링/live_vibe/{file_name}', index=False, encoding='utf-8')

    print(f"{file_name} 파일 생성 완료")

    msg = ctypes.windll.user32.MessageBoxW(None, f'Vibe 순위 자료 스크래핑 완료.\n{file_name} 생성완료', '알림', 0)

# 일정 시간마다 반복
job = schedule.every().day.at("11:03").do( crawling )

count = 0

# 7번만 반복하도록 설정
while True:
    schedule.run_pending()
    time.sleep(60)

    if count > 7:
        schedule.cancel_job(job)