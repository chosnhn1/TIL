Today I Learned....

# git

~~git gud!!!~~

git is... **분산형 버전 관리 프로그램** 

* 분산형: (cf. 중앙집중형)
  * 모든 작업자가 변동내역을 들고 있게 됨 (분산)
  * 한 쪽에 저장된 git이 소실되어도 복구가능
  * git이 모든 버전을 통째로 들고 있는 것이 아님: 변동내역만 갖고 있음 (~ clothpatch)
* 버전 관리: 파일(코드)의 history를 기록/캡처(commit)하고 업데이트. 비교, 복구할 수 있게 해 줌

git is not...

* github (git에 특화된 저장소 서비스): ~gitlab bitbucket





## Command Line Interface

명령줄(Command Line) 인터페이스 (cf. GUI)

### 주요 개념

* Command: 명령어
* Path 경로

### 명령어

touch

mkdir

rm



pwd

date

clear

* Root Directory: /
* Home Directory: ~ (Tilde)
* 절대 경로: 현재 작업경로와 상관없이 직접적으로 참조할 수 있는 경로
  * /C/Users/ABC/...
* 상대 경로: 

\루트 디렉토리, 홈 디렉토리
절대 경로, 틸드 (~)
상대 경로
cf. . .. 



## git

### gitignore

git으로 관리될 필요가 없는 (ex. 게시가 불필요한 시스템 파일들) 것들 관리





# Markdown (*.md)

R 공부할 때 rmarkdown도 썼었는데.... 차이점 등에 유의해서 활용하면 좋을 것 같다.





# 웹 크롤링

### 용어

* Crawling
* Parsing

## 예제: 네이버 금융

```python
import requests # library import
from bs4 import BeautifulSoup

url_1 = "https://finance.naver.com/sise/" # 네이버 국내증시
url_2 = "https://finance.naver.com/world/" # 네이버 해외증시
response_1 = requests.get(url_1).text
response_2 = requests.get(url_2).text # 각자 응답받기

data1 = BeautifulSoup(response_1, 'html.parser')
data2 = BeautifulSoup(response_2, 'html.parser') # 각자 parsing

kospi = data1.select_one("#KOSPI_now") # KOSPI는 ID=KOSPI_now 있음
sp500 = data2.select_one("#worldIndexColumn3 > li:nth-child(1) > dl:nth-child(1) > dd:nth-child(2) > strong:nth-child(1)")
result1 = kospi.text 
result2 = sp500.text

print(f'현재 코스피 지수는 {result1}입니다. S&P500 지수는 {result2}입니다.')
```



-----

### 예제: 네이버 쇼핑 검색

```python
import requests

# naver 요청 시 필요 요소
naver_client_id = "~~~~~"
naver_client_secret = "~~~~~"

naver_url = "https://openapi.naver.com/v1/search/shop.json?query="

# 헤더 생성
headers = {
    'X-Naver-Client-Id': naver_client_id,
    'X-Naver-Client-Secret': naver_client_secret
}

# 쿼리 작성
query = "라이젠 노트북"

product = requests.get(naver_url+query, headers = headers).json()['items'][0]
product_name = product['title']
product_price = product['lprice']
product_link = product['link']

# 검색결과 출력
message = f"{product_name}\n{product_price}\n{product_link}"
print(message)

# 텔레그램 챗봇 기본 설정
tele_token = "~~~~~"
tele_url = f"https://api.telegram.org/bot{tele_token}"

# chat_id 가져오기
updates_url = f"{tele_url}/getUpdates"
response = requests.get(updates_url).json()
chat_id = response.get('result')[0].get('message').get('chat').get('id')

######

# 보낼 메시지 작성
text = f"Python으로 보낸 메시지입니다.\n" + message

# 메시지 전달
message_url = f"{tele_url}/sendMessage?chat_id={chat_id}&text={text}"
requests.get(message_url)
```
