from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.amazon.com/SAMSUNG-Android-Speakers-Upgraded-Graphite/product-reviews/B0CLF3VPMV/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&pageNumber=[]')

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

len(driver.find_elements(By.CLASS_NAME, 'cm_cr-review_list'))
review_list = driver.find_element(By.XPATH, '//*[@id="customer_review-RPA4U00SJ1MNU"]/div[4]/span') 

from bs4 import BeautifulSoup as bs

div_data = []

for b in div_data:
    soup = bs(driver.page_source, 'html.parser')
    soup.find_all('review-body')
    div_data = soup.find_all(
        "span", attrs = {'data-hook' : 'review-body'}
    )
    div_data[0].get_text()
    review_data = []
    for i in div_data:
        review_data.append(i.get_text().strip())
    a_link = driver.find_element(By.CLASS_NAME, 'a-last')