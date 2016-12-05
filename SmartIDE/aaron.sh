#!/bin/bash
osascript -e 'tell application "Terminal" to do script "cd /Users/BondK/Cloud/Dropbox/SJSU/CMPE272/Fall16-Team6/SmartIDE; python controller/controller.py"'
osascript -e 'tell application "Terminal" to do script "cd /Users/BondK/Cloud/Dropbox/SJSU/CMPE272/Fall16-Team6/SmartIDE; python GoogleAPI_DatParser/GoogleAPI/googleapi.py"'
osascript -e 'tell application "Terminal" to do script "cd /Users/BondK/Cloud/Dropbox/SJSU/CMPE272/Fall16-Team6/SmartIDE; mongod --dbpath Ani/272_Team6_ProjectRabbitMqServer/data --port 27017"'
# osascript -e 'tell application "Terminal" to do script "cd /Users/BondK/Cloud/Dropbox/SJSU/CMPE272/Fall16-Team6/SmartIDE; /usr/local/sbin/rabbitmq-server start"'
osascript -e 'tell application "Terminal" to do script "cd /Users/BondK/Cloud/Dropbox/SJSU/CMPE272/Fall16-Team6/SmartIDE; nvm use --delete-prefix v6.9.1; node Ani/272_Team6_Project/bin/www"'
osascript -e 'tell application "Terminal" to do script "cd /Users/BondK/Cloud/Dropbox/SJSU/CMPE272/Fall16-Team6/SmartIDE/Ani; nvm use --delete-prefix v6.9.1; node 272_Team6_ProjectRabbitMqServer/server.js"'



