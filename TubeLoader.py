from pytube import YouTube
from tkinter import *
from tkinter.filedialog import askdirectory
from threading import Thread
from tkinter.messagebox import showinfo


file_size = 0


#This function calls for updaiting for % :
def progress(stream = None, file_handle=None, bytes_remaining = None):
    #Get the percentage of file
    file_downloaded = file_size - bytes_remaining
    per = (file_downloaded / file_size)*100
    #dBtn.config(text = "{:00.0f} % downloaded".format(per))
    dBtn.config(text = "{:00.0f} % downloaded ({:00.00f} / {:00.00f} MB) ".format(per, file_downloaded/1000000, file_size/1000000))

def start_download():
            global file_size

            url = urlField.get()
            #print(url)
            dBtn.config(text = "Please wait...")
            dBtn.config(state = DISABLED)
            #url = "https://www.youtube.com/watch?v=NLOp_6uPccQ"
            path_to_save = askdirectory()
            print(path_to_save)
            if path_to_save is None:
                return
            # Creating youtube object with URl:
            ob = YouTube(url, on_progress_callback = progress)
            # strms = ob.streams.all()
            # for s in strms:
            #     print(s)
            strms = ob.streams.first()
            file_size= strms.filesize
            vTitle.pack(side=TOP)
            vTitle.config(text = strms.title)
            #print(strms)
            print("File Size :", ((file_size) / 1000000), "mb")
            print("Title :", strms.title)

            # Download Function:
            print("Downloading file...")
            strms.download(path_to_save)
            print("Done...")
            dBtn.config(text = "Start Download")
            dBtn.config(state = NORMAL)
            showinfo("Download Finished", "Downloaded Successfully")
            urlField.delete(0, END)
            vTitle.pack_forget()

    # except Exception as e:
    #     print(e)
    #     print("Error found!")

def DownThread ():
    #New Thread:
    thread= Thread(target = start_download)
    thread.start()

#url=str(input("Enter a url: "))
#start_download(url)
#Gui Design:
main= Tk()

#Setting the title:
main.title("TubeLoader")

#Icon setup:
main.iconbitmap("youtube flat.ico")
main.geometry("500x600")

#Heading icon:
file = PhotoImage (file ="youtube flat.png")
headingIcon = Label(main, image=file)
headingIcon.pack(side = TOP)


#url Field:
urlField = Entry(main, font = ("Verdana", 15), justify= CENTER)
urlField.pack(side = TOP, fill=X, padx=20, pady=10)
#url = urlField.get()

#Download button
dBtn = Button(main, text= 'Start Download', font= ("Verdana", 12), relief = 'ridge', command= DownThread)
dBtn.pack(side = TOP, pady=5)

#video title
vTitle = Label (main, text = "Video Title")

main.mainloop()

