# SMART IDE 
*Team6*

## Abstract

As programmers, when writing code, we come across errors. It is very often we have to open our browsers and search for solutions manually. This takes time and sometimes we don't even know the right question to ask to get relative answers. Our idea is to develop a plugin tool or a new function on existing open source IDE to make it "smarter". We expect our new function could be able to improve IDE, such as Eclipse, not only fixing syntax or semantic errors, but also tries to provide solutions for other compiler and runtime errors which current IDE do not provide. 

## Mechanism

Our structure is illustrated as the figure below. When encountering an error for the first time, SMART IDE directly provide the result through Google searching. Then it stores this question and answer pair in our database. In future, when other users come across same problem, the SMART IDE will first look through our database for the answer before searching Google. Furthermore, we would like to incorporate machine learning to analysis our Q&A pairs in our database. First, it will categorize questions so there would not be repeating questions. Secondly, since there might be different answers for each question, we would recommend the most suitable answer base on current situation.

![Structure](https://github.com/kanghuawu/Fall16-Team6/blob/master/abstract/abstract.png)


## Senario

### Example 1
George, a new Java programmer, wanted to start his first line of code. However, he accidently deleted `M` in the class name. 

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

### Example 2
Let's take look at another example. Anita who a software programmer is currently working on a project. She needed to insert strings into `map` and `set` within the map. She is struggle writting the code she wanted since she used to work in python not C++.

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

Those two examples are very common problems even for experienced programmers. The first one is that we simply do not understand error messages. The latter one is not know the laguage very well. In old fashion, both demonstrate one common thing: Open browser and google it! We would like to improve our productivity and make the lives earsier for other software developers as well.
