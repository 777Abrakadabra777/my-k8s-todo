from flask import Flask, jsonify, request

app = Flask(__name__)
tasks = []

@app.route('/')
def root():
    return 'Todo API is running. Use /tasks endpoint.'

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task = {'id': len(tasks) + 1, 'title': data.get('title')}
    tasks.append(task)
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
