from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my Flask app!"

@app.route('/user/<username>')
def profile(username):
    return f"Hello {username}!"

if __name__ == '__main__':
    app.run(debug=True)