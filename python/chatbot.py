import shlex
import googletrans 
import wikipediaapi
import pandas as pd
from autocorrect import Speller
from nltk.chat.util import Chat, reflections
from nltk.tokenize import wordpunct_tokenize
from stopwords import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
from language_pairs import pairs
from nltk.corpus import wordnet


def generate_token(msg):
    """Tokenize response and remove all stop words to simplify the statement"""
    text_tokens = wordpunct_tokenize(msg)
    tokens_without_sw = [word for word in text_tokens if not word in stopwords]
    print("Generated tokens: ", " ".join(tokens_without_sw))
    return " ".join(tokens_without_sw)

wiki = wikipediaapi.Wikipedia('en')

def Check_Wiki_Querry(msg):
    cutmsg = shlex.split(msg)

    #what are the some interesting things you know?
    if msg == 'what are the some interesting things you know?' or msg == 'what cool topics do you know' or msg == 'what interesing topics do you know' or msg == 'tell me something interesting':
        dfs = pd.read_html("https://en.wikipedia.org/wiki/Wikipedia:Top_25_Report")
        rtn_str = "Choose a topic, Sir: \n" + ", ".join(dfs[2]["Article"][0:5])# + ", \n" + dfs[2]["Article"][1] + ", " + dfs[2]["Article"][2] + ",\n" +  dfs[2]["Article"][3] + ", and " + dfs[2]["Article"][4] 
        return rtn_str + "\nand Sir, make sure to surround the topic with '_'"


    #what do you know about " "    #can you tell me about " "    #what can you tell me about 
    if msg[0:23] == 'what do you know about ' or msg[0:27] == 'what can you tell me about ' or msg[0:22] == 'can you tell me about ' or msg[0:14] == 'tell me about ' or msg[0:36] == 'tell me something interesting about ':
        
        page = wiki.page(cutmsg[-1])
        if not page.exists():
            return "I am sorry sir, what were you intereseted in? Remember to suround the topic with '_'"

        i = page.summary[0:500].rfind('.')
        if i == -1:            
            rtn_str = page.summary
        else: 
            rtn_str = page.summary[0:i+1]
        return rtn_str + "\nIf you would like related topics, Sir, write \"what topics are related to '"+cutmsg[-1]+"'\""

    #how many different topics involve " "
    if msg[0:27] == 'what topics are related to ':

        page = wiki.page("Category:"+cutmsg[-1])
        if not page.exists():
            return "I am sorry Sir, what were you intereseted in? Remember to suround the topic with '_'"
        
        temp = []
        for c in page.categorymembers.values():
            temp.append("'"+c.title+"'")
        rtn_str = ", ".join(temp[1:6])
        return rtn_str

#texTrans is a varaible that saves what a phrase means when the User checks what language it belongs to.
textTrans = None

def Check_Translation_Querry(msg):
    global textTrans
    translator = googletrans.Translator()

    #cutmsg will be used to clean the input given.
    cutmsg = shlex.split(msg)

    #Checks to see if *what language is* question asked, if not responds confused.
    if msg == 'what does it mean' and textTrans is not None:
        return textTrans
    elif msg == 'what does it mean' and textTrans is None:
        return "I am not sure what 'it' you refer to. Sir, please ask again"

    #Check what language is 'nacht der untoten' written in
    elif msg[0:17] == 'what language is ':
        result = translator.translate(cutmsg[3])

        textTrans = "it means '" + result.text + "'"
        return "That language is " + googletrans.LANGUAGES[result.src] + ", sir"

    #Check is the language of 'blank' *french*
    elif msg[:19] == 'is the language of ':
        result = translator.translate(cutmsg[4])

        if cutmsg[5] == googletrans.LANGUAGES[result.src]:
            return "You are correct, sir. The language is " +  googletrans.LANGUAGES[result.src]
        else:
            return "Sorry sir, but the language is " + googletrans.LANGUAGES[result.src]

    #Check what does 'nacht der untoten' mean 
    elif msg[0:10] == 'what does ':
        result = translator.translate(cutmsg[2])
        
        textTrans = None  
        return "The phrase you gave me means '" + result.text + "'" 

    #Check what does this mean 'nacht der untoten'
    elif msg[:19] == 'what does this mean':
        result = translator.translate(cutmsg[-1])
        
        textTrans = None
        return "The phrase you gave me means '" + result.text + "'"
    
    #Check can you translate 'night of the undead' into german
    elif msg[:18] == 'can you translate ':
        try:
            googletrans.LANGCODES[cutmsg[-1]]
        except:
            return 'I am sorry sir, that language eludes my knowledge' 
        result = translator.translate(cutmsg[3], dest=googletrans.LANGCODES[cutmsg[-1]])
        textTrans = None
        return "sure, here is the translated phrase:\n'" + result.text + "'" 
    
    #Check please translate " " into " "
    # or translate " " into " "
    elif cutmsg[-2] == 'into' and cutmsg[-4] == 'translate':
        try:
            googletrans.LANGCODES[cutmsg[-1]]
        except:
            return 'I am sorry sir, that language eludes my knowledge' 
        print(cutmsg[-3])
        result = translator.translate(cutmsg[-3], dest=googletrans.LANGCODES[cutmsg[-1]])
        textTrans = None
        return "the translated phrase is:\n'" + result.text + "'"

def Detect_Synonym(msg):
    text_tokens = msg.split()                           ## tokenizes based on spaces, does not make `'` a separate token
    pair_tokens = []
    for elem in pairs:
        pair_tokens.append(elem[0].split())

    new_input = []
    for elem in pair_tokens:
        if len(elem) is not len(text_tokens):           ## checks token length of user input, and makes sure it matches expected pair (EP)input
            continue
        
        new_input = []
        for i in range(len(text_tokens)):               ## loops through each work/token in EP input 
            if elem[i] == text_tokens[i]:                         
                new_input.append(elem[i])               ## if the the two words match, add to  
            else:
                for syn in wordnet.synsets(elem[i]):    ## if they do not match, loop thru EP input word synonyms, 
                    found = False

                    for l in syn.lemmas():
                        if l.name() == text_tokens[i]:  ## if the proposed synonym matches the user input
                            new_input.append(elem[i])   ## add the synonym to te new_input, then break out of two loops
                            found = True
                            break
                    if found:
                        break

    return " ".join(new_input)                          ## Makes the new_input list a string unput


class Botler:
    """This is the bolter class it is in charge of maintaining the conversation"""

    def __init__(self):
        """Creates chat object from NLTK"""
        self.chat = Chat(pairs, reflections)
        self.name = "Botler"
        self.sentiment_analyzer = SentimentIntensityAnalyzer()
        self.speller = Speller()

    def generate_response(self, msg):
        # Correct any spelling mistakes
        clean_input = self.speller(msg)

        # Check translations
        
        response = Check_Translation_Querry(msg)

        if not response:
            response = Check_Wiki_Querry(msg)

        if not response:
            response = Check_Wiki_Querry(clean_input)

        # Generate a response from the chatbot
        if not response:
            response = self.chat.respond(clean_input)


        # If response is still none, tokenize words and try again
        if not response:
            tokens_without_sw = generate_token(clean_input)
            response = self.chat.respond(tokens_without_sw)
        
        if not response:
            response = self.chat.respond(Detect_Synonym(clean_input))

        # Getting sia_value to hold the dictionary from polarity_scores
        sia_value = self.sentiment_analyzer.polarity_scores(clean_input) 

        # sia_value['compound'] holds overall sentiment. 

        if response:
            return response
        elif sia_value['compound'] <= -0.5:
            return("I'm sorry you feel that way, but I am\nunable to fix this for you.\nPlease ask something different.")
        elif sia_value['compound'] >= 0.5:
            return("I'm happy to hear that sir,\nalthough I don't quite know what to do with that\ninformation.\nWould you mind asking something else?")
        else:
            return("I didn't quite hear that sir,\nwould you mind repeating that?")
        
