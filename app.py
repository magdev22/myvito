from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/clouds')
def clouds():
    return render_template('clouds.html')

@app.route('/auto')
def auto():
    return render_template('auto.html')

@app.route('/realty')
def realty():
    return render_template('realty.html')


if __name__ == '__main__':
    app.run(debug=True)