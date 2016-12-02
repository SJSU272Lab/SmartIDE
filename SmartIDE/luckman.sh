#!/bin/bash
osascript -e 'tell application "Terminal" to do script "cd /Users/Luckman/Documents/SJSU/Course/2016_Fall/272/project/Fall16-Team6/SmartIDE; python controller/controller.py"'
osascript -e 'tell application "Terminal" to do script "cd /Users/Luckman/Documents/SJSU/Course/2016_Fall/272/project/Fall16-Team6/SmartIDE; python GoogleAPI_DatParser/GoogleAPI/googleapi.py"'
osascript -e 'tell application "Terminal" to do script "cd /Users/Luckman/Documents/SJSU/Course/2016_Fall/272/project/Fall16-Team6/SmartIDE; mongod --dbpath Ani/272_Team6_ProjectRabbitMqServer/data --port 27017"'
osascript -e 'tell application "Terminal" to do script "cd /Users/Luckman/Documents/SJSU/Course/2016_Fall/272/project/Fall16-Team6/SmartIDE; /usr/local/sbin/rabbitmq-server start"'
osascript -e 'tell application "Terminal" to do script "cd /Users/Luckman/Documents/SJSU/Course/2016_Fall/272/project/Fall16-Team6/SmartIDE; node Ani/272_Team6_Project/bin/www"'
osascript -e 'tell application "Terminal" to do script "cd /Users/Luckman/Documents/SJSU/Course/2016_Fall/272/project/Fall16-Team6/SmartIDE; node Ani/272_Team6_ProjectRabbitMqServer/server.js"'



