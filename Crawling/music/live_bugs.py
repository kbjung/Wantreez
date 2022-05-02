import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from datetime import datetime
import os, schedule, ctypes

def bugs_crawling():
    # 현재 경로 확인
    code_path = os.path.dirname(__file__).replace('\\', '/')

    # 수집한 파일 저장할 폴더 생성
    crawled_folder_path = code_path + '/crawled_data/live_bugs/'
    os.makedirs(crawled_folder_path, exist_ok=True)

    # 페이지 접속
    url = 'https://music.bugs.co.kr/chart'
    headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
    data = requests.get(url, headers=headers)
    soup = bs(data.text, 'lxml')

    # tr_soup
    tr_soup = soup.find('tbody').find_all('tr')

    # 현재 날짜
    repeat_rank_date_list = []
    today_date = datetime.today().strftime('%Y-%m-%d')
    for i in range(100):
        repeat_rank_date_list.append(today_date)

    # rank
    rank_list = []
    for i in range(1, 101):
        rank_list.append(i)

    # song_title
    song_title_list = []
    for one in tr_soup:
        song_title = one.find('p', 'title').text.strip()
        song_title_list.append(song_title)

    # artist
    artist_list = []
    for one in tr_soup:
        artist = one.find('p', 'artist').text.strip()
        artist_list.append(artist)

    # album
    album_list = []
    for one in tr_soup:
        album = one.find('a', 'album').text
        album_list.append(album)

    # df
    dict = {'날짜':repeat_rank_date_list, '순위':rank_list, '곡':song_title_list, '가수':artist_list, '앨범':album_list}
    df = pd.DataFrame(dict)

    # 파일 생성
    date = str(datetime.today().strftime("%Y%m%d_%H%M%S"))
    file_name = 'live_bugs_' + date + '.xlsx'
    df.to_excel(crawled_folder_path + file_name, index=False, encoding='utf-8')

    df.to_excel(f'\\\\192.168.100.178/d/용역/2022/2022년 음원사재기 관련 모니터링 위탁용역/음원순위_크롤링/live_bugs/{file_name}', index=False, encoding='utf-8')

    print(f"{file_name} 파일 생성 완료")

    msg = ctypes.windll.user32.MessageBoxW(None, f'Bugs 순위 자료 스크래핑 완료.\n{file_name} 생성완료', '알림', 0)

# 일정 시간마다 반복
job = schedule.every().day.at("11:08").do( bugs_crawling )