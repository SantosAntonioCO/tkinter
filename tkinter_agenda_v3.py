from Tkinter import *
import tkinter as tk
import tkFont
 
#http://www.java2s.com/Code/Python/GUI-Tk/LayoutframefillBOTHexpandYES.htm
#https://www.python-course.eu/tkinter_layout_management.php
#http://www.java2s.com/Code/Python/GUI-Tk/LayoutsideTOPLEFTLEFT.htm
#https://askubuntu.com/questions/27097/how-to-print-a-regular-file-to-pdf-from-command-line

import subprocess
#proc = subprocess.Popen(['pluma', 'extra_info.dat'])
#command_0="paps extra_info.txt | ps2pdf - output.pdf"
#subprocess.call([command_0], shell=True)


import datetime #https://stackabuse.com/how-to-format-dates-in-python/
today = datetime.date.today()  
#print(today) 
data=today.ctime() 
#print data[0:10], data[-4:]
#data_dia=data[0:10]+data[-5:]


def callback():
    print "click!"

def opentext():
    proc = subprocess.Popen(['pluma', '/home/extra_info.txt'])
#    command_1="evince output.pdf"
#    command_1="evince /home/antonio/Documents/programming/python/general/screen/white/pygame/examples/output.pdf"
    subprocess.call([command_1], shell=True)


# text font
from itertools import cycle
fonts = cycle((('Helvetica', '9'),('Helvetica', '9'),('Helvetica', '9')))
fontsII = cycle((('Helvetica', '7'),('Helvetica', '7'),('Helvetica', '7')))
# put there =>font=next(fonts)


#data
from datetime import date
f_date = date(2019, 8, 22)
later_date = date(2019, 9, 6)
delta = later_date - f_date

def data_left(diafinal,mesfinal,anofinal):
  from datetime import date
  import datetime
  today = datetime.date.today()  
  today_date = date(2019, today.month, today.day)
  later_date = date(anofinal, mesfinal, diafinal)
  diasleft = later_date - today_date
  
  return int(diasleft.days)


#button color
dataifusp=data_left(31,8,2019)
dataTese=data_left(29,8,2019)
dataufrn=data_left(27,9,2019)
dataufrpe=data_left(6,9,2019)

def colorbutton(corbasica,data):
  if data>=9:
    cor1=corbasica
  elif data<=8 and data>=5:
    cor1="chocolate3"    #chocolate1
  else:
    cor1="red"    #chocolate1
  return cor1
   
print colorbutton("snow3",dataifusp)
print colorbutton("coral",dataTese)
print colorbutton("coral",dataufrn)
# COLORS https://stackoverflow.com/questions/4969543/colour-chart-for-tkinter-and-tix


class App:
    def __init__(self, master):
        master.geometry("400x900")  # size is defined below in  center_window(200, 400)
        fm = Frame(master)
        fm1 = Frame(master)
        Button(fm, text = "X",bg = "gray", command = lambda: root.destroy()).pack(side=TOP,fill=X, expand=YES)
        Button(fm, text= data[0:10]+data[-5:], fg="orange",bg = "SkyBlue4", command=opentext).pack(side=TOP,    fill=X, expand=YES)
    
        Button(fm, text='Tese >'+str(int(29-float(data[8:10]))),bg = colorbutton("coral",dataTese)).pack(side=TOP, fill=X, expand=YES)

        #Button(fm1, text='Tese 2').pack(side=TOP, fill=X, expand=YES) 
        Button(fm, text='(Paper)', relief=FLAT).pack(side=TOP, fill=X, expand=YES)




        Button(fm, text='Act I'+str(data_left(31,8,2019)), command=opentext,bg = colorbutton("snow3",dataifusp)).pack(side=TOP, fill=X, expand=YES)
        Button(fm, text='Act II', fg="orange",bg = "black").pack(side=TOP,    fill=X, expand=YES)

        Button(fm, text='Act III 27'+str([data_left(27,8,2019),data_left(15,9,2019),data_left(20,9,2019)]), command=opentext, fg="black" ,bg = colorbutton("coral",dataufrn) ,font=next(fonts)).pack(side=TOP, fill=X, expand=YES) 

        Button(fm, text='Act IV 06/09->'+str([data_left(6,9,2019)]), command=opentext, fg="black" ,bg = colorbutton("turquoise1",dataufrpe),font=next(fontsII)).pack(side=TOP, fill=X, expand=YES) 

        Button(fm, text='Act V', relief= SUNKEN).pack(side=TOP, fill=X, expand=YES)
        #Button(fm, text='Pos-Doc uaf.ufcg 21 june').pack(side=TOP, fill=X, expand=YES)

        Button(fm, text='Act VI', command=opentext).pack(side=TOP, fill=X, expand=YES)
#        Button(fm, text='Concursos IF',  fg="black" ).pack(side=TOP, fill=X, expand=YES)
   #     Button(fm, text='Concurso PB', command=opentext, fg="black" ).pack(side=TOP, fill=X, expand=YES)

        
        #Button(fm, text='Algo mais', fg="white", relief=GROOVE ).pack(side=TOP, fill=X, expand=YES)
        #Button(fm, text='RIDGE', fg="white", relief=RIDGE ).pack(side=TOP, fill=X, expand=YES) 
        #Button(fm, text = "Close",bg = "blue", command = lambda: root.destroy()).pack(side=TOP, fill=X, expand=YES)
    
        Button(fm, text= 'Act VII',bg = "seashell2",font=next(fontsII)).pack(side=LEFT) #\u03a9 h^2
#        Button(fm, text= u'<\u03C3v^2>').pack(side=LEFT) #\u03a9 h^2
        Button(fm, text='Act VIII',bg = "seashell3").pack(side=LEFT)
        #Button(fm, text='Tese', relief=FLAT).pack(side=TOP, fill=X, expand=YES)
        Button(fm, text='Act IX',bg ='dark orange').pack(side=RIGHT, fill=X, expand=YES)

        #Button(fm, text='M2').pack(side=BOTTOM, fill=X, expand=YES)   # working but no space 

        #Button(fm, text = "cuts").pack(side=BOTTOM, fill=X, expand=YES)
        #Button(fm, text='Right').pack(side=LEFT) 

        #Button(fm, text="Black", fg="black").pack( side = BOTTOM, fill=X, expand=YES)


        fm.pack(fill=X, expand=YES)
        #fm1.pack(fill=X, expand=YES,padx=5,pady=0, side=LEFT)
        #fm.pack(fill=BOTH, expand=YES)

#*****************************+
class Drag:
    ''' Makes a window dragable. '''
 


    def __init__ (self, par, dissable=None, releasecmd=None) :

        self.Par        = par
        self.Dissable   = dissable

        self.ReleaseCMD = releasecmd

        self.Par.bind('<Button-1>', self.relative_position)
        self.Par.bind('<ButtonRelease-1>', self.drag_unbind)


    def relative_position (self, event) :

        cx, cy = self.Par.winfo_pointerxy()
        x, y = event.x, event.y # event.x, event.y

        self.OriX = x
        self.OriY = y

        self.RelX = cx - x
        self.RelY = cy - y

        self.Par.bind('<Motion>', self.drag_wid)

    def drag_wid (self, event) :

        cx, cy = self.Par.winfo_pointerxy()

        d = self.Dissable

        if d == 'x' :
            x = self.OriX
            y = cy - self.RelY
        elif d == 'y' :
            x = cx - self.RelX
            y = self.OriY
        else:
            x = cx - self.RelX
            y = cy - self.RelY

        if x < 0 :
            x = 0

        if y < 0 :
            y = 0

        self.Par.wm_geometry('+' + str(x) + '+' + str(y))

    def drag_unbind (self, event) :

        self.Par.unbind('<Motion>')

        if self.ReleaseCMD != None :
            self.ReleaseCMD()


    def dissable (self) :

        self.Par.unbind('<Button-1>')
        self.Par.unbind('<ButtonRelease-1>')
        self.Par.unbind('<Motion>')


#**********************

        
root = Tk()
root.option_add('*font', ('times', 12, 'bold'))
root.title("Pack - Example 8a")
display = App(root)
#window = Toplevel(root)
def center_window(width=100, height=50):
    # get screen width and height
    screen_width = 0.1*root.winfo_screenwidth()
    screen_height = 0.1*root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (3.95*screen_width) #- (width/2)
    y = (.3*screen_height) #- (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

root.overrideredirect(True) #Remove border
center_window(200, 450)
Drag(root)
#transparency  https://stackoverflow.com/questions/18394597/is-there-a-way-to-create-transparent-windows-with-tkinter
root.wait_visibility(root)
root.wm_attributes('-alpha',0.99) 
 


root.mainloop()   # just to show



'''

COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
          'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
          'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
          'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
          'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
          'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
          'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
          'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
          'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
          'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
          'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
          'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
          'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
          'indian red', 'saddle brown', 'sandy brown',
          'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
          'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
          'pale violet red', 'maroon', 'medium violet red', 'violet red',
          'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
          'thistle', 'snow2', 'snow3',
          'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
          'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
          'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
          'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
          'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
          'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
          'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
          'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
          'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
          'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
          'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
          'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
          'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
          'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
          'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
          'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
          'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
          'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
          'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
          'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
          'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
          'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
          'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
          'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
          'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
          'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
          'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
          'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
          'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
          'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
          'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
          'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
          'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
          'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
          'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
          'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
          'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
          'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
          'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
          'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
          'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
          'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
          'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
          'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
          'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
          'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
          'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
          'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
          'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
          'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
          'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
          'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
          'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
          'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
          'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
          'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
          'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']
'''









