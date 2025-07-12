"""
Exercise 1: User Auth, Email, and Search Extension
Extend the application to:
- Add user registration/login functionality
- Implement email notifications
- Add search/filter capabilities
(Simulate Flask app structure and logic in a single file, no real email sending.)
"""

from flask import Flask, request, render_template_string, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'secret'

# Simulated user database
users = {}

# Simulated email notification
def send_email(to, subject, body):
    print(f"[Email] To: {to} | Subject: {subject} | Body: {body}")

@app.route('/')
def home():
    query = request.args.get('q', '')
    # Simulated data
    items = [
        {'title': 'First Post', 'content': 'Hello world!'},
        {'title': 'Second Post', 'content': 'Python is great.'},
        {'title': 'Third Post', 'content': 'Flask makes web easy.'}
    ]
    if query:
        items = [item for item in items if query.lower() in item['title'].lower() or query.lower() in item['content'].lower()]
    return render_template_string("""
    <h1>Welcome</h1>
    {% if session.get('user') %}
      <p>Logged in as {{ session['user'] }}</p>
      <a href='{{ url_for('logout') }}'>Logout</a>
    {% else %}
      <a href='{{ url_for('login') }}'>Login</a> | <a href='{{ url_for('register') }}'>Register</a>
    {% endif %}
    <form method='get'>
      <input name='q' placeholder='Search...' value='{{ request.args.get('q', '') }}'>
      <input type='submit' value='Search'>
    </form>
    <ul>
      {% for item in items %}
        <li><b>{{ item.title }}</b>: {{ item.content }}</li>
      {% endfor %}
    </ul>
    """, items=items)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        if username in users:
            return 'Username already exists.'
        users[username] = {'password': password, 'email': email}
        send_email(email, 'Welcome!', f'Thank you for registering, {username}!')
        return redirect(url_for('login'))
    return render_template_string("""
    <h2>Register</h2>
    <form method='post'>
      Username: <input name='username'><br>
      Email: <input name='email'><br>
      Password: <input name='password' type='password'><br>
      <input type='submit' value='Register'>
    </form>
    """)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if not user or user['password'] != password:
            return 'Invalid credentials.'
        session['user'] = username
        return redirect(url_for('home'))
    return render_template_string("""
    <h2>Login</h2>
    <form method='post'>
      Username: <input name='username'><br>
      Password: <input name='password' type='password'><br>
      <input type='submit' value='Login'>
    </form>
    """)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True) 