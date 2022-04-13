from bs4 import BeautifulSoup as bs
import pandas as pd
import time, random, schedule, ctypes, os
from datetime import datetime
import requests

def crawling():
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

# 일정 시간마다 반복
job = schedule.every().day.at("11:01").do( crawling )

count = 0

# 7번만 반복하도록 설정
while True:
    schedule.run_pending()
    time.sleep(60)

    if count > 7:
        schedule.cancel_job(job)