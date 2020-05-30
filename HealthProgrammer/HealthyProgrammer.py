from time import *
from datetime import *
from pygame import mixer  # Load the popular external library
import tkinter as tk

path="N:\\Python Program\\HealthyProgrammerLog.txt"
morningTime=18
eveningTime=18
chk='y'
while(chk=='y'):
  if datetime(datetime.now().year,datetime.now().month,datetime.now().day,morningTime)<datetime.now()<datetime(datetime.now().year,datetime.now().month,datetime.now().day,eveningTime,59):
    newtime=60
    mixer.init()
    mixer.music.load('N:\Python Program\Desi Swag - Kambi (DjPunjab.Com).mp3')
    mixer.music.play()

    # this is for popup-----------------
    master = tk.Tk()

    tk.Label(master, text="DO you want more Reminder").grid(row=0)
    tk.Label(master, text="If yes Then please Enter second for next reminder").grid(row=1)


    def reminder():
      global newtime
      if e1.get()=='y' or e1.get()=='yes' or e1.get()=='YES' or e1.get()=='Y' :
        try :
          newtime=int(e2.get())
          file=open(path,"a+")
          str="Date is : {} \n And Time is : {} \n and You want More Reminder of {}sec \n\n\n".format(datetime.now().date(),datetime.now().time(),e2.get())
          file.write(str)
          file.close()
        except:
          newtime = 60
          file = open(path, "a+")
          str = "Date is : {} \n And Time is : {} \n and You Entered incorrect seconds so new Reminder time is {}sec \n\n\n".format(datetime.now().date(),
                                                                                        datetime.now().time(), newtime)
          file.write(str)
          file.close()
      else:
        newtime=4
        file = open(path, "a+")
        str = "Date is : {} \n And Time is : {} \n and You dont want any Reminder Now \n\n\n".format(datetime.now().date(),datetime.now().time())

        file.write(str)
        file.close()



    e1 = tk.Entry(master)
    e2 = tk.Entry(master)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    tk.Button(master,
              text='Save',
              command=reminder).grid(row=3,column=0,sticky=tk.W,pady=4)
    master.mainloop()

    #----------------------

    mixer.music.stop()
    sleep(newtime)


