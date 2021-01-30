
class MyException(Exception):
	def __init__(self, msg):
		self.args = (msg,)