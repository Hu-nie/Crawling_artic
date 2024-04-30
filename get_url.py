import pandas as pd
import json
import urllib.request
from bs4 import BeautifulSoup

# HTML 태그 제거 함수
def remove_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

# 네이버 뉴스 검색 함수
def search_naver_news(query,display_num, client_id, client_secret):
    encText = urllib.parse.quote(query) 
    url = "https://openapi.naver.com/v1/search/news.json?query=" + encText + f"&display={display_num}" # JSON 결과

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if rescode == 200:
        df = pd.DataFrame(json.loads(response.read().decode('utf-8'))['items'])
        df = df[df['link'].str.contains('https://n.news')]
        df['title'] = df['title'].apply(remove_html_tags)
        df['description'] = df['description'].apply(remove_html_tags)
        return df
    else:
        print("Error Code:" + rescode)
        return None

