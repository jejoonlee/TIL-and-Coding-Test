from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

website = response.text

soup = BeautifulSoup(website, "html.parser")

movies = []

for title in soup.find_all(name="h3", class_="title"):
    movies.append(title.getText())

with open("movies.txt", mode="w", encoding="UTF8") as file:
    for i in range(len(movies) - 1, -1, -1):
        file.write(f"{movies[i]}\n")



# response = requests.get(url="https://news.ycombinator.com/front")

# website = response.text

# soup = BeautifulSoup(website, "html.parser")

# titles = soup.select(selector=".titleline > a")

# article_texts = []
# article_links = []

# for title in titles:
#     article_texts.append(title.getText())
#     article_links.append(title.get("href"))

# article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# most_upvote = max(article_upvote)
# most_upvote_index = article_upvote.index(most_upvote)

# print(article_texts[most_upvote_index])
# print(article_links[most_upvote_index])
# print(most_upvote)

#\33 4775549 > td:nth-child(3) > span > a

# with open("website.html", encoding="UTF8") as file:
#     content = file.read()

# soup = BeautifulSoup(content, "html.parser")

# print(soup.title)
# print(soup.title.name)

# all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# section_heading = soup.find(name="h3", class_="heading")
# print(heading.getText())
# print(section_heading.getText())

# company_url = soup.select_one(selector="p a")
# # id를 #과, class는 .을 사용해서, 사용할 수 있다