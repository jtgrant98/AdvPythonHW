Dict_1 = {'CS101':'3004','CS102':'4501','CS103':'6755','NT110':'1244','CM241':'1411'}

Dict_2 = {'CS101':'Haynes','CS102':'Alvarado','CS103':'Rich','NT110':'Burke','CM241':'Lee'}

Dict_3 = {'CS101':'8:00am','CS102':'9:00am','CS103':'10:00am','NT110':'11:00am','CM241':'1:00pm'}

room = "Your room number is: "
Teacher = "Your teacher is: "
Time = "Your class time is: "

def main():
    course_num = input("Enter your course number")
    print(room)
    print(Dict_1[course_num])
    print(Teacher)
    print(Dict_2[course_num])
    print(Time)
    print(Dict_3[course_num])

main()