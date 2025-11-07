import sqlalchemy

class Post:

	def __init__(self):
		pass

	def open_connection(self):
		pass

	def close_connection(self):
		pass

	def get_post(self, id_post):
		pass

	def add_post(self, post):
		"""
		post - словарь, примерная структура которого:
		{'name_post': 'text_post', 'autor': 'nickname', 'datetime': datetime}
		Так как, скорее всего, будет один автор (я), тогда ключ 'autor' можно
		убрать. При добавлении в бд эти данные должны быть добавлены, а
		также не забыть установить id для каждого поста. И по id выдавать
		соответсвующий пост.
		"""

	def del_post(self, id_post):
		pass