import os
import pytz
import datetime
import pynput
import time
import webbrowser
import mouse
import pyautogui

#ข้อมูลเว็บไซต์มีทที่โปรแกรมจะเข้า[ปรับ หรือ เพิ่มเข้าไปได้ , ต้องเอาชื่อ Variable ไปใส่ใน Function จัดตาราง ตามตารางเรียนของผู้ใช้]
Gclass = "https://classroom.google.com/u/1/h" #Google classroom[ไม่ต้องปรับ]
ThaiWriting = "https://meet.google.com/lookup/cu2gnydn7e" #Thai Writing
Biology = "https://meet.google.com/lookup/fmbnlsmkgs" #Biology
Chemistry = "https://meet.google.com/lookup/bnnic5i3q4" #Chemical
Physic = "https://meet.google.com/lookup/aqdltd2icl" #Physic
ESMT = "https://meet.google.com/lookup/cy3knnbfnu" #ESMT
EFC = "https://meet.google.com/lookup/fzqdqwmsx2" #English for conversation
Naenaew = "https://meet.google.com/lookup/chmhns5csw" #Naenaew  
CG = "https://meet.google.com/lookup/g5rxmb3qus" #Computer Graphic
Engforcol = "https://meet.google.com/lookup/bb7odhsw7y" #Eng for college
Eng = "https://meet.google.com/lookup/hnmpm4wehj" #English
He = "https://meet.google.com/lookup/bhgcsumxjx" #Health Education
CS = "https://meet.google.com/lookup/f4bss4sms3" #Computer Science
EngAd = "https://classroom.google.com/u/1/c/MzUyNzY1NTA0NjA1" #Advanced English
Thai = "https://meet.google.com/lookup/dsw5hcl4kh" #Thai
Math = "https://meet.google.com/lookup/bri24lqgfk" #Math
History = False

#กฏ : ถ้าข้อมูลเว็บเป็น False จะข้าม ถ้าข้อมูลเว็บเป็น True จะจบคาบทันที
LunchBreak = False #พักเที่ยง
Current = False #คาบเดียวกับคาบที่แล้ว หรือ คาบซ้อน
Noclass = False #คาบว่างหรือไม่มีคาบ
Endclass = True #ใช้ในการปิดเว็บและไม่เปิดต่อ

joinmeet = ""

Active = False

#Dayset ระบบเวลาเอาไว้ตั้งคาบ[ไม่ต้องปรับ]
dayselect = 0
day = datetime.date.today()
timecheck = datetime.datetime.now()
Monday = 1
Tuesday = 2
Wednesday = 3
Thursday = 4
Friday = 5
Saturday = 6
Sunday = 7

#Class trigger เวลาคาบ [ปรับได้]
TimeHit = "00:00:00" #เวลาคาบถัดไป
TimeC1 = "08:25:00" #เวลาคาบแรก
TimeC2 = "09:25:00"
TimeC3 = "10:20:00"
TimeC4 = "11:15:00"
TimeC5 = "12:10:00"
TimeC6 = "13:00:00"
TimeC7 = "14:00:00"
TimeC8 = "14:55:00" #เวลาคาบสุดท้าย
TimeEC = "15:50:00" #Final class

#ตารางเรียนที่โปรแกรมจะตั้งให้เอง [ไม่ต้องปรับ]
FirstTime = True
ClassNum = 1
C1 = ""
C2 = ""
C3 = ""
C4 = ""
C5 = ""
C6 = ""
C7 = ""
C8 = ""

#Command trigger
Recalibrate = "00:00:00"

#การเข้าโปรแกรม
class joinclass:
    def tojoin() :
        global ClassNum
        global Active
        global FirstTime
        global Endclass
        while True :
            if FirstTime == True : #Open the Google classroom the first time
                print("First time detected!")
                print("Opening Google Classroom. . .")
                webbrowser.open_new(Gclass)
                time.sleep(40)
                print("Waiting for google classroom to load")
                FirstTime = False

            if joinmeet == False : #Skip the class
                print("No class detected.")
                print("Reason : Free class , Lunch break , No class at the moment")
                ClassNum += 1
                print(ClassNum)
                break

            if Active == True : #Leave the current class
                print("Current Class is active. Exiting meet . . .")
                pyautogui.moveTo(1084,991)
                mouse.click()
                pyautogui.moveTo(977,580)
                mouse.click()
                time.sleep(1)
                pyautogui.hotkey('ctrlleft','w')
                Active = False

            if joinmeet == Endclass :
                print("Class's ended!")
                break

            print("Joining meet . . .")
            webbrowser.open_new(joinmeet)
            time.sleep(3)
        
            print("Picking the account . . .")
            pyautogui.moveTo(956,518)
            mouse.click()
            time.sleep(5)
    
            print("Turning off the mic . . .")
            pyautogui.moveTo(686,714)
            mouse.click()
            time.sleep(1)
   
        
            print("Turning off the camera . . .")
            pyautogui.moveTo(765,713)
            mouse.click()
            time.sleep(1)
        
            print("Attending the class . . .")
            pyautogui.moveTo(1239,582)
            mouse.click()

            print("Done!")
            Active = True
            ClassNum += 1
            print(ClassNum)
            break

class Daycheck: #setting up schedule for the day
    def tocheckweekdate():
        #Import in TimeValue
        global TimeHit
        global TimeC1
        global TimeC2
        global TimeC3
        global TimeC4
        global TimeC5
        global TimeC6
        global TimeC7
        global TimeC8
        global TimeC9
        global TimeEC

        global joinmeet
        global C1
        global C2
        global C3
        global C4
        global C5
        global C6
        global C7
        global C8

        global Gclass #Google classroom
        global ThaiWriting  #Thai Writing
        global Biology  #Biology
        global Chemistry #Chemical
        global Physic #Physic
        global ESMT #ESMT
        global EFC  #English for conversation
        global Naenaew  #Naenaew  
        global CG  #Computer Graphic
        global Engforcol #Eng for college
        global Eng  #English
        global He  #Health Education
        global CS  #Computer Science
        global EngAd  #Advanced English
        global Thai  #Thai
        global Math  #Math
        global History 
        global LunchBreak  #Exceptions
        global Current 
        global Noclass
        global Endclass


        #ตั้งคาบแต่ละวัน [ต้องปรับ , เอาชื่อ String จากข้างบนมาใส่]
        if day.isoweekday() == Monday : 
            print("It's Monday")
            print("Setting up the schedule . . .")
            dayselect = Monday
            C1 = ThaiWriting
            C2 = Math
            C3 = Physic
            C4 = Current
            C5 = LunchBreak
            C6 = EFC
            C7 = Eng
            C8 = ESMT
            ClassNum = 1
            FirstTime = True
            print("Completed")

        elif day.isoweekday() == Tuesday :
            print("It's Tuesday")
            print("Setting up the schedule . . .")
            dayselect = Tuesday
            C1 = Noclass
            C2 = Thai
            C3 = Noclass
            C4 = Engforcol
            C5 = LunchBreak
            C6 = EngAd
            C7 = Math
            C8 = History
            ClassNum = 1
            FirstTime = True
            print("Completed")

        elif day.isoweekday() == Wednesday :
            print("It's Wednesday")
            print("Setting up the schedule . . .")
            dayselect = Wednesday
            C1 = History
            C2 = Math
            C3 = Eng
            C4 = Biology
            C5 = LunchBreak
            C6 = Chemistry
            C7 = ESMT
            C8 = Noclass
            ClassNum = 1
            FirstTime = True
            print("Completed")

        elif day.isoweekday() == Thursday :
            print("It's Thursday")
            print("Setting up the schedule . . .")
            dayselect = Thursday
            C1 = Chemistry
            C2 = Current
            C3 = Math
            C4 = Physic
            C5 = LunchBreak
            C6 = CG
            C7 = Current
            C8 = Naenaew
            ClassNum = 1
            FirstTime = True
            print("Completed")

        elif day.isoweekday() == Friday :
            print("It's Friday")
            print("Setting up the schedule . . .")
            dayselect = Friday
            C1 = Biology
            C2 = Current
            C3 = EngAd
            C4 = He
            C5 = LunchBreak
            C6 = Thai
            C7 = Math
            C8 = CS
            ClassNum = 1
            FirstTime = True
            print("Completed")

        else :
            print("It's Saturday or Sunday , There's no class at the moment...")
            C1 = Noclass
            C2 = Noclass
            C3 = Noclass
            C4 = Noclass
            C5 = Noclass
            C6 = Noclass
            C7 = Noclass
            C8 = Noclass
            ClassNum = 1
            FirstTime = False
            print("Feel free to exit the program or leave it on if you'd like.")
            print(day.isoweekday())

    def ChangeSubject(): #ToChangeSubject
        
        #Import in TimeValue ตัวปรับคาบถัดไป [ไม่ต้องปรับ]
        global TimeHit
        global TimeC1
        global TimeC2
        global TimeC3
        global TimeC4
        global TimeC5
        global TimeC6
        global TimeC7
        global TimeC8
        global TimeC9
        global TimeEC

        global Endclass
        global joinmeet
        global C1
        global C2
        global C3
        global C4
        global C5
        global C6
        global C7
        global C8


        if ClassNum == 1 :
            print("Setting Schedule's time . . .")
            joinmeet = C1
            TimeHit = TimeC1
            print("Done!")
            print("The next class is at " + TimeHit)

        elif ClassNum == 2 :
            print("Setting Schedule's time . . .")
            joinmeet = C2
            TimeHit = TimeC2
            print("Done!")
            print("The next class is at " + TimeHit)

        elif ClassNum == 3 :
            print("Setting Schedule's time . . .")
            joinmeet = C3
            TimeHit = TimeC3
            print("Done!")
            print("The next class is at " + TimeHit)

        elif ClassNum == 4 :
            print("Setting Schedule's time . . .")
            joinmeet = C4
            TimeHit = TimeC4
            print("Done!")
            print("The next class is at " + TimeHit)

        elif ClassNum == 5 :
            print("Setting Schedule's time . . .")
            LunchBreak = True
            joinmeet = C5
            TimeHit = TimeC5
            print("Done!")
            print("The next class is at " + TimeHit)

        elif ClassNum == 6 :
            print("Setting Schedule's time . . .")
            joinmeet = C6
            TimeHit = TimeC6
            print("Done!")
            print("The next class is at " + TimeHit)

        elif ClassNum == 7 :
            print("Setting Schedule's time . . .")
            joinmeet = C7
            TimeHit = TimeC7
            print("Done!")
            print("The next class is at " + TimeHit)

        elif ClassNum == 8 :
            print("Setting Schedule's time . . .")
            joinmeet = C8
            TimeHit = TimeC8   
            print("Done!")
            print("The next class is at " + TimeHit)

        elif ClassNum == 9 :
            print("Setting Schedule's time . . .")
            joinmeet = Endclass
            TimeHit = TimeEC
            print("The class's about to end. The program will reschedule once the time hit midnight!")
            print("The class is over at " + TimeHit)
        else :
            print("Error at ChangeSubject()")
            SystemExit
    
    def latetimecheck() : #ตัวเช็คคาบปัจจุบัน
        global ClassNum
        print("Checking the current time . . .")
        print("Input your starting class in INTEGER (0-8)")
        Latetime = int(input(">>>> "))
        print("Configuring . . .")

        if Latetime == 1 :
            ClassNum = ClassNum + 1
            print("Completed!")
        elif Latetime == 2 :
            ClassNum = ClassNum + 2
            print("Completed!")
        elif Latetime == 3 :
            ClassNum = ClassNum + 3
            print("Completed!")
        elif Latetime == 4 :
            ClassNum = ClassNum + 4
            print("Completed!")
        elif Latetime == 5 :
            ClassNum = ClassNum + 5
            print("Completed!")
        elif Latetime == 6 :
            ClassNum = ClassNum + 6
            print("Completed!")
        elif Latetime == 7 :
            ClassNum = ClassNum + 7
            print("Completed!")
        elif Latetime == 8 :
            ClassNum = ClassNum + 8
            print("Completed!")
        elif Latetime == 0 :
            print("Early time detected!")
        else :
            print("Early time detected!")


class TimeSystem : #Time System. ระบบเวลาและ Trigger
    def TimeCheck() :
        while True :
            timenow = datetime.datetime.now()
            print("-----" * 15)
            print("[Update] Time : " + timenow.strftime('%X'))
            print("[Update] The next class's at : " + TimeHit)
            print(joinmeet)
            time.sleep(1)

            if timenow.strftime('%X') == TimeHit :
                print("Time's matched! Proceeding . . .")
                joinclass.tojoin()
                Daycheck.ChangeSubject()

            if timenow.strftime('%X') == Recalibrate:
                print("The current day is done. Managing the schedule . . .")
                Daycheck.tocheckweekdate()


#Execute Space พื้นที่ทำงาน
#Intro
print("Auto Google Meet Attender. by JJWithNoSauce // THIS IS A PROTOTYPE PROGRAM AND NOT FINAL! (personalver)")
print("This program is still in prototype state. If you wish to change the schedule or meet's link.")
print("Please configure them in script. For instruction , check the README file. The program will begin in 5 seconds.")
time.sleep(5)
print("-----" * 12)

Daycheck.tocheckweekdate()
Daycheck.latetimecheck()
Daycheck.ChangeSubject()

while True :
    TimeSystem.TimeCheck()
