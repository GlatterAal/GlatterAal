from tkinter import * 
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
import os 

Ordner_Name='' #Variable mit leerem string in welcher später der Pfad zum speicherort der datei gespeichert wird

def öffneDenWeg(): #diese methode lässt den benutzer einen Pfad/ Ordner auswählen
    global Order_Name
    Order_Name = filedialog.askdirectory()
    if len(Order_Name)>1:
        locationErrormsg.config(text=Order_Name,fg='green') #wenn ein ordner ausgewählt und somit die länge des Strings größer als 0 ist wird keine error msg ausgegeben sonder lediglich der ausgewählte Pfad in grüner schrift darsgestellt
    else:
        locationErrormsg.config(text='Please choose Folder',fg='red') # wenn kein pfad ausgewählt und somit der string der variable 0 ist wird die error msg "Please choose folder" in roter schrift ausgegeben

def Video_Runterladen(): # diese Methode läd mit hilfe der Libary "Pytube" das ausgewählte video in der ausgewählten auflösung herunter. 
    choice=choicesButton.get() #in dieser variable wird der in dem Tkinter Element, choicesbutton, ausgewählte String gespeichert 
    url=UrlInput.get() #in dieser variable wird der in dem Tkinter Element, Urlinput, ausgewählte String gespeichert 
    if len(url)>1:
        InputErrormsg.config(text='')  
        yt= YouTube(url) # es wird ein neues objekt der klasse Youtube mit der vom user übergebenen Url iniziirt
        
        if choice==choices[0]: # je nach der wahl wird die entsprechende methode der Youtube klasse ausgeführt und der zurückgegebene wert, in der select variable gespeichert
            select= yt.streams.filter(progressive=True).first() 
        elif choice==choices[1]:
            select= yt.streams.filter(progressive=True,file_extension='mp4').last()
        elif choice==choices[2]:
            select= yt.streams.filter(progressive=True,file_extension='mp4').last()
        else:
            InputErrormsg.config(text='please paste link again',fg='red')

    if choice==choices[0] or choice==choices[1]: #ist die wahl auf auf einen mp4 video in schlechter oder guter qualität defienert so kann die methode download mit dem pfad als übergabewert ausgeführt werden. diese läd automatisch das video herunter und speichert es in dem gewünschten pfad
        select.download(Order_Name)
    else: #wenn ein mp3 download erwünscht ist muss die mp4 datei in eine mp3 datei umgewndelt werden
        old_File=select.download(Order_Name) #dazu wird die gedownloadtete datei in eine variable gespeichert 
        base, ext= os.path.splitext(old_File) #in der base variable wird der name der datei gespeichert in der ext variable die datei endung 
        new_File= base+'.mp3' # nun wird die base variable mit einer neuen endung ".mp3" in der new_file variable gespeichert
        os.rename(old_File,new_File) #die datei old file wird nun mit dem erstellten string new_File mit hilfe der Funktion "rename" aus der klasse "os" neu benannt und somit eine mp3 datei
        
    InputErrormsg.config(text='Download Complete')

root = Tk() #es wird ein neues objekt der klasse Tk iniziirt. dieses objekt bildet die UI und lässt input felder einfügen
root.title('Youtube Dowbnloader') #setzt den Titel der anwendung auf "Youtube Downloader"
root.geometry('350x400')   #setzt die größe der anwendung auf 350 mal 400 px
root.columnconfigure(0,weight=1) #teilt die anweundung in ein grid für eine besssere übersicht

ytLabel= Label(root,text='Enter URL',font=('jost',15)) #fügt der anwendung ein Label/ Text Objekt hinzu
ytLabel.grid() # die grid methode fügt das objekt der anwendung hinzu 

UrlInput= StringVar() 
UrlInput= Entry(root,width=50,textvariable=UrlInput)#hier wird ein text input feld in dem grid eingefügt. der eingegeben input wird in der variable URLInput gespeichert. Somit ist es möglich die url des benutzers zu erlangen
UrlInput.grid()

InputErrormsg= Label(root, text='',fg='red',font=('jost',15))
InputErrormsg.grid()

saveLabel= Label(root, text='Choose Path',font=('jost',15))
saveLabel.grid()

saveButton= Button(root,width=10, bg='red',fg='white',text='path',command=öffneDenWeg) # hier wird ein button in das grid eingefügt welcher bei klicken die methode "öffneDenWeg" ausführt 
saveButton.grid()

locationErrormsg= Label(root, text='',fg='red',font=('jost',15))
locationErrormsg.grid()

LabelwähleQualität=Label(root, text='Choose mode')
LabelwähleQualität.grid()

choices=["highest resolution",'lowest resolution','mp3']
choicesButton=ttk.Combobox(root,values=choices) #hier wird eine auswahl box mit den auswahlmöglichkeiten welche in dem Array "choices" gespeichert sind in das grid eingefügt.
choicesButton.grid()

DownloadButton= Button(root,text='Download',width=10,bg='red',fg='white',command=Video_Runterladen) #hier wird ein button dem Grid hinzugefügt welcher bei klicken die Methode "Video_Herunterladen" ausführt
DownloadButton.grid()
root.mainloop() #Die Methode mainloop des Objektes root führt die anwendung in einer endlosschleife aus.