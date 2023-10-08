from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "Hi"

# создаем ввод данных ИМЯ - помещаем в переменную, и выводим обратно клиенту


@app.route('/submit/', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Hello {name}!'
    return render_template('post_html.html')


# разделение функциии на обработку get и post запросы
@app.get('/submit')
def submit_get():
    return render_template('post_html.html')


@app.post('/submit')
def submit_post():
    name = request.form.get('name')
    return f'Hello {name} !'


if __name__ == '__main__':
    app.run(debug=True)

