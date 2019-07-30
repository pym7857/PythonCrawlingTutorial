from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

html = urlopen('http://www.naver.com')      # url 객체
bsObject = bs(html, "html.parser")          # 파싱된 객체가 bsObject 에 담긴다
'''
파싱이란 일련의 문자열로 구성된 문서를 의미 있는 토큰(token)으로 분해하고  
토큰으로 구성된 파스 트리(parse tree)를 만드는 것입니다. 
'''
list = []
for rank in bsObject.find_all("span", class_="ah_k"):
    list.append(rank.get_text())
print(list)