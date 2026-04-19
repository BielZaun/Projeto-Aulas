import tkinter as tk
import random
from tkinter import messagebox


# Função quando clicar em "Sim"
def clicou_sim():
    label.config(text="Você é meu amor mesmo!! 💖")
    messagebox.showinfo("💖", "Meu bem maior 💖")

# Função para mover o botão "Não"
def mover_botao(event):
    largura = janela.winfo_width()
    altura = janela.winfo_height()

    # Tamanho do botão
    botao_largura = botao_nao.winfo_width()
    botao_altura = botao_nao.winfo_height()

    # Gera posição aleatória dentro da janela
    x = random.randint(0, largura - botao_largura)
    y = random.randint(0, altura - botao_altura)

    botao_nao.place(x=x, y=y)

# Criando a janela
janela = tk.Tk()
janela.title("Pergunta importante 💘")
janela.geometry("400x300")
janela.configure(bg="#ffc0cb")  # rosa claro

# Texto principal
label = tk.Label(
    janela,
    text="Quer namorar comigo?",
    bg="#ffc0cb",
    font=("Arial", 18)
)
label.pack(pady=40)

# Botão SIM
botao_sim = tk.Button(janela, text="Sim 💖", command=clicou_sim)
botao_sim.pack(pady=10)

# Botão NÃO
botao_nao = tk.Button(janela, text="Não 😢")
botao_nao.place(x=150, y=180)

# Evento de passar o mouse
botao_nao.bind("<Enter>", mover_botao)

# Rodar aplicação
janela.mainloop()