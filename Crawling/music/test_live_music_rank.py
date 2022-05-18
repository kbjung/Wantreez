import pandas as pd
from bs4 import BeautifulSoup as bs
import chromedriver_autoinstaller as ca
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import requests
from datetime import datetime
import time, os, schedule, random, ctypes

# 실행 메세지
# msg = ctypes.windll.user32.MessageBoxW(None, '파일 실행.', '알림', 0)

# Flo
def flo_crawling():
    # 현재 경로 확인
    code_path = os.getcwd().replace('\\', '/')

    # 수집한 파일 저장할 폴더 생성
    crawled_folder_path = code_path + '/crawled_data/live_flo/'
    os.makedirs(crawled_folder_path, exist_ok=True)

    # USB error 메세지 발생 해결을 위한 코드
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    # 크롬 드라이버 확인 및 설치
    ca.install(True)
    driver = webdriver.Chrome(options=options)

    # 페이지 접속
    url = 'https://www.music-flo.com/browse'
    driver.get(url)
    driver.implicitly_wait(3)
    driver.maximize_window()

     # 닫기 버튼 클릭
    try:
        close_button = driver.find_element_by_xpath('//*[@id="app"]/div[4]/div[2]/button')
        close_button.click()
    except:
        pass

    # 더보기 버튼
    try:
        more_view_button = driver.find_element_by_xpath('//*[@id="browseRank"]/div[2]/div/button')
        more_view_button.send_keys(Keys.ENTER)
        time.sleep(1)
    except:
        more_view_button = driver.find_element_by_xpath('//*[@id="browseRank"]/div[2]/div/button')
        ActionChains(driver).move_to_element(more_view_button).perform()
        for d in range(4):
            driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
        more_view_button.click()
        time.sleep(1)

    # 수프에 담기
    soup = bs(driver.page_source, 'lxml')

    # webdriver quit
    driver.quit()

    # 사이트 명
    site_name_list = ['Flo' for i in range(100)]

    # 순위 날짜
    rank_date = datetime.today().strftime('%Y-%m-%d')

    repeat_rank_date_list = []
    for i in range(100):
        repeat_rank_date_list.append(rank_date)

    # song_title
    song_titles = soup.find_all('strong', 'tit__text')

    title_list = []
    for one in song_titles:
        temp = one.text.strip()
        title_list.append(temp)

    # artist
    artists = soup.find_all('a', 'last')

    artist_list = []
    for one in artists:
        # temp = eval(one.attrs['data-rake'])['artistId'] # eval : str -> dict 변환 함수
        temp = one.text.strip()
        artist_list.append(temp)

    # album
    albums = soup.find_all('p', 'album')

    album_list = []
    for one in albums:
        temp = one.text.strip()
        album_list.append(temp)

    # rank
    rank_list = []
    for i in range(1, 101):
        rank_list.append(i)

    # make df
    dict = {'사이트':site_name_list, '날짜':repeat_rank_date_list, '순위':rank_list, '곡':title_list, '가수': artist_list, '앨범':album_list}
    df = pd.DataFrame(dict)

    # make excel
    today_date = datetime.today().strftime("%Y%m%d_%H%M%S")
    file_name = f'live_flo_{today_date}.xlsx'
    df.to_excel(crawled_folder_path + file_name, index=False, encoding='utf-8')

    df.to_excel(f'\\\\192.168.100.178/d/용역/2022/2022년 음원사재기 관련 모니터링 위탁용역/음원순위_크롤링/live_flo/{file_name}', index=False, encoding='utf-8')

    print(f"{file_name} 파일 생성 완료")

    # msg = ctypes.windll.user32.MessageBoxW(None, f'Flo 순위 자료 스크래핑 완료.\n{file_name} 생성완료', '알림', 0)

# Genie
def genie_crawling():
    # 현재 경로 확인
    code_path = os.getcwd().replace('\\', '/')
    
    # 수집한 파일 저장할 폴더 생성
    crawled_folder_path = code_path + '/crawled_data/live_genie/'
    os.makedirs(crawled_folder_path, exist_ok=True)

    # make link
    today_date = str(datetime.today().strftime("%Y%m%d"))

    today_hour = str(datetime.today().strftime("%H"))

    link_list = []
    first_link = f'https://www.genie.co.kr/chart/top200?ditc=D&ymd={today_date}&hh={today_hour}&rtm=Y&pg=1'
    second_link = f'https://www.genie.co.kr/chart/top200?ditc=D&ymd={today_date}&hh={today_hour}&rtm=Y&pg=2'
    link_list.append(first_link)
    link_list.append(second_link)

    # 사이트 명
    site_name_list = ['Genie' for i in range(100)]

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
    dict = {'사이트':site_name_list, '날짜':repeat_rank_date_list, '순위':rank_list, '곡':title_list, '가수':artist_list, '앨범':album_list}
    df = pd.DataFrame(dict)

    # excel 파일로 출력
    today_date = str(datetime.today().strftime("%Y%m%d_%H%M%S"))
    file_name = f'live_genie_{today_date}.xlsx'
    df.to_excel(crawled_folder_path + file_name, index=False, encoding='utf-8')

    df.to_excel(f'\\\\192.168.100.178/d/용역/2022/2022년 음원사재기 관련 모니터링 위탁용역/음원순위_크롤링/live_genie/{file_name}', index=False, encoding='utf-8')

    print(f"{file_name} 파일 생성 완료")

    # msg = ctypes.windll.user32.MessageBoxW(None, f'Genie 순위 자료 스크래핑 완료.\n{file_name} 생성완료', '알림', 0)

# Melon
def melon_crawling():
    # 파일 경로 확인
    code_path = os.getcwd().replace('\\', '/')

    # 수집한 파일 저장할 폴더 생성
    crawled_folder_path = code_path + '/crawled_data/live_melon/'
    os.makedirs(crawled_folder_path, exist_ok=True)

    # 페이지 접속
    url = 'https://www.melon.com/chart/index.htm'
    headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
    # 지니뮤직 url
    data = requests.get(url, headers=headers)
    # soup : html형식
    soup = bs(data.text, 'lxml')

    # 사이트 명
    site_name_list = ['Melon' for i in range(100)]

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
    dict = {'사이트':site_name_list, '날짜':repeat_rank_date_list, '순위':rank_list, '곡':title_list, '가수':artist_list, '앨범':album_list}
    df = pd.DataFrame(dict)

    # make file
    today_date = datetime.today().strftime("%Y%m%d_%H%M%S")
    file_name = f'live_melon_{today_date}.xlsx'
    df.to_excel(crawled_folder_path + file_name, index=False, encoding='utf-8')

    df.to_excel(f'\\\\192.168.100.178/d/용역/2022/2022년 음원사재기 관련 모니터링 위탁용역/음원순위_크롤링/live_melon/{file_name}', index=False, encoding='utf-8')

    print(f"{file_name} 파일 생성 완료")
    
    # msg = ctypes.windll.user32.MessageBoxW(None, f'Melon 순위 자료 스크래핑 완료.\n{file_name} 생성완료', '알림', 0)

# Vibe
def vibe_crawling():
    # 현재 경로 확인
    code_path = os.getcwd().replace('\\', '/')

    # 수집한 파일 저장할 폴더 생성
    crawled_folder_path = code_path + '/crawled_data/live_vibe/'
    os.makedirs(crawled_folder_path, exist_ok=True)

    # 현재 크롬 버전 확인
    chrome_ver = ca.get_chrome_version().split('.')[0]

    # headless 설정(크롬 창을 띄우지 않음)
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    # USB error 메세지 발생 해결을 위한 코드
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    # 크롬 드라이버 확인 및 설치
    ca.install(True)
    driver = webdriver.Chrome(options=options)

    # 페이지 접속
    url = 'https://vibe.naver.com/chart/total'
    driver.get(url)
    driver.implicitly_wait(3)
    driver.maximize_window()

    # 정보 수프에 담기
    soup = bs(driver.page_source, 'lxml')

    # driver quit
    driver.quit()

    # 사이트 명
    site_name_list = ['Vibe' for i in range(100)]

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
    dict = {'사이트':site_name_list, '날짜':repeat_rank_date_list, '순위':rank_list, '곡':title_list, '가수':artist_list, '앨범':album_list}
    df = pd.DataFrame(dict)

    # make excel
    today_date = datetime.today().strftime("%Y%m%d_%H%M%S")
    file_name = f'live_vibe_{today_date}.xlsx'
    df.to_excel(crawled_folder_path + file_name, index=False)

    df.to_excel(f'\\\\192.168.100.178/d/용역/2022/2022년 음원사재기 관련 모니터링 위탁용역/음원순위_크롤링/live_vibe/{file_name}', index=False, encoding='utf-8')

    print(f"{file_name} 파일 생성 완료")

    # msg = ctypes.windll.user32.MessageBoxW(None, f'Vibe 순위 자료 스크래핑 완료.\n{file_name} 생성완료', '알림', 0)

# Bugs
def bugs_crawling():
    # 현재 경로 확인
    code_path = os.getcwd().replace('\\', '/')

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

    # 사이트 명
    site_name_list = ['Bugs' for i in range(100)]

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
        song_title = one.find('p', 'title').find('a')['title'].strip()
        song_title = song_title.replace('[19금]', '').strip()
        song_title_list.append(song_title)

    # artist
    artist_list = []
    for one in tr_soup:
        artist = one.find('p', 'artist').find('a')['title'].strip()
        artist_list.append(artist)

    # album
    album_list = []
    for one in tr_soup:
        album = one.find('a', 'album')['title'].strip()
        album_list.append(album)

    # df
    dict = {'사이트':site_name_list, '날짜':repeat_rank_date_list, '순위':rank_list, '곡':song_title_list, '가수':artist_list, '앨범':album_list}
    df = pd.DataFrame(dict)

    # 파일 생성
    date = str(datetime.today().strftime("%Y%m%d_%H%M%S"))
    file_name = 'live_bugs_' + date + '.xlsx'
    df.to_excel(crawled_folder_path + file_name, index=False, encoding='utf-8')

    df.to_excel(f'\\\\192.168.100.178/d/용역/2022/2022년 음원사재기 관련 모니터링 위탁용역/음원순위_크롤링/live_bugs/{file_name}', index=False, encoding='utf-8')

    print(f"{file_name} 파일 생성 완료")

    # msg = ctypes.windll.user32.MessageBoxW(None, f'Bugs 순위 자료 스크래핑 완료.\n{file_name} 생성완료', '알림', 0)

# Soribada
def soribada_crawling():
    # 현재 경로 확인
    code_path = os.getcwd().replace('\\', '/')

    # 파일 저장할 폴더 생성
    crawled_folder_path = code_path + '/crawled_data/live_soribada/'
    os.makedirs(crawled_folder_path, exist_ok=True)

    # 현재 크롬 버전 확인
    chrome_ver = ca.get_chrome_version().split('.')[0]

    # headless 설정(크롬 창을 띄우지 않음)
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    # USB error 메세지 발생 해결을 위한 코드
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    # 크롬 드라이버 확인 및 설치
    ca.install(True)
    driver = webdriver.Chrome(options=options)

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

    # 사이트 명
    site_name_list = ['Soribada' for i in range(100)]

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
    dict = {'사이트':site_name_list, '날짜':repeat_rank_date_list, '순위':rank_list, '곡':song_title_list, '가수':artist_list, '앨범':album_list}
    df = pd.DataFrame(dict)

    # make excel
    today_date = datetime.today().strftime("%Y%m%d_%H%M%S")
    date = rank_date.split('_')[0].replace('-', '')
    file_name = f'live_soribada_{date}_{today_date}.xlsx'
    df.to_excel(crawled_folder_path + file_name, index=False)

    df.to_excel(f'\\\\192.168.100.178/d/용역/2022/2022년 음원사재기 관련 모니터링 위탁용역/음원순위_크롤링/live_soribada/{file_name}', index=False, encoding='utf-8')

    print(f"{file_name} 파일 생성 완료")

    # msg = ctypes.windll.user32.MessageBoxW(None, f'Soribada 순위 자료 스크래핑 완료.\n{file_name} 생성완료', '알림', 0)

# KY
def ky_crawling():
    # 현재 경로 확인
    code_path = os.getcwd().replace('\\', '/')
    # 수집한 파일 저장할 폴더 생성
    crawled_folder_path = code_path + '/crawled_data/live_ky'
    os.makedirs(crawled_folder_path, exist_ok=True)

    # 1 페이지(1~50) 접속
    url1 = 'https://kysing.kr/popular/?range=1'
    headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
    data = requests.get(url1, headers=headers)

    # 수프에 담기
    soup = bs(data.text, 'lxml')
    ul_soup = soup.find_all('ul', 'popular_chart_list clear')[1:]

    # 사이트 명
    site_name_list = ['Ky' for i in range(100)]

    # 순위 날짜
    rank_date = datetime.today().strftime('%Y-%m-%d')
    repeat_rank_date_list = []
    for i in range(100):
        repeat_rank_date_list.append(rank_date)
    # 노래 제목
    title_list = []
    for one in ul_soup:
        temp = one.find('span', 'tit').text.strip()
        title_list.append(temp)
    len(title_list)
    # 가수
    artist_list = []
    for one in ul_soup:
        temp = one.find('span', 'tit mo-art').text.strip()
        artist_list.append(temp)
    # rank
    rank_list = []
    for i in range(1, 101):
        rank_list.append(i)

    # 2 페이지(51~100위)
    url2 = 'https://kysing.kr/popular/?range=2'
    data = requests.get(url2, headers=headers)

    # 수프에 담기
    soup = bs(data.text, 'lxml')
    ul_soup = soup.find_all('ul', 'popular_chart_list clear')[1:]

    # 노래 제목
    for one in ul_soup:
        temp = one.find('span', 'tit').text.strip()
        title_list.append(temp)
    # 가수
    for one in ul_soup:
        temp = one.find('span', 'tit mo-art').text.strip()
        artist_list.append(temp)

    # make df
    dict = {'사이트':site_name_list, '날짜':repeat_rank_date_list, '순위':rank_list, '곡':title_list, '가수': artist_list}
    df = pd.DataFrame(dict)
    # make excel
    today_date = datetime.today().strftime("%Y%m%d_%H%M%S")
    file_name = f'live_ky_{today_date}.xlsx'
    path = crawled_folder_path + '/'
    df.to_excel(path + file_name, index=False, encoding='utf-8')

    df.to_excel(f'\\\\192.168.100.178/d/용역/2022/2022년 음원사재기 관련 모니터링 위탁용역/음원순위_크롤링/live_ky/{file_name}', index=False, encoding='utf-8')

    print(f"{file_name} 파일 생성 완료")

# TJ
def tj_crawling():
    # 현재 경로 확인
    code_path = os.getcwd().replace('\\', '/')
    # 수집한 파일 저장할 폴더 생성
    crawled_folder_path = code_path + '/crawled_data/live_tj'
    os.makedirs(crawled_folder_path, exist_ok=True)

    # 페이지 접속
    crawled_date = datetime.today().strftime("%Y-%m-%d")
    year = crawled_date.split('-')[0]
    month = crawled_date.split('-')[1]
    day = crawled_date.split('-')[2]
    day2 = str(int(day)-1)
    url = f'http://www.tjmedia.com/tjsong/song_monthPopular.asp?strType=1&SYY={year}&SMM={month}&SDD={day2}&EYY={year}&EMM={month}&EDD={day}'
    headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
    data = requests.get(url, headers=headers)
    # 수프에 담기
    # 한글 깨짐 해결
    soup = bs(data.content.decode('utf-8', 'replace'), 'lxml')
    tr_soup = soup.find('div', id='BoardType1').find('tbody').find_all('tr')[1:]

    # 사이트 명
    site_name_list = ['Tj' for i in range(100)]

    # 순위 날짜
    rank_date = datetime.today().strftime('%Y-%m-%d')
    repeat_rank_date_list = []
    for i in range(100):
        repeat_rank_date_list.append(rank_date)
    # 노래 제목
    title_list = []
    for one in tr_soup:
        temp = one.find_all('td')[2].text.strip()
        title_list.append(temp)
    # 가수
    artist_list = []
    for one in tr_soup:
        temp = one.find_all('td')[3].text.strip()
        artist_list.append(temp)
    # rank
    rank_list = []
    for i in range(1, 101):
        rank_list.append(i)
    
    # make df
    dict = {'사이트':site_name_list, '날짜':repeat_rank_date_list, '순위':rank_list, '곡':title_list, '가수': artist_list}
    df = pd.DataFrame(dict)

    # make excel
    today_date = datetime.today().strftime("%Y%m%d_%H%M%S")
    file_name = f'live_tj_{today_date}.xlsx'
    path = crawled_folder_path + '/'
    df.to_excel(path + file_name, index=False, encoding='utf-8')

    df.to_excel(f'\\\\192.168.100.178/d/용역/2022/2022년 음원사재기 관련 모니터링 위탁용역/음원순위_크롤링/live_tj/{file_name}', index=False, encoding='utf-8')

    print(f"{file_name} 파일 생성 완료")

# 일정 시간마다 반복
# job1 = schedule.every().day.at("11:00").do( flo_crawling )
# job2 = schedule.every().day.at("11:02").do( genie_crawling )
# job3 = schedule.every().day.at("11:04").do( melon_crawling )
# job4 = schedule.every().day.at("11:06").do( vibe_crawling )
# job5 = schedule.every().day.at("11:08").do( bugs_crawling )
# job6 = schedule.every().day.at("11:10").do( soribada_crawling )
# job7 = schedule.every().day.at("11:12").do( ky_crawling )
# job8 = schedule.every().day.at("11:14").do( tj_crawling )

# count = 0

# while True:
#     schedule.run_pending()

    # # 7번만 반복하도록 설정
    # if count > 7:
    #     schedule.cancel_job(job1)
    #     schedule.cancel_job(job2)
    #     schedule.cancel_job(job3)
    #     schedule.cancel_job(job4)
    #     schedule.cancel_job(job5)
    #     schedule.cancel_job(job6)
    #     schedule.cancel_job(job7)
    #     schedule.cancel_job(job8)

# 테스트
flo_crawling() #1 
genie_crawling() #2
melon_crawling() #3
vibe_crawling() #4
bugs_crawling() #5
soribada_crawling() #63/
ky_crawling() #7
tj_crawling() #8

# 종료 메세지
msg = ctypes.windll.user32.MessageBoxW(None, '파일 실행 완료.', '알림', 0)