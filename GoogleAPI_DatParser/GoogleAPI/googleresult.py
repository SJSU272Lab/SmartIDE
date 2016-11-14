import json
from pprint import pprint


class googleresult(object):
	def __init__(self, ques, lnk):
		self.question = ques
		self.link = lnk
	def get_ques(self):
		return self.question
	def get_link(self):
		return link
	def get_dict(self):
		return {"question:": self.question, "link": self.link}
