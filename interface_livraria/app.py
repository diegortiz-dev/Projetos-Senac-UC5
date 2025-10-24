import customtkinter
from PIL import Image
import datetime
from tkinter import filedialog, messagebox
from main import Livro, Leitor, Emprestimo, ListaLivros, ListaLeitores

lista_livros = ListaLivros("TELivraria")
lista_leitores = ListaLeitores("TELivraria")
lista_emprestimos = []
capa_livro_path = None
livro_selecionado = None
leitor_selecionado = None

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

janela = customtkinter.CTk()
janela.title("Interface Livraria")
janela.geometry("1920x1080")
janela.configure(fg_color="#a2a2a2")

frame_header = customtkinter.CTkFrame(
    master=janela,
    width=1920,
    height=160,
    corner_radius=0,
    fg_color="#001126"
)
frame_header.pack(pady=0, padx=0, fill="x", side="top")

imagem_pil = Image.open("assets/imagemlivraria.png")
imagem_redimensionada = imagem_pil.resize((120, 120))
icone_app = customtkinter.CTkImage(
    dark_image=imagem_redimensionada,
    light_image=imagem_redimensionada,
    size=(120, 120)
)
label_icone = customtkinter.CTkLabel(
    master=frame_header,
    image=icone_app,
    text=""
)
label_icone.grid(row=0, column=0, pady=20, padx=20, sticky="w")

nome_app = customtkinter.CTkLabel(
    master=frame_header,
    text="TELivraria",
    text_color="white",
    font=("Libre Baskerville", 32, "bold"),
    width=300
)
nome_app.grid(row=0, column=1, pady=20, padx=5, sticky="w")

imagem_lupa = Image.open("assets/search.png")
lupa_redimensionada = imagem_lupa.resize((30, 30))
icone_lupa = customtkinter.CTkImage(
    dark_image=lupa_redimensionada,
    light_image=lupa_redimensionada,
    size=(30, 30)
)

frame_livros = customtkinter.CTkFrame(
    master=janela,
    width=1200,
    height=960,
    corner_radius=0,
    fg_color="#a2a2a2"
)
frame_leitores = customtkinter.CTkFrame(
    master=janela,
    width=1200,
    height=960,
    corner_radius=0,
    fg_color="#a2a2a2"
)
frame_emprestimos = customtkinter.CTkFrame(
    master=janela,
    width=1200,
    height=960,
    corner_radius=0,
    fg_color="#a2a2a2"
)

def mostrar_frame_livros():
    frame_leitores.pack_forget()
    frame_emprestimos.pack_forget()
    frame_livros.pack(fill="both", expand=True)

def mostrar_frame_leitores():
    frame_livros.pack_forget()
    frame_emprestimos.pack_forget()
    frame_leitores.pack(fill="both", expand=True)

def mostrar_frame_emprestimos():
    frame_livros.pack_forget()
    frame_leitores.pack_forget()
    frame_emprestimos.pack(fill="both", expand=True)

botao_livros = customtkinter.CTkButton(
    master=frame_header,
    text="Livros",
    text_color="white",
    width=250,
    height=100,
    font=("Libre Baskerville", 30, "bold"),
    corner_radius=30,
    fg_color="#003e7e",
    bg_color="#001126",
    command=mostrar_frame_livros
)
botao_livros.grid(row=0, column=2, pady=20, padx=20, sticky="w")

botao_leitores = customtkinter.CTkButton(
    master=frame_header,
    text="Leitores",
    text_color="white",
    width=250,
    height=100,
    font=("Libre Baskerville", 30, "bold"),
    corner_radius=30,
    fg_color="#003e7e",
    bg_color="#001126",
    command=mostrar_frame_leitores
)
botao_leitores.grid(row=0, column=3, pady=20, padx=20, sticky="w")

botao_emprestimos = customtkinter.CTkButton(
    master=frame_header,
    text="Empréstimos",
    text_color="white",
    width=250,
    height=100,
    font=("Libre Baskerville", 30, "bold"),
    corner_radius=30,
    fg_color="#003e7e",
    bg_color="#001126",
    command=mostrar_frame_emprestimos
)
botao_emprestimos.grid(row=0, column=4, pady=20, padx=20, sticky="w")

frame_pesquisas = customtkinter.CTkFrame(
    master=frame_livros,
    width=1200,
    height=960,
    corner_radius=0,
    fg_color="#a2a2a2"
)
frame_pesquisas.pack(pady=0, padx=0, fill="both", side="left", expand=True)

frame_cadastro = customtkinter.CTkFrame(
    master=frame_livros,
    width=720,
    height=840,
    corner_radius=50,
    border_color="#001126",
    border_width=2,
    fg_color="#cacaca"
)
frame_cadastro.pack(pady=20, padx=10, side="right", expand=False, fill="both")

entrada_pesquisas = customtkinter.CTkEntry(
    master=frame_pesquisas,
    width=850,
    height=90,
    placeholder_text="Pesquisar...",
    font=("Libre Baskerville", 30),
    corner_radius=30,
    fg_color="#d9d9d9",
    border_color="#001126",
    border_width=2,
    text_color="#001126"
)
entrada_pesquisas.grid(row=0, column=0, pady=10, padx=10, sticky="w")

botao_pesquisar = customtkinter.CTkButton(
    master=frame_pesquisas,
    text="",
    image=icone_lupa,
    width=90,
    height=90,
    corner_radius=200,
    fg_color="#d9d9d9",
    border_width=2,
    border_color="#001126",
    hover_color="#c0c0c0"
)
botao_pesquisar.grid(row=0, column=1, pady=10, padx=10, sticky="w")

frame_resultados_livros = customtkinter.CTkScrollableFrame(
    master=frame_pesquisas,
    width=950,
    height=800,
    fg_color="#a2a2a2"
)
frame_resultados_livros.grid(row=1, column=0, pady=10, padx=10, sticky="nsew", columnspan=2)

imagem_livro = customtkinter.CTkButton(
    master=frame_cadastro,
    width=200,
    height=250,
    fg_color="#d9d9d9",
    border_color="#001126",
    border_width=2,
    text="📷",
    font=("Arial", 60),
    corner_radius=20,
    hover_color="#c0c0c0"
)
imagem_livro.grid(row=0, column=0, pady=20, padx=20, sticky="w", columnspan=2)

nome_livro = customtkinter.CTkEntry(
    master=frame_cadastro,
    width=600,
    height=70,
    placeholder_text="Título do Livro",
    font=("Libre Baskerville", 24),
    corner_radius=20,
    fg_color="#d9d9d9",
    border_color="#001126",
    border_width=2,
    text_color="#001126",
    placeholder_text_color="#808080"
)
nome_livro.grid(row=1, column=0, pady=20, padx=20, sticky="w", columnspan=2)

autor_livro = customtkinter.CTkEntry(
    master=frame_cadastro,
    width=600,
    height=70,
    placeholder_text="Nome do Autor",
    font=("Libre Baskerville", 24),
    corner_radius=20,
    fg_color="#d9d9d9",
    border_color="#001126",
    border_width=2,
    text_color="#001126",
    placeholder_text_color="#808080"
)
autor_livro.grid(row=2, column=0, pady=20, padx=20, sticky="w", columnspan=2)

quantidade_livro = customtkinter.CTkEntry(
    master=frame_cadastro,
    width=600,
    height=70,
    placeholder_text="Qtd. Exemplares",
    font=("Libre Baskerville", 24),
    corner_radius=20,
    fg_color="#d9d9d9",
    border_color="#001126",
    border_width=2,
    text_color="#001126",
    placeholder_text_color="#808080"
)
quantidade_livro.grid(row=3, column=0, pady=20, padx=20, sticky="w", columnspan=2)

isbn_livro = customtkinter.CTkEntry(
    master=frame_cadastro,
    width=280,
    height=70,
    placeholder_text="ISBN",
    font=("Libre Baskerville", 24),
    corner_radius=20,
    fg_color="#d9d9d9",
    border_color="#001126",
    border_width=2,
    text_color="#001126",
    placeholder_text_color="#808080"
)
isbn_livro.grid(row=4, column=0, pady=20, padx=20, sticky="w")

edicao_livro = customtkinter.CTkEntry(
    master=frame_cadastro,
    width=280,
    height=70,
    placeholder_text="Edição",
    font=("Libre Baskerville", 24),
    corner_radius=20,
    fg_color="#d9d9d9",
    border_color="#001126",
    border_width=2,
    text_color="#001126",
    placeholder_text_color="#808080"
)
edicao_livro.grid(row=4, column=1, pady=20, padx=20, sticky="w")

botao_cadastrar = customtkinter.CTkButton(
    master=frame_cadastro,
    text="Cadastrar Livro",
    width=600,
    height=70,
    font=("Libre Baskerville", 24, "bold"),
    corner_radius=20,
    fg_color="#001126",
    border_width=2,
    border_color="#001126",
    hover_color="#003e7e",
    text_color="white"
)
botao_cadastrar.grid(row=5, column=0, pady=20, padx=20, sticky="w", columnspan=2)

frame_pesquisa_leitores = customtkinter.CTkFrame(
    master=frame_leitores,
    width=1200,
    height=960,
    corner_radius=0,
    fg_color="#a2a2a2"
)
frame_pesquisa_leitores.pack(pady=0, padx=0, fill="both", side="left", expand=True)

frame_cadastro_leitores = customtkinter.CTkFrame(
    master=frame_leitores,
    width=720,
    height=840,
    corner_radius=50,
    border_color="#001126",
    border_width=2,
    fg_color="#cacaca"
)
frame_cadastro_leitores.pack(pady=20, padx=10, side="right", expand=False, fill="both")

entrada_pesquisa_leitores = customtkinter.CTkEntry(
    master=frame_pesquisa_leitores,
    width=850,
    height=90,
    placeholder_text="Pesquisar...",
    font=("Libre Baskerville", 30),
    corner_radius=30,
    fg_color="#d9d9d9",
    border_color="#001126",
    border_width=2,
    text_color="#001126"
)
entrada_pesquisa_leitores.grid(row=0, column=0, pady=10, padx=10, sticky="w")

botao_pesquisar_leitores = customtkinter.CTkButton(
    master=frame_pesquisa_leitores,
    text="",
    image=icone_lupa,
    width=90,
    height=90,
    corner_radius=200,
    fg_color="#d9d9d9",
    border_width=2,
    border_color="#001126",
    hover_color="#c0c0c0"
)
botao_pesquisar_leitores.grid(row=0, column=1, pady=10, padx=10, sticky="w")

frame_resultados_leitores = customtkinter.CTkScrollableFrame(
    master=frame_pesquisa_leitores,
    width=950,
    height=800,
    fg_color="#a2a2a2"
)
frame_resultados_leitores.grid(row=1, column=0, pady=10, padx=10, sticky="nsew", columnspan=2)

nome_leitor = customtkinter.CTkEntry(
    master=frame_cadastro_leitores,
    width=600,
    height=70,
    placeholder_text="Nome do Leitor",
    font=("Libre Baskerville", 24),
    corner_radius=20,
    fg_color="#d9d9d9",
    border_color="#001126",
    border_width=2,
    text_color="#001126",
    placeholder_text_color="#808080"
)
nome_leitor.grid(row=0, column=0, pady=20, padx=20, sticky="w", columnspan=2)

telefone_leitor = customtkinter.CTkEntry(
    master=frame_cadastro_leitores,
    width=600,
    height=70,
    placeholder_text="Telefone",
    font=("Libre Baskerville", 24),
    corner_radius=20,
    fg_color="#d9d9d9",
    border_color="#001126",
    border_width=2,
    text_color="#001126",
    placeholder_text_color="#808080"
)
telefone_leitor.grid(row=1, column=0, pady=20, padx=20, sticky="w", columnspan=2)

id_leitor = customtkinter.CTkEntry(
    master=frame_cadastro_leitores,
    width=600,
    height=70,
    placeholder_text="ID Leitor",
    font=("Libre Baskerville", 24),
    corner_radius=20,
    fg_color="#d9d9d9",
    border_color="#001126",
    border_width=2,
    text_color="#001126",
    placeholder_text_color="#808080"
)
id_leitor.grid(row=2, column=0, pady=20, padx=20, sticky="w", columnspan=2)

botao_cadastrar_leitor = customtkinter.CTkButton(
    master=frame_cadastro_leitores,
    text="Cadastrar Leitor",
    width=600,
    height=70,
    font=("Libre Baskerville", 24, "bold"),
    corner_radius=20,
    fg_color="#001126",
    border_width=2,
    border_color="#001126",
    hover_color="#003e7e",
    text_color="white"
)
botao_cadastrar_leitor.grid(row=3, column=0, pady=20, padx=20, sticky="w", columnspan=2)

frame_pesquisa_emprestimos = customtkinter.CTkFrame(
    master=frame_emprestimos,
    width=1200,
    height=960,
    corner_radius=0,
    fg_color="#a2a2a2"
)
frame_pesquisa_emprestimos.pack(pady=0, padx=0, fill="both", side="left", expand=True)

frame_registro_emprestimos = customtkinter.CTkFrame(
    master=frame_emprestimos,
    width=720,
    height=840,
    corner_radius=50,
    border_color="#001126",
    border_width=2,
    fg_color="#cacaca"
)
frame_registro_emprestimos.pack(pady=20, padx=10, side="right", expand=False, fill="both")

entrada_pesquisa_emprestimos = customtkinter.CTkEntry(
    master=frame_pesquisa_emprestimos,
    width=850,
    height=90,
    placeholder_text="Pesquisar...",
    font=("Libre Baskerville", 30),
    corner_radius=30,
    fg_color="#d9d9d9",
    border_color="#001126",
    border_width=2,
    text_color="#001126"
)
entrada_pesquisa_emprestimos.grid(row=0, column=0, pady=10, padx=10, sticky="w")

botao_pesquisar_emprestimos = customtkinter.CTkButton(
    master=frame_pesquisa_emprestimos,
    text="",
    image=icone_lupa,
    width=90,
    height=90,
    corner_radius=200,
    fg_color="#d9d9d9",
    border_width=2,
    border_color="#001126",
    hover_color="#c0c0c0"
)
botao_pesquisar_emprestimos.grid(row=0, column=1, pady=10, padx=10, sticky="w")

frame_resultados_emprestimos = customtkinter.CTkScrollableFrame(
    master=frame_pesquisa_emprestimos,
    width=950,
    height=800,
    fg_color="#a2a2a2"
)
frame_resultados_emprestimos.grid(row=1, column=0, pady=10, padx=10, sticky="nsew", columnspan=2)

nome_leitor_emprestimo = customtkinter.CTkEntry(
    master=frame_registro_emprestimos,
    width=600,
    height=70,
    placeholder_text="Nome do Leitor",
    font=("Libre Baskerville", 24),
    corner_radius=20,
    fg_color="#d9d9d9",
    border_color="#001126",
    border_width=2,
    text_color="#001126",
    placeholder_text_color="#808080"
)
nome_leitor_emprestimo.grid(row=0, column=0, pady=20, padx=20, sticky="w", columnspan=2)

nome_livro_emprestimo = customtkinter.CTkEntry(
    master=frame_registro_emprestimos,
    width=600,
    height=70,
    placeholder_text="Nome do Livro",
    font=("Libre Baskerville", 24),
    corner_radius=20,
    fg_color="#d9d9d9",
    border_color="#001126",
    border_width=2,
    text_color="#001126",
    placeholder_text_color="#808080"
)
nome_livro_emprestimo.grid(row=1, column=0, pady=20, padx=20, sticky="w", columnspan=2)

data_emprestimo_label = customtkinter.CTkEntry(
    master=frame_registro_emprestimos,
    width=600,
    height=70,
    font=("Libre Baskerville", 24),
    corner_radius=20,
    fg_color="#d9d9d9",
    border_color="#001126",
    border_width=2,
    text_color="#808080"
)
data_emprestimo_label.insert(0, str(datetime.date.today().strftime("%d/%m/%y")))
data_emprestimo_label.configure(state="disabled")
data_emprestimo_label.grid(row=2, column=0, pady=20, padx=20, sticky="w", columnspan=2)

botao_registrar_emprestimo = customtkinter.CTkButton(
    master=frame_registro_emprestimos,
    text="Registrar Empréstimo",
    width=600,
    height=70,
    font=("Libre Baskerville", 24, "bold"),
    corner_radius=20,
    fg_color="#001126",
    border_width=2,
    border_color="#001126",
    hover_color="#003e7e",
    text_color="white"
)
botao_registrar_emprestimo.grid(row=3, column=0, pady=20, padx=20, sticky="w", columnspan=2)
def selecionar_capa():
    global capa_livro_path
    arquivo = filedialog.askopenfilename(filetypes=[("Imagens", "*.png *.jpg *.jpeg")])
    if arquivo:
        capa_livro_path = arquivo
        img = Image.open(arquivo)
        img = img.resize((200, 250))
        img_tk = customtkinter.CTkImage(dark_image=img, light_image=img, size=(200, 250))
        imagem_livro.configure(image=img_tk, text="")

def criar_card_livro(livro, master):
    frame_card = customtkinter.CTkFrame(
        master=master,
        width=900,
        height=160,
        fg_color="#cacaca",
        corner_radius=10,
        border_color="#001126",
        border_width=3
    )
    frame_card.pack(pady=5, padx=10, fill="x")
    frame_card.pack_propagate(False)
    
    if hasattr(livro, 'capa_path') and livro.capa_path:
        try:
            img = Image.open(livro.capa_path)
            img = img.resize((100, 140))
            img_tk = customtkinter.CTkImage(dark_image=img, light_image=img, size=(100, 140))
            img_label = customtkinter.CTkLabel(master=frame_card, image=img_tk, text="")
            img_label.place(x=10, y=10)
        except:
            img_placeholder = customtkinter.CTkLabel(
                master=frame_card,
                width=100,
                height=140,
                text="",
                fg_color="#d9d9d9",
                corner_radius=5
            )
            img_placeholder.place(x=10, y=10)
    else:
        img_placeholder = customtkinter.CTkLabel(
            master=frame_card,
            width=100,
            height=140,
            text="",
            fg_color="#d9d9d9",
            corner_radius=5
        )
        img_placeholder.place(x=10, y=10)
    
    customtkinter.CTkLabel(
        master=frame_card,
        text=livro.titulo,
        font=("Libre Baskerville", 18, "bold"),
        text_color="#001126"
    ).place(x=130, y=15)
    
    customtkinter.CTkLabel(
        master=frame_card,
        text=livro.autor,
        font=("Libre Baskerville", 16),
        text_color="#001126"
    ).place(x=130, y=50)
    
    customtkinter.CTkLabel(
        master=frame_card,
        text=f"ISBN:{livro.isbn}",
        font=("Libre Baskerville", 14),
        text_color="#001126"
    ).place(x=130, y=85)
    
    cor_disponivel = "#00b300" if livro.qtd_exemplar > 0 else "#ff0000"
    customtkinter.CTkLabel(
        master=frame_card,
        text=f"Disponíveis:{livro.qtd_exemplar}",
        font=("Libre Baskerville", 16, "bold"),
        text_color=cor_disponivel
    ).place(x=130, y=120)
    
    btn_editar = customtkinter.CTkButton(
        master=frame_card,
        width=50,
        height=50,
        text="✎",
        font=("Arial", 24),
        fg_color="#001126",
        corner_radius=25,
        hover_color="#003e7e",
        command=lambda: editar_livro(livro)
    )
    btn_editar.place(x=820, y=55)

def criar_card_leitor(leitor, master):
    frame_card = customtkinter.CTkFrame(
        master=master,
        width=900,
        height=120,
        fg_color="#cacaca",
        corner_radius=10,
        border_color="#001126",
        border_width=3
    )
    frame_card.pack(pady=5, padx=10, fill="x")
    frame_card.pack_propagate(False)
    
    customtkinter.CTkLabel(
        master=frame_card,
        text=leitor.nome,
        font=("Libre Baskerville", 18, "bold"),
        text_color="#001126"
    ).place(x=20, y=15)
    
    customtkinter.CTkLabel(
        master=frame_card,
        text=leitor.telefone,
        font=("Libre Baskerville", 16),
        text_color="#001126"
    ).place(x=20, y=50)
    
    customtkinter.CTkLabel(
        master=frame_card,
        text=f"ID:{leitor.id_leitor}",
        font=("Libre Baskerville", 16),
        text_color="#001126"
    ).place(x=20, y=80)
    
    btn_editar = customtkinter.CTkButton(
        master=frame_card,
        width=50,
        height=50,
        text="✎",
        font=("Arial", 24),
        fg_color="#001126",
        corner_radius=25,
        hover_color="#003e7e",
        command=lambda: editar_leitor(leitor)
    )
    btn_editar.place(x=820, y=35)

def criar_card_emprestimo(emprestimo, master):
    frame_card = customtkinter.CTkFrame(
        master=master,
        width=900,
        height=120,
        fg_color="#cacaca",
        corner_radius=10,
        border_color="#001126",
        border_width=3
    )
    frame_card.pack(pady=5, padx=10, fill="x")
    frame_card.pack_propagate(False)
    
    customtkinter.CTkLabel(
        master=frame_card,
        text=emprestimo.leitor.nome,
        font=("Libre Baskerville", 18, "bold"),
        text_color="#001126"
    ).place(x=20, y=15)
    
    customtkinter.CTkLabel(
        master=frame_card,
        text=f"Pegou o livro:{emprestimo.livro.titulo}",
        font=("Libre Baskerville", 16),
        text_color="#001126"
    ).place(x=20, y=50)
    
    customtkinter.CTkLabel(
        master=frame_card,
        text=emprestimo.dataempr.strftime("%d/%m/%y"),
        font=("Libre Baskerville", 16),
        text_color="#001126"
    ).place(x=20, y=80)
    
    btn_check = customtkinter.CTkButton(
        master=frame_card,
        width=50,
        height=50,
        text="✓",
        font=("Arial", 30, "bold"),
        fg_color="#001126",
        corner_radius=25,
        hover_color="#00b300",
        command=lambda: confirmar_devolucao(emprestimo, frame_card)
    )
    btn_check.place(x=820, y=35)

def editar_livro(livro):
    global livro_selecionado, capa_livro_path
    livro_selecionado = livro
    capa_livro_path = livro.capa_path if hasattr(livro, 'capa_path') else None
    
    if capa_livro_path:
        try:
            img = Image.open(capa_livro_path)
            img = img.resize((200, 250))
            img_tk = customtkinter.CTkImage(dark_image=img, light_image=img, size=(200, 250))
            imagem_livro.configure(image=img_tk, text="")
        except:
            imagem_livro.configure(image=None, text="📷")
    else:
        imagem_livro.configure(image=None, text="📷")
    
    nome_livro.delete(0, 'end')
    nome_livro.insert(0, livro.titulo)
    autor_livro.delete(0, 'end')
    autor_livro.insert(0, livro.autor)
    quantidade_livro.delete(0, 'end')
    quantidade_livro.insert(0, str(livro.qtd_exemplar))
    isbn_livro.delete(0, 'end')
    isbn_livro.insert(0, livro.isbn)
    edicao_livro.delete(0, 'end')
    edicao_livro.insert(0, livro.edicao)
    
    botao_cadastrar.configure(text="Salvar alterações", command=salvar_alteracoes_livro)
    
    if not hasattr(botao_cadastrar, 'botao_deletar_criado'):
        botao_deletar_livro = customtkinter.CTkButton(
            master=frame_cadastro,
            text="🗑",
            width=80,
            height=70,
            font=("Arial", 40),
            corner_radius=20,
            fg_color="#d9d9d9",
            border_width=2,
            border_color="#001126",
            hover_color="#ff0000",
            text_color="#001126",
            command=confirmar_deletar_livro
        )
        botao_deletar_livro.grid(row=0, column=1, pady=20, padx=(0, 20), sticky="ne")
        botao_cadastrar.botao_deletar_criado = True

def editar_leitor(leitor):
    global leitor_selecionado
    leitor_selecionado = leitor
    
    nome_leitor.delete(0, 'end')
    nome_leitor.insert(0, leitor.nome)
    telefone_leitor.delete(0, 'end')
    telefone_leitor.insert(0, leitor.telefone)
    id_leitor.delete(0, 'end')
    id_leitor.insert(0, leitor.id_leitor)
    
    botao_cadastrar_leitor.configure(text="Salvar alterações", command=salvar_alteracoes_leitor)
    
    if not hasattr(botao_cadastrar_leitor, 'botao_excluir_criado'):
        botao_excluir_leitor = customtkinter.CTkButton(
            master=frame_cadastro_leitores,
            text="Excluir Leitor",
            width=600,
            height=70,
            font=("Libre Baskerville", 24, "bold"),
            corner_radius=20,
            fg_color="#001126",
            border_width=2,
            border_color="#001126",
            hover_color="#ff0000",
            text_color="white",
            command=confirmar_deletar_leitor
        )
        botao_excluir_leitor.grid(row=4, column=0, pady=20, padx=20, sticky="w", columnspan=2)
        botao_cadastrar_leitor.botao_excluir_criado = True

def salvar_alteracoes_livro():
    global livro_selecionado, capa_livro_path
    if livro_selecionado:
        livro_selecionado.titulo = nome_livro.get()
        livro_selecionado.autor = autor_livro.get()
        livro_selecionado.qtd_exemplar = int(quantidade_livro.get())
        livro_selecionado.isbn = isbn_livro.get()
        livro_selecionado.edicao = edicao_livro.get()
        livro_selecionado.capa_path = capa_livro_path
        
        limpar_frame(frame_resultados_livros)
        for l in lista_livros.listalivros:
            criar_card_livro(l, frame_resultados_livros)
        
        limpar_campos_livro()
        livro_selecionado = None

def salvar_alteracoes_leitor():
    global leitor_selecionado
    if leitor_selecionado:
        leitor_selecionado.nome = nome_leitor.get()
        leitor_selecionado.telefone = telefone_leitor.get()
        leitor_selecionado.id_leitor = id_leitor.get()
        
        limpar_frame(frame_resultados_leitores)
        for l in lista_leitores.listaleitores:
            criar_card_leitor(l, frame_resultados_leitores)
        
        limpar_campos_leitor()
        leitor_selecionado = None

def confirmar_deletar_livro():
    global livro_selecionado
    if livro_selecionado:
        dialog = customtkinter.CTkToplevel(janela)
        dialog.title("")
        dialog.geometry("600x300")
        dialog.configure(fg_color="#cacaca")
        dialog.transient(janela)
        dialog.grab_set()
        
        customtkinter.CTkLabel(
            master=dialog,
            text="Você deseja\ndeletar esse\nlivro?",
            font=("Libre Baskerville", 32, "bold"),
            text_color="#001126"
        ).pack(pady=40)
        
        frame_botoes = customtkinter.CTkFrame(master=dialog, fg_color="transparent")
        frame_botoes.pack(pady=20)
        
        customtkinter.CTkButton(
            master=frame_botoes,
            text="Sim",
            width=150,
            height=60,
            font=("Libre Baskerville", 24, "bold"),
            fg_color="#001126",
            corner_radius=20,
            command=lambda: deletar_livro(dialog)
        ).pack(side="left", padx=20)
        
        customtkinter.CTkButton(
            master=frame_botoes,
            text="Não",
            width=150,
            height=60,
            font=("Libre Baskerville", 24, "bold"),
            fg_color="#001126",
            corner_radius=20,
            command=dialog.destroy
        ).pack(side="left", padx=20)

def deletar_livro(dialog):
    global livro_selecionado
    if livro_selecionado:
        lista_livros.listalivros.remove(livro_selecionado)
        limpar_frame(frame_resultados_livros)
        for l in lista_livros.listalivros:
            criar_card_livro(l, frame_resultados_livros)
        limpar_campos_livro()
        livro_selecionado = None
        dialog.destroy()

def confirmar_deletar_leitor():
    global leitor_selecionado
    if leitor_selecionado:
        dialog = customtkinter.CTkToplevel(janela)
        dialog.title("")
        dialog.geometry("600x300")
        dialog.configure(fg_color="#cacaca")
        dialog.transient(janela)
        dialog.grab_set()
        
        customtkinter.CTkLabel(
            master=dialog,
            text="Você deseja\ndeletar esse\nleitor?",
            font=("Libre Baskerville", 32, "bold"),
            text_color="#001126"
        ).pack(pady=40)
        
        frame_botoes = customtkinter.CTkFrame(master=dialog, fg_color="transparent")
        frame_botoes.pack(pady=20)
        
        customtkinter.CTkButton(
            master=frame_botoes,
            text="Sim",
            width=150,
            height=60,
            font=("Libre Baskerville", 24, "bold"),
            fg_color="#001126",
            corner_radius=20,
            command=lambda: deletar_leitor(dialog)
        ).pack(side="left", padx=20)
        
        customtkinter.CTkButton(
            master=frame_botoes,
            text="Não",
            width=150,
            height=60,
            font=("Libre Baskerville", 24, "bold"),
            fg_color="#001126",
            corner_radius=20,
            command=dialog.destroy
        ).pack(side="left", padx=20)

def deletar_leitor(dialog):
    global leitor_selecionado
    if leitor_selecionado:
        lista_leitores.listaleitores.remove(leitor_selecionado)
        limpar_frame(frame_resultados_leitores)
        for l in lista_leitores.listaleitores:
            criar_card_leitor(l, frame_resultados_leitores)
        limpar_campos_leitor()
        leitor_selecionado = None
        dialog.destroy()

def confirmar_devolucao(emprestimo, card):
    dialog = customtkinter.CTkToplevel(janela)
    dialog.title("")
    dialog.geometry("700x350")
    dialog.configure(fg_color="#cacaca")
    dialog.transient(janela)
    dialog.grab_set()
    
    customtkinter.CTkLabel(
        master=dialog,
        text="Você deseja\nregistrar a\ndevolução desse\nempréstimo?",
        font=("Libre Baskerville", 28, "bold"),
        text_color="#001126"
    ).pack(pady=30)
    
    frame_botoes = customtkinter.CTkFrame(master=dialog, fg_color="transparent")
    frame_botoes.pack(pady=20)
    
    customtkinter.CTkButton(
        master=frame_botoes,
        text="Sim",
        width=150,
        height=60,
        font=("Libre Baskerville", 24, "bold"),
        fg_color="#001126",
        corner_radius=20,
        command=lambda: devolver_livro(emprestimo, card, dialog)
    ).pack(side="left", padx=20)
    
    customtkinter.CTkButton(
        master=frame_botoes,
        text="Não",
        width=150,
        height=60,
        font=("Libre Baskerville", 24, "bold"),
        fg_color="#001126",
        corner_radius=20,
        command=dialog.destroy
    ).pack(side="left", padx=20)

def devolver_livro(emprestimo, card, dialog):
    emprestimo.registrardevolucao()
    card.destroy()
    limpar_frame(frame_resultados_livros)
    for l in lista_livros.listalivros:
        criar_card_livro(l, frame_resultados_livros)
    dialog.destroy()

def limpar_campos_livro():
    global capa_livro_path
    isbn_livro.delete(0, 'end')
    nome_livro.delete(0, 'end')
    autor_livro.delete(0, 'end')
    edicao_livro.delete(0, 'end')
    quantidade_livro.delete(0, 'end')
    capa_livro_path = None
    imagem_livro.configure(image=None, text="📷")
    botao_cadastrar.configure(text="Cadastrar Livro", command=cadastrar_livro)

def limpar_campos_leitor():
    id_leitor.delete(0, 'end')
    nome_leitor.delete(0, 'end')
    telefone_leitor.delete(0, 'end')
    botao_cadastrar_leitor.configure(text="Cadastrar Leitor", command=cadastrar_leitor)

def cadastrar_livro():
    global capa_livro_path
    try:
        livro = Livro(
            isbn=isbn_livro.get(),
            titulo=nome_livro.get(),
            autor=autor_livro.get(),
            edicao=edicao_livro.get(),
            qtd_exemplar=int(quantidade_livro.get())
        )
        livro.capa_path = capa_livro_path
        lista_livros.cadastrar_livro(livro)
        
        limpar_frame(frame_resultados_livros)
        for l in lista_livros.listalivros:
            criar_card_livro(l, frame_resultados_livros)
        
        limpar_campos_livro()
    except:
        pass

def cadastrar_leitor():
    try:
        leitor = Leitor(
            id_leitor=id_leitor.get(),
            nome=nome_leitor.get(),
            telefone=telefone_leitor.get()
        )
        lista_leitores.cadastrarleitor(leitor)
        
        limpar_frame(frame_resultados_leitores)
        for l in lista_leitores.listaleitores:
            criar_card_leitor(l, frame_resultados_leitores)
        
        limpar_campos_leitor()
    except:
        pass

def registrar_emprestimo():
    try:
        nome_busca = nome_leitor_emprestimo.get()
        livro_busca = nome_livro_emprestimo.get()
        
        leitor = None
        for l in lista_leitores.listaleitores:
            if l.nome.lower() == nome_busca.lower():
                leitor = l
                break
        
        livro = None
        for lv in lista_livros.listalivros:
            if lv.titulo.lower() == livro_busca.lower():
                livro = lv
                break
        
        if leitor and livro:
            emprestimo = Emprestimo(livro, leitor)
            resultado = emprestimo.registrar_emprestimo()
            
            if "Sem exemplares" not in resultado:
                lista_emprestimos.append(emprestimo)
                
                limpar_frame(frame_resultados_emprestimos)
                for e in lista_emprestimos:
                    if e.datadev is None:
                        criar_card_emprestimo(e, frame_resultados_emprestimos)
                
                limpar_frame(frame_resultados_livros)
                for l in lista_livros.listalivros:
                    criar_card_livro(l, frame_resultados_livros)
            
            nome_leitor_emprestimo.delete(0, 'end')
            nome_livro_emprestimo.delete(0, 'end')
    except:
        pass

def pesquisar_livros():
    termo = entrada_pesquisas.get().lower()
    if termo == "":
        for livro in lista_livros.listalivros:
            criar_card_livro(livro, frame_resultados_livros)
    else:
        for livro in lista_livros.listalivros:
            if termo in livro.titulo.lower() or termo in livro.autor.lower() or termo in str(livro.isbn):
                criar_card_livro(livro, frame_resultados_livros)

def pesquisar_leitores():
    termo = entrada_pesquisa_leitores.get().lower()
    if termo == "":
        for leitor in lista_leitores.listaleitores:
            criar_card_leitor(leitor, frame_resultados_leitores)
    else:
        for leitor in lista_leitores.listaleitores:
            if termo in leitor.nome.lower() or termo in leitor.telefone or termo in str(leitor.id_leitor):
                criar_card_leitor(leitor, frame_resultados_leitores)

def pesquisar_emprestimos():
    termo = entrada_pesquisa_emprestimos.get().lower()
    for emprestimo in lista_emprestimos:
        if emprestimo.datadev is None:
            if termo == "" or termo in emprestimo.leitor.nome.lower() or termo in emprestimo.livro.titulo.lower():
                criar_card_emprestimo(emprestimo, frame_resultados_emprestimos)

def limpar_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def pesquisar_livros_com_limpa():
    limpar_frame(frame_resultados_livros)
    pesquisar_livros()

def pesquisar_leitores_com_limpa():
    limpar_frame(frame_resultados_leitores)
    pesquisar_leitores()

def pesquisar_emprestimos_com_limpa():
    limpar_frame(frame_resultados_emprestimos)
    pesquisar_emprestimos()

imagem_livro.configure(command=selecionar_capa)
botao_cadastrar.configure(command=cadastrar_livro)
botao_cadastrar_leitor.configure(command=cadastrar_leitor)
botao_registrar_emprestimo.configure(command=registrar_emprestimo)
botao_pesquisar.configure(command=pesquisar_livros_com_limpa)
botao_pesquisar_leitores.configure(command=pesquisar_leitores_com_limpa)
botao_pesquisar_emprestimos.configure(command=pesquisar_emprestimos_com_limpa)

frame_livros.pack(fill="both", expand=True)
janela.mainloop()
