from tkinter import messagebox
import customtkinter
import random
import string
import pyperclip  # To copy text to the clipboard

def generate_password():
    # Initialize an empty list for the characters to use in the password
    characters = ''
    
    # Append selected character types to the list
    if Maiusculas_var.get():
        characters += string.ascii_uppercase
    if Minusculas_var.get():
        characters += string.ascii_lowercase
    if Numeros_var.get():
        characters += string.digits
    if Simbolos_var.get():
        characters += string.punctuation
    
    # Get the number of characters for the password
    length = int(SChars.get())
    
    # Generate the password if the character set is not empty
    if characters:
        password = ''.join(random.choice(characters) for _ in range(length))
        ESenha.delete(0, customtkinter.END)
        ESenha.insert(0, password)
    else:
        ESenha.delete(0, customtkinter.END)
        ESenha.insert(0, "Selecione pelo menos uma opção")

    messagebox.showinfo('Senha','Senha Gerada Com sucesso!')    

def copy_password():
    pyperclip.copy(ESenha.get())
    messagebox.showinfo('Valores','Valores Copiados Com sucesso!')

def clear_fields():
    ESenha.delete(0, customtkinter.END)
    SChars.set(0)
    Maiusculas_var.set(0)
    Minusculas_var.set(0)
    Numeros_var.set(0)
    Simbolos_var.set(0)
    messagebox.showinfo('Valores','Valores Limpos Com sucesso!')

def exit_app():
    resposta = messagebox.askquestion("Sair", "Deseja sair da aplicação?")
    if resposta == 'yes':  # Se o usuário clicar em "Sim"
        janela.destroy() 

# Create the main window
janela = customtkinter.CTk()
janela.geometry('800x200+100+100')
janela.resizable(0,0)
janela.title('Gerador de Senhas © Dev Joel')

# Create widgets
ESenha = customtkinter.CTkEntry(janela, width=759)
ESenha.place(x=10, y=10)

Maiusculas_var = customtkinter.IntVar()
Maiusculas = customtkinter.CTkCheckBox(janela, text='Letras Maiusculas', variable=Maiusculas_var)
Maiusculas.place(x=10, y=52)

Minusculas_var = customtkinter.IntVar()
Minusculas = customtkinter.CTkCheckBox(janela, text='Letras Minusculas', variable=Minusculas_var)
Minusculas.place(x=175, y=52)

Numeros_var = customtkinter.IntVar()
Numeros = customtkinter.CTkCheckBox(janela, text='Numeros', variable=Numeros_var)
Numeros.place(x=475, y=52)

Simbolos_var = customtkinter.IntVar()
Simbolos = customtkinter.CTkCheckBox(janela, text='Simbolos', variable=Simbolos_var)
Simbolos.place(x=345, y=52)

Caracteres = customtkinter.CTkLabel(janela,  text='Caracteres 0')
Caracteres.place(x=10, y=85)

SChars = customtkinter.CTkSlider(janela, from_=0, to=255, width=759)
SChars.place(x=10, y=115)

# Update label when slider is moved
def update_label(value):
    Caracteres.configure(text=f'Caracteres {int(value)}')

SChars.configure(command=update_label)

Gerar = customtkinter.CTkButton(janela, text='Gerar', command=generate_password)
Gerar.place(x=10, y=155)
Copiar = customtkinter.CTkButton(janela, text='Copiar', command=copy_password)
Copiar.place(x=155, y=155)
Limpar = customtkinter.CTkButton(janela, text='Limpar', command=clear_fields)
Limpar.place(x=300, y=155)
Sair = customtkinter.CTkButton(janela, text='Sair', command=exit_app)
Sair.place(x=445, y=155)

# Run the application
janela.mainloop()
