from tkinter import *
import json
import requests

class MovieData:

    def __init__(self):
        self.window = Tk()
        self.window.title("Movie Data")
        self.window.geometry("500x400+300+150")



        self.frame=Frame(self.window)
        self.frame.pack()

        self.text_entry = Entry(self.frame, font="arial 16", width=30)
        self.text_entry.grid(row=0, column=0)

        self.button_search = Button(self.frame, text="Procura", font="arial 13", command = self.search)
        self.button_search.grid(row=0, column=1)

        self.list = Listbox(self.window)
        self.list.pack(fill=BOTH, expand=YES)



        #print(self.dict)

        self.window.mainloop()

    def search(self):

        request = requests.get("http://www.omdbapi.com/?t=" + self.text_entry.get() + "&apikey=1a3ff30")
        dict = json.loads(request.text)

       # print(dict)

        #print(len(dict))

        #print(dict['Search'])

        try:

            self.list.delete(0, END)
            self.list.insert(END, "Título:  " + "  " + dict["Title"])
            self.list.insert(END, "Ano:  " + "  " + dict["Year"])
            self.list.insert(END, "Lançamento:  " + "  " + dict["Released"])
            self.list.insert(END, "Duração:  " + "  " + dict["Runtime"])
            self.list.insert(END, "Gêndero:  " + "  " + dict["Genre"])
            self.list.insert(END, "Diretor:  " + "  " + dict["Director"])
        except:

            self.list.delete(0, END)
            self.list.insert(END, "Filme não encontrado")



MovieData()