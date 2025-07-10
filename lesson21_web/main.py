from flask import Flask
from markupsafe import escape
from google import genai

app = Flask(__name__)

@app.route("/")
@app.route("/<string:question>")
def index(question:str=''):
    if question == '':
        return '<hl>這是Gemini畫面</hl>'
    else:
        client = genai.Client()
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=f"{question},回答請輸出為html格式"
        )
        html_format = response.text
        html_format = response.text.replace('```html,""').replace('```,""')
        return html_format

