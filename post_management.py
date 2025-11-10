import sqlite3


class Post:

	@classmethod
	def create_table(cls):
		conn = sqlite3.connect('posts.db')
		cur = conn.cursor()
		cur.execute('''
				CREATE TABLE IF NOT EXISTS Posts (
					id INTEGER PRIMARY KEY NOT NULL,
					title TEXT NOT NULL,
					content TEXT NOT NULL,
					creation_date DATE NOT NULL,
					creation_time TIME NOT NULL)
				''')

		conn.commit()
		conn.close()

	def __init__(self):
		self.conn = sqlite3.connect('posts.db')

	def __del__(self):
		self.conn.close()

	def add_post(self, post) -> None:
		self.cur = self.conn.cursor()
		title = post['title']
		content = post['content']
		creation_date = post['creation_date'].strftime('%Y-%m-%d')
		creation_time = post['creation_time'].strftime('%H:%M:%S')
		self.cur.execute('INSERT INTO Posts(title, content, creation_date, creation_time) VALUES(?, ?, ?, ?)', (title, content, creation_date, creation_time))
		self.conn.commit()
		self.cur.close()