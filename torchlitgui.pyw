from Tkinter import *
import pythoncom, pyHook
import SendKeys
from multiprocessing import *
import ctypes
def realwork(mouseup,mousedown,middlemouse,n):

    def OnMouseEvent(event):
        rc=True

        
        if event.Message==519 and n.value==1:
            rc=False
            #tx="8 9 {PAUSE .70} 0"
            SendKeys.SendKeys(middlemouse.value)
        if event.Wheel==-1 and n.value==1:
            rc=False
            SendKeys.SendKeys(mousedown.value)
        if event.Wheel==1 and n.value==1:
            rc=False
            SendKeys.SendKeys(mouseup.value)
        # return True to pass the event to other handlers
        return rc
    
    i=0
    #middleclick=""
    #while (i<len(middlemouse)):
    #    middleclick=middleclick+middlemouse[i]
    #print mouseup,mousedown,middleclick
    hm = pyHook.HookManager()
    # watch for all mouse events
    hm.MouseAll = OnMouseEvent
    # set the hook
    hm.HookMouse()
    # wait forever
    pythoncom.PumpMessages()
    if v.get()=="Disabled":
        return 0
############################################################################################
def main():
    freeze_support()
    num = Value('i')
    top = Tk()
    top.wm_title("Torchlit!")
    RWidth=top.winfo_screenwidth()/5
    RHeight=top.winfo_screenheight()/4
    top.geometry(("%dx%d")%(RWidth,RHeight))
    tx="Disabled"
    v=StringVar()
    mu=StringVar()
    md=StringVar()
    mm=StringVar()
    mu.set("'")
    md.set(";")
    mm.set("8 9 {PAUSE .70} 0")
    num.value=0
    #p = Process(target=realwork,args=(mu.get(),md.get(),mm.get(),num))
    up=Value(ctypes.c_char,mu.get())
    down=Value(ctypes.c_char,md.get())
    middle=Array(ctypes.c_char,mm.get())
    p = Process(target=realwork,args=(up,down,middle,num))
    p.start()
    def fun1():
        
        #thread.start_new_thread ( realwork, (mu.get(),md.get(),mm.get()) )
        up.value=mu.get()
        #print up.value
        down.value=md.get()
        #print down.value
        middle.value=mm.get()
        #print middle[:]
        num.value=1
        
        #p.join()
        v.set("Enabled")
    def fun2():
        num.value=0
        v.set("Disabled")
    
    L1 = Label(top, text="Mouse Up")
    L1.pack( side = TOP)
    E1 = Entry(top, bd =5,textvariable=mu,justify=CENTER)
    E1.pack(side = TOP)
    L2 = Label(top, text="Mouse Down")
    L2.pack( side = TOP)
    E2 = Entry(top, bd =5,textvariable=md,justify=CENTER)
    E2.pack(side = TOP)
    L3 = Label(top, text="Middle Mouse")
    L3.pack( side = TOP)
    E3 = Entry(top, bd =5,textvariable=mm,justify=CENTER)
    E3.pack(side = TOP)
    v.set("Disabled")
    L3 = Label(top, textvariable=v)
    L3.pack()
    B1 = Button(top, text ="Start", command = fun1)
    B1.pack(side = LEFT)
    B2 = Button(top, text ="Stop", command = fun2)
    B2.pack(side = RIGHT)
    
    def doSomething():
        # check if saving
        # if not:
        fun2()
        p.terminate()
        top.destroy()
    top.protocol('WM_DELETE_WINDOW', doSomething)
    top.mainloop()
if __name__ == '__main__':
  main()