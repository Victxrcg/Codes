import customtkinter as ctk
janela = ctk.CTk()
janela.geometry('200x200')
ctk.set_appearance_mode('dark')
texto = ctk.CTkLabel(janela,text=("Ola mundo!"))
texto.pack()
numero = ctk.CTkEntry(janela, placeholder_text=("Digite um numero:"))
numero.pack()
botao = ctk.CTkButton(janela, text="Salvar")
botao.pack()
x = botao.place(x=150, y=150) 
janela.destroy

janela.mainloop()