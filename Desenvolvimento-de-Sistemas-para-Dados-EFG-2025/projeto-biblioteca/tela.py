from tkinter import *
from PIL import Image, ImageTk

# pip install pillow
from tkinter import ttk

# Cores
# Definindo as cores com seus códigos hexadecimais
c00 = "#2e2d2b"  # Preta
c01 = "#ffffff"  # Branca
c02 = "#4fa882"  # Verde
c03 = "#38576b"  # Valor
c04 = "#403d3d"  # Letra
c05 = "#0e6636"  # Profit
c06 = "#e9a178"
c07 = "#3fbfb9"  # Verde
c08 = "#263238"  # Verde
c09 = "#9e9df5"  # Verde
c10 = "#6e8faf"
c11 = "#f2f4f2"

# Criando a janela principal
janela = Tk()
janela.title("Biblioteca")
janela.geometry("770x330")
janela.configure(background=c01)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

# Frame ---------------------------------------------------------
frameCima = Frame(janela, width=770, height=50, bg=c06, relief="flat")
frameCima.grid(row=0, column=0, columnspan=2, sticky=NSEW)

frameEsquerda = Frame(janela, width=150, height=265, bg=c04, relief="solid")
frameEsquerda.grid(row=1, column=0, sticky=NSEW)

frameDireita = Frame(janela, width=600, height=265, bg=c01, relief="raised")
frameDireita.grid(row=1, column=1, sticky=NSEW)

# Logo da Aplicação ---------------------------------------------
# Abrindo imagem titulo no cabeçalho
app_img = Image.open(r"D:\ARQUIVOS DOS CURSOS DE PROGRAMACAO CIENCIA DE DADOS E MAIS (NUNCA APAGAR EM HIPOTESE NENHUMA)\Ciencia-De-Dados-EFG\Desenvolvimento-de-Sistemas-para-Dados-EFG-2025\projeto-biblioteca\img\icons8-biblioteca-50.png")
app_img = app_img.resize((40, 40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, width=1000, compound=LEFT, padx=5, anchor=NW, font=('Verdana 15 bold'), bg=c06, fg=c01)
app_logo.place(x=5, y=0)

app_ = Label(frameCima, text="Sistema de Gerenciamento de Livros", compound=LEFT, padx=5, anchor=NW, font=('Verdana 15 bold'), bg=c06, fg=c01)
app_.place(x=50, y=7)

# Linha de borda de cabeçalho
app_linha = Label(frameCima, width=770, padx=5, anchor=NW, font=('Verdana 1'), bg=c03, fg=c01)
app_linha.place(x=0, y=47)

# Menu ----------------------------------------------------------
# Novo usuário---------------------------------------------------
img_usuario = Image.open(r"D:\ARQUIVOS DOS CURSOS DE PROGRAMACAO CIENCIA DE DADOS E MAIS (NUNCA APAGAR EM HIPOTESE NENHUMA)\Ciencia-De-Dados-EFG\Desenvolvimento-de-Sistemas-para-Dados-EFG-2025\projeto-biblioteca\img\icons8-usuário-100.png")
img_usuario = img_usuario.resize((18, 18))
img_usuario = ImageTk.PhotoImage(img_usuario)
b_usuario = Button(frameEsquerda, image=img_usuario, compound=LEFT, anchor=NW, text="Novo Usuário", bg=c04, fg=c01, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_usuario.grid(row=0, column=0, sticky=NSEW, padx=5, pady=6)

# Novo livro---------------------------------------------------
img_novo_livro = Image.open(r"D:\ARQUIVOS DOS CURSOS DE PROGRAMACAO CIENCIA DE DADOS E MAIS (NUNCA APAGAR EM HIPOTESE NENHUMA)\Ciencia-De-Dados-EFG\Desenvolvimento-de-Sistemas-para-Dados-EFG-2025\projeto-biblioteca\img\icons8-livro-100.png")
img_novo_livro = img_novo_livro.resize((18, 18))
img_novo_livro = ImageTk.PhotoImage(img_novo_livro)
b_novo_livro = Button(frameEsquerda, image=img_novo_livro, compound=LEFT, anchor=NW, text="Novo Livro", bg=c04, fg=c01, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_novo_livro.grid(row=1, column=0, sticky=NSEW, padx=5, pady=6)

# Ver livro---------------------------------------------------
img_ver_livro = Image.open(r"D:\ARQUIVOS DOS CURSOS DE PROGRAMACAO CIENCIA DE DADOS E MAIS (NUNCA APAGAR EM HIPOTESE NENHUMA)\Ciencia-De-Dados-EFG\Desenvolvimento-de-Sistemas-para-Dados-EFG-2025\projeto-biblioteca\img\icons8-livro-100.png")
img_ver_livro = img_ver_livro.resize((18, 18))
img_ver_livro = ImageTk.PhotoImage(img_ver_livro)
b_ver_livro = Button(frameEsquerda, image=img_ver_livro, compound=LEFT, anchor=NW, text="Novo Livro", bg=c04, fg=c01, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_livro.grid(row=2, column=0, sticky=NSEW, padx=5, pady=6)

# Realizar um empréstimo-------------------
img_emprestimo = Image.open(r"D:\ARQUIVOS DOS CURSOS DE PROGRAMACAO CIENCIA DE DADOS E MAIS (NUNCA APAGAR EM HIPOTESE NENHUMA)\Ciencia-De-Dados-EFG\Desenvolvimento-de-Sistemas-para-Dados-EFG-2025\projeto-biblioteca\img\icons8-adicionar-100.png")
img_emprestimo = img_emprestimo.resize((18, 18))
img_emprestimo = ImageTk.PhotoImage(img_emprestimo)
b_emprestimo = Button(frameEsquerda, image=img_emprestimo, compound=LEFT, anchor=NW, text="Realizar empréstimos", bg=c04, fg=c01, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_emprestimo.grid(row=4, column=0, sticky=NSEW, padx=5, pady=6)

# Devolução de empréstimos-------------------
img_devolucao = Image.open(r"D:\ARQUIVOS DOS CURSOS DE PROGRAMACAO CIENCIA DE DADOS E MAIS (NUNCA APAGAR EM HIPOTESE NENHUMA)\Ciencia-De-Dados-EFG\Desenvolvimento-de-Sistemas-para-Dados-EFG-2025\projeto-biblioteca\img\icons8-adicionar-100.png")
img_devolucao = img_devolucao.resize((18, 18))
img_devolucao = ImageTk.PhotoImage(img_devolucao)
b_devolucao = Button(frameEsquerda, image=img_devolucao, compound=LEFT, anchor=NW, text="Devolução de empréstimos", bg=c04, fg=c01, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_devolucao.grid(row=5, column=0, sticky=NSEW, padx=5, pady=6)

# Livros emprestados no momento-------------------
img_livros_emprestados = Image.open(r"D:\ARQUIVOS DOS CURSOS DE PROGRAMACAO CIENCIA DE DADOS E MAIS (NUNCA APAGAR EM HIPOTESE NENHUMA)\Ciencia-De-Dados-EFG\Desenvolvimento-de-Sistemas-para-Dados-EFG-2025\projeto-biblioteca\img\icons8-adicionar-100.png")
img_livros_emprestados = img_livros_emprestados.resize((18, 18))
img_livros_emprestados = ImageTk.PhotoImage(img_livros_emprestados)
b_livros_emprestados = Button(frameEsquerda, image=img_livros_emprestados, compound=LEFT, anchor=NW, text="Livros emprestados no momento", bg=c04, fg=c01, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_livros_emprestados.grid(row=6, column=0, sticky=NSEW, padx=5, pady=6)

janela.mainloop()
