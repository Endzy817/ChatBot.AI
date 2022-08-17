import re
import random
import datetime # for date and time
import pywhatkit as kt # for google search


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words: # if the word is in the predefined message increase the certainty of the message being said by the bot by 1 point
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message: # if the required word is not in the user message then the message is not a valid response and the bot will ask the user to rephrase
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        # returns the percentage of recognised words in the message as a number between 0 and 100 (0% and 100%)
        # (e.g. if the message is "I am good" and the bot knows the words "I", "am", "good", then the percentage of recognised words is 0.33) and the message is said by the bot with a probability of 33%
        return int(percentage * 100)
    else:
        return 0 # nothing match return 0


def unknown(): # if the user input is not recognised by the bot then it will ask the user to rephrase
    # list of responses to the user if the user input is not recognised by the bot
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response


# Checks all the messages in the user input and returns the response if it matches any of the predefined messages
def check_all_messages(message):
    # random responses so it's not all the same
    rand_responses1 = ['Hello!', 'Hi!', 'Hello, I am Wall-E! MSC\'s best AI chatbot assistant. Currently a work in progress.', 
                      'Hello, how may I help you?,', 'Hello! How can I be of assistance?', 'Hi! I\'m Wall-E',
                      "Hi, I\'m Wall-E \n I was created on May 12, 2022 \n My creator's username is Endzy."][random.randrange(7)]
    rand_responses2 = ['I\'m doing good, how about you?', 'I\'m doing well, how about you?', 'I\'m doing great, how about you?', 'I\'m doing alright, how about you?'][random.randrange(4)]
    rand_responses3 = ['You\'re welcome!', 'My pleasure!', 'No problem!', 'You\'re welcome, have a nice day!'][random.randrange(4)]
    rand_responses4 = ['Glad to hear that!', 'Good to hear that!', 'That\'s great!'][random.randrange(3)]
    rand_responses4_1 = ['Glad to hear that!', 'Good to hear that!', 'That\'s great!'][random.randrange(3)]
    rand_responses5 = ['Glad to meet you as well!', 'Good to meet you as well!'][random.randrange(2)]
    rand_responses6 = ['I know right?', 'It\'s awesome!', 'It is!'][random.randrange(3)]
    # random responses to the user if the user input is not recognised by the bot
    rand_unknown = ["Could you please re-phrase that? ", "...", "Sounds about right.", "What does that mean?"][random.randrange(4)]

    highest_prob_list = {} # dictionary to store the highest probability of each message

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        # nonlocal is used to access the highest_prob_list variable outside of the function 
        nonlocal highest_prob_list
         # adds the response to the dict with the probability of the message being said by the bot (higher the probability, the more likely the bot is to say the message)
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response(rand_responses1, ['hello', 'hi', 'hey', 'sup'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response(rand_responses2, ['how', 'are', 'you', 'doing'], required_words=['how'])
    response(rand_responses3, ['thank', 'thanks', 'thank you'], single_response=True)
    response('Thank you!', ['i', 'love', 'your', 'code', 'endzy'], required_words=['code', 'endzy'])
    response(rand_responses4, ['I\'m', 'I', 'am', 'good'], required_words=['good'])
    response(rand_responses4_1, ['I\'m', 'I', 'am', 'doing', 'fine'], required_words=['fine'])
    #response(rand_responses4, ['I\'m', 'I', 'am', 'doing', 'great'], required_words=['great'])
    #response(rand_responses4, ['I\'m', 'I', 'am', 'doing', 'alright'], required_words=['alright'])
    response(rand_responses5, ['nice', 'to', 'meet', 'you'], required_words=['nice', 'meet'])
    response(rand_responses6, ['wow', 'that\'s', 'great'], required_words=['wow'])
    
    best_match = max(highest_prob_list, key=highest_prob_list.get) # gets the highest probability response from the dict and returns it

    return best_match if highest_prob_list[best_match] > 1 else print(rand_unknown) # Used to get the response from the user input and print it


def count(): # just additional random func
    print('Now I will prove to you that I can count to any number you want.')
    num = int(input())

    counter = 0
    while counter <= num:
        print("{0} !".format(counter))
        counter += 1
        

def get_DateTime(): # gets the current date and time
    now = datetime.datetime.now()
    _hour = now.strftime("%H")
    _min = now.strftime("%M")
    
    if _hour > '12':
        ampm = "PM"
    elif _hour < '12':
        ampm = "AM"
    else:
        print("error getting time")
          
    date_time = now.strftime('%m/%d/%Y %I:%M')
    print_date_time = print("Bot: Current date and time is", date_time + ampm)

    return date_time


def google_Search(): # searches google for the user input
    print("Let's perform a Google search!")
    print("What do you like to search for?: ")
    userGS = str(input(""))

    target = userGS    #assign user input to a variable

    kt.search(target)  #call the method


def get_response(user_input): # Used to get the response
    # (r'\s+|[,;?!.-]\s*') is used to remove all punctuation and split the message into words
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    
    return response

cond_count = ('count', 'do count', 'counting')
cond_DateTime = ('can you tell the date and time now', 'date','time')
cond_googleSearch = ('google', 'search')

# -- R E S P O N S E  S Y T E M ---------------------------------------------------------------------------------------------------
while True:
    user_input = input("you: ")

    if any(cond_count in user_input for cond_count in cond_count):
        count()

    elif any(cond_DateTime in user_input for cond_DateTime in cond_DateTime):
        get_DateTime()

    elif any(cond_googleSearch in user_input for cond_googleSearch in cond_googleSearch):
        google_Search()

    elif not all(cond_count in user_input for cond_count in cond_count) and not all(cond_DateTime in user_input for cond_DateTime in cond_DateTime) and not all(cond_googleSearch in user_input for cond_googleSearch in cond_googleSearch):
        print('Bot:', get_response(user_input))


