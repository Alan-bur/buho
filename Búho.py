# Libraries
from instabot import Bot
from tkinter import *
from tkinter import messagebox
import os as os
import webbrowser
import urllib.request

# Window
win = Tk()
win.title("búho")
win.resizable(width=False, height=False)
win.geometry("900x600")
win.iconbitmap("icon.ico")
win.iconposition(x=100, y=10)
afont = "Bahnschrift"  # App Font

# InstaBot
bot = Bot()
botv = bot.version()

# Console Welcome
def console_welcome():
    print("")
    print("     ▓▓                                   ")
    print("     ▓▓         ▓                       ")
    print("     ▓▓        ▓                        ")
    print("     ▓▓▓▓▓▓ ▓▓  ▓▓ ▓▓  ▓▓ ▓▓▓▓▓▓")
    print("     ▓▓▓▓▓▓ ▓▓  ▓▓ ▓▓  ▓▓ ▓▓▓▓▓▓")
    print("     ▓▓  ▓▓ ▓▓  ▓▓ ▓▓▓▓▓▓ ▓▓  ▓▓")
    print("     ▓▓▓▓▓▓ ▓▓▓▓▓▓ ▓▓  ▓▓ ▓▓▓▓▓▓")
    print("     ▓▓▓▓▓▓ ▓▓▓▓▓▓ ▓▓  ▓▓ ▓▓▓▓▓▓")
    print("")
    print("#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-#")
    print("             Welcome, " + os.getlogin())
    print("#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-#")
console_welcome()

# Console Clean
def console_clean():
    global clean
    clean = os.system("cls")


# ------------------------------Useful Variables------------------------------
# -----Colors-----
tcolor = "grey16"
abcolor = "grey40"  # Active Button Background
abcolorback = "grey20"  # Active Button background for "Back" buttons
abcoloreye = "grey25"  # Active Button for see password
# -----App Background Width/Height
background_w = width = 900
background_h = height = 600

# -----Bars Width/Height-----
bw, bh = 223, 600
# -----Square Width/height-----
sw, sh = 223, 226

# -----Buttons Width/Height (Logged in bar)-----
logedin_w = 223
logedin_h = 64
# ----settings buttons Width/height----
setw, seth = 223, 41

# ************** User Interface **************


# App Background

background_img = PhotoImage(file="UI/Background/buho.png")
background = Label(win, width=background_w, height=background_h, image=background_img)
background.place(x=-2, y=-2)

# Bar
barimg = PhotoImage(file="UI/bar/bar.png")
bar = Label(win, image=barimg, borderwidth=0, highlightthickness=0, width=bw, height=bh)
bar.place(x=0, y=0)

# Bar (Error)
bar_errorimg = PhotoImage(file="UI/bar/error/bar_error.png")
bar_error_show = Label(win, image=bar_errorimg, borderwidth=0, highlightthickness=0, width=bw, height=bh)

# Bar (Already loged in)

bar_loginimg = PhotoImage(file="UI/bar/login_bar/bar_login.png")
bar_login = Label(win, image=bar_loginimg, borderwidth=0, highlightthickness=0, width=bw, height=bh)


# ***Unfollow Unfollowers***
def unfollowfunction():
    global unfollowbar
    unfollowbar.place(x=0, y=0)
    settingsback()


    accessbutton.place_forget()
    showpostscount.place_forget()
    showfollowing.place_forget()
    showfollowers.place_forget()
    showname.place_forget()
    unfollowbutton.place_forget()
    followbackbutton.place_forget()


unfollowbarimg = PhotoImage(file="UI/bar/unfollowersbar/unfollowers_bar.png")
unfollowbar = Label(win, width=bw, height=bh, image=unfollowbarimg, highlightthickness=0, borderwidth=0)

unfollowimg = PhotoImage(file="UI/bar/login_bar/unfollow_unfollowers.png")
unfollowbutton = Button(win, width=logedin_w, height=logedin_h, image=unfollowimg, borderwidth=0, highlightthickness=0,
                        command=lambda: unfollowfunction())


def btm2_button():
    global btm2, btm2_button
    btm2 = Button(win, width=0, height=0, text="◀", font="Bahnschrift 14", fg="white", bg="grey17",
                      borderwidth=0,
                      highlightthickness=0, activebackground=abcolorback, command=lambda: bts())
    btm2.place(x=8, y=168)


# Follow back
def followback():
    global followbackimg
    global followbackbutton
    followbackimg = PhotoImage(file="UI/bar/login_bar/followback.png")
    followbackbutton = Button(win, width=logedin_w, height=logedin_h, image=followbackimg, borderwidth=0,
                              highlightthickness=0, command=lambda: followbackfunction())
    followbackbutton.place(x=0, y=315)

    def followbackfunction():
        bot.follow_followers()


# Login
status = "waiting"
login = Button(win, text="Log In", borderwidth=0, highlightthickness=0, width=25, height=2, bg="grey18", fg="LightSkyBlue", font=afont + "0", activebackground="grey20", activeforeground="LightSkyBlue", command=lambda: botonlogin())
login.place(x= -6, y=395)

def botonlogin():
    global username
    username = usernameentry.get()
    global password
    password = passwordentry.get()
    global loginbot
    loginbot = bot.login(username=username, password=password)
    login_tf()


def login_tf():
    global loginbot, status
    if loginbot == TRUE:
        status = "successful"
        getuserid = bot.get_user_id_from_username(username)
        userinfo = bot.get_user_info(user_id=getuserid)
        userfollowersid = bot.get_user_followers(user_id=getuserid)
        followers = userinfo['follower_count']
        following = userinfo['following_count']
        posts = userinfo['media_count']

        userpicurl = userinfo['profile_pic_url']
        urllib.request(url=userpicurl)
        print(userinfo)
        hide_menu1()
        bar_login.place(x=0, y=0)
        logoutbutton.place(x=851, y=0)
        unfollowbutton.place(x=0, y=240)
        settings.place(x=97, y=545)
        accessbutton.place_forget()
        followback()
        console_clean()
        print("-----------------------------")
        print("********Account Info********")
        print("-----------------------------")
        print("Username | @" + username)
        print("-----------------------------")
        print("UserID | " + getuserid)
        print("-----------------------------")
        print("Followers | " + str(followers))
        print("-----------------------------")
        print("Following | " + str(following))
        print("-----------------------------")
        print("Posts | " + str(posts))
        print("-----------------------------")
        global showname
        showname = Label(win, text=username, font=afont, fg="white", bg="grey23")
        showname.place(x=70, y=138)
        global showfollowers
        showfollowers = Label(win, text=followers, width=3, height=1, highlightthickness=0, borderwidth=0, bg="grey17",
                              fg="white", font=afont)
        showfollowers.place(x=30, y=195)
        global showfollowing
        showfollowing = Label(win, text=following, width=3, height=1, highlightthickness=0, borderwidth=0, bg="grey17",
                              fg="white", font=afont)
        showfollowing.place(x=165, y=195)
        global showpostscount
        showpostscount = Label(win, text=posts, width=3, height=1, highlightthickness=0, borderwidth=0, bg="grey17",
                               fg="white", font=afont)
        showpostscount.place(x=100, y=195)
        messagebox.showinfo(title="Congratulations!", message="Successfully connected!")
    if loginbot == False:
        status = "waiting"
        square_error()
        messagebox.showerror(title="Ouch.. Something went wrong",
                             message="See if you have used the correct Username/Password, if everything seems fine, consider changing your password. If you still have problems, check the console for more detailed info")


# Back To Settings
global btsb , bts_button

def bts():
    set_function()
    setbar.place(x=0, y=0)
    donate_button.place(x=0, y=348)
    btsb.place_forget()
    if here == "about":
        credit.place_forget()
        version_text.place_forget()
        instabot_text.place_forget()
    if here == "donate":
        paypalbutton.place_forget()
        igbutton.place_forget()
        donationbar.place_forget()
    if here == "language":
        lanbar.place_forget()

def bts_button():
    global btsb
    btsb = Button(win, width=0, height=0, text="◀", font="Bahnschrift 14", fg="white", bg="grey17",
                      borderwidth=0,
                      highlightthickness=0, activebackground=abcolorback, command=lambda: bts())
    btsb.place(x=8, y=168)

# Settings
def settingsback():
    global settingsback, sb
    if status == "waiting":
        sb = Button(win, width=0, height=0, text="◀", font="Bahnschrift 14", fg="white", bg="grey17", borderwidth=0,
                        highlightthickness=0, activebackground=abcolorback, command=lambda: menu1())

    if status =="successful":
        sb = Button(win, width=0, height=0, text="◀", font="Bahnschrift 14", fg="white", bg="grey17", borderwidth=0,
                     highlightthickness=0, activebackground=abcolorback, command=lambda: menu2())

    sb.place(x=8, y=168)

def set_function():
    settingsback()
    setbar.place(x=0, y=0)
    global setlabel
    setlabel = Label(win, text="Settings", font=afont + "10", bg=tcolor, fg="lightskyblue")
    setlabel.place(x=78, y=174)
    donate_button.place(x=0, y=348)
    accessbutton.place(x=0, y=255)
    language.place(x=0, y=209)
    aboutbutton.place(x=0, y=301)
    aboutbar.place_forget()
    paypalbutton.place_forget()
    igbutton.place_forget()
    donationbar.place_forget()
    hide_menu1()
    if status == "successful":
        hide_menu2()


setimg = PhotoImage(file="UI/bar/settingsbar/settings.png")
settings = Button(win, width=30, height=30, image=setimg, borderwidth=0, highlightthickness=0,
                  activebackground=abcolor, command=lambda: set_function())
settings.place(x=97, y=545)

# Menu 1
def menu1():
    square.place(x=0, y=169)
    tip.place(x=20, y=175)
    passwordl.place(x=31, y=300)
    usernamel.place(x=31, y=235)
    eye_closed.place(x=190, y=338)
    settings.place(x=97, y=545)
    bar.place(x=0, y=0)
    usernameentry.place(x=37, y=270)
    passwordentry.place(x=37, y=336)
    login.place(x=-6, y=395)
    usernamel.config(fg="grey45")
    tip.config(fg="lightskyblue")
    passwordl.config(fg="grey45")
    language.place_forget()
    app_version()
    recoverbutton()
    setlabel.place_forget()
    donate_button.place_forget()
    setbar.place_forget()
    aboutbutton.place_forget()
    sb.place_forget()


# Menu 2
def menu2():
    hide_set()
    showpostscount.place(x=100, y=195)
    showfollowing.place(x=165, y=195)
    showfollowers.place(x=30, y=195)
    showname.place(x=70, y=138)
    unfollowbutton.place(x=0, y=240)
    followbackbutton.place(x=0, y=315)
    bar_login.place(x=0, y=0)
    settings.place(x=97, y=545)
    unfollowbar.place_forget()
    app_version()
    sb.place_forget()
    language.place_forget()
    bar.place_forget()
    donate_button.place_forget()
    setbar.place_forget()
    donationbar.place_forget()
    aboutbutton.place_forget()

# Hide Menu 1
def hide_menu1():
    square.place_forget()
    tip.place_forget()
    passwordl.place_forget()
    usernamel.place_forget()
    eye_opened.place_forget()
    eye_closed.place_forget()
    settings.place_forget()
    bar.place_forget()
    usernameentry.place_forget()
    passwordentry.place_forget()
    login.place_forget()
    bar_error_show.place_forget()
    recoverpassword.place_forget()
# Hide Menu 2
def hide_menu2():
    showfollowers.place_forget()
    showfollowing.place_forget()
    showpostscount.place_forget()
    recoverpassword.place_forget()
    showname.place_forget()
    bar_login.place_forget()
    unfollowbutton.place_forget()
    followbackbutton.place_forget()
    unfollowbar.place_forget()

# Hide Settings
def hide_set():
    setlabel.place_forget()
    accessbutton.place_forget()
    donate_button.place_forget()
    language.place_forget()
    aboutbutton.place_forget()
    setbar.place_forget()
    app_versionlabel.place_forget()
    sb.place_forget()
    settings.place_forget()

# Settings bar
setbarimg = PhotoImage(file="UI/bar/settingsbar/settingsbar.png")
setbar = Label(win, image=setbarimg, width=bw, height=bh, borderwidth=0, highlightthickness=0)

# Accesibility
def accesibilityfunction():
    global here
    here = "accesibility"
    hide_set()
    bts_button()
    app_version()


aboutbarimg = PhotoImage(file="UI/bar/aboutbar/aboutbar.png")
aboutbar = Label(win, image=aboutbarimg, width=bw, height=bh, highlightthickness=0, borderwidth=0)

accessimg = PhotoImage(file="UI/bar/settingsbar/accessibility.png")
accessbutton = Button(win, anchor="w", text="  Accessibility", font=afont + "10", bg="grey20", fg="grey60", width=221, height=41, highlightthickness=0, borderwidth=0, activebackground=abcolor,
                       image=accessimg, compound="left", command=lambda: accesibilityfunction())
accessbutton.place(x=0, y=300)

# About
def aboutfunction():
    global here
    here = "about"
    global  version_text, credit, instabot_text

    version_text = Label(text="App version: " + aversion, font=afont + "8", bg="grey16", fg="grey")
    version_text.place(x=10, y=220)

    credit = Label(text="Credit: Alan Burcet", font=afont + "8", bg="grey16", fg="grey")
    credit.place(x=10, y=250)

    instabot_text = Label(text="Instabot: " + botv, font=afont + "8", bg="grey16", fg="grey")
    instabot_text.place(x=10, y=280)

    hide_set()
    bts_button()
    app_version()
    aboutbar.place(x=0, y=0)


aboutbarimg = PhotoImage(file="UI/bar/aboutbar/aboutbar.png")
aboutbar = Label(win, image=aboutbarimg, width=bw, height=bh, highlightthickness=0, borderwidth=0)

aboutimg = PhotoImage(file="UI/bar/settingsbar/about.png")
aboutbutton = Button(win, anchor="w", text="  About", font=afont + "10", bg="grey20", fg="grey60", width=221, height=41, highlightthickness=0, borderwidth=0, activebackground=abcolor,
                       image=aboutimg, compound="left", command=lambda: aboutfunction())

# Donations

donate_button_img = PhotoImage(file="UI/bar/settingsbar/donations.png")
donate_button = Button(win, anchor="w", text="  Donation", font=afont + "10", bg="grey20", fg="grey60", width=221, height=41, highlightthickness=0, borderwidth=0, activebackground=abcolor,
                       image=donate_button_img, compound="left", command=lambda: donation())

donate_bar_img = PhotoImage(file="UI/bar/donationbar/donationbar.png")
donationbar = Label(win, image=donate_bar_img, width=bw, height=bh, highlightthickness=0, borderwidth=0)

paypalimg = PhotoImage(file="UI/bar/donationbar/paypal.png")
paypalbutton = Button(win, image=paypalimg, width=102, height=35, activebackground="navy", borderwidth=0,
                      highlightthickness=0, command=lambda: paypal())

igimg = PhotoImage(file="UI/bar/donationbar/ig.png")
igbutton = Button(win, image=igimg, width=102, height=35, borderwidth=0, highlightthickness=0,
                  activebackground="purple", command=lambda: ig())



def donation():
    global here
    here = "donate"
    hide_set()
    app_version()
    bts_button()
    paypalbutton.place(x=62, y=280)
    igbutton.place(x=62, y=321)
    donationbar.place(x=0, y=0)
    global ig

    def ig():
        link = "https://www.instagram.com/alanburcet/"
        webbrowser.open(link)

    global paypal

    def paypal():
        link = "https://paypal.me/deadpxlz?locale.x=es_XC"
        webbrowser.open(link)

# ***Language****

lanbarimg = PhotoImage(file="UI/bar/languagebar/languagebar.png")
lanbar = Label(win, image=lanbarimg, width=bw, height=bh, highlightthickness=0, borderwidth=0)

def lanfunction():
    global here
    here = "language"
    lanbar.place(x=0, y=0)
    hide_set()
    app_version()
    bts_button()



lanimg = PhotoImage(file="UI/bar/settingsbar/language.png")
language = Button(win, anchor="w", text="  Language", font=afont + "10", bg="grey20", fg="grey60", width=221, height=41, highlightthickness=0, borderwidth=0, activebackground=abcolor,
                       image=lanimg, compound="left", command=lambda: lanfunction())

def español_arg():
    setlabel.config(text="Configuracion")
    tip.config(text="Ingrese su Instagram")
    passwordl.config(text="Contraseña")
    usernamel.config(text="Usuario")



# *** Square ***
def square_normal():
    square.place(x=0, y=169)
    global tip, passwordl, usernamel
    usernamel = Label(win, width=9, height=1, text="Username", font=afont + "15", bg="grey23", fg="grey45")
    passwordl = Label(win, width=9, height=1, text="Password", font=afont + "15", bg="grey23", fg="grey45")
    tip = Label(win, width=20, height=1, text="Use Instagram Details", font=afont + "15", bg="grey16",
                fg="lightskyblue")
    tip.place(x=20, y=175)
    passwordl.place(x=31, y=300)
    usernamel.place(x=31, y=235)

squareimg = PhotoImage(file="UI/bar/square.png")
square = Label(win, image=squareimg, borderwidth=0, highlightthickness=0, width=sw, height=sh)
square_normal()
def square_error():
    bar_error_show.place(x=0, y=0)
    usernamel.config(fg="red3")
    tip.config(fg="red3")
    passwordl.config(fg="red3")

square_red_img = PhotoImage(file="UI/bar/error/squareerror.png")
square_red = Label(win, image=square_red_img, borderwidth=0, highlightthickness=0, width=sw, height=sh)

# *** Username entry***
usernameentry = Entry(win, borderwidth=0, highlightthickness=0, width=16, bg="grey", fg="black", font="Bahnschrift")
usernameentry.place(x=37, y=270)

# *** Password ***
passwordentry = Entry(win, borderwidth=0, highlightthickness=0, width=16, bg="grey", fg="black", font="Bahnschrift",
                      show="*")
passwordentry.place(x=37, y=336)

def eye_opened_function():
    eye_closed.place_forget()
    eye_opened.place(x=190, y=338)
    passwordentry.config(show="")

def eye_closed_function():
    eye_closed.place(x=190, y=338)
    eye_opened.place_forget()
    passwordentry.config(show="*")


eye_closedimg = PhotoImage(file="UI/bar/eye_closed.png")
eye_closed = Button(win, width=30, height=15, image=eye_closedimg, borderwidth=0, highlightthickness=0, bg="grey23",
             activebackground=abcoloreye, command=lambda: eye_opened_function())
eye_closed.place(x=190, y=338)

eye_openedimg = PhotoImage(file="UI/bar/eye_open.png")
eye_opened = Button(win, width=30, height=15, image=eye_openedimg, borderwidth=0, highlightthickness=0, bg="grey23",
             activebackground=abcoloreye, command=lambda: eye_closed_function())

# ***Log out***
def logout():
    logoutmsg = messagebox.askyesno(title="Account action",
                                    message="You are about to disconect your account and go back to the main screen, do you want to continue?")
    if logoutmsg == YES:
        global status
        status = "waiting"
        bot.logout()
        hide_menu2()
        menu1()
        usernameentry.delete(0, END)
        passwordentry.delete(0, END)
        logoutbutton.place_forget()


logoutimg = PhotoImage(file="UI/endsession/close_login.png")
logoutbutton = Button(win, width=50, height=50, image=logoutimg, borderwidth=0, highlightthickness=0,
                      command=lambda: logout())


# Recover Password
def recoverbutton():
    global recoverpassword
    recoverpassword = Button(win, text="Recover Password", font="Bahnschrift 10", bg="grey20", fg="grey60", width=20,
                             height=1, activebackground="grey60", activeforeground="grey20", highlightthickness=0,
                             borderwidth=0, command=lambda: recoverfunction())
    recoverpassword.place(x=40, y=455)

    def recoverfunction():
        message = messagebox.askyesno(title="Password recovery page",
                                      message="This will open your browser, do you want to continue?")
        if message == YES:
            webbrowser.open("https://www.instagram.com/accounts/password/reset/?hl=en")


recoverbutton()


# App Version
def app_version():
    global aversion, app_versionlabel
    aversion = "Alpha"  # App Version text
    app_versionlabel = Label(win, text=aversion, width=31, height=1, font="Bahnschrift 10", fg="darkgrey", bg="gray13")
    app_versionlabel.place(x=0, y=577)


app_version()

# End Window
win.mainloop()
