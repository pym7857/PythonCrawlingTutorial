import requests
from bs4 import BeautifulSoup as bs

class Conversation:
    # 질문(quesion), 응답(answer) 두 변수로 구성됩니다.
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __str__(self):
        return "질문: " + self.question + "\n답변: " + self.answer + "\n"

# 모든 영어 대화 주제를 추출하는 함수
def get_subjects():
    subjects = []

    # 전체 주제 목록을 보여주는 페이지로의 요청 (Request) 객체를 생성
    req = requests.get('https://basicenglishspeaking.com/daily-english-conversation-topics/')
    html = req.text
    bsObject = bs(html, 'html.parser')

    for div in bsObject.findAll('div', {'class': 'su-column-inner su-clearfix'}):
        for link in div.findAll('a'):
            subject = link.text
            subjects.append(subject)

    return subjects

subjects = get_subjects()
print('총 ', len(subjects), ' 개의 주제를 찾았습니다.')
print(subjects)

# 사용자 입력 받는 부분
print('원하시는 주제를 입력해주세요:')
user_input = input()
if user_input not in subjects:
    print('해당하는 주제가 없습니다.')
print('주제: ', user_input, ' 을(를) 선택하셨습니다!\n')

# (사용자 입력에 해당하는) 주제의 페이지 정보 가져오기
req = requests.get('https://basicenglishspeaking.com/' + user_input)
html = req.text
bsObject = bs(html, 'html.parser')

# (사용자 입력에 해당하는) 주제의 질문&답변 가져오기
qnas = bsObject.findAll('div', {'class': 'sc_player_container1'})
qna_list = []
for qna in qnas:
    if qnas.index(qna) %2 == 0:
        q = qna.next_sibling
    else:
        a = qna.next_sibling
        c = Conversation(q, a)      # 항상 질문 다음에 답변을 가져온다.
        qna_list.append(c)

# (사용자 입력에 해당하는) 주제의 질문&답변 출력
for c in qna_list:
    print(str(c))