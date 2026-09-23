import tkinter as tk

janela = tk.Tk()
janela.title("Minha Primeira Janela")
janela.geometry("1920x1080")

botao = tk.Button(janela, text="Enviar")
botao.pack(pady=5)

grid = tk.grid_bbox (1, 1, 1, 1)

janela.mainloop()
