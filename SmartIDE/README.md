# SMART IDE 
*Team6*

Slide:  https://www.dropbox.com/s/j0g5ylk2xw47xr1/Final%20Presentation.pdf?dl=0  
Report:  https://www.dropbox.com/s/5e1gr561aiurpee/FinalReport.pdf?dl=0    


## How to Run
[Step 0] Download and install the SmartIDE plugin on Netbeans

0. go to SmartIDE/build
1. download plugin file "org-myorg-smartide.nbm"
2. open Netbeans and go to Tools > Plugins > Downloads > Add Plugins...
3. select downloaded .nbm plugin file
4. click Install

[Step 1] Run Controller service

0. go to controller/
1. docker build -t controller .
2. docker run -d -p 1314:1314 controller

[Step 2] Run QA bot service

0. go to QA/
1. docker build -t qa .
2. docker run -d -p 2666:2666 qa

[Step 3] Run Google Search API service

0. go to GoogleAPI_DatParser/
1. docker build -t googleapi .
2. docker run -d -p 4000:4000 googleapi


[Step 4] Running the DB server is a two step process first we need to run message broker RabbitMQ and then we run the node js server, detailed steps are given, please follow the order.

a.Running the RabbitMQ Server 

0. go to /Ani/272_Team6_ProjectRabbitMqServer/
1. docker pull rabbitmq
2. docker run -d --hostname smartide-rabbit –name ide-rabbit rabbitmq:3
3. docker run -d --hostname smartide-rabbit --name some-rabbit -p 15672:15672 rabbitmq:3-management
4. docker build -f Dockerfile -t smartiderabbit/node .
5. docker run -d --name smartide-mongo mongo
6. docker run -d --name rabbit-server -p 7000:7000 --link smartide-mongo:mongodb --link ide-rabbit smartiderabbit/node

b.Running the Node Server

0. go to /Ani/272_Team6_Project/
1. docker build -f Dockerfile -t smartide/node .
2. docker run -d --name node-server -p 3000:3000 --link rabbit-server --link ide-rabbit smartide/node

## Abstract

As programmers, when writing code, we come across errors. It is very often we have to open our browsers and search for solutions manually. This takes time and sometimes we don't even know the right question to ask to get relative answers. Our idea is to develop a plugin tool or a new function on existing open source IDE to make it "smarter". We expect our new function could be able to improve IDE, such as Eclipse, not only fixing syntax or semantic errors, but also tries to provide solutions for other compiler and runtime errors which current IDE do not provide. 

## Mechanism

Our structure is illustrated as the figure below. When encountering an error for the first time, SMART IDE directly provide the result through Google searching. Then it stores this question and answer pair in our database. In future, when other users come across same problem, the SMART IDE will first look through our database for the answer before searching Google. Furthermore, we would like to incorporate machine learning to analysis our Q&A pairs in our database. First, it will categorize questions so there would not be repeating questions. Secondly, since there might be different answers for each question, we would recommend the most suitable answer base on current situation.

![Structure](abstract/abstract.png?raw=true)


## User Stories

### Persona 1
As a student, George wanted to understand the error of his code. He started his first line of code. However, he accidently deleted `M` in the class name. 

```java
class Printessage
{

   public static void main(String[] args) {
     
     System.out.println("Smart IDE Rocks");

   }
}
```

Therefore, when he tried to run the program, he received an error message he could not understand. Obviously, Eclipse has no way to help him.

```
Error: Could not find or load main class smartide.PrintMessage
```

Smart IDE first searched through our data base for similar questions. It revealed a human readable answer next to the error message where George could instantly understand the reason for this error. Also, SMART IDE would ask him if it can revise the error for him. 

### Persona 2
As a senior software programmer, Anita wanted to find methods for the language she is not familiar with. She needed to insert strings into `map` and `set` within the map. She is struggling writting the code she wanted since she does not work in C++ previously.

```c++
int main()
{      

  std::map<string, set<string> > m;

  m.insert ( std::pair<string, set<string> > ("car" , "orange") );

}

```
The SMART IDE found two methods in database and recommended both methods to her.

```c++

	set<string> myset;
	myset.insert("orange");

	//first method
	mymap["car"] = myset; //will overwrite existing data!!

	//second method
	mymap.insert(make_pair("car", myset));

```

Those two stories are very common problems even for both new and experienced programmers. The first one is that we simply do not understand error messages. The latter one is not knowing the laguage very well. In old fashion, both users would do one common thing: Open browser and google it! Creating a SMART IDE would improve our productivity and also make the lives earsier for other software developers.

# <a name="team-members"></a>Team Members
* "Aniruddha Pratap Singh" https://github.com/aniruddha-pratap
* "Janis Vasquez"  https://github.com/jcarolev
* "Kang-Hua Wu" https://github.com/kanghuawu
* "HsunFu Liu" https://github.com/lucky20511
