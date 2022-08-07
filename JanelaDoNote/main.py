import tkinter

def NovoArquivo():
    areaDeTexto.delete(1.0,"end")

def SalvaArquivo():
    textoDoNote=areaDeTexto.get(1.0,"end")
    arquivoA_Gravar=open("notepad.txt", "w")
    arquivoA_Gravar.write(textoDoNote)
    arquivoA_Gravar.close()

def Abrir():
    arquivoA_Ler=open("notepad.txt","r")
    textoDoNote=arquivoA_Ler.read()
    areaDeTexto.insert(1.0,textoDoNote)


def AtualizaFonte():
    tamanho = rolarTamanho.get()
    fonte=rolarTipoDoFonte.get()
    areaDeTexto.config(font="{} {}". format(fonte,tamanho))

janela = tkinter.Tk()

janela.title("Notepad do Marcio")

janela.geometry("1200x720")

areaDeTexto=tkinter.Text(janela,font="Arial 20 bold", width=1280, height=720)

frame = tkinter.Frame(janela, height=30)
frame.pack(fill="x")

fonteDoTexto=tkinter.Label(frame, text=" Fonte ")
fonteDoTexto.pack(side="left")

rolarTipoDoFonte=tkinter.Spinbox(frame, values=("Arial", "Verdana"))
rolarTipoDoFonte.pack(side="left")

tamanhoDoFonte=tkinter.Label(frame,text="  Tamanho do Fonte:  ")
tamanhoDoFonte.pack(side="left")

rolarTamanho=tkinter.Spinbox(frame,from_=0, to=60)
rolarTamanho.pack(side="left")

botao_atualiza=tkinter.Button(frame,text="Atualiza", command=AtualizaFonte)
botao_atualiza.pack(side="left")

areaDeTexto=tkinter.Text(janela, font="Arial 20 bold",width=1280,height=720)


areaDeTexto.pack()


menuPrincipal = tkinter.Menu(janela)

arquivoDeMenu=tkinter.Menu(menuPrincipal, tearoff=0)
arquivoDeMenu.add_command(label="Novo", command=NovoArquivo)
arquivoDeMenu.add_command(label="Salvar",command=SalvaArquivo)
arquivoDeMenu.add_command(label="Abrir",command=Abrir)
arquivoDeMenu.add_command(label="Sair", command=janela.quit)

menuPrincipal.add_cascade(label = "Arquivos", menu=arquivoDeMenu)

janela.config(menu=menuPrincipal)

janela.mainloop()

