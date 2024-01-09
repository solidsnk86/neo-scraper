| Neo - Scraper  |
-----------------|

<p class="description-scraper">Neo-Scraper es una aplicación simple hecha con Flask, Python y Beautifulsoup para hacer web-scraping.</p>

>[!Note]
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

> [!NOTE]
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


> [!Warning]
> El web scraping debe realizarse éticamente y de acuerdo con los términos de servicio del sitio web. Siempre ten en cuenta las consideraciones legales y éticas al extraer datos de sitios web.


<a href='https://youtu.be/_rqO9D4aFAw' target='_blank' style='color: tomato; text-decoration:underline;'>
    Tengo un breve video en YouTube que te muestra cómo funciona esta aplicación. En mi caso, lo uso en mi aplicación web de React y lo llamo con Axios. Sigue este enlace.
</a>


- Aquí hay una breve descripción del `JSON` que recibiremos de la aplicación Python.


```python
from flask import Flask, jsonify
return jsonify({'titles': titles , 'paragraphs': paragraphs , 'list_items': list_items })
```

<img width="100%" src="https://github.com/solidsnk86/neo-scraper/blob/master/public/json_scraping.png?raw=true" alt="Descripción de la imagen JSON." />

Para obtener ese resultado <abbr title="Graphics Interchange Format">JSON</abbr> en tu aplicación web desde React, necesitas tener un componente como este:

```javascript
import React, { useState } from 'react';
import axios from 'axios';
import { ArrowLeftIcon } from 'lucide-react';

export default function Scraping() {
    const [titles, setTitles] = useState([]);
    const [paragraphs, setParagraphs] = useState([]);
    const [items, setItems] = useState([]);

    const handleScrape = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:5000/api/scrape');
            setTitles(response.data.titles);
            setParagraphs(response.data.paragraphs);
            setItems(response.data.list_items);
        } catch (error) {
            console.error('Error al obtener datos del servidor:', error);
        }
    };

    return (
        <main className=" text-text-primary flex flex-col justify-center m-auto p-10 xl:w-1/2">
            <ArrowLeftIcon
                className="text-text-primary cursor-pointer hover:translate-x-[-2px] transition-all left-6 top-6 fixed"
                onClick={() => window.open('/docs/program')}
            />
            <h1 className="flex justify-center mx-auto text-5xl underline mb-3">
                Web Scraping
            </h1>
            <hr className="border-zinc-800 my-6" />
            <p className="list-css-span">
                Resultados del web scraping:
            </p>
            <button
                className="justify-center mx-auto text-button-variant border border-zinc-700 rounded p-2 w-fit my-3 hover:bg-zinc-800 hover:text-zinc-100"
                onClick={handleScrape}
            >
                ¡Scrapear!
            </button>
            {titles.map((title, index) => (
                <article className="text-zinc-100 space-y-3 border-zinc-300 border-[
```


Con esto seremos capaces de levantar un servidor de nuestra aplicación python y poder requerir el `JSON` desde nuestra react app.

#

<p>
  <strong>Reporte de Errores:</strong> Si encuentras algún problema o error al utilizar nuestra aplicación, no dudes en ponerte en contacto. Proporciona detalles sobre el problema y trabajaré para resolverlo rápidamente.
</p>
<p>
  <strong>Contribuciones:</strong> ¿Interesado en contribuir al proyecto? Siéntete libre de hacer un fork del repositorio en GitHub y enviar un pull request. ¡Aprecio cualquier mejora, corrección de errores o nuevas características que puedas aportar!
</p>
<p>
  <strong>Consultas Generales:</strong> Ya sea que tengas preguntas sobre la funcionalidad de la aplicación, sugerencias para mejorarla o simplemente quieras saludar, tu retroalimentación siempre es bienvenida.
</p>

<p>Para cualquier consulta o comentario, no dudes en ponerte en contacto a través de mi correo electrónico:</p>

[![Gmail Badge](https://img.shields.io/badge/-calcagni.gabriel86@gmail.com-d14836?style=flat&logo=Gmail&logoColor=white&link=mailto:mailto:calcagni.gabriel86@gmail.com)](mailto:calcagni.gabriel86@gmail.com)

#

<div align="center">
  <p>NeoTecs Dev ©2023</p>
</div>

