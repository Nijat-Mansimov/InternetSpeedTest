from tkinter import *
import speedtest

window = Tk()
window.title("Internet Speed Test")
window.geometry("360x600")
window.resizable(False, False)
window.config(bg="#1a212d")

def check():
    global upload, download, Download
    test = speedtest.Speedtest()
    uploading = round(test.upload()/(1024*1024), 2)
    print(uploading)
    upload.config(text=uploading)

    downloading = round(test.download()/(1024*1024), 2)
    # print(downloading)
    download.config(text=downloading)
    Download.config(text=downloading)

    servernames = []
    test.get_servers(servernames)
    # print(test.results.ping)
    ping.config(text=test.results.ping)

image_icon = PhotoImage(file="Images/logo.png")
window.iconphoto(False, image_icon)

panel = PhotoImage(file="Images/top.png")
Label(window, image=panel, bg="#1a212d").pack()

table = PhotoImage(file="Images/main.png")
Label(window, image=table, bg="#1a212d").pack(pady=(40, 0))

button = PhotoImage(file="Images/button.png")
start = Button(
                window, image=button,
                bg="#1a212d", bd=0, 
                activebackground="#1a212d", 
                cursor="hand2", command=check)
start.pack(pady=10)

Label(window, text="PING", font="arial 10 bold", bg="#384056").place(x=50, y=0)
Label(window, text="DOWNLOAD", font="arial 10 bold", bg="#384056").place(x=140, y=0)
Label(window, text="UPLOAD", font="arial 10 bold", bg="#384056").place(x=260, y=0)

Label(window, text="MS", font="arial 7 bold", bg="#384056", fg="white").place(x=60, y=80)
Label(window, text="MBPS", font="arial 7 bold", bg="#384056", fg="white").place(x=165, y=80)
Label(window, text="MBPS", font="arial 7 bold", bg="#384056", fg="white").place(x=275, y=80)

Label(window, text="Download", font="arial 15 bold", bg="#384056", fg="white").place(x=140, y=280)
Label(window, text="MBPS", font="arial 15 bold", bg="#384056", fg="white").place(x=155, y=380)

ping = Label(window, text="00", font="arial 13 bold", bg="#384056", fg="white").place(x=70, y=60, anchor="center")
download = Label(window, text="00", font="arial 13 bold", bg="#384056", fg="white").place(x=180, y=60, anchor="center")
upload = Label(window, text="00", font="arial 13 bold", bg="#384056", fg="white").place(x=290, y=60, anchor="center")

Download = Label(window, text="00", font="arial 40 bold", bg="#384056").place(x=185, y=350, anchor="center")


window.mainloop()