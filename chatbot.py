# Natural Language Toolkit: Chatbot Utilities
#
# Copyright (C) 2001-2017 NLTK Project
# Authors: Steven Bird <stevenbird1@gmail.com>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

# Based on an Eliza implementation by Joe Strout <joe@strout.net>,
# Jeff Epler <jepler@inetnebr.com> and Jez Higgins <jez@jezuk.co.uk>.
from __future__ import print_function

import re
import random


reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}

# a table of response pairs, where each pair consists of a
# regular expression, and a list of possible responses,
# with group-macros labelled as %1, %2.

pairs = (
  (r'(.*)Hello(.*)',
  ( "Hi! How may I help you?",)),

  (r'(.*)Add(.*)',
  ( "We're currently working on the feature. It will be deployed in the next update!\n-Team Wisopt",)),

  (r'(.*)would be nice(.*)',
  ("We're currently working on the feature. It will be deployed in the next update!\n-Team Wisopt",)),

  (r'(.*)include(.*)',
  ( "We're currently working on the feature. It will be deployed in the next update!\n-Team Wisopt",)),

  (r'(.*)no option(.*)',
  ( "Sorry for the inconvenience. We will resolve it asap.\n-Team Wisopt",)),

  (r'(.*)help me(.*)',
  ( "Kindly register with your credentials and then try to login. If the problem persists please email us your details\n-Team Wisopt",)),

  (r'(.*)Confusing(.*)',
  ( "We apologise for the confusion caused by us to you in our app. We will surely work on that and will reply to you for the same!\n-Team Wisopt",)),

  (r'(.*)Attendance(.*)',
  ( "We are working on that module, and will deploy this feature in our next update!\n-Team Wisopt",)),

  (r'(.*)Please Check(.*)',
  ( "We will check for the problem as soon as possible, and will report you for the same.\n-Team Wisopt",)),

  (r'(.*)Showing(.*)',
  ( "Sorry for the inconvenience. We will see to it.\n-Team Wisopt",))   ,

  (r'(.*)cant able(.*)',
  ( "Kindly check if you have updated the application. If the problem still persists, kindly inform us. We will take the necessary action as soon as possible.\n-Team Wisopt",)),

  (r"(.*)can't able(.*)",
  ( "Kindly check if you have updated the application. If the problem still persists, kindly inform us. We will take the necessary action as soon as possible.\n-Team Wisopt",)),

  (r'(.*)Can you(.*)',
  ( "Surely we will try to do so as soon as possible and we advise you to keep the app updated!\n-Team Wisopt",)),

  (r'(.*)Useful For(.*)',
  ( "Thanks for your valuable feedback.\n-Team Wisopt",)),

  (r'(.*)Add an option(.*)',
  ( "We are happy that you inspected our application and gave your precious time to us. We are glad. Thanks for your feedback.\n-Team Wisopt",)),

  (r'(.*)Forget(.*)Password(.*)',
  ( "please try clicking forgot password and verify your account.If you didn't receive any email doing this, please contact us again and it will be handled immediately.\n-Team Wisopt",)),

  (r'(.*)Forgot(.*)Password(.*)',
  ( "please try clicking forgot password and verify your account.If you didn't receive any email doing this, please contact us again and it will be handled immediately.\n-Team Wisopt",)),

  (r'(.*)incorrect email(.*)',
  ( "PLease recheck the email you are entering. If still the problem persist kindly inform us. We will take some action as quickly as possible.\n-Team Wisopt",)),

  (r'(.*)any email(.*)',
  ( "Sorry for the inconvenience. We are trying our best to resolve it. Have patience!\n-Team Wisopt",)),

  (r'(.*)confirmation email(.*)',
  ("Please try clicking forgot password and verify your account.If you didn't receive any email doing this, please contact us again and it will be handled immediately.\n-Team Wisopt",)),

  (r'(.*)confirmation mail(.*)',
  ("Please try clicking forgot password and verify your account.If you didn't receive any email doing this, please contact us again and it will be handled immediately.\n-Team Wisopt",)),

  (r'(.*)verify email(.*)',
  ("Please try clicking forgot password and verify your account.If you didn't receive any email doing this, please contact us again and it will be handled immediately.\n-Team Wisopt",)),

  (r'(.*)no mail(.*)',
  ("Sorry for the inconvenience. We will try our best to resolve it.\n-Team Wisopt",)),

  (r'(.*)verification(.*)',
  ( "Please try clicking forgot password and verify your account.If you didn't receive any email doing this, please contact us again and it will be handled immediately.\n-Team Wisopt",)),

  (r'(.*)not able to(.*)',
  ( "We apologise for the inconvenience. We will solve your problem as soon as possible.\n-Team Wisopt",)),

  (r'(.*)not getting(.*)',
  ( "We apologise for the inconvenience. We will solve your problem as soon as possible.\n-Team Wisopt",)),

  (r'(.*)resolve(.*)',
  ("We apologise for the inconvenience. We will solve your problem as soon as possible.\n-Team Wisopt",)),

  (r'(.*)app crashes(.*)',
  ("Kindly Check if you have updated the application. If still this peroblem persist, we will solve it as sson as possible.\n-Team Wisopt",)),

  (r'(.*)unable(.*)',
  ( "Sorry For the inconvenience. We will resolve it asap.\n-Team Wisopt",)),

   (r'(.*)annoying(.*)',
   ("Sorry For the inconvenience. We will resolve it asap.\n-Team Wisopt",)),

  (r'(.*)rectify(.*)',
  ( "Sorry For the inconvenience. We will resolve it asap.\n-Team Wisopt",)),

  (r'(.*)error(.*)',
  ( "Sorry For the inconvenience. We will resolve it asap.\n-Team Wisopt",)),

  (r'(.*)Invalid(.*)',
  ( "Kindly check your credentials and try to login again. If still the problem persists kindly contact us.\n-Team Wisopt",)),

  (r'(.*)log in(.*)',
  ("Kindly try to re-register. If the problem persists we will resolve it asap.\n-Team Wisopt",)),

  (r'(.*)not logging(.*)',
  ( "Kindly check your credentials and try to login again. If still the problem persists kindly contact us.\n-Team Wisopt",)),

  (r"(.*)Email id doesn't exist(.*)",
  ( "Kindly check your credentials and try to login again. If still the problem persists kindly contact us.\n-Team Wisopt",)),

  (r'(.*)problem(.*)',
  ( "Sorry for the problem created to you. We will check it from our side and then immediately inform you for the same.\n-Team Wisopt",)),

  (r'(.*)problems(.*)',
  ( "Sorry for the problem created to you. We will check it from our side and then immediately inform you for the same.\n-Team Wisopt",)),

  (r'(.*)no response(.*)',
  ( "Sorry for the problem created to you. We will check it from our side and then immediately inform you for the same.\n-Team Wisopt",)),

  (r"(.*)fix(.*)",
  ( "Sorry for the problem created to you. We will check it from our side and then immediately inform you for the same.\n-Team Wisopt",)),

  (r"(.*)didn't recieve(.*)",
  ( "Kindly check your credentials and try to login again. If still the problem persists kindly contact us.\n-Team Wisopt",)),

  (r"(.*)not receiving(.*)",
  ( "Kindly check your credentials and try to login again. If still the problem persists kindly contact us.\n-Team Wisopt",)),

  (r"(.*)not working(.*)",
  ( "We apologise for the inconvenience created by us to you. We will solve your problem as soon as possible.\n-Team Wisopt",)),

  (r'(.*)it shows(.*)',
  ( "Sorry for the problem created to you. We will check it from our side and then immediately inform you for the same.\n-Team Wisopt",)),

  (r'(.*)not able(.*)',
  ( "Sorry for the problem created to you. We will check it from our side and then immediately inform you for the same.\n-Team Wisopt",)),

  (r'quit',
  ( "Thank you for talking with me.",
    "Good-bye.",
    "Thank you, Have a good day!")),

  (r'(.*)',
  ( "Sorry for the inconvenience. We will try to resolve it as soon as possible.",))
)

class Chat(object):
    def __init__(self, pairs, reflections={}):
        """
        Initialize the chatbot.  Pairs is a list of patterns and responses.  Each
        pattern is a regular expression matching the user's statement or question,
        e.g. r'I like (.*)'.  For each such pattern a list of possible responses
        is given, e.g. ['Why do you like %1', 'Did you ever dislike %1'].  Material
        which is matched by parenthesized sections of the patterns (e.g. .*) is mapped to
        the numbered positions in the responses, e.g. %1.

        :type pairs: list of tuple
        :param pairs: The patterns and responses
        :type reflections: dict
        :param reflections: A mapping between first and second person expressions
        :rtype: None
        """

        self._pairs = [(re.compile(x, re.IGNORECASE),y) for (x,y) in pairs]
        self._reflections = reflections
        self._regex = self._compile_reflections()

    def _compile_reflections(self):
        sorted_refl = sorted(self._reflections.keys(), key=len,
                reverse=True)
        return  re.compile(r"\b({0})\b".format("|".join(map(re.escape,
            sorted_refl))), re.IGNORECASE)

    def _substitute(self, str):
        """
        Substitute words in the string, according to the specified reflections,
        e.g. "I'm" -> "you are"

        :type str: str
        :param str: The string to be mapped
        :rtype: str
        """

        return self._regex.sub(lambda mo:
                self._reflections[mo.string[mo.start():mo.end()]],
                    str.lower())

    def _wildcards(self, response, match):
        pos = response.find('%')
        while pos >= 0:
            num = int(response[pos+1:pos+2])
            response = response[:pos] + \
                self._substitute(match.group(num)) + \
                response[pos+2:]
            pos = response.find('%')
        return response

    def respond(self, str):
        """
        Generate a response to the user input.

        :type str: str
        :param str: The string to be mapped
        :rtype: str
        """

        # check each pattern
        for (pattern, response) in self._pairs:
            match = pattern.match(str)

            # did the pattern match?
            if match:
                resp = random.choice(response)    # pick a random response
                resp = self._wildcards(resp, match) # process wildcards

                # fix munged punctuation at the end
                if resp[-2:] == '?.': resp = resp[:-2] + '.'
                if resp[-2:] == '??': resp = resp[:-2] + '?'
                return resp

    # Hold a conversation with a chatbot
    def converse(self, request):
        user_input =""
        try: user_input = request
        except EOFError:
            print(user_input)
        if user_input:
            while user_input[-1] in "!.": user_input = user_input[:-1]
            return (self.respond(user_input))




'''
def eliza_chat():
    print("Therapist\n---------")
    print("Talk to the program by typing in plain English, using normal upper-")
    print('and lower-case letters and punctuation.  Enter "quit" when done.')
    print('=' * 72)
    print("Hello.  How are you feeling today?")

    eliza_chatbot.converse()


def demo():
    eliza_chat()


if __name__ == "__main__":
    demo()
'''
