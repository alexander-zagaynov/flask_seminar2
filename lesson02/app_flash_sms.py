from flask import Flask, flash, redirect
from flask import Flask, render_template, request, url_for

app = Flask(__name__)
app.secret_key = b'5b60daa8ee9e36f9d26f01ea2d642389b415e34f1e81b919c604ef79f933dc5f'
"""
Создание секретного ключа 
>>> import secrets
>>> secrets.token_hex()
"""

@app.route('/')
def index():
    return 'Привет !'


@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('flash_form.html')


if __name__ == '__main__':
    app.run(debug=True)

