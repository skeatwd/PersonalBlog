from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

from post_management import Post
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
		title = request.form.get('title_post')
		datetime_now = datetime.now()
		date_now = datetime_now.date()
		time_now = datetime_now.time()
		post_dict = {'title': title, 'content': text, 'creation_date': date_now, 'creation_time': time_now}
		create = Post()
		create.add_post(post_dict)
		return '<h1>Greate!</h1>'

@app.route('/error')
def error():
	return render_template('/error.html')


if __name__ == '__main__':
	Post.create_table()
	app.run(debug=True)