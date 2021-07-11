from flask import Flask, jsonify, request
from flask.templating import render_template

app = Flask(__name__)

@app.route('/login')
def login():
  username = request.args.get('user_name')
  passwd = request.args.get('pw')
  email = request.args.get('email_address')
  print(username, passwd, email)

  if username == 'chan':
    return_data = {'auth':'success'}
  else:
    return_data = {'auth':'failed'}
  return jsonify(return_data)

@app.route('/html_test')
def hello_html():
  return render_template('login_test.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port='8080')

