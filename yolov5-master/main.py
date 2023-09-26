from operator import length_hint
import tkinter as tk
from tkinter import *
import cv2
import PIL.Image, PIL.ImageTk
import time
import datetime as dt
import argparse
import PIL
from object_detector import *
import detect
import numpy as np
class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        self.ok=False
 
        #timer
        self.timer=ElapsedTimeClock(self.window)
 
        # open video source (by default this will try to open the computer webcam)
        self.vid = VideoCapture(self.video_source)
 
        # Create a canvas that can fit the above video source size
        self.canvas = tk.Canvas(window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()
 
        # Button that lets the user take a snapshot
        self.btn_snapshot=tk.Button(window, text="Snapshot", command=self.snapshot)
        self.btn_snapshot.pack(side=tk.LEFT)
 
        #video control buttons
 
        self.btn_start=tk.Button(window, text='START', command=self.open_camera)
        self.btn_start.pack(side=tk.LEFT)
 
        self.btn_stop=tk.Button(window, text='STOP', command=self.close_camera)
        self.btn_stop.pack(side=tk.LEFT)
 
        # quit button
        self.btn_quit=tk.Button(window, text='QUIT', command=quit)
        self.btn_quit.pack(side=tk.LEFT)
 
        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay=10
        self.update()
 
        self.window.mainloop()
 
    def snapshot(self):
        berat_final = 0
        # Get a frame from the video source
        ret,frame=self.vid.get_frame()
        total = []
        xmiddle = []
        ymiddle = []
        height = []
        width = []
        if ret:
            filename = "frame-"+time.strftime("%d-%m-%Y-%H-%M-%S")
            cv2.imwrite(filename + ".jpg",cv2.cvtColor(frame,cv2.COLOR_RGB2BGR))
            detect.run(source=filename + ".jpg",project='result',name='',weights="yolov5-master/best.pt",save_txt=True)
            #weights="runs/train/exp29/weights/best.pt"
            def unique(list1):
                listunique = []
                # initialize a null list
                unique_list = []
            
                # traverse for all elements
                for x in list1:
                    # check if exists in unique_list or not
                    if x not in unique_list:
                        unique_list.append(x)
                # print list
                for x in unique_list:
                    # print(x),
                    listunique.append(x)
                return listunique
            finaltotal = []
            total = []
            organik = 0 
            botol_plastik = 0 
            logam = 0
            kaca = 0
            styrofoam = 0
            lain_lain = 0
            with open ("result4/labels/" + filename + ".txt" ) as f:
                textfile = f.read()
            for i in range(len(textfile.splitlines())):
                if textfile.splitlines()[i].split()[0] == "0":
                    organik = organik + 1
                elif textfile.splitlines()[i].split()[0] == "1":
                    botol_plastik = botol_plastik + 1
                elif textfile.splitlines()[i].split()[0] == "2":
                    logam  = logam + 1
                elif textfile.splitlines()[i].split()[0] == "3":
                    kaca  = kaca + 1
                elif textfile.splitlines()[i].split()[0] == "4":
                    styrofoam  = styrofoam + 1
                elif textfile.splitlines()[i].split()[0] == "5":
                    lain_lain  = lain_lain + 1
                total.append(int(textfile.splitlines()[i].split()[0]))
                xmiddle.append(float(textfile.splitlines()[i].split()[1]))
                ymiddle.append(float(textfile.splitlines()[i].split()[2]))
                height.append(float(textfile.splitlines()[i].split()[3]) * 2)
                width.append(float(textfile.splitlines()[i].split()[4]) * 1.2)

            image_result = PIL.ImageTk.PhotoImage(PIL.Image.open("result4/" + filename + ".jpg"))
            self.popupwindow = Toplevel(self.window)
            self.popupwindow.title("Result")
            self.imageresult = Label(self.popupwindow,image=image_result)

            # parameters = cv2.aruco.DetectorParameters_create()
            # aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)
            # img = cv2.imread('result4/' + filename + ".jpg" )
            # corners, _, _ = cv2.aruco.detectMarkers(img, aruco_dict, parameters=parameters)
            # int_corners = np.int0(corners)
            # cv2.polylines(img, int_corners, True, (0, 255, 0), 5)
            # aruco_perimeter = cv2.arcLength(corners[0], True)
            # pixel_cm_ratio = aruco_perimeter / 19000
            # berat_final = 0        
            massa_jenis = 0
            gravitasi = 9.81

            for cnt in range(len(total)):
                if textfile.splitlines()[cnt].split()[0] == "0":
                    print(massa_jenis)
                    massa_jenis = 769 #gandum
                elif textfile.splitlines()[cnt].split()[0] == "1":
                    massa_jenis = 40.83333333333333 #kg/ m3
                    print(massa_jenis)
                elif textfile.splitlines()[cnt].split()[0] == "2":
                    massa_jenis = 2000 #besi
                    print(massa_jenis)
                elif textfile.splitlines()[cnt].split()[0] == "3":
                    massa_jenis = 689 #kardus
                    print(massa_jenis)
                elif textfile.splitlines()[cnt].split()[0] == "4":
                    massa_jenis = 1500 #kaca
                    print(massa_jenis)
                elif textfile.splitlines()[cnt].split()[0] == "5":
                    massa_jenis = 65 # styrofoam 30 - 100
                    print(massa_jenis)

                # object_width = width[cnt] / pixel_cm_ratio
                # object_height = height[cnt] / pixel_cm_ratio

                # object_width = object_width / 100 
                # object_height = object_height / 100
                # object_length = (object_width + object_height) / 2

                # volume = object_width * object_height * object_length
                # # volume_final = volume_final + volume
                
                # berat = volume * massa_jenis * gravitasi
                # # print(volume)
                # # print(massa_jenis)
                # # print(gravitasi)
                # # print(berat)
                # berat_final = berat_final + berat
                
               # print("width: " + str(object_width * 100) + " " + "length: " + str(object_length  * 100) + "height: " + str(object_height  * 100))
            hargasampahperkg = 2000
            finaltotal = unique(total)
            
            berat_final = berat_final / 100
            print(finaltotal)
            if len(finaltotal) > 1:
                self.material=tk.Label(self.popupwindow,text='> 1 material, dengan estimasi bobot: ' + str("%.2f" % berat_final) + " kg" + ", Estimasi Denda: Rp." + str(int(hargasampahperkg * berat_final)) + ",00" ,font=('times', 20, 'bold'), bg='green')
            elif len(finaltotal) < 2:
                #print('hanya terdapat satu material, dengan estimasi bobot: ' +   + str("%.2f" % berat_final) + " kg")
                self.material=tk.Label(self.popupwindow,text='== 1 material, dengan estimasi bobot: '  + str("%.2f" % berat_final) + " kg" + ", Estimasi Upah: Rp." + str(int(hargasampahperkg * berat_final)) + ",00",font=('times', 20, 'bold'), bg='green')
            elif len(finaltotal) == 0:
                print("objek tidak terdeteksi, silahkan coba lagi")


            self.material.pack(fill=tk.BOTH, expand=1)
            self.imageresult.pack()
            self.popupwindow.mainloop()
            
    def open_camera(self):
        self.ok = True
        self.timer.start()
        print("camera opened => Recording")
 
 
    def close_camera(self):
        self.ok = False
        self.timer.stop()
        print("camera closed => Not Recording")

    def update(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()
        if self.ok:
            self.vid.out.write(cv2.cvtColor(frame,cv2.COLOR_RGB2BGR))
 
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tk.NW)
        self.window.after(self.delay,self.update)

class VideoCapture:
    def __init__(self, video_source=0):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)
 
        # Command Line Parser
        args=CommandLineParser().args
 
        
        #create videowriter
 
        # 1. Video Type
        VIDEO_TYPE = {
            'avi': cv2.VideoWriter_fourcc(*'XVID'),
            #'mp4': cv2.VideoWriter_fourcc(*'H264'),
            'mp4': cv2.VideoWriter_fourcc(*'XVID'),
        }
 
        self.fourcc=VIDEO_TYPE[args.type[0]]
 
        # 2. Video Dimension
        STD_DIMENSIONS =  {
            '480p': (640, 480),
            '720p': (1280, 720),
            '1080p': (1920, 1080),
            '4k': (3840, 2160),
        }
        res=STD_DIMENSIONS[args.res[0]]
        print(args.name,self.fourcc,res)
        self.out = cv2.VideoWriter(args.name[0]+'.'+args.type[0],self.fourcc,10,res)

 
        #set video sourec width and height
        self.vid.set(3,res[0])
        self.vid.set(4,res[1])
 
        # Get video source width and height
        self.width,self.height=res
 
 
    # To get frames
    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
            else:
                return (ret, None)
        else:
            return (ret, None)
 
    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
            self.out.release()
            cv2.destroyAllWindows()
 
 
class ElapsedTimeClock:
    def __init__(self,window):
        self.T=tk.Label(window,text='00:00:00',font=('times', 20, 'bold'), bg='green')
        self.T.pack(fill=tk.BOTH, expand=1)
        self.elapsedTime=dt.datetime(1,1,1)
        self.running=0
        self.lastTime=''
        t = time.localtime()
        self.zeroTime = dt.timedelta(hours=t[3], minutes=t[4], seconds=t[5])
        # self.tick()
 
    def tick(self):
        # get the current local time from the PC
        self.now = dt.datetime(1, 1, 1).now()
        self.elapsedTime = self.now - self.zeroTime
        self.time2 = self.elapsedTime.strftime('%H:%M:%S')
        # if time string has changed, update it
        if self.time2 != self.lastTime:
            self.lastTime = self.time2
            self.T.config(text=self.time2)
        # calls itself every 200 milliseconds
        # to update the time display as needed
        # could use >200 ms, but display gets jerky
        self.updwin=self.T.after(100, self.tick)
 
 
    def start(self):
            if not self.running:
                self.zeroTime=dt.datetime(1, 1, 1).now()-self.elapsedTime
                self.tick()
                self.running=1
 
    def stop(self):
            if self.running:
                self.T.after_cancel(self.updwin)
                self.elapsedTime=dt.datetime(1, 1, 1).now()-self.zeroTime
                self.time2=self.elapsedTime
                self.running=0
 
 
class CommandLineParser:
    
    def __init__(self):
 
        # Create object of the Argument Parser
        parser=argparse.ArgumentParser(description='Script to record videos')
 
        # Create a group for requirement
        # for now no required arguments
        # required_arguments=parser.add_argument_group('Required command line arguments')
 
        # Only values is supporting for the tag --type. So nargs will be '1' to get
        parser.add_argument('--type', nargs=1, default=['avi'], type=str, help='Type of the video output: for now we have only AVI & MP4')
 
        # Only one values are going to accept for the tag --res. So nargs will be '1'
        parser.add_argument('--res', nargs=1, default=['480p'], type=str, help='Resolution of the video output: for now we have 480p, 720p, 1080p & 4k')
 
        # Only one values are going to accept for the tag --name. So nargs will be '1'
        parser.add_argument('--name', nargs=1, default=['output'], type=str, help='Enter Output video title/name')
 
        # Parse the arguments and get all the values in the form of namespace.
        # Here args is of namespace and values will be accessed through tag names
        self.args = parser.parse_args()
 
 
 
def main():
    # Create a window and pass it to the Application object
    App(tk.Tk(),'Video Recorder')
 
main()