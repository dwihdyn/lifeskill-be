import models as m
import speech_recognition as sr
import os
import sys
import re
import webbrowser
import smtplib
import requests
import subprocess
from pyowm import OWM
from time import strftime


#This functions takes input from microphone and converts input into a string
def my_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('....')
        command = my_command()
    return command

#This function convert string into audio 
def sofia_response(audio):                                      
    print(audio)
    os.system("say " + audio)

def assistant(command):
    # lifeskills = [ls.]
    student_list = [sn.fullname.lower() for sn in m.Student.select()]
    print(student_list)

    for s in m.Student.select():
        if s.fullname.lower() in command.lower():
            if 'creativity' in command:
                current_point = s.creativity
                current_point += 5
                s.creativity = current_point
                s.save()
                s.accumulative = s.creativity + s.leadership + s.respect
                s.save()
                sofia_response(f"5 points have been added to {s.fullname}\\'s creativity score")

            elif 'leadership' in command:
                current_point = s.leadership
                current_point += 5
                s.leadership = current_point
                s.save()
                s.accumulative = s.creativity + s.leadership + s.respect
                s.save()
                sofia_response(f"5 points have been added to {s.fullname}\\'s leadership score") 

            elif 'respect' in command:
                current_point = s.respect
                current_point += 5
                s.respect = current_point
                s.save()
                s.accumulative = s.creativity + s.leadership + s.respect
                s.save()
                sofia_response(f"5 points have been added to {s.fullname}\\'s respect score")

            else:
                sofia_response("cant hear you")

assistant(my_command())

    # if "9 + 10" in command:
    #     sofia_response("21.") 
    #     # if "you stupid" in command:
    #     #     sofia_response("nah am not")
    # if 'open' in command:
    #     reg_ex = re.search('open (.+)', command)
    #     if reg_ex:
    #         domain = reg_ex.group(1)
    #         print(domain)
    #         url = 'https://www.https://www.youtube.com/watch?v=oH80ItAP4KY' + domain
    #         webbrowser.open(url)
    #         sofiaResponse('The website you have requested has been opened for you Sir.')
    # if 'hello' in command:
    #     day_time = int(strftime('%H'))
    #     if day_time < 12:
    #         sofia_response('Hello Faris. Good morning')
    #     elif 12 <= day_time < 18:
    #         sofia_response('Hello Faris. Good afternoon')
    #     else:
    #         sofia_response('Hello Faris. Good evening')

    # for student in student_list:
    #             # .....
    # if any([name in command for name in student_list]) and 'creativity' in command:
    #     print(name)
    #     current_point = m.Student.get_or_none(m.Student.fullname.iregexp(name)).creativity
    #     current_point += 5
    #     new_point = m.Student.update(creativity=current_point).where(m.Student.fullname.iregexp(name))
    #     new_point.execute()
    #     sofia_response(f"5 points have been added to {name}'s creativity score")

        # elif student and 'respect' in command:
        #     current_student = student
        #     current_point = m.Student.get_or_none(m.Student.fullname == student).respect
        #     current_point += 5
        #     new_point = m.Student.update(respect=current_point).where(m.Student.fullname == student)
        #     new_point.execute()
        #     sofia_response(f"5 points have been added to {student}'s respect score")

        # elif student and 'leadership' in command:
        #     current_student = student
        #     current_point = m.Student.get_or_none(m.Student.fullname == student).leadership
        #     current_point += 5
        #     new_point = m.Student.update(leadership=current_point).where(m.Student.fullname == student)
        #     new_point.execute()
        #     sofia_response(f"5 points have been added to {student}'s leadership score")


# while True:



# print("===================================")
# print("\n")
# print("     CREDIT AWARDING SYSTEM")
# print("\n")
# print("===================================")

# student_list = [sn.fullname for sn in m.Student]

# print(student_list)

# search_user = input("Who would you like to give points to?")

# if search_user in student_list:
#     print("===================================")
#     print("\n")
#     print(f"     GIVE CREDITS TO {search_user}")
#     print("\n")
#     print("===================================")
#     print("\n")
#     print("1: Leadership")
#     print("2: Respect")
#     print("3: Creativity")
#     print("\n")
#     print("===================================")

# else: 
#     print("Student doesnt exist")

# select_cat = int(input("Select which category you'd like to award: "))

# if select_cat == 1:
#     current_point = m.Student.get_or_none(m.Student.fullname == search_user).leadership
#     current_point += 5
#     new_point = m.Student.update(leadership=current_point).where(m.Student.fullname == search_user)
#     new_point.execute()
#     total_points = m.Student.get_or_none(m.Student.fullname == search_user).leadership + m.Student.get_or_none(m.Student.fullname == search_user).respect + m.Student.get_or_none(m.Student.fullname == search_user).creativity
#     total_points = m.Student.update(accumulative=total_points).where(m.Student.fullname == search_user)
#     total_points.execute()

# if select_cat == 2:
#     current_point = m.Student.get_or_none(m.Student.fullname == search_user).respect
#     current_point += 5
#     new_point = m.Student.update(respect=current_point).where(m.Student.fullname == search_user)
#     new_point.execute()
#     total_points = m.Student.get_or_none(m.Student.fullname == search_user).leadership + m.Student.get_or_none(m.Student.fullname == search_user).respect + m.Student.get_or_none(m.Student.fullname == search_user).creativity
#     total_points = m.Student.update(accumulative=total_points).where(m.Student.fullname == search_user)
#     total_points.execute()

# if select_cat == 3:
    # current_point = m.Student.get_or_none(m.Student.fullname == search_user).creativity
    # current_point += 5
    # new_point = m.Student.update(creativity=current_point).where(m.Student.fullname == search_user)
    # new_point.execute()
#     total_points = m.Student.get_or_none(m.Student.fullname == search_user).leadership + m.Student.get_or_none(m.Student.fullname == search_user).respect + m.Student.get_or_none(m.Student.fullname == search_user).creativity
#     total_points = m.Student.update(accumulative=total_points).where(m.Student.fullname == search_user)
#     total_points.execute()



        



    

