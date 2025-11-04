from flask import Flask, render_template, request

import random_code

app = Flask(__name__)

ID_PAGE = 0


@app.route('/', methods=['GET', 'POST'])
def main():
	if request.method == 'GET':
		return render_template('index.html')
	elif request.method == 'POST':
		global ID_PAGE
		get_email = request.form.get('email')
		get_password = request.form.get('password')
		ID_PAGE = random_code.CODE
		random_code.send_email(get_email, get_password)
		return render_template('index.html')


@app.route('/admin/admminpage.html')
def return_secret_page():
	return render_template('/admin/admminpage.html')

@app.route('/admin/createPost.html', methods=['POST', 'GET'])
def create_post():
	if request.method == 'GET':
		return render_template('/admin/createPost.html')
	elif request.method == "POST":
		text = request.form.get('text_post')
		return f'<p>{text}</p>'


@app.route('/<int:id_page>')
def page(id_page):
	if id_page == ID_PAGE:
			return render_template('/admin/admminpage.html')
	else:
			return render_template('/error.html')



if __name__ == '__main__':
	app.run(debug=True)