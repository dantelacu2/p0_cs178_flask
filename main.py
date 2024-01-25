from flask import Flask, jsonify

app = Flask(__name__)

# In-memory database
database = [
  {'id': 1, 'name': 'Item 1'},
  {'id': 2, 'name': 'Item 2'},
  {'id': 3, 'name': 'Item 3'}
]

@app.route('/hello')
def hello_world():
  return 'Hello, World!'

@app.route('/info/<int:item_id>')
def get_info(item_id):
  item = next((item for item in database if item['id'] == item_id), None)
  
  if item:
    return jsonify(item)
  else:
    return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
  app.run(debug=True)
