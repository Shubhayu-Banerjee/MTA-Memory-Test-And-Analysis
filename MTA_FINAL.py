# MTA Program
# Shubhayu X Vignan + Saalim

import random
import matplotlib.pyplot as plt
from playsound import playsound
import time

page = 100
few_lines = 5
turbo = True  # False = Fast, True = Slow


def ynturbo():
    global turbo
    turbo = input("Turbo? (Y/N)>>>")
    if turbo.lower() == "y":
        turbo = False
    elif turbo.lower() == "n":
        turbo = True
    else:
        turbo = True

ynturbo()

def soundplay (sound_type):
    if sound_type == "ping":
        playsound('F:\MTA-Memory-Test-And-Analysis-main\ping.mp3')
    elif sound_type == "correct":
        playsound('F:\MTA-Memory-Test-And-Analysis-main\Correct_Ping.mp3')
    elif sound_type == "wrong":
        playsound('F:\MTA-Memory-Test-And-Analysis-main\wrong_buzz.mp3')
    elif sound_type == "click":
        playsound('F:\MTA-Memory-Test-And-Analysis-main\click.mp3')


if turbo == False:
    soundplay("ping")
    print("-------Debug-------")
    print("---Turbo:Enabled---")
else:
    soundplay("ping")
    print("-------Debug--------")
    print("---Turbo:Disabled---")


def clsscr(wait_time, amount, turbo):
    print("Clearing screen in " + str(round((wait_time), 1)) + " seconds.")
    if turbo == True:
        time.sleep(wait_time)
    print("\n" * amount)


def simplecls(wait_time, amount, turbo):
    if turbo == True:
        time.sleep(wait_time)
    print("\n" * amount)


def bold_mta(Time):
    print(" ___________________________________________")
    time.sleep(Time)
    print("|         __  __     ________     __        |")
    time.sleep(Time)
    print('|        //||//||   |________|   //||       |')
    time.sleep(Time)
    print("| >---  //     ||       ||      //_||  ---< |")
    time.sleep(Time)
    print("|      //      ||       ||     //  ||       |")
    time.sleep(Time)
    print("|___________________________________________|")
    print("\n")
    soundplay("correct")
    
# DataBases

String_lib = ["ability", "able", "about", "above", "accept", "according", "account", "across", "act", "bag", 'ball',
              'bank', 'bar', 'base',
              'be', 'beat', 'beautiful', 'because', 'become', 'bed', 'before', 'begin', 'behavior', 'camera',
              'campaign', 'can', 'cancer',
              'candidate', 'capital', 'car', 'card', 'care', 'career', 'carry', 'case', 'catch', 'debate', 'decade',
              'decide', 'decision',
              'deepen', 'defense', 'degree', 'Democrat', 'democratic', 'describe', 'design', 'despite', 'detail',
              'determine', 'develop',
              'development', 'education''effect', 'effort', 'eight', 'either', 'election', 'else', 'end', 'energy',
              'enjoy', 'enough',
              'enter', 'entire', 'environment', 'environmental', 'face', 'fact', 'factor', 'fail', 'fall', 'family',
              'far', 'fast', 'father',
              'fear', 'federal', 'feel', 'feeling', 'few', 'field', 'fight', 'figure', 'fill', 'film', 'final',
              'finally', 'financial', 'find', 'fine',
              'finish', 'finger', 'fire', 'firm', 'first', 'fish', 'five', 'floor', 'fly', 'focus', 'game', 'garden',
              'gas', 'general', 'generation',
              'get', 'glass', 'go', 'goal', 'good','government','great','green', 'ground', 'group', 'grow',
              'growth''guess', 'gun',
              'guy', 'girl', 'give', 'hair', 'half', 'hand', 'hang', 'happen', 'happy', 'hard', 'have', 'he', 'head',
              'health', 'hear', 'heart',
              'heat', 'heavy', 'help', 'her', 'here', 'herself', 'high', 'him', 'himself',
              'his', 'history', 'hit', 'hold', 'home', 'hope', 'hospital', 'absorb', 'abuse', 'academic', 'accept',
              'according', 'account',
              'across', 'act', 'action', 'activity', 'actually', 'add', 'address', 'administration', 'admit', 'adult',
              'affect', 'after', 'again',
              'idea', 'identify', 'if', 'image', 'imagine', 'impact', 'important', 'improve', 'include', 'including',
              'increase', 'indeed', 'indicate',
              'individual', 'industry', 'information', 'inside', 'instead', 'institution', 'interest', 'interesting',
              'international', 'interview',
              'into', 'introduce', 'introduction', 'investment', 'involve', 'issue', 'it', 'item', 'its', 'itself',
              'job','join','just','keep','key','kid','kill','kind','kitchen','know','knowledge','land','language','large',
              'last','late','later','laugh','law','lawyer','lay','lead','leader','learn','least','leave','left','leg',
              'legal','less','let','letter','level','lie','life','light','like','likely','line','list','listen','little',
              'live','local','long','look','lose','loss','lot','love','machine','magazine','main','maintain','major',
              'majority','make','man','manage','management','manager','many','market','marriage','material','matter','may',
              'maybe','me','mean','measure','media','mention','message','method',
              'middle','might','military','million','mind','minute','miss','mission','model','modern','moment','money','month',
              'more','morning','most','mother','name','nation','national','natural','nature','near','nearly','necessary','need',
              'network','never','new','news','newspaper','next','nice','night','no','none','nor','north','not','note',
              'nothing','notice','now',
              ]

Character_lib = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z",
                 "x", "c", "v", "b", "n", "m",
                 "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@"]

pi = "3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196442881097566593344612847564823378678316527120190914564856692346034861045432664821339360726024914127372458700660631558817488152092096282925"


# Word test
def met_string(string_count, type):
    db_len = len(String_lib) - 1
    print("Database length:" + str(len(String_lib)))
    time_wait_str = int(input("How long do you want to remember?  (Seconds)>>>"))
    soundplay("ping")
    n = 0
    mem_list = []
    if type.lower() == "line":
        while n < string_count:
            string = String_lib[random.randint(0, db_len)]

            mem_list.append(string)

            n += 1
        print("Remember the following words:")
        print(mem_list)

    elif type.lower() == "list":
        print("Remember the following words:")
        soundplay("ping")
        while n < string_count:
            string = String_lib[random.randint(0, db_len)]
            print(string)
            mem_list.append(string)
            n += 1

    clsscr(time_wait_str, page, turbo=True)

    def acc_time_test_str():

        # Accuracy Test
        input_words = input("Now, Enter the words with a space in between. eg: (cat apple ball) >>>")
        input_words_list = input_words.split()
        print(input_words_list)
        length = len(mem_list)
        i = 0
        correct_words = 0
        while i < length:
            try:
                if mem_list[i] == input_words_list[i]:
                    correct_words += 1


            except:
                None
            i += 1
        accuracy_percentage = round((correct_words / (len(mem_list)) * 100), 3)
        print("The word list was: " + str(mem_list))
        print(("Your words were:  " + str(input_words_list)))
        print("Your accuracy is " + str(accuracy_percentage) + "%")
        
        if accuracy_percentage >= 80:
            soundplay("correct")
        elif accuracy_percentage >= 60:
            soundplay("ping")
        else:
            soundplay("wrong")

        # x-coordinates of left sides of bars
        left = [1, 2]

        # heights of bars
        height = [65, accuracy_percentage]

        # labels for bars
        tick_label = ['Average', 'Your Score']

        # plotting a bar chart
        if 65 > accuracy_percentage:
            plt.bar(left, height, tick_label=tick_label,
                    width=0.5, color=['green', 'red'])
        elif 65 == accuracy_percentage:
            plt.bar(left, height, tick_label=tick_label,
                    width=0.5, color=['orange', 'orange'])
        else:
            plt.bar(left, height, tick_label=tick_label,
                    width=0.5, color=['red', 'green'])
        # naming the x-axis
        plt.xlabel('x - axis')
        # naming the y-axis
        plt.ylabel('y - axis (percentage-%)')
        # plot title
        plt.title('Accuracy Comparison')

        # function to show the plot
        soundplay("ping")
        plt.show()

    acc_time_test_str()


# Character Test
def met_character(character_count):
    n = 0
    db_len = len(Character_lib)
    mem_chr = ""
    print("Database length:" + str(len(Character_lib)))
    db_len = db_len - 1
    while n < character_count:
        chacacter = Character_lib[random.randint(0, db_len)]
        mem_chr = mem_chr + chacacter

        n += 1
    code_wait_time = int(input("How much time do you want to remember?(Seconds)>>>"))
    soundplay("ping")
    print("\n")
    print("Remember the following code:")
    soundplay("ping")
    mem_chr = str(mem_chr)
    print(mem_chr)

    clsscr(code_wait_time, page, turbo=True)

    inputcode = input("Now type out the code>")
    inputcode = str(inputcode)

    def acc_time_test_chr():

        # Accuracy Test
        length = len(mem_chr)
        i = 0
        correct_letters = 0
        while i < length:
            try:
                if (mem_chr[i]) == inputcode[i]:
                    correct_letters += 1
            except:
                None
            i += 1
        accuracy_percentage = round(((correct_letters / length) * 100), 3)

        # Chr/sec Test
        speed = round((correct_letters * (1 / code_wait_time)), 2)

        if accuracy_percentage >= 80:
            soundplay("correct")
        elif accuracy_percentage >= 60:
            soundplay("ping")
        else:
            soundplay(wrong)
               
        accuracy_percentage_num = accuracy_percentage
        accuracy_percentage = str(accuracy_percentage)
        print("The original code was:" + mem_chr)
        print("Your accuracy is " + accuracy_percentage + "%")
        print("\n")
        print("Your speed is " + str(speed) + " Chr/Second")

        # x-coordinates of left sides of bars
        left = [1, 2]

        # heights of bars
        height = [75, accuracy_percentage_num]

        # labels for bars
        tick_label = ['Average', 'Your Score']

        # plotting a bar chart
        if 75 > accuracy_percentage_num:
            plt.bar(left, height, tick_label=tick_label,
                    width=0.5, color=['green', 'red'])
        elif 75 == accuracy_percentage_num:
            plt.bar(left, height, tick_label=tick_label,
                    width=0.5, color=['orange', 'orange'])
        else:
            plt.bar(left, height, tick_label=tick_label,
                    width=0.5, color=['red', 'green'])
        # naming the x-axis
        plt.xlabel('x - axis')
        # naming the y-axis
        plt.ylabel('y - axis (percentage-%)')
        # plot title
        plt.title('Accuracy Comparison')

        # function to show the plot
        soundplay("ping")
        plt.show()

    acc_time_test_chr()


# Pi Test
def pi_test():
    print("Welcome to pi game.")
    time.sleep(1)
    print("You will be shown the digits of pi for a set amount of time, with an increment of your choosing, "
          "you must type down the digits as you remember.")
    time.sleep(0.5)
    digit_increment = int(input("By how many digits do you want to increment?>>>"))
    time.sleep(0.5)
    remembrance_time = int(input("Enter amount of time to wait per increment:"))
    clsscr(2, few_lines, turbo=True)
    print("---Pi Game---")
    i = 0
    num_of_digits = 4
    time.sleep(1)
    Round = 1
    while i < 10:
        shown_digits = pi[0:num_of_digits]
        print("---Round " + str(Round) + "---")
        print("Your digits are:" + shown_digits)
        clsscr(remembrance_time, page, turbo=True)
        input_digits = str(input("Type the digits down:"))
        if shown_digits == input_digits:
            print("Well done!")
            num_of_digits += digit_increment
            remembrance_time += 0.2
            Round += 1
            clsscr(2, few_lines, turbo=True)
        else:
            soundplay("click")
            print("You are wrong, your sequence of digits is:" + input_digits)
            print("The correct sequence was:" + shown_digits)
            print("You Lost on round :", Round)
            i = 11

    def accuracy_pi():

        # Accuracy Test
        length = len(shown_digits)
        i = 0
        correct_num = 0
        while i < length:
            try:
                if (input_digits[i]) == shown_digits[i]:
                    correct_num += 1
            except:
                None
            i += 1

        accuracy_percentage = round(((correct_num / length) * 100), 3)
        print("Your accuracy is:" + str(accuracy_percentage) + "%")

        if accuracy_percentage >= 80:
            soundplay(correct)
        elif accuracy_percentage >= 60:
            soundplay(ping)
        else:
            soundplay(wrong)

        # x-coordinates of left sides of bars
        left = [1, 2]

        progressive_percentage = 100
        progressive_percentage = progressive_percentage - (Round * (digit_increment * 3) + num_of_digits)

        if progressive_percentage < 0:
            progressive_percentage = 3

        # heights of bars
        height = [progressive_percentage, accuracy_percentage]

        # labels for bars
        tick_label = [f'Average For Round: {Round}, Increment: {digit_increment}', 'Your Score']

        # plotting a bar chart
        if progressive_percentage > accuracy_percentage:
            plt.bar(left, height, tick_label=tick_label,
                    width=0.5, color=['green', 'red'])
        elif progressive_percentage == accuracy_percentage:
            plt.bar(left, height, tick_label=tick_label,
                    width=0.5, color=['orange', 'orange'])
        else:
            plt.bar(left, height, tick_label=tick_label,
                    width=0.5, color=['red', 'green'])
        # naming the x-axis
        plt.xlabel('x - axis Comparison Between Values')
        # naming the y-axis
        plt.ylabel('y - axis (percentage-%)')
        # plot title
        plt.title('Accuracy Comparison')

        # function to show the plot
        plt.show()

    accuracy_pi()


# Program
def Main_Program():
    time.sleep(0.7)
    print("Loading Program")
    if turbo == True:
        time.sleep(random.randint(1, 5))

    print("Loading complete!")
    simplecls(1, few_lines, turbo)

    bold_mta(0.2)

    if turbo == True:
        time.sleep(1)
    print("Welcome to MTA, Memory Test and Analysis Program")
    if turbo:
        time.sleep(2.2)
    choice = input(
        "Do you want to test your remembrance speed for words (W), alphanumeric codes?(C), or pi test? (P)>>>")

    if choice.lower() == "w":
        num_str = int(input("How many words do you want?"))
        str_type = (input("Welcome, In what format do you want your lines to remember? (List/Line)"))
        met_string(num_str, str_type)


    elif choice.lower() == "c":
        num_chr = int(input("How many characters do you want?"))
        met_character(num_chr)

    elif choice.lower() == "p":
        print("Starting game")
        time.sleep(5)
        pi_test()


rep = True

Main_Program()

while rep == True:
    rep_inp = input("Do you want to repeat (Y/N)")
    if rep_inp.lower() == "y":
        Main_Program()
    else:
        rep = False
        print("\n")
        time.sleep(0.5)
        print("Here are a few links for a few helpful techniques to remember in a more efficient manner.")
        print("\n")
        print("1. https://learningcenter.unc.edu/tips-and-tools/enhancing-your-memory/")
        time.sleep(0.5)
        print("2. https://www.magneticmemorymethod.com/how-to-remember-things/")
        time.sleep(0.5)
        print("3. https://zapier.com/blog/better-memory/")
        time.sleep(0.5)
        print("\n")
        print("For official documentation visit: https://atl-1.gitbook.io/mta")
        time.sleep(0.5)
        print("Thank for using MTA - Have a nice day!")
        bold_mta(0.5)
        print("\n")
        print("Offloading Program")
        time.sleep(random.randint(2, 5))
        print("\n")

# ---Program Done---
