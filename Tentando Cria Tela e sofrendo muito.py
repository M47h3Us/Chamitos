from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
variaveis = []
#Janela em Geral
janela = Tk()
janela.configure( bg = "white")
janela.title("MINHA JANELA MUITO LOKA")
janela.iconbitmap("images/cara-robo.ico")
janela.geometry('430x920')

treco = Canvas(janela, width = 500, height = 500, bg = "blue")
treco.place(x = 175 , y = 75)

quadrado =  treco.create_rectangle(0, 0 , 250 , 250, fill = "green")
quadrado2 =  treco.create_rectangle(250, 250 ,500, 0, fill = "red")
#treco.tag_raise(quadrado2)
#CRIA UMA LINHA
#treco.create_line(x1, y1, x2, y2, fill = "cor")
#x1 e y1 é aonde começa as coisas
#x2  e y2 é aonde termina
treco.create_line(0 , 350 ,  250 , 1, fill= "red")
janela.mainloop()