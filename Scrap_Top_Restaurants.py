import numpy as np
import pandas as pd
from Get_Page_Html import GetPageHtml
from Scrap_Reviews import ScrapReviews

url = "https://www.zomato.com/ncr/top-restaurants"
top_restaurants_html = GetPageHtml(url)
main_div = top_restaurants_html.find('div',{'class':"bke1zw-0 cMipmx"})

restaurants_urls = []
for divs in main_div.children:
    url = divs.contents[0].contents[1].contents[0]['href'].split("?")[0]
    restaurants_urls.append(url)

rest_reviews = {}
for rest in restaurants_urls[1:2:2]:
    rest_reviews.update(ScrapReviews(rest))

print(rest_reviews)


