from flask import Flask,render_template


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    first_name = 'alex'
    pizza_list = ['pepperoni','cheese','chicken']
    return render_template('index.html',first_name=first_name,pizza_list=pizza_list)

@app.route('/user/<name>')
def user(name):

    return render_template('user.html',user_name = name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404



if __name__ == '__main__':
    app.run(debug=True)