import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")

soup = BeautifulSoup(response.text,"html.parser")

pages = soup.select(".s-pagination site1 themed pager float-left")

print(pages)

#questions = soup.select(".question-summary")
#for question in questions:
 #   print(question.select_one(".question-hyperlink").getText())
  #  print(question.select_one(".vote-count-post").getText())