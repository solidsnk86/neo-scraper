from flask import Flask, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)

@app.route('/api/scrape', methods=['GET'])
def scrape():
    try:
        url = 'https://solidsnk86.netlify.app/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        titles = [h1.text for h1 in soup.find_all('h1')]
        paragraphs = [paragraphs.text for paragraphs in soup.find_all('p')]
        list_items = [li.text for li in soup.find_all('li')]

        return jsonify({'titles': titles , 'paragraphs': paragraphs , 'list_items': list_items })
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
