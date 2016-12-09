import json
from bs4 import BeautifulSoup
import urllib
# from googleapiclient import discovery
# import sys
# from oauth2client.client import GoogleCredentials
# from google.cloud import language
# import rake
# import operator

class googleresult(object):
	def __init__(self, ques, lnk):
		self.question = ques
		self.link = lnk
		htmltxt = urllib.urlopen(lnk).read()
		self.soup = soup = BeautifulSoup(htmltxt, "html.parser")
		self.answer = ""
		self.keywords = []
		self.vote = 0
	def get_ques(self):
		return self.question
	def get_link(self):
		return self.link
	def get_dict(self):
		return {"question": self.get_ques(), "link": self.get_link(), "answer": self.get_ans(), "vote": self.get_vote()}
	def get_ans(self):
		# if tag != None:
		# 	for tag_in in tag.findAll(['p', 'pre']):
			
		''' parse multi answers
		for tag in self.soup.findAll('td', { 'class' : 'answercell'}):
			ans = ""
			for tag_all in tag.findAll(['p', 'pre']):
		
				for tag_in_p in tag_all.strings:
					ans += tag_in_p
			self.answer.append(ans)
		'''
		# parse single answer
		ans = "<html><body>"
		tag = self.soup.find('td', { 'class' : 'answercell'})
		if tag != None:
			
			for tag_ans in tag.findAll(['p', 'pre']):
				ans += str(tag_ans)
				# return string format instead of html format
				# for tag_string in tag_ans.strings:
				# 	ans += tag_string
		ans = ans + "</body></html>"
		self.answer = ans
		return self.answer
	def get_keywords(self):
		# use google natural language for keyword extraction
		# pip install --upgrade google-cloud 

		myKey = "AIzaSyB5WuNAoxjfDMdxbKzmReBSgWgOrJUrwwI"
		lang_service = discovery.build('language', 'v1beta1', developerKey= myKey)
		the_data = {"document": {"content": "The cat sat on the mat", "type": "PLAIN_TEXT"}, "encodingType":"UTF8","features": {"extractSyntax": True}}
		ret = lang_service.documents().analyzeEntities(body = the_data).execute()
		# client = language.Client()
		# document = client.document_from_html(self.answer)
		# entities = document.analyze_entities()
		# for entity in entities:
		# 	if entity.salience > 0.4:
		# 		print entity.name
		# 		self.keywords.append(entity.name)
		print json.dumps(ret, indent=2)
		return self.keywords
		'''
		# use entire paragraph and use rake for keyword extraction
		htmltxt = urllib.urlopen(self.link).read()
		soup = BeautifulSoup(htmltxt, "html.parser")
		tag = soup.find('td', { 'class' : 'answercell'})
		paragraph = ""
		if tag != None:
			for tag_in in tag.findAll(['p']):
				for tag_string in tag_in.stripped_strings:
					paragraph += tag_string
		paragraph = self.question + ". " + paragraph
		return paragraph
		'''
	def get_vote(self):
		tag = self.soup.find('div', { 'class' : 'answer'})
		if tag != None:
			tag_vote = tag.find('span', { 'class' : 'vote-count-post'})
			# self.vote = int(tag_vote.strings)
		self.vote = int(tag_vote.string)
		return self.vote


