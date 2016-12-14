import json
from bs4 import BeautifulSoup
import urllib
# import time
# import random
import rake
from pymongo import MongoClient
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

kw_list = ["sort", "exception", "difference", "arrayindexoutofboundsexception", "function"]
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
		if(len(kw_result) == 1): break
	return kw_result

num_items = 0
tot_items = 0
# lines = ['http://stackoverflow.com/questions/513832/how-do-i-compare-strings-in-java']
word_dic = {}
single_key_list = []

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
	vote = int(tag_vote.string)

	# exclude vote less than 10
	if(vote < 10): continue
	
	question = soup.find('h1', {'itemprop': 'name'}).string

	tag_first_ans = tag.find('td', { 'class' : 'answercell'})	
	for tag_first_ans_segment in tag_first_ans.findAll(['p', 'pre', 'li']):
		answer += str(tag_first_ans_segment)
	answer = answer + "</body></html>"
	

	tag_ques_post = soup.find('td', { 'class' : 'postcell'})
	for tag_ques_post_segment in tag_ques_post.findAll('p'):
		if tag_ques_post_segment.find('pre'): continue
		for tag_pos in tag_ques_post_segment.strings:
			question_post += tag_pos + " "

	keywords = get_keywords(question_post + " " + question)

	# for key in keywords:
	# 	word_dic[key] = word_dic.get(key, 0) + 1

	if len(keywords) == 0:
		continue
	elif keywords[0] in kw_list:
		num_items += 1
	elif keywords[0] not in single_key_list:
		single_key_list.append(keywords[0])
	else:
		continue
			
	# insert in to mongodb: database - record; collection - records
	db = client['record']
	collection = db['records']
	insertID = collection.insert({
		"link" : link,
		"answer" : answer,
		"question" : question,
		"keyword" : keywords,
		"votes" : vote,
		"__v" : 0
	})

	# accumulate keyowrds together
	key_list = ""
	for w in keywords:
		key_list += w + " "
	
	
	# insertID = num_items    # temporary insertID
	
	# print I_splitter + str(insertID)
	# print Q_splitter + str(question) + "\n" + str(question_post)
	# print L_splitter + link
	# print K_splitter + key_list
	# print A_splitter + str(vote) + "\n" + str(answer) + "\n\n"


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

	tot_items += 1
	if num_items == 20 or tot_items == 300: break
	
	# break
print num_items
print tot_items
for item in single_key_list:
	print item
# print json.dumps(word_dic, indent = 2, sort_keys = True)