from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import os, time, schedule, ctypes
from datetime import datetime

def crawling():
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

# 일정 시간마다 반복
job = schedule.every().day.at("11:02").do( crawling )

count = 0

# 7번만 반복하도록 설정
while True:
    schedule.run_pending()
    time.sleep(60)

    if count > 7:
        schedule.cancel_job(job)