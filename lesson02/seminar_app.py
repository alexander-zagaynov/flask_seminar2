from flask import Flask, url_for
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Привет! Hello !"



@app.route('/login', methods=['GET', 'POST'])
def login():
    context = {
        'title': 'Login page',
    }
    user_login = request.form.get('login')
    user_password = request.form.get('password')
    u_login = 'admin'
    u_password = '12345'

    if user_login == u_login and user_password == u_password:
        return render_template(url_for('index'), context=context)
    else:
        return render_template(url_for('login.html'), context=context)







if __name__ == '__main__':
    app.run(debug=True)
