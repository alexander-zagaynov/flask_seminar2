from flask import Flask, url_for
from flask import render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world'


@app.route('/number/<int:num>/')
def set_number(num):
    return f'Передано число {num}'


@app.route('/')
def index():
    return 'Введите путь к файлу в адресной строке'


@app.route('/<path:file>/')
def get_file(file):
    print(file)
    return f'Ваш файл находится в {escape(file)}!'

функция escape - позволяет принимать только строки от пользователя,
тем самым, не сайт не закинут разные файлы.

http://127.0.0.1:5000/<script>alert("I am Alexander haсker")</script>/


@app.route('/test_url_for/<int:num>')
def test_url(num):
    text = f'В num лежит {num}<br>'
    text += f'Функция {url_for("test_url", num=42) = }<br>'
    text += f'Функция {url_for("test_url", num=42, data="new_data") = }<br>'
    text += f'Функция {url_for("test_url", num=42, data="new_data", pi=3.14515) = }<br>'

    return text


@app.route('/about/')
def about():
    context = {
        'title': 'Обо мне',
        'name': 'Alexander',
    }
    return render_template('about.html', **context)


if __name__ == '__main__':
    app.run(debug=True)






