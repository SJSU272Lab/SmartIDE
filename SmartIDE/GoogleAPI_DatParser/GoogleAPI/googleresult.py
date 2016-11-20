import json
from bs4 import BeautifulSoup
import urllib

class googleresult(object):
	def __init__(self, ques, lnk):
		self.question = ques
		self.link = lnk
		self.answer = ""
	def get_ques(self):
		return self.question
	def get_link(self):
		return self.link
	def get_dict(self):
		return {"question:": self.get_ques(), "link": self.get_link(), "answer": self.get_ans()}
	def get_ans(self):
		htmltxt = urllib.urlopen(self.link).read()
		soup = BeautifulSoup(htmltxt, "html.parser")
		''' parse multi answers
		for tag in soup.findAll('td', { 'class' : 'answercell'}):
			ans = ""
			for tag_all in tag.findAll(['p', 'pre']):
		
				for tag_in_p in tag_all.strings:
					ans += tag_in_p
			self.answer.append(ans)
		'''
		# parse single answer
		ans = ""
		tag = soup.find('td', { 'class' : 'answercell'})
		if tag != None:
			for tag_in in tag.findAll(['p', 'pre']):
				for tag_string in tag_in.strings:
					ans += tag_string
		self.answer = ans
		return self.answer
