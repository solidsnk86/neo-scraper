# neo-scraper
Neo-Scraper is an application made with Flask, Python, Beautifulsoup to do a web-scraping at any page which are made by React.

>[!Note]
>If you wanna use this app, you need to install all these dependencies:

- Falsk
```bash
pip install Flask
```
- Flask-CORS
```bash
pip isntall flask-cors
```
- Selenium
```bash
pip install selenium
```
- Requests
```bash
pip install requests
```
- BeautifulSoup
```bash
pip install beautifulsoup4
```
Or if you want to install all the modules, I created a `requirements.txt` file. ¿Do you know how to generate an automatic `requirements.txt`?
```bash
pip freeze > requirements.txt
```
This will save all dependencies and their versions in the <i style="color:tomato">requirements.txt</i> file. You can then use this file to install the same dependencies in another environment with the command:

```bash
pip install -r requirements.txt
```

On the other hand, we need to execute the virtual server.
>[!Important]
>These commands must be run in your terminal or command prompt. Make sure you are in a virtual environment if you are working on a specific project. You can create a virtual environment using `venv` as follows:

```bash
# Create virtual environment
python -m venv myenv

# Activate Virtual Enviroment (Windows)
myenv\Scripts\activate

# To activate Virtual Enviroment (Unix o MacOS)
source myenv/bin/activate
```
You can then install the dependencies within the virtual environment.

After installing the dependencies, you can run your Flask script. Make sure you have the complete Flask code and adjust the port or any other settings as necessary. For example, if your file is called `app.py`, you could run it like this:
```bash
python app.py
```
- This will start your Flask application on the local server and you can access it from your browser. Make sure you open the browser and visit the address the console displays after running the script (by default, it's usually something like http://127.0.0.1:5000/).
- Certainly! The provided code is a simple Flask web application that utilizes Selenium and BeautifulSoup to scrape data from a website. Let's break down the code:
```python
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
```
