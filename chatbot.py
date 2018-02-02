from __future__ import print_function
from nltk.chat.util import Chat, reflections

# a table of response pairs, where each pair consists of a
# regular expression, and a list of possible responses,
# with group-macros labelled as %1, %2.

pairs = (
    (r'(.*)Hello(.*)',
     ("Hi! How may I help you?",)),

    (r'(.*)Add(.*)',
     ("We're currently working on the feature. It will be deployed in the next update!\n-Team Wisopt",)),

    (r'(.*)include(.*)',
     ("We're currently working on the feature. It will be deployed in the next update!\n-Team Wisopt",)),

    (r'(.*)no option(.*)',
     ("We're currently working on the feature. It will be deployed in the next update!\n-Team Wisopt",)),

    (r'(.*)Confusing(.*)',
     (
         "We apologise for the confusion caused by us to you in our app. We will surely work on that and will reply to you for the same!\n-Team Wisopt",)),

    (r'(.*)Attendance(.*)',
     ("We are working on that module, and will deploy this feature in our next update!\n-Team Wisopt",)),

    (r'(.*)Please Check(.*)',
     ("We will check for the problem as soon as possible, and will report you for the same.\n-Team Wisopt",)),

    (r'(.*)Showing(.*)',
     (
         "Kindly check if you have updated the application. If the problem still persists, kindly inform us. We will take the necessary action as soon as possible.\n-Team Wisopt",)),

    (r'(.*)Not Showing(.*)',
     (
         "Kindly check if you have updated the application. If the problem still persists, kindly inform us. We will take the necessary action as soon as possible.\n-Team Wisopt",)),

    (r'(.*)Can you(.*)',
     ("Surely we will try to do so as soon as possible and we advise you to keep the app updated!\n-Team Wisopt",)),

    (r'(.*)Useful For(.*)',
     ("Thanks for your valuable feedback.\n-Team Wisopt",)),

    (r'(.*)Add an option(.*)',
     (
         "We are happy that you inspected our application and gave your precious time to us. We are glad. Thanks for your feedback.\n-Team Wisopt",)),

    (r'(.*)Forget(.*)Password(.*)',
     (
         "please try clicking forgot password and verify your account.If you didn't receive any email doing this, please contact us again and it will be handled immediately.\n-Team Wisopt",)),

    (r'(.*)Forgot(.*)Password(.*)',
     (
         "please try clicking forgot password and verify your account.If you didn't receive any email doing this, please contact us again and it will be handled immediately.\n-Team Wisopt",)),

    (r'(.*)email(.*)',
     (
         "Please try clicking forgot password and verify your account.If you didn't receive any email doing this, please contact us again and it will be handled immediately.\n-Team Wisopt",)),

    (r'(.*)any email(.*)',
     (
         "Please try clicking forgot password and verify your account.If you didn't receive any email doing this, please contact us again and it will be handled immediately.\n-Team Wisopt",)),

    (r'(.*)confirmation email(.*)',
     (
         "Please try clicking forgot password and verify your account.If you didn't receive any email doing this, please contact us again and it will be handled immediately.\n-Team Wisopt",)),

    (r'(.*)confirmation mail(.*)',
     (
         "Please try clicking forgot password and verify your account.If you didn't receive any email doing this, please contact us again and it will be handled immediately.\n-Team Wisopt",)),

    (r'(.*)verify email(.*)',
     (
         "Please try clicking forgot password and verify your account.If you didn't receive any email doing this, please contact us again and it will be handled immediately.\n-Team Wisopt",)),

    (r'(.*)no mail(.*)',
     (
         "Please try clicking forgot password and verify your account.If you didn't receive any email doing this, please contact us again and it will be handled immediately.\n-Team Wisopt",)),

    (r'(.*)verification(.*)',
     (
         "Please try clicking forgot password and verify your account.If you didn't receive any email doing this, please contact us again and it will be handled immediately.\n-Team Wisopt",)),

    (r'(.*)not able to(.*)',
     (
         "We apologise for the inconvenience created by us to you. We will solve your problem as soon as possible.\n-Team Wisopt",)),

    (r'(.*)resolve(.*)',
     (
         "We apologise for the inconvenience created by us to you. We will solve your problem as soon as possible.\n-Team Wisopt",)),

    (r'(.*)app crashes(.*)',
     (
         "We apologise for the inconvenience created by us to you. We will solve your problem as soon as possible.\n-Team Wisopt",)),

    (r'(.*)unable(.*)',
     ("Sorry For the inconvenience. We will resolve it asap.\n-Team Wisopt",)),

    (r'(.*)rectify(.*)',
     ("Sorry For the inconvenience. We will resolve it asap.\n-Team Wisopt",)),

    (r'(.*)error in(.*)',
     ("Sorry For the inconvenience. We will resolve it asap.\n-Team Wisopt",)),

    (r'(.*)Invalid(.*)',
     (
         "Kindly check your credentials and try to login again. If still the problem persists kindly contact us.\n-Team Wisopt",)),

    (r'(.*)not logging(.*)',
     (
         "Kindly check your credentials and try to login again. If still the problem persists kindly contact us.\n-Team Wisopt",)),

    (r"(.*)Email id doesn't exist(.*)",
     (
         "Kindly check your credentials and try to login again. If still the problem persists kindly contact us.\n-Team Wisopt",)),

    (r'(.*)problem(.*)',
     (
         "Sorry for the problem created to you. We will check it from our side and then immediately inform you for the same.\n-Team Wisopt",)),

    (r'(.*)problems(.*)',
     (
         "Sorry for the problem created to you. We will check it from our side and then immediately inform you for the same.\n-Team Wisopt",)),

    (r'(.*)no response(.*)',
     (
         "Sorry for the problem created to you. We will check it from our side and then immediately inform you for the same.\n-Team Wisopt",)),

    (r"(.*)fix(.*)",
     (
         "Sorry for the problem created to you. We will check it from our side and then immediately inform you for the same.\n-Team Wisopt",)),

    (r"(.*)didn't recieve(.*)",
     (
         "Kindly check your credentials and try to login again. If still the problem persists kindly contact us.\n-Team Wisopt",)),

    (r"(.*)not receiving(.*)",
     (
         "Kindly check your credentials and try to login again. If still the problem persists kindly contact us.\n-Team Wisopt",)),

    (r"(.*)it's not working(.*)",
     (
         "We apologise for the inconvenience created by us to you. We will solve your problem as soon as possible.\n-Team Wisopt",)),

    (r'(.*)it shows(.*)',
     (
         "Sorry for the problem created to you. We will check it from our side and then immediately inform you for the same.\n-Team Wisopt",)),

    (r'(.*)not able(.*)',
     (
         "Sorry for the problem created to you. We will check it from our side and then immediately inform you for the same.\n-Team Wisopt",)),

    (r'quit',
     ("Thank you for talking with me.",
      "Good-bye.",
      "Thank you, Have a good day!")),

    (r'(.*)',
     ("I don't understand. Can you be more specific?",))
)


def getResponse(request):
    eliza_chatbot = Chat(pairs, request, reflections)
    return eliza_chatbot.converse(request)


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
