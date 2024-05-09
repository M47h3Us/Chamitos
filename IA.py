import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb
def abrir_segunda_janela():
    segunda_janela = tk.Toplevel()
    segunda_janela.title("Segunda Janela")
    segunda_janela.config(bg= "#20EE70")

    #tamanho janela

    largura_janela = 430
    altura_janela = 920

    #obter as dimensões da tela do monitor
    largura_tela = segunda_janela.winfo_screenwidth()
    altura_tela = segunda_janela.winfo_screenwidth()

    #calcular as coordenadas para centralizar a janela 2
    x = (largura_tela - largura_janela) // 2
    y = (altura_tela - altura_janela) // 2

    #definir a geometria da janela 2
    segunda_janela.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")

#criar janela principal
janela_principal = tk.Tk()
janela_principal.title("Janela principal")
janela_principal.geometry("430x920")

janela_principal.bind("<Button-1>", lambda event:abrir_segunda_janela())

#<Button-1> capta o botão direito do mause e executa alguma coisa
#lambda event: oque vier a seguir disso é o que vai acontecer quando clicka com o botão direito
janela_principal.mainloop()