import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

url = "https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y"

response = requests.get(url)

html_data = response.text

# BeautifulSoup을 이용하여 데이터를 파싱
soup = bs(html_data, 'html.parser')

div_data = soup.find(
    'div',
    attrs={
        'id' : 'main_content'
    }
)

div_data2 = soup.find(
    'div',
    attrs = {
        'class' : 'list_body'
    }
)

a_list = div_data2.find_all('a')

data_list = []

for a in a_list:
    # print(a.get_text())
        #추출한 텍스트가 데이터가 존재하는 경우

    if a.get_text().strip(): # strip()은 좌우 여백 없앤다. \n (줄바꿈 의미) 이 나와서 이걸 없애기 위함.
        data_list.append(a.get_text())

link_list = []

for a in a_list:
    # link_list.append(a['href'])
    link_data = a['href']
    # 주소에서 ? 전까지 텍스트를 확인
    index = link_data.find("?") 
    data = link_data[:index]
    # "link_list에 data가 포함되어 있지 않다면" 구문을 추가해서 중복 데이터 삭제
    if data not in link_list:
        link_list.append(data)

df_data = {
    '헤드라인' : data_list,
    '주소' : link_list
}

df = pd.DataFrame(df_data)

# 데이터프레임을 excel로 저장
df.to_excel('네이버 연합뉴스1.xlsx', index=False)


#윈도우에서는 작업 스케쥴러를 켜서 매일 또는 주기적으로 데이터 가져올 수 있도록 설정 가능.
#맥은 덮어씌워질 것이므로 파일명을 다르게~