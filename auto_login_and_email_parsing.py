import requests
from bs4 import BeautifulSoup as bs

# 반드시 먼저, 서버를 작동시킨 후에 크롤링을 진행하세요.

USER_DATA = {
    'userID': 'Nancy',
    'userPassword': '11'
}

'''
http://localhost:8084/UserChat/userLogin?userID=Nancy&userPassword=11
userLoginServlet 에서 'GET' 방식으로도 로그인을 할 수 있도록 미리 작업해 주었다.
'''
# 하나의 세션(Session) 객체를 생성해 일시적으로 유지합니다.★
with requests.Session() as s:
    # 로그인 페이지로의 POST 요청(request) 객체를 생성합니다.
    req = s.post('http://localhost:8084/UserChat/userLogin', data=USER_DATA)
    url = req.url
print(url)      # index.jsp 로 리다이렉트 된것을 확인할 수 있다.


# 유저 이메일 정보 가져오기
req = s.get('http://localhost:8084/UserChat/update.jsp?userID=Nancy')
html = req.text
bsObject = bs(html, 'html.parser')
result = bsObject.findAll('input', {'name': 'userEmail'})
print(result[0].get('value'))