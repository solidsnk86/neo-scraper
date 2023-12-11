from flask import Flask, jsonify
from flask_cors import CORS
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)

@app.route('/scream')
def scrape():
    url = 'https://solidsnk86.netlify.app/'
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        driver.implicitly_wait(5)

        html = driver.page_source

        soup = BeautifulSoup(html, 'html.parser')

        titles = [h1.text for h1 in soup.find_all('h1')]
        articles = [p.text for p in soup.find_all('p')]

        return jsonify({'titles': titles, 'articles': articles})

    finally:
        driver.quit()

if __name__ == '__main__':
    app.run(debug=True)
