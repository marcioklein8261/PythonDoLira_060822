from tkinter import *

import requests
import json


# key  apikey=43f0ef38

class MovieData:

    def __init__(self):
        self.window = Tk()
        self.window.title("Movie Data")
        self.window.geometry("1280x720+300+150")
        self.window.resizable(0, 0)

        self.request = requests.get("http://www.https://www.omdbapi.com/?=starwars&apikey=43f0ef38")
        self.dict = json.loads(self.request.text)

        print(self.dict)

        self.window.mainloop()


MovieData()
