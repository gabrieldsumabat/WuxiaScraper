from bs4 import BeautifulSoup
from requests import get
from html2text import html2text
import re


def incChapterNum(url):
    notNums = re.findall("[^0-9]", url)
    nums = re.findall("[0-9]", url)
    return ''.join(notNums) + str(int(''.join(nums)) + 1)


def getStoryName(url):
    urlSplit = url[27:].split('/')
    return urlSplit[1]


def saveChapterText(url, story):
    soup = BeautifulSoup(get(url).text, "html.parser")
    chapter = str(soup.findAll("p", {"dir": "ltr"}))
    text = html2text(chapter)

    with open(story + ".txt", "a+", encoding="utf-8") as file:
        file.write(text)


def wuxiaScrape():
    url = input("Please enter WuxiaWorld Chapter URL:")
    chapCount = int(input("Please enter the number of chapters to save:"))
    story = getStoryName(url)
    while (chapCount > 0):
        saveChapterText(url, story)
        url = incChapterNum(url)
        chapCount -= 1


if __name__ == "__main__":
    wuxiaScrape()
