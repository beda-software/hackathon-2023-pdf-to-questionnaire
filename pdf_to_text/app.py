import asyncio
import aiohttp
from aiohttp import web
import re
import tempfile
import os

import fitz


def preprocess(text):
    text = text.replace('\n', ' ')
    text = re.sub('\s+', ' ', text)
    return text


def pdf_to_text(path, start_page=1, end_page=None):
    doc = fitz.open(path)
    total_pages = doc.page_count

    if end_page is None:
        end_page = total_pages

    text_list = []

    for i in range(start_page - 1, end_page):
        text = doc.load_page(i).get_text("text")
        text = preprocess(text)
        text_list.append(text)

    doc.close()
    return text_list

def convert_pdf_content_to_text(content):
    tmp = tempfile.NamedTemporaryFile(suffix=".pdf")
    with open(tmp.name, 'w+b') as f:
        f.write(content)

    return '\n'.join([f"{i+1} Page: {x}" for i,x in enumerate(pdf_to_text(tmp.name))])


async def handle_pdf_content(request):
    data = await request.read()

    return web.Response(text=convert_pdf_content_to_text(data))

app = web.Application()
app.add_routes([web.post('/', handle_pdf_content)])

if __name__ == "__main__":
    web.run_app(app)

