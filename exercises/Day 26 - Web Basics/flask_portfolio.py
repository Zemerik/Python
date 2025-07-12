"""
Exercise 1: Flask Portfolio Site
Create a Flask portfolio site that:
- Has routes for Home/About/Contact pages
- Uses base template inheritance
- Handles form submissions
(Simulate templates and form handling in code comments if not using real files.)
"""

from flask import Flask, render_template_string, request

app = Flask(__name__)

# Simulated base template
base_template = """
<!doctype html>
<title>{% block title %}Portfolio{% endblock %}</title>
<body>
  <header><h1>My Portfolio</h1></header>
  <nav>
    <a href='/'>Home</a> | <a href='/about'>About</a> | <a href='/contact'>Contact</a>
  </nav>
  <main>
    {% block content %}{% endblock %}
  </main>
  <footer><p>&copy; 2024</p></footer>
</body>
"""

@app.route('/')
def home():
    return render_template_string("""
    {% extends base %}
    {% block title %}Home - Portfolio{% endblock %}
    {% block content %}<h2>Welcome to my portfolio!</h2>{% endblock %}
    """, base=base_template)

@app.route('/about')
def about():
    return render_template_string("""
    {% extends base %}
    {% block title %}About - Portfolio{% endblock %}
    {% block content %}<h2>About Me</h2><p>This is the about page.</p>{% endblock %}
    """, base=base_template)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    message = ''
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        msg = request.form.get('message')
        # Simulate form processing
        message = f"Thank you, {name}! Your message has been received."
    return render_template_string("""
    {% extends base %}
    {% block title %}Contact - Portfolio{% endblock %}
    {% block content %}
      <h2>Contact</h2>
      <form method='post'>
        Name: <input name='name'><br>
        Email: <input name='email'><br>
        Message: <textarea name='message'></textarea><br>
        <input type='submit' value='Send'>
      </form>
      <p>{{ message }}</p>
    {% endblock %}
    """, base=base_template, message=message)

if __name__ == '__main__':
    app.run(debug=True) 