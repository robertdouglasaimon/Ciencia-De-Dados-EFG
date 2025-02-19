# pip install pillow
from tkinter .ttk import *
from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk
from tkinter import messagebox

# Importando as funções da view
from view import *

# Cores ----------------------
co0 = "#2e2d2b"  # Preta
co1 = "#ffffff"  # Branca
co2 = "#4fa882"  # Verde
co3 = "#38576b"  # Valor
co4 = "#403d3d"  # Letra
co5 = "#0e6636"  # Profit
co6 = "#e9a178"  #
co7 = "#3fbfb9"  # Verde
co8 = "#263238"  # Verde
co9 = "#9e9df5"  # Verde
co10 = "#6e8faf" #
co11 = "#f2f4f2" #

# Criando janela ----------------
janela = Tk()
janela.title("")
janela.geometry("770x330")
janela.configure(background=co1)
janela.resizable(width=False, height=False)

style = Style(janela)
style.theme_use("clam")

# Frame --------------------------
frameCima = Frame(janela, width=770, height=50, bg=co6, relief="flat")
frameCima.grid(row=0, column=0, columnspan=2, sticky=NSEW)

frameEsquerda = Frame(janela, width=150, height=265, bg=co1, relief="raised")
frameEsquerda.grid(row=1, column=0, sticky=NSEW)

frameDireita = Frame(janela, width=600, height=265, bg=co1, relief="raised")
frameDireita.grid(row=1, column=1, sticky=NSEW)

# Logo
# Abrindo imagem título no cabeçalho -----------------
app_img = Image.open("C:/Users/Robert Douglas/Downloads/biblioteca-projeto/icons8-biblioteca-100.png")
app_img = app_img.resize((40, 40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, width=1000, compound=LEFT, padx=5, anchor=NW, bg=co6, fg=co1)
app_logo.place(x=5, y=0)

app_=Label(frameCima, text="Sistema de Gerenciamento de Livro", compound=LEFT, padx=5, anchor=NW, font=('Verdana 15 bold'), bg=co6, fg=co1)
app_.place(x=50, y=7)

# Linha de borda do cabeçalho -----------------------
app_linha = Label(frameCima, width=770, padx=5, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
app_linha.place(x=0, y=47)

# Menu
# Novo usuário ----------------------
img_usuario = Image.open("C:/Users/Robert Douglas/Downloads/biblioteca-projeto/icons8-adicionar-100.png")
img_usuario = img_usuario.resize((18, 18))
img_usuario = ImageTk.PhotoImage(img_usuario)
b_usuario = Button(frameEsquerda, command=lambda: control('novo_usuario') ,image=img_usuario, compound=LEFT, anchor=NW, text="Novo usuário", bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_usuario.grid(row=0, column=0, sticky=NSEW, padx=5, pady=6)

# Novo livro-------------------
img_novo_livro = Image.open("C:/Users/Robert Douglas/Downloads/biblioteca-projeto/icons8-adicionar-livro-50.png")
img_novo_livro = img_novo_livro.resize((18, 18))
img_novo_livro = ImageTk.PhotoImage(img_novo_livro)
b_novo_livro = Button(frameEsquerda, image=img_novo_livro, compound=LEFT, anchor=NW, text="Novo livro", bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_novo_livro.grid(row=1, column=0, sticky=NSEW, padx=5, pady=6)

# Ver livro----------------------
img_ver_livro = Image.open("C:/Users/Robert Douglas/Downloads/biblioteca-projeto/icons8-livros-48.png")
print("Imagem carregada:", img_ver_livro)
img_ver_livro = img_ver_livro.resize((18, 18))
img_ver_livro = ImageTk.PhotoImage(img_ver_livro)
print("Imagem convertida:", img_ver_livro)
b_ver_livro = Button(frameEsquerda, image=img_ver_livro, compound=LEFT, anchor=NW, text="Exibir todos os livros", bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_livro.image = img_ver_livro 
b_ver_livro.grid(row=2, column=0, sticky=NSEW, padx=5, pady=6)


# Ver usuário----------------------
img_ver_usuario = Image.open("C:/Users/Robert Douglas/Downloads/biblioteca-projeto/icons8-usuário-100.png")
img_ver_usuario = img_ver_usuario.resize((18, 18))
img_ver_livro = ImageTk.PhotoImage(img_ver_usuario)
b_ver_usuario = Button(frameEsquerda, image=img_ver_livro, compound=LEFT, anchor=NW, text="Exibir todos os usuários", bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_usuario.grid(row=3, column=0, sticky=NSEW, padx=5, pady=6)


# Realizar um emprestimo----------------------
img_emprestimo = Image.open("C:/Users/Robert Douglas/Downloads/biblioteca-projeto/icons8-empréstimo-contra-títulos-48.png")
img_emprestimo = img_emprestimo.resize((18, 18))
img_emprestimo = ImageTk.PhotoImage(img_emprestimo)
b_emprestimo = Button(frameEsquerda, image=img_emprestimo, compound=LEFT, anchor=NW, text="Realizar um empréstimo", bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_emprestimo.grid(row=4, column=0, sticky=NSEW, padx=5, pady=6)

# Devolução de empréstimos----------------------
img_devolucao = Image.open("C:/Users/Robert Douglas/Downloads/biblioteca-projeto/icons8-devolver-compra-48.png")
img_devolucao = img_devolucao.resize((18, 18))
img_devolucao = ImageTk.PhotoImage(img_devolucao)
b_devolucao = Button(frameEsquerda, image=img_devolucao, compound=LEFT, anchor=NW, text="Devolução de empréstimos", bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_devolucao.image = img_devolucao  # Mantém uma referência à imagem
b_devolucao.grid(row=5, column=0, sticky=NSEW, padx=5, pady=6)

# Livros emprestados no momentos----------------------
img_livros_emprestados = Image.open("C:/Users/Robert Douglas/Downloads/biblioteca-projeto/icons8-livros-32.png")
img_livros_emprestados = img_livros_emprestados.resize((18, 18))
img_livros_emprestados = ImageTk.PhotoImage(img_livros_emprestados)
b_livros_emprestados = Button(frameEsquerda, image=img_livros_emprestados, compound=LEFT, anchor=NW, text="Livros emprestados no momento", bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_livros_emprestados.image = img_livros_emprestados  # Mantém uma referência à imagem
b_livros_emprestados.grid(row=6, column=0, sticky=NSEW, padx=5, pady=6)

# Função para controlar o menu
def control(i):
    
    # Novo usuário
    if i == 'novo_usuario':
        # Limpa elementos da tela
        for widget in frameDireita.winfo_children():
            widget.destroy()
        # Chamando a função 'novo_usuario'
        novo_usuario()
    
    if i == 'ver_usuarios':
        # Limpa elementos da tela
        for widget in frameDireita.winfo_children():
            widget.destroy()
        # Chamando a função 'ver_usuarios'
        ver_usuarios()
        
    if i == 'ver_livros_emprestados':
        # Limpa elementos da tela
        for widget in frameDireita.winfo_children():
            widget.destroy()
        # Chamando a função 'ver_livros_emprestados'
        ver_livros_emprestados()
    
    if i == 'exibir_todos_livros':
        # Limpa elementos da tela
        for widget in frameDireita.winfo_children():
            widget.destroy()
        # Chamando a função 'exibir_todos_livros'
        exibir_todos_livros()
        
    if i == 'devolucao_emprestimos':
        # Limpa elementos da tela
        for widget in frameDireita.winfo_children():
            widget.destroy()
        # Chamando a função 'devolucao_emprestimos'
        devolucao_emprestimos()
        
    
        
# Linha de borda do cabeçalho
app_linha = Label(frameCima, width=770, padx=5, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
app_linha.place(x=0, y=47)

# Novo usuário
def novo_usuario():
    
    global img_salvar
    
    def add():
        first_name = e_p_nome.get()
        last_name = e_sobrenome.get()
        address = e_endereco.get()
        email = e_email.get()
        phone = e_numero.get()
        
        lista = [first_name, last_name, address, email, phone]
        
        for i in lista:
            if i == '':
                messagebox.showerror('Erro', 'Todos os campos devem ser preenchidos')
                return
        # Inserindo os dados no banco de dados
        insert_user(None, first_name, last_name, address, email, phone)
        messagebox.showinfo('Sucesso', 'Usuário cadastrado com sucesso')

        # Limpando os campos de entradas
        e_p_nome.delete(0, END)
        e_sobrenome.delete(0, END)
        e_endereco.delete(0, END)
        e_email.delete(0, END)
        e_numero.delete(0, END)
          
    app_ = Label(frameDireita, text="Inserir um novo usuário", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    app_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)
    
    
    l_p_nome = Label(frameDireita, text="Primeiro nome ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_p_nome.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    e_p_nome = Entry(frameDireita, width=25, justify='left', relief='solid')
    e_p_nome.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    l_sobrenome = Label(frameDireita, text="Sobrenome*", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_sobrenome.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e_sobrenome = Entry(frameDireita, width=25, justify='left', relief='solid')
    e_sobrenome.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)
    
    l_endereco = Label(frameDireita, text="Endereço do usuário* ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_endereco.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
    e_endereco = Entry(frameDireita, width=25, justify='left', relief='solid')
    e_endereco.grid(row=4, column=1, padx=5, pady=5, sticky=NSEW)
    
    l_email = Label(frameDireita, text="Endereço de email* ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_email.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)
    e_email = Entry(frameDireita, width=25, justify='left', relief='solid')
    e_email.grid(row=5, column=1, padx=5, pady=5, sticky=NSEW)

    l_numero = Label(frameDireita, text="Número de telefone* ", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_numero.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)
    e_numero = Entry(frameDireita, width=25, justify='left', relief='solid')
    e_numero.grid(row=6, column=1, padx=5, pady=5, sticky=NSEW)
    
    # Botão para salvar os dados
    img_salvar = Image.open("icons8-salvar-100.png")
    img_salvar = img_salvar.resize((18, 18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDireita, image=img_salvar, compound=LEFT, anchor=NW, text="Salvar", bg=co1, fg=co4, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE, command=add)
    b_salvar.grid(row=7, column=1, sticky=NSEW)
    
def ver_usuarios():

    app_= Label(frameDireita, text="Todos os usuários do banco de dados", width=50, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    l_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
    l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW) 
    
    dados = get_users()
    list_header = ['id', 'nome', 'sobrenome', 'endereco', 'email', 'telefone']
    
    global tree
    
    tree = ttk.Treeview(frameDireita, selectmode="extended",
                        columns=list_header, show="headings")
    
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    
    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)
    
    hd = ["nw", "nw", "nw", "nw", "nw", "nw"]
    h = [20, 80, 80, 120, 120, 76, 100]
    n = 0
    
    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        tree.column(col, width=h[n], anchor=hd[n])
        
        n += 1
        
    for item in dados:
        tree.insert('', 'end', values=item)

# Ver usuário----------------------
img_ver_usuario = Image.open("C:/Users/Robert Douglas/Downloads/biblioteca-projeto/icons8-usuário-100.png")
img_ver_usuario = img_ver_usuario.resize((18, 18))
img_ver_usuario = ImageTk.PhotoImage(img_ver_usuario)
b_ver_usuario = Button(frameEsquerda, command=lambda:control('ver_usuarios'), image=img_ver_usuario, compound=LEFT, anchor=NW, text="Exibir todos os usuários", bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_usuario.grid(row=3, column=0, sticky=NSEW, padx=5, pady=6)  
# ---------------------------------------------------- 

def exibir_todos_livros():
    app_= Label(frameDireita, text="Exibir todos os livros", width=50, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    l_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
    l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)
    
    dados = exibir_livros()
    
    list_header = ['ID', 'Título', 'Autor', 'Editora', 'Ano de publicação', 'ISBN']
    
    global tree
    
    tree = ttk.Treeview(frameDireita, selectmode="extended",
                        columns=list_header, show="headings")
    
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    
    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)
    
    hd = ["nw", "nw", "nw", "nw", "nw", "nw"]
    h = [20, 80, 80, 120, 120, 76, 100]
    n = 0
    
    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        tree.column(col, width=h[n], anchor=hd[n])
        
        n += 1
        
    for item in dados:
        tree.insert('', 'end', values=item)
        tree.update()
    
# Exibe todos os livros----------------------
img_exibir_livro = Image.open("C:/Users/Robert Douglas/Downloads/biblioteca-projeto/icons8-livros-48.png")
img_exibir_livro = img_exibir_livro.resize((18, 18))
img_exibir_livro = ImageTk.PhotoImage(img_exibir_livro)
b_exibir_todos_livros = Button(frameEsquerda, image=img_exibir_livro, command=lambda:control('exibir_todos_livros'), compound=LEFT, anchor=NW, text="Exibir todos os livros", bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_exibir_todos_livros.grid(row=2, column=0, sticky=NSEW, padx=5, pady=6)
# ---------------------------------------------------- 

def devolucao_emprestimos():
    
    app_= Label(frameDireita, text="Devolução de empréstimos", width=50, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    l_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
    l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW) 
    
    dados = exibir_devolucoes()
    list_header = ['livro_titulo', 'usuario_nome', 'id', 'usuario_sobrenome', 'data_emprestimo', 'data_devolucao']
    
    global tree
    
    tree = ttk.Treeview(frameDireita, selectmode="extended",
                        columns=list_header, show="headings")
    
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    
    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)
    
    hd = ["nw", "nw", "nw", "nw", "nw", "nw"]
    h = [20, 80, 80, 120, 120, 76, 100]
    n = 0
    
    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        tree.column(col, width=h[n], anchor=hd[n])
        
        n += 1
        
    for item in dados:
        tree.insert('', 'end', values=item)
        tree.update()
# Devolução de empréstimos----------------------
img_devolucao = Image.open("C:/Users/Robert Douglas/Downloads/biblioteca-projeto/icons8-devolver-compra-48.png")
img_devolucao = img_devolucao.resize((18, 18))
img_devolucao = ImageTk.PhotoImage(img_devolucao)
b_devolucao = Button(frameEsquerda, image=img_devolucao,command=lambda:control('devolucao_emprestimos'), compound=LEFT, anchor=NW, text="Devolução de empréstimos", bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_devolucao.grid(row=5, column=0, sticky=NSEW, padx=5, pady=6)
# ---------------------------------------------------- 

def ver_livros_emprestados():
    print("Função ver_livros_emprestados() chamada")
    # resto do código
    app_= Label(frameDireita, text="Livros emprestados no momento", width=50, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    l_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
    l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW) 
    
    dados = get_books_on_loan()
    print(dados)
    list_header = ['id', 'usuario_nome', 'usuario_sobrenome', 'livro_titulo', 'data_emprestimo', 'data_devolucao']
    
    global tree
    
    tree = ttk.Treeview(frameDireita, selectmode="extended",
                        columns=list_header, show="headings")
    
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    
    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)
    
    hd = ["nw", "nw", "nw", "nw", "nw", "nw"]
    h = [20, 80, 80, 120, 120, 76, 100]
    n = 0
    
    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        tree.column(col, width=h[n], anchor=hd[n])
        
        n += 1
        
    for item in dados:
        tree.insert('', 'end', values=item)
        tree.update()        

# Ver livro emprestado----------------------
img_ver_livro = Image.open("C:/Users/Robert Douglas/Downloads/biblioteca-projeto/icons8-livros-32.png")
img_ver_livro = img_ver_livro.resize((18, 18))
img_ver_livro = ImageTk.PhotoImage(img_ver_livro)
b_livros_emprestados = Button(frameEsquerda, image=img_ver_livro, command=lambda:control('ver_livros_emprestados'), compound=LEFT, anchor=NW, text="Livros emprestados no momento", bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_livros_emprestados.grid(row=6, column=0, sticky=NSEW, padx=5, pady=6)
# ---------------------------------------------------- 

janela.mainloop()
