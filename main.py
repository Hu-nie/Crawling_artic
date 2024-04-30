# 네이버 뉴스 검색 실행
from get_url import *
from scrape_article import *

#id & secret 는 https://this-circle-jeong.tistory.com/167 통해서 어플 신청하고 발급
client_id = ""
client_secret = "" 
query = "" # 검색어 작성
display_num = 100 # 100개를 불러오지만 네이버에서 재작성 뉴스만 스크랩 하기 때문에 양이 적을순 있음
output_dir = "news_crawling/output" # 저장 위치

df = search_naver_news(query,display_num, client_id, client_secret)

article_list = []

for link in df['link']:
    artic = art_crawl(link)
    article_list.append(artic)


article_df = pd.DataFrame(article_list).applymap(remove_html_tags)
article_df.to_csv(f"{output_dir}/result.csv", index=False)
