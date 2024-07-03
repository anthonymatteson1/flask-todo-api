# app.py

from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy data for initial testing
todos = [
    {'id': 1, 'title': 'Learn Flask', 'description': 'Learn how to create a RESTful API with Flask', 'completed': False},
    {'id': 2, 'title': 'Build TODO App', 'description': 'Build a TODO application using Flask and Vue.js', 'completed': False}
]

# Routes
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos/<int:id>', methods=['GET'])
def get_todo(id):
    todo = next((todo for todo in todos if todo['id'] == id), None)
    if todo:
        return jsonify(todo)
    else:
        return jsonify({'message': 'Todo not found'}), 404

@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    new_todo = {
        'id': len(todos) + 1,
        'title': data['title'],
        'description': data.get('description', ''),
        'completed': False
    }
    todos.append(new_todo)
    return jsonify(new_todo), 201

@app.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    todo = next((todo for todo in todos if todo['id'] == id), None)
    if not todo:
        return jsonify({'message': 'Todo not found'}), 404
    data = request.get_json()
    todo.update({
        'title': data['title'],
        'description': data.get('description', todo['description']),
        'completed': data.get('completed', todo['completed'])
    })
    return jsonify(todo)

@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    global todos
    todos = [todo for todo in todos if todo['id'] != id]
    return jsonify({'message': 'Todo deleted'})

if __name__ == '__main__':
    app.run(debug=True)
