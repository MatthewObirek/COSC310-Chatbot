# M.A.A.M.Y's Chat Bot
Software Engineering Term 2, 2022

Our group has decide to create a chatbot using python. We have used the <a href="https://www.nltk.org/" target="_blank">***NLTK***</a> python Library in order to create our chatbot. The bot will be taking the role of a sassy, well educated, butler with a good scence of humour, meanwhile the user will take the role of its master.

In A3 we have made significant in terms of user experience with new GUI and also technical improvements in the conversation flow with help of sentiment analysis and autocorrect for spelling mistakes, which was not possible in our previous A2 version of the bot.

As we promised in the A2 version, "Future revisions and additions could improve versatility", we have delivered on that promise.

You can find a list of the features and improvements in A3 [here](#a3-features-and-improvements).

### API's used in Individual Asssignment

For the Individual Assignment, I added the <a href="https://pypi.org/project/googletrans/" target="_blank">***Google Translate***</a> API and the <a href="https://pypi.org/project/Wikipedia-API/" target="_blank">***Wikipedia***</a> API. The <a href="https://pypi.org/project/googletrans/" target="_blank">***Google Translate***</a> API is set up to translate other languages into English, or, if specified, another language. Just start by asking `do you translate?`. Botler will give you directions.
Examples of texr: `what does this mean: "Nacht der untoten"`, or `please translate "how are you" into french`. 
The <a href="https://pypi.org/project/Wikipedia-API/" target="_blank">***Wikipedia***</a> API is set up to give a little bit of information on a lot of topics. Using the page.summary function, Botler is able to provide a little bit of info for the reader. Just start by saying `tell me something interesing` and Botler will lead the way.

You can find the complete list of features and improvements done in the Individual Assignment [here](#ia-features-and-improvements).

The MIT liscence is in this same direcory and is named <a href="https://github.com/Software-Engineering-Group-4-Maamy/chat-bot/blob/main/LICENSE" target="_blank">LICENSE</a>.

## API's in use
The <a href="https://www.nltk.org/" target="_blank">***NLTK***</a> API - `pip install --user -U nltk`<br>
The <a href="https://pypi.org/project/ChatApp/" target="_blank">***ChatApplication***</a> API - `pip install chatapp` <br> 
The <a href="https://pypi.org/project/autocorrect/" target="_blank">***Autocorrect***</a> API - `pip install autocorrect`<br>
The <a href="https://pypi.org/project/googletrans/" target="_blank">***Google Translate***</a> API - `pip install googletrans==3.1.0a0`<br>
The <a href="https://pypi.org/project/pandas/" target="_blank">***Pandas***</a> API - `pip install pandas`<br>
The <a href="https://pypi.org/project/Wikipedia-API/" target="_blank">***Wikipedia***</a> API - `pip install wikipedia-api`<br>

## Instalation guide
1. First, install <a href="https://pip.pypa.io/en/stable/installation/">pip</a> if you have not already
2. Run `pip install --user -U nltk googletrans==3.1.0a0 wikipedia-api pandas autocorrect tk-tools chatapp lxml`
3. Then, clone this git reposotory, or download the zip file and move to the python directory. 
4. Inside the python directory, run the initlibs.py file `python initlibs.py`  
5. Then run the main.py file `python main.py`
6. Vouala - you now own a human soul.

## Sample output

A2: Terminal Conversation Flow

        B:Hi, I'm Botler want to have a conversation with you!
        B:Please speak to me in lowercase English. Type quit if you wish to end this conversation. 
        U:hello
        B:Greetings!
        U:my name is Matthew
        B:Hello matthew, How are you feeling today?
        U:I am a bit concerned about this recent stock market fiasco
        B:Do not be alarmed sir, I've handled your investments accordingly
        U:sorry for ever doubting you
        B:You needn't worry at all
        U:can you find the next best stock for me
        B:I am unable to search for the next best stock, for now.
        U:sorry for expecting so much
        B:You needn't worry at all
        U:have you seen my underwear?
        B:I believe you left it under your bed again sir
        U:I like underwear  
        B:Exquisite taste sir
        U:i am not a sir
        B:Apologies, but sir it is the best I can do.
        U:you're being difficult
        B:You literally programed me, I can only say what you allowed me to say
        U:i love you botler, and you have to love me back
        B:That is sweet sir, but I only think of you as a an aquaintence
        U:that was mean
        B:I am doing my best to be polite, you are just making it difficult
        U:yes    
        B:Glad we agree
        U:sorry botler, i was argumentative
        B:It is already forgiven.
        U:can you make me happy
        B:Of course, sire, I will get you happy but first I'll need milk, brb
        U:how long will it take you to make me happy
        B:I cannot say, an hour, a week maybe a decade.  You must find it in yourself to wait
        U:quit
        B:Thank you for chatting with me
	
## A3: Git Commit Graph

![Git Commit Graph](./python/CommitGraphA3.png)
	
## A3: Data Flow Diagrams

### Level 0:

![DFD Level 0](./python/DFD_level0.png)

### Level 1:

![DFD Level 0](./python/DFDLevel1.png)

Improved A3: GUI Conversation Flow

![GUI Image](./python/demo_ss.png)

As you can see, we can now handle upper case but also mixed case.
### Errors in output
        U:what's your favotite movie
        B:Sorry sir, I didn't understand
Botler responds this way because Botler cannot recognize a phraze that is not exactly the same as what it uses as examples.

## A3: Features and improvements

1. Case Handling: Botler now handles all types of cases lower, upper and mixed case.

        
        U: MY NaMe IS YasH
        Botler: Hello, how are you feeling today?
        

2. Sentiment Analysis: Botler now uses the <a href="https://www.nltk.org/api/nltk.sentiment.html" target="_blank">nltk.sentiment</a> to determine the sentiment of the user's input.

        U: THAT WAS MEAN
        B: I am doing my best to be polite, you are just making it difficult

3. Autocorrect: Botler now uses the ```Speller``` class from  <a href=https://github.com/filyp/autocorrect target="_blank">autocorrect</a> to correct the spelling of the user's input.
        
        U: Hellooo
        B: Salutations!

4. Unit Testing: Added unit tests for ```chatbot.py``` and ```app.py``` in the ```test_chatbot.py``` and ```test_app.py``` files respectively. These test whether the classes have been initialized correctly and whether the methods are working as expected.
More details about unit testing can be found [here](#unit-testing).

5. Phrasal: Botler now handles all types of input regardless of the exact wording of the statement.

        
        U: Sorry BolTer I didnt know
        Botler: You needn't worry at all

6. Further Prospective API abilities
 
	1) Autocorrect Function: The Botler could be utilized as a polite bot for implementing autocorrect.	
	2) Speech analysis: Understanding Speech patterns when learning a new language can be difficult. This process can be made easier by using Botlers synonym recognizer, allowing the identification of similar sentiments even when a different word is used. 
	3) Sentiment Analysis: Botler has an advanced understanding of the English lexicon and can help a user understand the tone of one’s email. 
	4) Continuous Chat: Botlers ability to handle long drawn out conversations can be utilized to handle email conversations you just really don’t want to have.
	5) Unique Dialogue Library: Botler can handle all your automated messages through use of its language library. This could be implanted as an API so that an email gets forwarded to it and the library would allow Botler to select the correct, and polite, reply. 

## IA: Features and Improvements
#### Part 1 - Translation
1. Language detection: botler can detect what language a phrase is written in, and tell the user that language.	
		
		U: what language is "nacht der untoten"
		Botler: That language is German, sir

2. Language translation to English: botler can translate phrases that are in other languages to English
	
		U: what does 'nacht der untoten' mean
		Botler: the phrase you gave me means 'Night of the Living Dead'
		
3. Language translation from English: botler can translate phrases to and from english, or any language.

		U: please translate 'I love you' into french
		Botler: the translated phrase is: 
		'Je vous aime'

4. Unknown language handling: aslong as that language is known.

		U: please translate 'I love you' into greyman
		Botler: I am sorry sir, that language eludes my knowledge

#### Part 2 - Wikipedia
1. Interesting topics: botler will suggest interesting topics based on the <a href="https://en.wikipedia.org/wiki/Wikipedia:Top_25_Report">Wikipedia:Top 25 Report</a> page

		You: tell me something interesting
		Botler: Choose a topic, Sir: 
		Jada Pinkett Smith, Will Smith, RRR (film), Chris Rock, 94th Academy Awards
		and Sir, make sure to surround the topic with '_'
		
2. Summarise topic: botler will provide a summary of a topic you are interested in

		You: tell me about "Will Smith"
		Botler: Willard Carroll  Smith II (born September 25, 1968), also known by his stage name the Fresh Prince[...]
		If you would like related topics, Sir, write "what topics are related to 'will smith'"
		
3. Related Topics: botler will give 5 related topics when the User gives a topic

		You: what topics are related to 'Awards'
		Botler: 'Badge of honour', 'Awards ceremony', 'EURYI', 'Internet Buzzword Award', 'Jagranjosh Education Award
## Class Organization

1. ***Botler:***
The Botler class is in charge of creating and maintaining all aspects of the chat object imported from the NLTK.

The Botler class has three members within it. `def __init__(self)`, `def converse(self)` and `def generate_response(self, msg)`. 

`__init__(self)` member acts as the Constructor for the Botler object. It creates the chat object as well.

`converse(self)` is now deprecated. But it used to start the conversation with a custom message. It also includes all of the error handling and logic required for the main conversation to take place with the chat bot.
to start a conversation, write this line of code: `ch.Botler().converse()`

`generate_response(self, msg)` generates a response for a specific message inputted by the user. 

2. ***ChatApplication:***
The ChatApplication class is in charge of creating and managing the application. That is it creates the corresponding GUI elements and then manages them. This class was adapted from the MIT licensed project titled <a href=https://github.com/python-engineer/python-fun>***Python Fun***</a> Under `python-fun/chatbot-gui/app.py`. 

This class has `_insert_message(self, msg, sender), _on_enter_pressed(self, event), run(self), _init_window(self), __init__(self)`

`_insert_message(self, msg, sender)` inserts a message to the GUI given a message and the name of the sender.

`_on_enter_pressed(self, event)` calls `_insert_message(self, msg, sender)` with the user's message and generates a response from the chatbot.

`run(self)` initiates the program by creating the window and starting the chatbot. It is the only public member of the class.

`_init_window(self)` creates the GUI and initializes all settings.

`__init__(self)` calls `_init_window(self)`, and initialises `Botler` in order to run the app.

### Unit Testing

The unit tests have been written with the help of the [unittest](https://docs.python.org/3/library/unittest.html) module, which is a unit testing framework inspired by JUnit of Java.

1. Unit Tests for ```app.py```

- ```def test_app_instances(self):```
        This tests whether the class has been initialized correctly. Checks all the various types of instances required to run the application and ensures that they are all initialized correctly.
- ```def test_app_title(self):```
        Tests whether the title of the window is correct.
- ```def test_app_insert_message(self):```
        Tests whether the message is inserted correctly in the GUI and passed to Botler.

2. Unit Tests for ```chatbot.py```

- ```def test_generate_token(self):```
        Tests whether the return type is a string so that it can be processed and understood by Botler.
        This is was required to test because tokenization splits a string into a list of words.
- ```def test_Botler_init_attributes(self):```
        Tests whether the Botler class has been initialized correctly by checking the instances of the various attributes it contains
- ```def test_Botler(self):```
        Tests whether the response generated by Botler is a string
