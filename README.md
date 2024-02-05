
| Neo - Scraper  |
-----------------|

<p class="description-scraper">Neo-Scraper is an simple application made with Flask, Python, Beautifulsoup to do a web-scraping.</p>

>[!Note]
>If you wanna use this app, you need to install all these dependencies:

- Flask
```bash
pip isntall Flask
```
- Flask-CORS
```bash
pip isntall flask-cors
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
- Certainly! The provided code is a simple Flask web application that utilizes Flask and BeautifulSoup to scrape data from a website. Let's break down the code:
```python
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
# This code runs the Flask application when the script is executed directly
# (not imported as a module), with debugging enabled.
```

## Web Scraping Logic:
- The script specifies a target URL and configures Flask like an api route to get this URL from Axios.
- Inside the try block, it navigates to the specified URL, retrieves the page source, and parses it using BeautifulSoup.
- The titles and articles are extracted from the HTML content using BeautifulSoup.
- The results are returned as a JSON response using Flask's jsonify function.

> [!WARNING]
>  Web scraping should be done ethically and in accordance with the website's terms of service. Always be aware of legal and ethical
> considerations when scraping data from websites.

<a href='https://youtu.be/_rqO9D4aFAw' target='_blank' style='color: tomato; text-decoration:underline;'>
    I have a short video on YouTube that show you how this app works. In my case, I use it in my React web app and call it with Axios. Follow this link.
</a>

# 

- Here is a brief description from the JSON that we will receive from the Python app.
```python
from flask import Flask, jsonify
return jsonify({'titles': titles , 'paragraphs': paragraphs , 'list_items': list_items })
```
<img width="100%" src="https://github.com/solidsnk86/neo-scraper/blob/master/public/json_scraping.png?raw=true" alt="JSON image description." />
<p>To get that JSON result into your web app from React, you need to have a component like this:</p>

```javascript
import { useState } from 'react';
import axios from 'axios';

export default function Scraper() {
  const [disabled, setDisabled] = useState(false);
  const [scrape, setScraping] = useState({
    titles: [],
    paragraphs: [],
    items: [],
    inputs: [],
    images: [],
    links: [],
  });

  const handleScrape = async () => {
    try {
      const response = await axios.post(
        'https://www.pythonanywhere.com/user/SolidSnk86/files/home/SolidSnk86/scrape/flask_app.py',
      );
      setScraping(response.data);
      setDisabled(true);
    } catch (error) {
      console.error('Error al realizar el raspado:', error);
    }
  };

  return (
    <>
      <div className="justify-center mx-auto my-6">
        <button
          onClick={handleScrape}
          disabled={disabled}
          className="border p-3 bg-zinc-300 dark:bg-zinc-800/95 dark:border-zinc-600/75 cursor-not-allowed rounded dark:border-zinc-800 border-zinc-00/10 hover:opacity-[.6] transition-all"
        >
          Hacer Scraping
        </button>
      </div>
      {Object.keys(scrape.titles).map((index) => (
        <article
          key={index}
          className="text-zinc-100 space-y-3 border-zinc-200 border-[1px] shadow-md rounded shadow-zinc-200 mt-6 p-6 dark:!shadow dark:border-zinc-800 overflow-x-auto"
        >
          <h1 className="text-[tomato] underline text-lg">
            {scrape.titles[index]}
          </h1>
          <p className="text-text-primary p-3 text-sm">
            {scrape.paragraphs[index]}
          </p>
          <ul className="text-zinc-500">
            {Array.isArray(scrape.images[index]) &&
              scrape.images[index].map((image, i) => (
                <li key={i}>
                  <p>Alt: {image.alt}</p>
                  <p>Src: {image.src}</p>
                </li>
              ))}
          </ul>
          <div>
            <p>Links:</p>
            <ul>
              {Array.isArray(scrape.links[index]) &&
                scrape.links[index].map((link, i) => (
                  <li key={i}>
                    <p>Alt: {link.alt}</p>
                    <p>Src: {link.src}</p>
                  </li>
                ))}
            </ul>
          </div>
        </article>
      ))}
    </>
  );
}
```
#

<p>
  <strong>Error Reporting:</strong> If you encounter any issues or errors while using our application, please don't hesitate to reach out. Provide details about the problem, and I'll work to address it promptly.
</p>
<p>
  <strong>Contributions:</strong> Interested in contributing to the project? Feel free to fork the repository on GitHub and submit a pull request. I appreciate any enhancements, bug fixes, or new features you may bring!
</p>
<p>
  <strong>General Inquiries:</strong> Whether you have questions about the application's functionality, suggestions for improvement, or just want to say hello, your feedback is always welcome.
</p>

<p>Contact for any queries or feedback, feel free to reach out to my email at:</p>

[![Gmail Badge](https://img.shields.io/badge/-calcagni.gabriel86@gmail.com-d14836?style=flat&logo=Gmail&logoColor=white&link=mailto:mailto:calcagni.gabriel86@gmail.com)](mailto:calcagni.gabriel86@gmail.com)

#

<div align="center">
  <p>NeoTecs Dev ©2023</p>
</div>


