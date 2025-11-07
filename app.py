from flask import Flask, render_template, request, redirect, url_for

import random_code

app = Flask(__name__)

SECRET_CODE = 0


@app.route('/', methods=['GET', 'POST'])
def main():
	if request.method == 'GET':
		return render_template('index.html')
	elif request.method == 'POST':
		global SECRET_CODE
		get_email = request.form.get('email')
		SECRET_CODE = random_code.RANDOM_CODE
		random_code.send_email(e=get_email)
		return redirect(url_for('varify'))

@app.route('/varify', methods=['GET', 'POST'])
def varify():
	if request.method == 'GET':
		return render_template('/checkingcode.html')
	elif request.method == 'POST':
		user_code = int(request.form.get('code'))
		if random_code.check_code(user_code):
			return redirect(url_for('admin'))
		else:
			return redirect(url_for('error'))

@app.route('/admin')
def admin():
	return redirect('create_post')

@app.route('/create_post', methods=['POST', 'GET'])
def create_post():
	if request.method == 'GET':
		return render_template('/admin/createPost.html')
	elif request.method == "POST":
		text = request.form.get('text_post')
		return f'<p>{text}</p>'

@app.route('/error')
def error():
	return render_template('/error.html')


if __name__ == '__main__':
	app.run(debug=True)