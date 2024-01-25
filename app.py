from flask import Flask, jsonify, session, request

app = Flask(__name__)

database = [
    {'id': 1, 'name': 'Item 1'},
    {'id': 2, 'name': 'Item 2'},
    {'id': 3, 'name': 'Item 3'}
]

app.secret_key = 'MOCK_KEY'

# CANDIDATE CONCEPT: Routing to functions
@app.route('/hello')
def hello_world():
  return 'Hello, World!'

# CANDIDATE CONCEPT: Input parameters
@app.route('/info/<int:item_id>')
def get_info(item_id):
  # Check if 'caller_id' is present in the session
  if 'caller_id' not in session:
    # Generate some random ID for callers
    session['caller_id'] = hash(request.headers.get('User-Agent'))

  caller_id = session['caller_id']

  item = next((item for item in database if item['id'] == item_id), None)

  if item:
    # Include caller_id in the response
    item['caller_id'] = caller_id
    return jsonify(item)
  else:
    return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
  # CANDIDATE CONCEPT: Input parameters
  app.run(debug=True)
