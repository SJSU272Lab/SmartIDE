# import json
from bs4 import BeautifulSoup
import urllib
# import time
# import random
import rake
from pymongo import MongoClient
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


outTextFile = 'data/QA_ori.data'
outListFile = 'data/url_ori.list'

I_splitter = "===ID===\n"
Q_splitter = "===QUESTION===\n"
L_splitter = "===LINK===\n"
K_splitter = "===KEYWORDS===\n"
A_splitter = "===ANSWER===\n"

client = MongoClient()

with open(outListFile) as f:
    lines = f.readlines()

def get_keywords(paragraph):
    kw_result = []
    rake_object = rake.Rake("SmartStoplist.txt", 3, 1, 1)
    keywords = rake_object.run(paragraph)
    for word in keywords:
        kw_result.append(word[0])
        if(len(kw_result) == 5): break
    return kw_result

num_items = 0

# lines = ['http://stackoverflow.com/questions/513832/how-do-i-compare-strings-in-java']

for line in lines:
	link = line.rstrip('\n');
	htmltxt = urllib.urlopen(link).read()
	soup = BeautifulSoup(htmltxt, "html.parser")
	
	vote = ""
	question = ""
	question_post = ""
	answer = "<html><body>"
	keywords = []
	
	tag = soup.find('div', { 'class' : 'answer'})
	if tag == None: continue

	# find vote tag
	tag_vote = tag.find('span', { 'class' : 'vote-count-post'})
	vote = tag_vote.string

	# exclude vote less than 10
	if(vote < 10): continue
	
	question = soup.find('h1', {'itemprop': 'name'}).string

	tag_first_ans = tag.find('td', { 'class' : 'answercell'})	
	for tag_first_ans_segment in tag_first_ans.findAll(['p', 'pre']):
		answer += str(tag_first_ans_segment)
	answer = answer + "</body></html>"
	

	tag_ques_post = soup.find('td', { 'class' : 'postcell'})
	for tag_ques_post_segment in tag_ques_post.findAll('p'):
		if tag_ques_post_segment.find('pre'): continue
		for tag_pos in tag_ques_post_segment.strings:
			question_post += tag_pos + " "

	keywords = get_keywords(question_post + " " + question)


	db = client['record']
	collection = db['records']
	insertID = collection.insert({
		"link" : link,
		"answer" : answer,
		"question" : question,
		"keyword" : keywords,
		"votes" : vote
	})

	# print Q_splitter
	# print link
	# print question
	# print question_post
	# print "\n"
	# print A_splitter
	key_list = ""
	for w in keywords:
		key_list += w + " "
	
	# print key_list + "\n"
	# print answer

	f_ptr = open(outTextFile, 'a')
	try:
		f_ptr.write(I_splitter + str(insertID) + "\n")
		f_ptr.write(Q_splitter + str(question) + "\n" + str(question_post) + "\n")
		f_ptr.write(L_splitter + link + "\n")
		f_ptr.write(K_splitter + key_list + "\n")
		f_ptr.write(A_splitter + str(vote) + "\n" + str(answer) + "\n\n")	
	except Exception, e:
		print e		
	f_ptr.close()

	num_items += 1
	if num_items == 500: break
	
	# break
