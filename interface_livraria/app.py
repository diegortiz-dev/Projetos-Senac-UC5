import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")       

janela = customtkinter.CTk()
janela.title("Interface Livraria")
janela.geometry("1920x1080")
janela.configure(fg_color="#a2a2a2")
frame_header = customtkinter.CTkFrame(master=janela, width=1920, height=120, corner_radius=0, fg_color="#001126")
frame_header.pack(pady=0, padx=0, fill="x", side="top")
frame_pesquisas= customtkinter.CTkFrame(master=janela, width=1100, height=960, corner_radius=0, fg_color="#a2a2a2")
frame_pesquisas.pack(pady=0, padx=0, fill="both", side="left", expand=True)
frame_cadastro=customtkinter.CTkFrame(master=janela, width=820, height=960, corner_radius=0, fg_color="#a2a2a2")
frame_cadastro.pack(pady=0, padx=0, fill="both", side="right", expand=True)
imagem_pil = Image.open("assets/imagemlivraria.png")
imagem_redimensionada = imagem_pil.resize((150, 150))
icone_app = customtkinter.CTkImage(master=frame_header, dark_image=imagem_redimensionada, light_image=imagem_redimensionada)
icone_app.grid(row=0, column=0, pady=20, padx=5, sticky="w")
nome_app = customtkinter.CTkLabel(master=frame_header, text="TELivraria", text_color="white", font=("Libre Baskerville", 32),width=600)
nome_app.grid(row=0, column=0, pady=20, padx=5, sticky="w")
botao_livros = customtkinter.CTkButton(master=frame_header, text="Livros",text_color="white",width=250,height=100,font=("Libre Baskerville", 30),corner_radius=30,fg_color="#003e7e",bg_color="#001126")
botao_livros.grid(row=0, column=1, pady=20, padx=20, sticky="w")
botao_leitores = customtkinter.CTkButton(master=frame_header, text="Leitores",text_color="white",width=250,height=100,font=("Libre Baskerville", 30),corner_radius=30,fg_color="#003e7e",bg_color="#001126")
botao_leitores.grid(row=0, column=2, pady=20, padx=20, sticky="w")
botao_emprestimos = customtkinter.CTkButton(master=frame_header, text="Empréstimos",text_color="white",width=250,height=100,font=("Libre Baskerville", 30),corner_radius=30,fg_color="#003e7e",bg_color="#001126")
botao_emprestimos.grid(row=0, column=3, pady=20, padx=20, sticky="w")
entrada_pesquisas = customtkinter.CTkEntry(master=frame_pesquisas, width=750,height=90, placeholder_text="Pesquisar...",font=("Libre Baskerville", 30),corner_radius=30,fg_color="#d9d9d9")
entrada_pesquisas.grid(row=0, column=0, pady=10, padx=10, sticky="w")


janela.mainloop()
