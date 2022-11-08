# imports
import random
import requests
import pickle
from bs4 import BeautifulSoup
from selenium import webdriver

# global variabled
sites = ["https://allthatsinteresting.com/tag/history", "https://allthatsinteresting.com/tag/science","https://www.reddit.com/r/WritingPrompts/", "https://www.reddit.com/r/indepthstories/", "https://getpocket.com/explore", "https://medium.com/"]


# start the chrome web browser with certain settings
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options, executable_path='./chromedriver.exe')

def scrapeController(site):
    if site == "https://allthatsinteresting.com/tag/science":
        content = interestingScrape(site)

    return content

def pickArticle(links):
    link = random.choice(tuple(links))
    return link

# scrap the site "All Thats Interesting"
def interestingScrape(site):

    # open the main page of the site and parse it
    browser.get(site)
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")
    
    # find the large element container that holds all of the articles
    bigContainer = soup.find_all("div", class_="css-175oi2r r-14lw9ot r-1do4pyk r-dnmrzs r-1sv84sj r-1yt7n81 r-ry3cjt r-1s6pnzw r-13qz1uu")[1]
    
    # find the all the <a> elements which contain the links or articles
    smallerContainer = bigContainer.find_all("a", class_="css-175oi2r r-13awgt0 r-1wtj0ep r-13qz1uu")
    
    # this will become a list of the links of the reccomened articles
    links = []
    
    # get the links of all the articles
    for item in smallerContainer:
        links.append(item.get("href"))
        
    # pick a random article that hasnt been picked before
    link = pickArticle(links)
    
    # Now it is time to scrape the article itself, open the article page and parse its html
    browser.get(link)
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")
    
    # get the title of the article
    articleTitle = soup.find("h1", class_="post-title")
    articleTitle = articleTitle.text
    
    # get all the elements of the article in order, such as headings, paragraphs, and images
    article_container = soup.find("article")
    article_element_list = article_container.find_all(['h2', 'p', 'img'])
    
    # this will become the body of the article
    full_body = ""
    
    # this is just used to prevent duplicate image links
    allLinks = []
    
    # go through every element of the list and add it to the full_body variable, also does some fancy stuff
    for element in article_element_list:
        
        # check if the element is a picture
        if element.name == 'img':
            
            # some elements dont have an src attribute so a try:execept is my temp solution
            try:
                # check if the src is a link
                if (element['src'][:5] == 'https'):

                    # make sure its not a duplicate
                    if element['src'] not in allLinks:
                    
                        # add the link to the full_body variable
                        full_body = full_body + str(element['src']) + "\n"
                    
                        # add the link to the allLinks var for future duplicate checking
                        allLinks.append(element['src'])
            except:
                # if the <img> element doesnt have an src attribute
                print("img doesnt have 'src'")
        
        # if the element is not an image, add it do the full_body var
        else:
            # this bit is to check if its an image caption
            if element.get('class') != None:
                if (element.get('class')[0] != 'wp-caption-text'):
                    full_body = full_body + element.text + "\n" + "\n"
                else: print("FOUND A NASTY CAPTION")
            else:
                full_body = full_body + element.text + "\n" + "\n"
    
    # create a dictionary with the whole article in it
    full_article = {
        "Title": articleTitle,
        "Body": full_body,
        }
    
    return full_article

def getData():
    article = scrapeController("https://allthatsinteresting.com/tag/science")
    return article