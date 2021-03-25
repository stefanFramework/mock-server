from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {
        'id': '1',
        'title': 'Hacer las compras',
        'description': 'Ir al supermercado y comprar comida y articulos de limpieza',
        'done': False
    },
    {
        'id': '2',
        'title': 'Limpiar la Casa',
        'description': 'Hacer la cama, limpiar el living y la cocina',
        'done': False
    },
    {
        'id': '3',
        'title': 'Lavar la ropa',
        'description': 'Lavar la ropa y las sabanas',
        'done': False
    }
]

@app.route('/')
def index():
    return jsonify(tasks)

@app.route('/task', methods=['POST'])
def store():
    input_data = request.form

    if not input_data.get('title', None):
        return 'Invalid input data', 400

    last_task = max(tasks, key=lambda t: t['id'])

    new_task = {
        'id': int(last_task['id']) + 1,
        'title': input_data.get('title'),
        'description': input_data.get('description', ''),
        'done': False
    }
    tasks.append(new_task)
    return jsonify(new_task['id']), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)