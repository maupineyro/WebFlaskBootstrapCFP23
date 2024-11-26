import os

from flask import Flask, send_file

app = Flask(__name__, static_folder='src', static_url_path='/')


@app.route("/")
def index():
    return send_file('src/index.html')

@app.route("/contacto")
def contacto():
    return send_file('src/contacto.html')

@app.route("/cursos")
def cursos():
    return send_file('src/cursos.html')

@app.route("/faq")
def faq():
    return send_file('src/faq.html')

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
