from socket import *

import tkinter as tk

import PIL.ImageTk as imgTK

from imutils import face_utils

import dlib

import cv2 as cv

import numpy as np

import threading

import sys

 

 

def receiveMessage():

    HOST = ""

    PORT = 6667

    

    with socket(AF_INET, SOCK_STREAM) as s:
        
        s.bind((HOST, PORT))

        s.listen(1)

 

        print('Now waiting for connection..')

        conn, addr = s.accept()

        

        with conn:
            
            print('Connected by', addr)

            while True:
                
                data = conn.recv(5000)

                print(data.decode())

                if data.decode() == "_a\n" or data.decode() == "_ya\n" or data.decode() == "_uh\n" or data.decode() == "_yuh\n" or data.decode() == "_ga\n" or data.decode() == "_na\n" or data.decode() == "_da\n" or data.decode() == "_ra\n" or data.decode() == "_ma\n" or data.decode() == "_ba\n" or data.decode() == "_sa\n" or data.decode() == "_ja\n" or data.decode() == "_cha\n" or data.decode() == "_ca\n" or data.decode() == "_ta\n" or data.decode() == "_pa\n" or data.decode() == "_ha\n" or data.decode() == "_oh\n" or data.decode() == "_yo\n" or data.decode() == "_wu\n" or data.decode() == "_yu\n" or data.decode() == "_go\n" or data.decode() == "_no\n" or data.decode() == "_do\n" or data.decode() == "_ro\n" or data.decode() == "_mo\n" or data.decode() == "_uu\n" or data.decode() == "_i\n" or data.decode() == "_gi\n" or data.decode() == "_ni\n" or data.decode() == "_di\n" or data.decode() == "_ri\n" or data.decode() == "_mi\n" :

                    edu = 1 

                if data.decode() == "_oh\n" or data.decode() == "_yo\n" or data.decode() == "_wu\n" or data.decode() == "_yu\n" or data.decode() == "_go\n" or data.decode() == "_no\n" or data.decode() == "_do\n" or data.decode() == "_ro\n" or data.decode() == "_mo\n" :

                    edu = 2

                if data.decode() == "_uu\n" or data.decode() == "_i\n" or data.decode() == "_gi\n" or data.decode() == "_ni\n" or data.decode() == "_di\n" or data.decode() == "_ri\n" or data.decode() == "_mi\n" :

                    edu = 3

 

                print(data.decode())

 

                if data.decode() == 'voice\n' :

 

                        detector = dlib.get_frontal_face_detector()

 

                        predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

 

                        cap = cv.VideoCapture(0)

 

                        ALL = list(range(0, 68)) 

 

                        MOUTH_OUTLINE = list(range(48, 61))  

 

                        MOUTH_INNER = list(range(61, 68))

 

                        ret, img_frame = cap.read()

 

                        img_gray = cv.cvtColor(img_frame, cv.COLOR_BGR2GRAY)

 

                        dets = detector(img_gray)

 

                        for face in dets:
                        
                            shape = predictor(img_frame, face) #얼굴에서 68개 점 찾기

                            shape = face_utils.shape_to_np(shape)

 

        

 

                        for (x, y) in shape[48:68]:

 

                            cv.circle(img_frame, (x, y), 1, (0, 255, 0), -1)

 

                        #cv.imshow("face", img_frame)

 

                        cv.waitKey(1000)

 

                    #k = cv.waitKey(30) & 0xff

 

                    #if k == 27: # press 'ESC' to quit # ESC를 누르면 종료

 

                    #        break

 

    

 

                        width = (shape[64][0]-shape[60][0])

 

                        height = (shape[66][1]-shape[62][1])

 

 

 

                        middle1 = width/2

 

                        middle_point = shape[60][0]+middle1

 

                        outer = shape[13][0]-middle_point

 

                        inner = shape[64][0]-middle_point

 

    

 

                        ratio = width/height

 

                        ratio2 = outer/inner

 

 

 

                        if(3 < (shape[64][0]-shape[60][0])/(shape[66][1]-shape[62][1])):

 

        

 

                            if (ratio2 <= 3) :

 

                                print("classification : uu\n")

                                if edu == 3:

                                    lip_result=1000

                                    print(lip_result)

                                    continue

                                else :

                                    lip_result=1001

                                    print(lip_result)

                                    continue

 

                            elif (ratio2 >=3 ):

 

                                print("classification : oh\n")

                                if edu== 2:

                                    lip_result=1000

                                    print(lip_result)

                                    continue

                                else:

                                    lip_result=1001

                                    print(lip_result)

                                    continue

 

                        elif((shape[64][0]-shape[60][0])/(shape[66][1]-shape[62][1]) <= 3):

 

                            print("classification : ah\n")

 

                            if edu == 1 :

                                lip_result = 1000

                                print(lip_result)

                                continue

                            

                            else :

                                lip_result=1001

                                print(lip_result)

                                continue

                        

                if data.decode() == "okok\n\n" or "nono\n\n" :

                    if data.decode() == "okok\n\n" and lip_result == 1000 :

                        print("CORRECT!")
                        img4 = imgTK.PhotoImage(file="1.png")
                        panel4.configure(image=img4)
                        panel4.image = img4

        

                    elif data.decode() == "okok\n\n" and lip_result == 1001 :

                        print("Voice : OK , Lip : WRONG")
                        img4 = imgTK.PhotoImage(file="2.png")
                        panel4.configure(image=img4)
                        panel4.image = img4

        

                    elif data.decode() == "nono\n\n" and lip_result == 1000 :

                        print("Voice : WRONG , Lip : OK")
                        img4 = imgTK.PhotoImage(file="3.png")
                        panel4.configure(image=img4)
                        panel4.image = img4

        

                    elif data.decode() == "nono\n\n" and lip_result == 1001 :

                        print("Voice : WRONG , Lip : WRONG")
                        img4 = imgTK.PhotoImage(file="4.png")
                        panel4.configure(image=img4)
                        panel4.image = img4

 

               

 

            

                if data.decode() == 'w' :

                    continue

                print(data.decode())

 

                if data.decode() == "_a\n":

 

                    img1 = imgTK.PhotoImage(file="black2.png")

 

                    panel1.configure(image=img1)

 

                    panel1.image = img1

 

                    

 

                    img2 = imgTK.PhotoImage(file="a.png")

 

                    panel2.configure(image=img2)

 

                    panel2.image = img2

 

                    

 

                    img3 = imgTK.PhotoImage(file="a2.png")

 

                    panel3.configure(image=img3)

 

                    panel3.image = img3

 

            

 

 

 

                if data.decode() == "_ya\n":

 

                    img1 = imgTK.PhotoImage(file="black2.png")

 

                    panel1.configure(image=img1)

 

                    panel1.image = img1

 

                    

 

                    img2 = imgTK.PhotoImage(file="ya.png")

 

                    panel2.configure(image=img2)

 

                    panel2.image = img2

 

                    

 

                    img3 = imgTK.PhotoImage(file="ya2.png")

 

                    panel3.configure(image=img3)

 

                    panel3.image = img3

 

                

 

                if data.decode() == "_uh\n":

 

                    img1 = imgTK.PhotoImage(file="black2.png")

 

                    panel1.configure(image=img1)

 

                    panel1.image = img1

 

                    

 

                    img2 = imgTK.PhotoImage(file="uh.png")

 

                    panel2.configure(image=img2)

 

                    panel2.image = img2

 

                    

 

                    img3 = imgTK.PhotoImage(file="uh2.png")

 

                    panel3.configure(image=img3)

 

                    panel3.image = img3

 

                    

 

                if data.decode() == "_yuh\n":

 

                    img1 = imgTK.PhotoImage(file="black2.png")

 

                    panel1.configure(image=img1)

 

                    panel1.image = img1

 

                    

 

                    img2 = imgTK.PhotoImage(file="yuh.png")

 

                    panel2.configure(image=img2)

 

                    panel2.image = img2

 

                    

 

                    img3 = imgTK.PhotoImage(file="yuh2.png")

 

                    panel3.configure(image=img3)

 

                    panel3.image = img3

 

                    

 

                if data.decode() == "_ga\n":

 

                    img1 = imgTK.PhotoImage(file="ga.gif")

 

                    panel1.configure(image=img1)

 

                    panel1.image = img1

 

                    

 

                    img2 = imgTK.PhotoImage(file="a.png")

 

                    panel2.configure(image=img2)

 

                    panel2.image = img2

 

                    

 

                    img3 = imgTK.PhotoImage(file="ga2.png")

 

                    panel3.configure(image=img3)

 

                    panel3.image = img3    

 

                    

 

                if data.decode() == "_na\n":

 

                    img1 = imgTK.PhotoImage(file="na.gif")

 

                    panel1.configure(image=img1)

 

                    panel1.image = img1

 

                    

 

                    img2 = imgTK.PhotoImage(file="a.png")

 

                    panel2.configure(image=img2)

 

                    panel2.image = img2

 

                    

 

                    img3 = imgTK.PhotoImage(file="na2.png")

 

                    panel3.configure(image=img3)

 

                    panel3.image = img3

 

                    

 

                if data.decode() == "_da\n":

 

                    img1 = imgTK.PhotoImage(file="da.gif")

 

                    panel1.configure(image=img1)

 

                    panel1.image = img1

 

                    

 

                    img2 = imgTK.PhotoImage(file="a.png")

 

                    panel2.configure(image=img2)

 

                    panel2.image = img2

 

                    

 

                    img3 = imgTK.PhotoImage(file="da2.png")

 

                    panel3.configure(image=img3)

 

                    panel3.image = img3

 

                    

 

                if data.decode() == "_ra\n":

 

                    img1 = imgTK.PhotoImage(file="ra.gif")

 

                    panel1.configure(image=img1)

 

                    panel1.image = img1

 

                    

 

                    img2 = imgTK.PhotoImage(file="a.png")

 

                    panel2.configure(image=img2)

 

                    panel2.image = img2

 

                    

 

                    img3 = imgTK.PhotoImage(file="ra2.png")

 

                    panel3.configure(image=img3)

 

                    panel3.image = img3

 

                    

 

                if data.decode() == "_ma\n":

 

                    img1 = imgTK.PhotoImage(file="ma.gif")

 

                    panel1.configure(image=img1)

 

                    panel1.image = img1

 

                    

 

                    img2 = imgTK.PhotoImage(file="a.png")

 

                    panel2.configure(image=img2)

 

                    panel2.image = img2

 

                    

 

                    img3 = imgTK.PhotoImage(file="ma2.png")

 

                    panel3.configure(image=img3)

 

                    panel3.image = img3

 

                    

 

                if data.decode() == "_ba\n":

 

                    img1 = imgTK.PhotoImage(file="ba.gif")

 

                    panel1.configure(image=img1)

 

                    panel1.image = img1

 

                    

 

                    img2 = imgTK.PhotoImage(file="a.png")

 

                    panel2.configure(image=img2)

 

                    panel2.image = img2

 

                    

 

                    img3 = imgTK.PhotoImage(file="ba2.png")

 

                    panel3.configure(image=img3)

 

                    panel3.image = img3

 

                    

 

                if data.decode() == "_sa\n":

 

                    img1 = imgTK.PhotoImage(file="sa.gif")

 

                    panel1.configure(image=img1)

 

                    panel1.image = img1

 

                    

 

                    img2 = imgTK.PhotoImage(file="a.png")

 

                    panel2.configure(image=img2)

 

                    panel2.image = img2

 

                    

 

                    img3 = imgTK.PhotoImage(file="sa2.png")

 

                    panel3.configure(image=img3)

 

                    panel3.image = img3

 

                    

 

                if data.decode() == "_ja\n":

 

                    img1 = imgTK.PhotoImage(file="ja.gif")

 

                    panel1.configure(image=img1)

 

                    panel1.image = img1

 

                    

 

                    img2 = imgTK.PhotoImage(file="a.png")

 

                    panel2.configure(image=img2)

 

                    panel2.image = img2

 

                    

 

                    img3 = imgTK.PhotoImage(file="ja2.png")

 

                    panel3.configure(image=img3)

 

                    panel3.image = img3

 

                    

 

                if data.decode() == "_cha\n":

 

                    img1 = imgTK.PhotoImage(file="cha.gif")

 

                    panel1.configure(image=img1)

 

                    panel1.image = img1

 

                    

 

                    img2 = imgTK.PhotoImage(file="a.png")

 

                    panel2.configure(image=img2)

 

                    panel2.image = img2

 

                    

 

                    img3 = imgTK.PhotoImage(file="cha2.png")

 

                    panel3.configure(image=img3)

 

                    panel3.image = img3

 

                    

 

                if data.decode() == "_ca\n":

 

                    img1 = imgTK.PhotoImage(file="ca.gif")

 

                    panel1.configure(image=img1)

 

                    panel1.image = img1

 

                    

 

                    img2 = imgTK.PhotoImage(file="a.png")

 

                    panel2.configure(image=img2)

 

                    panel2.image = img2

 

                    

 

                    img3 = imgTK.PhotoImage(file="ca2.png")

 

                    panel3.configure(image=img3)

 

                    panel3.image = img3

 

                    

 

                if data.decode() == "_ta\n":

 

                    img1 = imgTK.PhotoImage(file="ta.gif")

 

                    panel1.configure(image=img1)

 

                    panel1.image = img1

 

                    

 

                    img2 = imgTK.PhotoImage(file="a.png")

 

                    panel2.configure(image=img2)

 

                    panel2.image = img2

 

                    

 

                    img3 = imgTK.PhotoImage(file="ta2.png")

 

                    panel3.configure(image=img3)

 

                    panel3.image = img3

 

                    

 

                if data.decode() == "_pa\n":

 

                    img1 = imgTK.PhotoImage(file="pa.gif")

 

                    panel1.configure(image=img1)

 

                    panel1.image = img1

 

                    

 

                    img2 = imgTK.PhotoImage(file="a.png")

 

                    panel2.configure(image=img2)

 

                    panel2.image = img2

 

                    

 

                    img3 = imgTK.PhotoImage(file="pa2.png")

 

                    panel3.configure(image=img3)

 

                    panel3.image = img3

 

                    

 

                if data.decode() == "_ha\n":

 

                    img1 = imgTK.PhotoImage(file="ha.gif")

 

                    panel1.configure(image=img1)

 

                    panel1.image = img1

 

                    

 

                    img2 = imgTK.PhotoImage(file="a.png")

 

                    panel2.configure(image=img2)

 

                    panel2.image = img2

 

                    

 

                    img3 = imgTK.PhotoImage(file="ha2.png")

 

                    panel3.configure(image=img3)

 

                    panel3.image = img3

 

                    

 

                if data.decode() == "_oh\n":

 

                    img1 = imgTK.PhotoImage(file="black2.png")

 

                    panel1.configure(image=img1)

 

                    panel1.image = img1

 

                    

 

                    img2 = imgTK.PhotoImage(file="oh.png")

 

                    panel2.configure(image=img2)

 

                    panel2.image = img2

 

                    

 

                    img3 = imgTK.PhotoImage(file="oh2.png")

 

                    panel3.configure(image=img3)

 

                    panel3.image = img3

 

                    

 

                if data.decode() == "_yo\n":

 

                    img1 = imgTK.PhotoImage(file="black2.png")

 

                    panel1.configure(image=img1)

 

                    panel1.image = img1

 

                    

 

                    img2 = imgTK.PhotoImage(file="yo.png")

 

                    panel2.configure(image=img2)

 

                    panel2.image = img2

 

                    

 

                    img3 = imgTK.PhotoImage(file="yo2.png")

 

                    panel3.configure(image=img3)

 

                    panel3.image = img3

 

                    

 

                if data.decode() == "_wu\n":

 

                    img1 = imgTK.PhotoImage(file="black2.png")

 

                    panel1.configure(image=img1)

 

                    panel1.image = img1

 

                    

 

                    img2 = imgTK.PhotoImage(file="wu.png")

 

                    panel2.configure(image=img2)

 

                    panel2.image = img2

 

                    

 

                    img3 = imgTK.PhotoImage(file="wu2.png")

 

                    panel3.configure(image=img3)

 

                    panel3.image = img3

 

                    

 

                if data.decode() == "_yu\n":

 

                    img1 = imgTK.PhotoImage(file="black2.png")

 

                    panel1.configure(image=img1)

 

                    panel1.image = img1

 

                    

 

                    img2 = imgTK.PhotoImage(file="yu.png")

 

                    panel2.configure(image=img2)

 

                    panel2.image = img2

 

                    

 

                    img3 = imgTK.PhotoImage(file="yu2.png")

 

                    panel3.configure(image=img3)

 

                    panel3.image = img3

 

                    

 

                if data.decode() == "_uu\n":

 

                    img1 = imgTK.PhotoImage(file="black2.png")

 

                    panel1.configure(image=img1)

 

                    panel1.image = img1

 

                    

 

                    img2 = imgTK.PhotoImage(file="uu.png")

 

                    panel2.configure(image=img2)

 

                    panel2.image = img2

 

                    

 

                    img3 = imgTK.PhotoImage(file="uu2.png")

 

                    panel3.configure(image=img3)

 

                    panel3.image = img3

 

                    

 

                if data.decode() == "_i\n":

 

                    img1 = imgTK.PhotoImage(file="black2.png")

 

                    panel1.configure(image=img1)

 

                    panel1.image = img1

 

                    

 

                    img2 = imgTK.PhotoImage(file="i.png")

 

                    panel2.configure(image=img2)

 

                    panel2.image = img2

 

                    

 

                    img3 = imgTK.PhotoImage(file="i2.png")

 

                    panel3.configure(image=img3)

 

                    panel3.image = img3

 

                    

 

                if data.decode() == "_go\n":

 

                    img1 = imgTK.PhotoImage(file="ga.gif")

 

                    panel1.configure(image=img1)

 

                    panel1.image = img1

 

                    

 

                    img2 = imgTK.PhotoImage(file="oh.png")

 

                    panel2.configure(image=img2)

 

                    panel2.image = img2

 

                    

 

                    img3 = imgTK.PhotoImage(file="ga2.png")

 

                    panel3.configure(image=img3)

 

                    panel3.image = img3

 

                    

 

                if data.decode() == "_no\n":

 

                    img1 = imgTK.PhotoImage(file="na.gif")

 

                    panel1.configure(image=img1)

 

                    panel1.image = img1

 

                    

 

                    img2 = imgTK.PhotoImage(file="oh.png")

 

                    panel2.configure(image=img2)

 

                    panel2.image = img2

 

                    

 

                    img3 = imgTK.PhotoImage(file="na2.png")

 

                    panel3.configure(image=img3)

 

                    panel3.image = img3

 

                    

 

                if data.decode() == "_do\n":

 

                    img1 = imgTK.PhotoImage(file="da.gif")

 

                    panel1.configure(image=img1)

 

                    panel1.image = img1

 

                    

 

                    img2 = imgTK.PhotoImage(file="oh.png")

 

                    panel2.configure(image=img2)

 

                    panel2.image = img2

 

                    

 

                    img3 = imgTK.PhotoImage(file="da2.png")

 

                    panel3.configure(image=img3)

 

                    panel3.image = img3

 

                    

 

                if data.decode() == "_ro\n":

 

                    img1 = imgTK.PhotoImage(file="ra.gif")

 

                    panel1.configure(image=img1)

 

                    panel1.image = img1

 

                    

 

                    img2 = imgTK.PhotoImage(file="oh.png")

 

                    panel2.configure(image=img2)

 

                    panel2.image = img2

 

                    

 

                    img3 = imgTK.PhotoImage(file="ra2.png")

 

                    panel3.configure(image=img3)

 

                    panel3.image = img3

 

                    

 

                if data.decode() == "_mo\n":

 

                    img1 = imgTK.PhotoImage(file="ma.gif")

 

                    panel1.configure(image=img1)

 

                    panel1.image = img1

 

                    

 

                    img2 = imgTK.PhotoImage(file="oh.png")

 

                    panel2.configure(image=img2)

 

                    panel2.image = img2

 

                    

 

                    img3 = imgTK.PhotoImage(file="ma2.png")

 

                    panel3.configure(image=img3)

 

                    panel3.image = img3

 

                    

 

                if data.decode() == "_gi\n":

 

                    img1 = imgTK.PhotoImage(file="ga.gif")

 

                    panel1.configure(image=img1)

 

                    panel1.image = img1

 

                    

 

                    img2 = imgTK.PhotoImage(file="i.png")

 

                    panel2.configure(image=img2)

 

                    panel2.image = img2

 

                    

 

                    img3 = imgTK.PhotoImage(file="ga2.png")

 

                    panel3.configure(image=img3)

 

                    panel3.image = img3

 

                    

 

                if data.decode() == "_ni\n":

 

                    img1 = imgTK.PhotoImage(file="na.gif")

 

                    panel1.configure(image=img1)

 

                    panel1.image = img1

 

                    

 

                    img2 = imgTK.PhotoImage(file="i.png")

 

                    panel2.configure(image=img2)

 

                    panel2.image = img2

 

                    

 

                    img3 = imgTK.PhotoImage(file="na2.png")

 

                    panel3.configure(image=img3)

 

                    panel3.image = img3

 

                    

 

                if data.decode() == "_di\n":

 

                    img1 = imgTK.PhotoImage(file="da.gif")

 

                    panel1.configure(image=img1)

 

                    panel1.image = img1

 

                    

 

                    img2 = imgTK.PhotoImage(file="i.png")

 

                    panel2.configure(image=img2)

 

                    panel2.image = img2

 

                    

 

                    img3 = imgTK.PhotoImage(file="da2.png")

 

                    panel3.configure(image=img3)

 

                    panel3.image = img3

 

                    

 

                if data.decode() == "_ri\n":

 

                    img1 = imgTK.PhotoImage(file="ra.gif")

 

                    panel1.configure(image=img1)

 

                    panel1.image = img1

 

                    

 

                    img2 = imgTK.PhotoImage(file="i.png")

 

                    panel2.configure(image=img2)

 

                    panel2.image = img2

 

                    

 

                    img3 = imgTK.PhotoImage(file="ra2.png")

 

                    panel3.configure(image=img3)

 

                    panel3.image = img3

 

                    

 

                if data.decode() == "_mi\n":

 

                    img1 = imgTK.PhotoImage(file="ma.gif")

 

                    panel1.configure(image=img1)

 

                    panel1.image = img1

 

                    

 

                    img2 = imgTK.PhotoImage(file="i.png")

 

                    panel2.configure(image=img2)

 

                    panel2.image = img2

 

                    

 

                    img3 = imgTK.PhotoImage(file="ma2.png")

 

                    panel3.configure(image=img3)

 

                    panel3.image = img3

 

            

 

            

 

            

 

            

 

            

 

            

 

          

 

            

 

            

 

        conn.close()

 

 

 

        print ( "socket ends")

 

        s.close()

 

        window.destroy()

        cap.release()

        sys.exit()

 

 

window = tk.Tk()

window.title("Smart mirror")

window.geometry("1920x1000")

window.resizable(True, True)

window.configure(background="BLACK")


 

img1 = imgTK.PhotoImage(file="pack.png")

panel1 = tk.Label(window,image=img1,width=480,height=250)

panel1.place(x=100, y=100)

 

img2 = imgTK.PhotoImage(file="pack.png")

panel2 = tk.Label(window,image=img2,width=480,height=250)

panel2.place(x=100, y=500)

 

img3 = imgTK.PhotoImage(file="pack.png")

panel3 = tk.Label(window,image=img3,width=480,height=250)

panel3.place(x=700, y=300)


img4 = imgTK.PhotoImage(file="pack.png")

panel4 = tk.Label(window,image=img4,width=480,height=250)

panel4.place(x=700, y=700)

 

t = threading.Thread(target=receiveMessage)

t.start()


window.mainloop()