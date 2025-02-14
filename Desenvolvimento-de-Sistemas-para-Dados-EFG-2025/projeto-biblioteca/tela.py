from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from view import *
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
img_novo_livro = Image.open(r"D:\ARQUIVOS DOS CURSOS DE PROGRAMACAO CIENCIA DE DADOS E MAIS (NUNCA APAGAR EM HIPOTESE NENHUMA)\Ciencia-De-Dados-EFG\Desenvolvimento-de-Sistemas-para-Dados-EFG-2025\projeto-biblioteca\img\icons8-usuário-100.png")
img_novo_livro = img_novo_livro.resize((18, 18))
img_novo_livro = ImageTk.PhotoImage(img_novo_livro)
b_novo_livro = Button(frameEsquerda, image=img_novo_livro, compound=LEFT, anchor=NW, text="Novo Livro", bg=c04, fg=c01, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_novo_livro.grid(row=1, column=0, sticky=NSEW, padx=5, pady=6)

# Ver todos os usuários---------------------------------------------------
img_usuarios = Image.open(r"D:\ARQUIVOS DOS CURSOS DE PROGRAMACAO CIENCIA DE DADOS E MAIS (NUNCA APAGAR EM HIPOTESE NENHUMA)\Ciencia-De-Dados-EFG\Desenvolvimento-de-Sistemas-para-Dados-EFG-2025\projeto-biblioteca\img\icons8-usuário-100.png")
img_usuarios = img_usuarios.resize((18, 18))
img_usuarios = ImageTk.PhotoImage(img_usuarios)
b_usuarios = Button(frameEsquerda, image=img_usuarios, compound=LEFT, anchor=NW, text="Ver todos os usuários", bg=c04, fg=c01, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_usuarios.grid(row=2, column=0, sticky=NSEW, padx=5, pady=6)

# Ver todos os livros---------------------------------------------------
img_ver_livro = Image.open(r"D:\ARQUIVOS DOS CURSOS DE PROGRAMACAO CIENCIA DE DADOS E MAIS (NUNCA APAGAR EM HIPOTESE NENHUMA)\Ciencia-De-Dados-EFG\Desenvolvimento-de-Sistemas-para-Dados-EFG-2025\projeto-biblioteca\img\icons8-livro-100.png")
img_ver_livro = img_ver_livro.resize((18, 18))
img_ver_livro = ImageTk.PhotoImage(img_ver_livro)
b_ver_livro = Button(frameEsquerda, image=img_ver_livro, compound=LEFT, anchor=NW, text="Ver todos os livros", bg=c04, fg=c01, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_livro.grid(row=3, column=0, sticky=NSEW, padx=5, pady=6)

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

# Função para controlar o menu -------------------
def controle_menu(i):
    
    # Novo usuário------------
    if i == 'novo_usuario':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        # Chama a função "novo_usuario"
        novo_usuario()

# Linha de borda de cabeçalho
app_linha = Label(frameCima, width=770, padx=5, anchor=NW, font=('Verdana 1'), bg=c03, fg=c01)
app_linha.place(x=0, y=47)

# Novo usuario ----------------------------------------------------------
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
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return
            # Inserindo os dados no banco de dados
        inserir_usuario(first_name, last_name, address, email, phone)
        
        messagebox.showinfo('Sucesso', 'Usuário cadastrado com sucesso')
        
        # Limpando os campos de entradas
        e_p_nome.delete(0, END)
        e_sobrenome.delete(0, END)
        e_endereco.delete(0, END)
        e_email.delete(0, END)
        e_numero.delete(0, END)
        
    # Ver todos os usuários
    def ver_usuarios():
        
        app_=Label(frameDireita, text='Todos os usuários do banco de dados', width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), anchor=NW, relief=FLAT, bg=c01, fg=c04)
        app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
        l_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=c03, fg=c01)
        l_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)
        
        ver_usuarios()

        
    app_=Label(frameDireita, text="Inserir um novo usuário", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12'), bg=c01, fg=c04)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    app_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=c03, fg=c01)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)
    
    dados = novo_usuario()
    
    list_header = ['ID', 'Primeiro Nome', 'Sobrenome', 'Endereço', 'Email', 'Telefone']
    
    global tree
    
    tree = ttk.Treeview(frameDireita, selectmode='extended',
                        columns=list_header, show='headings')
    
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)
    
    hd = ['nw', 'nw', 'nw', 'nw', 'nw', 'nw']
    h = [20, 80, 80, 120, 120, 76, 100]
    n = 0
    
    for col in list_header:
        tree.heading(col, text=col.title(), anchor='nw')
        # Ajustar a coluna de acordo com o tamanho do cabeçalho
        tree.column(col, width=h[n], anchor=hd[n])
        
        n += 1
        
    for item in dados:
        tree.insert('', 'end', values=item)
        
    # Ver usuário --------------------------
    img_ver_usuario = Image.open(r"D:\ARQUIVOS DOS CURSOS DE PROGRAMACAO CIENCIA DE DADOS E MAIS (NUNCA APAGAR EM HIPOTESE NENHUMA)\Ciencia-De-Dados-EFG\Desenvolvimento-de-Sistemas-para-Dados-EFG-2025\projeto-biblioteca\img\icons8-usuário-100.png")
    img_ver_usuario = img_ver_usuario.resize((18, 18))
    img_ver_usuario = ImageTk.PhotoImage(img_ver_usuario)
    b_ver_usuario = Button(frameEsquerda, command=lambda: controle_menu('ver_usuarios'), image=img_ver_usuario, compound=LEFT, anchor=NW, text="Ver todos os usuários", bg=c04, fg=c01, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_ver_usuario.grid(row=3, column=0, sticky=NSEW, padx=5, pady=6)

# Novo Funcionário ----------------------------------------------------------
l_p_nome = Label(frameDireita, text="Primeiro nome ", anchor=NW, font=('Ivy 10'), bg=c01, fg=c04)
l_p_nome.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
e_p_nome = Entry(frameDireita, width=25, justify='left', relief='solid')
e_p_nome.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

l_sobrenome = Label(frameDireita, text="Sobrenome*", anchor=NW, font=('Ivy 10'), bg=c01, fg=c04)
l_sobrenome.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
e_sobrenome = Entry(frameDireita, width=25, justify='left', relief='solid')
e_sobrenome.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

l_email = Label(frameDireita, text="Email*", anchor=NW, font=('Ivy 10'), bg=c01, fg=c04)
l_email.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
e_email = Entry(frameDireita, width=25, justify='left', relief='solid')
e_email.grid(row=4, column=1, padx=5, pady=5, sticky=NSEW)

l_numero = Label(frameDireita, text="Telefone*", anchor=NW, font=('Ivy 10'), bg=c01, fg=c04)
l_numero.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)
e_numero = Entry(frameDireita, width=25, justify='left', relief='solid')
e_numero.grid(row=5, column=1, padx=5, pady=5, sticky=NSEW)

l_endereco = Label(frameDireita, text="Endereço*", anchor=NW, font=('Ivy 10'), bg=c01, fg=c04)
l_endereco.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)
e_endereco = Entry(frameDireita, width=25, justify='left', relief='solid')
e_endereco.grid(row=6, column=1, padx=5, pady=5, sticky=NSEW)

# Botão salvar ----------------------------------------------------------
img_salvar = Image.open(r"D:\ARQUIVOS DOS CURSOS DE PROGRAMACAO CIENCIA DE DADOS E MAIS (NUNCA APAGAR EM HIPOTESE NENHUMA)\Ciencia-De-Dados-EFG\Desenvolvimento-de-Sistemas-para-Dados-EFG-2025\projeto-biblioteca\img\icons8-salvar-100.png")
img_salvar = img_salvar.resize((18, 18))
img_salvar = ImageTk.PhotoImage(img_salvar)
b_salvar = Button(frameDireita, image=img_salvar, compound=LEFT, width=100, anchor=NW, text="Salvar", bg=c01, fg=c04, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_salvar.grid(row=7, column=1, sticky=NSEW, pady=5)

# Novo usuário ----------------------------------------------------------
img_novo_usuario = Image.open(r"D:\ARQUIVOS DOS CURSOS DE PROGRAMACAO CIENCIA DE DADOS E MAIS (NUNCA APAGAR EM HIPOTESE NENHUMA)\Ciencia-De-Dados-EFG\Desenvolvimento-de-Sistemas-para-Dados-EFG-2025\projeto-biblioteca\img\icons8-usuário-100.png")
img_novo_usuario = img_novo_usuario.resize((18, 18))
img_novo_usuario = ImageTk.PhotoImage(img_novo_usuario)
b_novo_usuario = Button(frameEsquerda, command=lambda: controle_menu('novo_usuario'), image=img_novo_usuario, compound=LEFT, anchor=NW, text="Novo Usuário", bg=c04, fg=c01, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_novo_usuario.grid(row=0, column=0, sticky=NSEW, padx=5, pady=6)


janela.mainloop()
