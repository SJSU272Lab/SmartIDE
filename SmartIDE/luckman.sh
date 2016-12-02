#!/bin/bash
# run controller
osascript -e 'tell application "Terminal" to do script "cd /Users/Luckman/Documents/SJSU/Course/2016_Fall/272/Final_Project/Fall16-Team6/SmartIDE; python controller/controller.py"'
# run googleapi
osascript -e 'tell application "Terminal" to do script "cd /Users/Luckman/Documents/SJSU/Course/2016_Fall/272/Final_Project/Fall16-Team6/SmartIDE; python GoogleAPI_DatParser/GoogleAPI/googleapi.py"'
# run monogoDB with dbpath Ani/272_Team6_ProjectRabbitMqServer/data
osascript -e 'tell application "Terminal" to do script "cd /Users/Luckman/Documents/SJSU/Course/2016_Fall/272/Final_Project/Fall16-Team6/SmartIDE; mongod --dbpath Ani/272_Team6_ProjectRabbitMqServer/data --port 27017"'
# run rabbit
osascript -e 'tell application "Terminal" to do script "cd /Users/Luckman/Documents/SJSU/Course/2016_Fall/272/Final_Project/Fall16-Team6/SmartIDE; /usr/local/sbin/rabbitmq-server start"'
# run restful service
osascript -e 'tell application "Terminal" to do script "cd /Users/Luckman/Documents/SJSU/Course/2016_Fall/272/Final_Project/Fall16-Team6/SmartIDE; node Ani/272_Team6_Project/bin/www"'
# run message queue service
osascript -e 'tell application "Terminal" to do script "cd /Users/Luckman/Documents/SJSU/Course/2016_Fall/272/Final_Project/Fall16-Team6/SmartIDE; node Ani/272_Team6_ProjectRabbitMqServer/server.js"'

# run QA
osascript -e 'tell application "Terminal" to do script "cd /Users/Luckman/Documents/SJSU/Course/2016_Fall/272/Final_Project/Fall16-Team6/SmartIDE/QA; python QA.py"'


