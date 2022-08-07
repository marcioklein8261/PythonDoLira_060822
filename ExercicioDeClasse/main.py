import tkinter


class App:
    def __init__(self):
        self.valor = 20

        self.janela = tkinter.Tk()
        self.janela.title("Marcador")
        self.janela.minsize(width=360, height=640)
        self.janela.maxsize(width=360, height=640, )

        self.text = tkinter.Label(self.janela, text="20", font="Arial 50 bold", pady=50)

        self.text.pack()

        self.frame = tkinter.Frame(self.janela, bg="white")
        self.frame.pack()

        self.botaoMais = (tkinter.Button(self.frame, text="Δ", bg="orange", pady=10, width=20, command=self.mais))
        self.botaoMais.pack(side="left")

        self.botaoMenos = (tkinter.Button(self.frame, text="∇", bg="orange", pady=10, width=20, command=self.menos))
        self.botaoMenos.pack(side="left")

        self.janela.mainloop()

    def mais(self):
        if self.valor<20:
            self.valor += 1
            self.text.config(text="{}".format(self.valor))

    def menos(self):
        if self.valor>0:
            self.valor -= 1
            self.text.config(text="{}".format(self.valor))


App()
