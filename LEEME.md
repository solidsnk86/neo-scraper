| Neo - Scraper  |
-----------------|

<p class="description-scraper">Neo-Scraper es una aplicación simple hecha con Flask, Python y Beautifulsoup para hacer web-scraping.</p>

>[!Nota]
>Si deseas usar esta aplicación, debes instalar todas estas dependencias:

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
O si deseas instalar todos los módulos, he creado un archivo requirements.txt. ¿Sabes cómo generar automáticamente un `requirements.txt`?

```bash
pip freeze > requirements.txt
```
Esto guardará todas las dependencias y sus versiones en el archivo <i style="color:tomato">requirements.txt</i>. Puedes usar este archivo para instalar las mismas dependencias en otro entorno con el siguiente comando:

```bash
pip install -r requirements.txt
```
Por otro lado, necesitamos ejecutar el servidor virtual.

> [!Importante]
> Estos comandos deben ejecutarse en tu terminal o símbolo del sistema. Asegúrate de estar en un entorno virtual si estás trabajando en un proyecto específico. Puedes crear un entorno virtual usando venv de la siguiente manera:

```bash
# Crear entorno virtual
python -m venv myenv

# Activar el entorno virtual (Windows)
myenv\Scripts\activate

# Para activar el entorno virtual (Unix o MacOS)
source myenv/bin/activate
```
Luego puedes instalar las dependencias dentro del entorno virtual.

Después de instalar las dependencias, puedes ejecutar tu script Flask. Asegúrate de tener el código completo de Flask y ajusta el puerto u otras configuraciones según sea necesario. Por ejemplo, si tu archivo se llama app.py, podrías ejecutarlo así:

```bash
python app.py
```
Esto iniciará tu aplicación Flask en el servidor local y podrás acceder a ella desde tu navegador. Asegúrate de abrir el navegador y visitar la dirección que la consola muestra después de ejecutar el script (por defecto, suele ser algo como http://127.0.0.1:5000/).
¡Por supuesto! El código proporcionado es una aplicación web simple de Flask que utiliza Flask y BeautifulSoup para hacer scraping de datos de un sitio web. Desglosemos el código:

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
        paragraphs = [paragraph.text for paragraph in soup.find_all('p')]
        list_items = [li.text for li in soup.find_all('li')]

        return jsonify({'titles': titles , 'paragraphs': paragraphs , 'list_items': list_items })
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
# Este código ejecuta la aplicación Flask cuando el script se ejecuta directamente
# (no importado como un módulo), con depuración habilitada.
```
## Lógica de Web Scraping:

El script especifica una URL de destino y configura Flask como una ruta de API para obtener esta URL desde Axios.
- Dentro del bloque try, navega a la URL especificada, obtiene el origen de la página y lo analiza con BeautifulSoup.
- Los títulos y párrafos se extraen del contenido HTML utilizando BeautifulSoup.
- Los resultados se devuelven como una respuesta JSON usando la función jsonify de Flask.

> [!ADVERTENCIA]
> El web scraping debe realizarse éticamente y de acuerdo con los términos de servicio del sitio web. Siempre ten en cuenta las consideraciones legales y éticas al extraer datos de sitios web.
