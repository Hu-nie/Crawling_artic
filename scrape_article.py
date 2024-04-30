import requests
from bs4 import BeautifulSoup

def get_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "\
        "(KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # HTTP 요청 오류 발생 시 예외 발생
    return response.text

def extract_content(soup, selectors):
    content = []
    for selector in selectors:
        elements = soup.select(selector)
        text = "".join(element.text.strip() for element in elements)
        content.append(text)
    return content

def art_crawl(url):
    selectors = {
        "title": "#title_area > span",
        "date": "#ct > div.media_end_head.go_trans > div.media_end_head_info.nv_notrans "\
                "> div.media_end_head_info_datestamp > div:nth-child(1) > span",
        "main": "#dic_area"
    }

    html = get_html(url)
    soup = BeautifulSoup(html, "lxml")

    article_data = {key: "" for key in selectors}
    for key, selector in selectors.items():
        article_data[key] = extract_content(soup, [selector])[0]

    return article_data
