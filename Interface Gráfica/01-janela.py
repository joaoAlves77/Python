from tkinter import Tk, Label, Button

janela = Tk()
janela.geometry('600x600')
janela.title('code com joão')

def clicar():
    meulabel.config(text='Cliquei no botão!')

meubotao = Button(janela, text='Clicar', command=clicar)
meubotao.pack()
meulabel = Label(janela, text='Olá mundo!')
meulabel.pack()

janela.mainloop()