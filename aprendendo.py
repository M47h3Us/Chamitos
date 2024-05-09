from tkinter import *
import customtkinter
from PIL import ImageTk, Image
#login = Tk()
login = customtkinter.CTk()
login.geometry("430x920")
login.config(bg  = "Spring green")
login.title("Lo0pin")
login.iconbitmap("images/macacofeio.ico")
#=======================================================================================
#DEFS DESGRAÇADOS QUE VÂO ME FODER MUITO NO FUTURO

def botao():
    botaoCagado = Button(canvaBemGay, text = "Crei uma")

def onclick(event):
    print("pararararararar")
#=======================================================================================
#QUADRADÂO BRANCO MUITO PICKA

quadradoDeFundo =  Label(login,width = 45,height = 45,text= "", bg = "white")
quadradoDeFundo.place(x = 56, y = 195)

#=======================================================================================
#Canva geral

canvaBemGay = Canvas(login, width = 320, height = 677, bg = "white")
canvaBemGay.place(x = 56 , y = 195)

#=======================================================================================
#TEXTO

texto1 = Label(canvaBemGay,text = "Login no Lo0pin", font =("K2D"), bg = "white")
texto1.place(x  = 100, y = 10)
texto1.bind("texto", onclick)

texto2 = Label(canvaBemGay,text = "Email ou nome do Usuário", font =("K2D"), bg = "white")
texto2.place(x  = 15, y = 210)


texto4 = Label(canvaBemGay, text = "Senha",width = 25, font =("K2D"), height = 1,  bg = "white")
texto4.place(x  = -75, y = 310)

texto5 = Label(canvaBemGay, text ="Não possui conta?", font =("K2D", 13), bg  = "white" )
texto5.place(x = 55 , y = 625)

#=======================================================================================
#LINHAS

linha1 = canvaBemGay.create_line(20, 45, 299, 45, fill ="black", width = 6)

linha2 = canvaBemGay.create_line(20, 200, 299, 200, fill ="black", width = 6)

linha3 = canvaBemGay.create_line(20, 600, 299, 600, fill ="black", width = 6)

#=======================================================================================
#BOTÂO
#Considerações sobre botoens: Button( PRIMERA COISA COLOCADA AQUI pODE seR USADA PRA INDICAR AINDA FICA ESSE BOTÂO, o resto vai normal eu acho)

botao1=Button(canvaBemGay,width=25,height=0,text="Contiuar com Google",font=("K2D",12))
botao1.place(x = 38, y = 55)

botao2 =Button(canvaBemGay, width= 25, height = 0, text = "Continuar com Facebook", font = ("Arial", 12))
botao2.place(x = 38, y = 145)

botao3=Button(canvaBemGay,width=18,height=3,text="ENTRAR",font=("K2D", 18),bg="Spring green")
botao3.place(x=28,y=425)

botao4 = Button(canvaBemGay, text = "Esqueceu algo?",width = 27, font =("K2D"), height = 0, )
botao4.place(x=35,y=550)

botao5 = Button(canvaBemGay, text = "crie uma",width = 7, font =("K2D", 13), height = 0,bg = "white" )
botao5.place(x= 195, y = 620)

#=======================================================================================
#ENTRY

entrada = Entry(canvaBemGay,width= 11,font = ("Arial", 35),bg = "azure2")
entrada.place(x = 15, y = 245 )

entrada = Entry(canvaBemGay,width= 11,font = ("Arial", 35),bg = "azure2")
entrada.place(x = 15, y = 345 )

#=======================================================================================
#IMAGEM DO QUADRADO DE CIMA...WARIO CAGADO KKKKKKKKKKKKKKKKKKKKKK

imagem = ImageTk.PhotoImage(Image.open("images/wariocadago.png"))

#=======================================================================================
#QUADRADO DE CIMA

quadradoPequeno =  Label(login, width = 200,height = 160,text= "",image = imagem ,bg = "blue")
quadradoPequeno.place(x = 110, y = 25)

#=======================================================================================

login.mainloop()

#grid vai bota na tela o bagulho
#width é a largura do botão
#height é a altura
#relief é  o estilo do botão
#fg é a cor da letra
#bg é a cor do fundo da letra
#row é a a altura do botão na tela
#column  é a largura do botão na tela
#padx faz ele mexer pra ca ---->
#pady faz ele mexer pra baxo
#Label dexa a variavel possivel de alterar, dentro do Label ta o exemplo

#ESTILOS DE BOTÂO

#groove



#flat

#raised

#sunken

#ridge