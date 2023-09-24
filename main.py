import time
import requests
import selectorlib
from datetime import datetime
import sqlite3

URL = "http://programmer100.pythonanywhere.com"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'
}

connection = sqlite3.connect("tempData.db")

def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["temperature"]
    return value

def store(extracted):
    now = datetime.now().strftime('%y-%m-%d-%H-%M-%S')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO temperature VALUES(?,?)", (now, extracted))
    connection.commit()


if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)
        store(extracted)
