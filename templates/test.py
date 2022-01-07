from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


def scrape():
    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    listings = {}

    url = "https://www.goodreads.com/book/show/1934.Little_Women?from_search=true&from_srp=true&qid=n9WFfEmVLM&rank=1"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    listings["title"] = soup.find("h1", id_="bookTitle").get_text()
    listings["author"] = soup.find("span", class_="authorName").get_text()

    # Quit the browser
    browser.quit()

    return listings