# TekkerNotes er en egentlig simpel notetagningsapp, som helt sikkert bliver udsat for scope creep

from fasthtml.common import *
from fasthtml.pico import picolink

import md2html

from file_handler import FileHandler

skabeloner = FileHandler('/skabeloner')

app = FastHTML(hdrs=picolink)

@app.get('/')
def home():
    content = P('Velkommen til TekkerNotes')

    return page(content)

@app.get('/skabeloner')
def skabeloner():
    content = P(str(skabeloner.list_md_files()))
    return page(content)

@app.get('/noter')
def noter():
    pass

def page(content):
    '''Hjælpefunktion til at gøre det lettere at få header og footer(?) på alle sider'''
    return Div(
        nav_bar(),
        content
    )

def nav_bar():
    content = Div(
        A('Hjem', href='/'),
        A('Skabeloner', href='/skabeloner'),
        A('Noter', href='/noter')
    )
    return content

if __name__ == '__main__':
    serve()