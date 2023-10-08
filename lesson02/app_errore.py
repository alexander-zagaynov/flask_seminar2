from flask import Flask, render_template, request
from flask import redirect, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return 'Добро пожаловать на главную страницу'


@app.errorhandler(404)
def page_not_found(e):
    app.logger.warning(e)
    context = {
        'title': 'Страница не найдена',
        'url': request.base_url,
    }
    return render_template('404.html', **context), 404


# перенаправление на главную страницу


@app.route('/redirect/')
def redirect_to_index():
    return redirect(url_for('index'))


@app.route('/external/')
def redirect_to_redirect():
    return redirect(url_for('https://gb.ru/'))


if __name__ == '__main__':
    app.run(debug=True)


