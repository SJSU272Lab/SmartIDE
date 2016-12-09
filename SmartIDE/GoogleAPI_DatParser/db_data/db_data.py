import json
from bs4 import BeautifulSoup
import urllib
import time
import random
import rake
from googleresult import *
import pymongo

outTextFile = 'data/db.json'

Q_splitter = "===QUESTION===\n"
A_splitter = "===ANSWER===\n"


#for page_num in range(1,1000):
for page_num in range(1001,4000):

	print "########### " + str(page_num)
	# given the stackoverflow page  get the all links  1~1000
	# http://stackoverflow.com/questions/tagged/java?page=10000&sort=frequent&pagesize=20
	htmltxt = urllib.urlopen("http://stackoverflow.com/questions/tagged/java?page="+str(page_num)+"&sort=frequent&pagesize=20").read()
	#print "http://stackoverflow.com/questions/tagged/java?page=1&sort=frequent&pagesize=20"
	soup = BeautifulSoup(htmltxt, "html.parser")
	lists = []

	root = "http://stackoverflow.com"
	for tag1 in soup.findAll('div', { 'class' : 'question-summary'}):
		lists.append(root+str(tag1.find('a', { 'class' : 'question-hyperlink'})['href']))
		#print str(tag1['href'])
	for s in lists:
		print s
		f_ptr = open(outListFile, 'a')
		f_ptr.write(s+"\n")		
		f_ptr.close()
		time.sleep(random.randint(0,1))

		# for each links get the answer and result
		#http://stackoverflow.com/questions/35324030/disabling-hibernate-validation-for-specific-methods
		htmltxt = urllib.urlopen(s).read()
		soup = BeautifulSoup(htmltxt, "html.parser")

		# parse single answer
		questions = ""
		tag1 = soup.find('a', { 'class' : 'question-hyperlink'})
		questions = tag1.text
		#print questions

		ans = ""
		tag = soup.find('td', { 'class' : 'answercell'})
		if tag != None:
			for tag_in in tag.findAll(['p', 'pre']):
				for tag_string in tag_in.strings:
					ans += tag_string
					answer = ans

		#print ans
		f_ptr = open(outTextFile, 'a')
		try:
			f_ptr.write(Q_splitter+str(questions)+"\n")
			f_ptr.write(A_splitter+str(ans)+"\n\n")	
		except Exception, e:
			print e
			
			
		f_ptr.close()
