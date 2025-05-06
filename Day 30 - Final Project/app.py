from flask import Flask, render_template, jsonify, request
from database import db, Task

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db.init_app(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'POST':
        new_task = Task(
            title=request.json['title'],
            description=request.json.get('description', '')
        )
        db.session.add(new_task)
        db.session.commit()
        return jsonify({"message": "Task created"}), 201
    
    tasks = Task.query.all()
    return jsonify([{
        "id": task.id,
        "title": task.title,
        "description": task.description
    } for task in tasks])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)