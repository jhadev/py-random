import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".question-summary")

for question in questions:
    print(question.select_one(".vote-count-post").getText())
    print(question.select_one(".question-hyperlink").getText())
    link = question.select_one(".question-hyperlink").get("href")
    print(url[0:25] + link)
