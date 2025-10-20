import customtkinter as ctk
from main import Livro, Leitor, Emprestimo, ListaLivros, ListaLeitores
import datetime

class BibliotecaApp:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.title("TELivraria")
        self.app.geometry("1200x800")
        
        # Set appearance
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Initialize data structures
        self.lista_livros = ListaLivros("TELivraria")
        self.lista_leitores = ListaLeitores("TELivraria")
        
        # Configure grid
        self.app.grid_columnconfigure(0, weight=1)
        self.app.grid_rowconfigure(1, weight=1)
        
        # Create navigation bar
        self.create_nav_bar()
        
        # Create main frame
        self.main_frame = ctk.CTkFrame(self.app)
        self.main_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        
        # Show livros frame by default
        self.show_livros_frame()

    def create_nav_bar(self):
        nav_frame = ctk.CTkFrame(self.app, fg_color="#000C1F", height=80)
        nav_frame.grid(row=0, column=0, sticky="ew")
        nav_frame.grid_columnconfigure(1, weight=1)
        
        # Logo
        logo_label = ctk.CTkLabel(nav_frame, text="TELivraria", font=("Arial", 28, "bold"), text_color="white")
        logo_label.grid(row=0, column=0, padx=30)
        
        # Navigation buttons frame
        buttons_frame = ctk.CTkFrame(nav_frame, fg_color="transparent")
        buttons_frame.grid(row=0, column=1, sticky="e", padx=30)
        
        # Navigation buttons
        button_font = ("Arial", 16)
        btn_livros = ctk.CTkButton(buttons_frame, text="Livros", command=self.show_livros_frame,
                                 font=button_font, width=120, height=40, fg_color="#000C1F",
                                 hover_color="#001F4D")
        btn_livros.pack(side="left", padx=10)
        
        btn_leitores = ctk.CTkButton(buttons_frame, text="Leitores", command=self.show_leitores_frame,
                                   font=button_font, width=120, height=40, fg_color="#000C1F",
                                   hover_color="#001F4D")
        btn_leitores.pack(side="left", padx=10)
        
        btn_emprestimos = ctk.CTkButton(buttons_frame, text="Empréstimos", command=self.show_emprestimos_frame,
                                      font=button_font, width=120, height=40, fg_color="#000C1F",
                                      hover_color="#001F4D")
        btn_emprestimos.pack(side="left", padx=10)

    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_livros_frame(self):
        self.clear_main_frame()
        self.main_frame.configure(fg_color="#E5E5E5")
        
        # Search bar
        search_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        search_frame.pack(fill="x", padx=50, pady=(30, 20))
        
        search_entry = ctk.CTkEntry(search_frame, placeholder_text="Pesquisar...", 
                                  width=500, height=40, 
                                  font=("Arial", 14))
        search_entry.pack(side="left", padx=(0, 10))
        
        search_button = ctk.CTkButton(search_frame, text="Buscar", 
                                    width=100, height=40,
                                    font=("Arial", 14),
                                    fg_color="#000C1F",
                                    hover_color="#001F4D")
        search_button.pack(side="left")
        
        # Book registration form
        form_frame = ctk.CTkFrame(self.main_frame, fg_color="white", corner_radius=10)
        form_frame.pack(fill="both", expand=True, padx=50, pady=20)
        
        # Image upload button (placeholder)
        upload_btn = ctk.CTkButton(form_frame, text="Carregar Imagem",
                                width=150, height=150,
                                font=("Arial", 14),
                                fg_color="#E5E5E5",
                                text_color="black",
                                hover_color="#CCCCCC")
        upload_btn.grid(row=0, column=0, padx=30, pady=30, rowspan=2)
        
        # Form fields
        labels = ["Título do Livro", "Nome do Autor", "Qtd. Exemplares", "ISBN", "Edição"]
        self.livro_entries = {}
        
        for i, label in enumerate(labels):
            ctk.CTkLabel(form_frame, text=label,
                        font=("Arial", 14),
                        text_color="black").grid(row=i, column=1, padx=20, pady=10, sticky="e")
            entry = ctk.CTkEntry(form_frame, width=400, height=35,
                               font=("Arial", 14),
                               fg_color="#F0F0F0",
                               border_color="#000C1F")
            entry.grid(row=i, column=2, padx=20, pady=10, sticky="w")
            self.livro_entries[label] = entry
        
        # Submit button
        submit_btn = ctk.CTkButton(form_frame, text="Cadastrar Livro",
                                command=self.cadastrar_livro,
                                font=("Arial", 16, "bold"),
                                width=200, height=45,
                                fg_color="#000C1F",
                                hover_color="#001F4D")
        submit_btn.grid(row=len(labels), column=1, columnspan=2, pady=30)

    def show_leitores_frame(self):
        self.clear_main_frame()
        self.main_frame.configure(fg_color="#E5E5E5")
        
        # Form frame
        form_frame = ctk.CTkFrame(self.main_frame, fg_color="white", corner_radius=10)
        form_frame.pack(fill="both", expand=True, padx=50, pady=50)
        
        # Title
        title_label = ctk.CTkLabel(form_frame, text="Cadastro de Leitores",
                                font=("Arial", 24, "bold"),
                                text_color="black")
        title_label.pack(pady=30)
        
        # Form fields
        labels = ["ID Leitor", "Nome", "Telefone"]
        self.leitor_entries = {}
        
        fields_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        fields_frame.pack(pady=20)
        
        for i, label in enumerate(labels):
            ctk.CTkLabel(fields_frame, text=label,
                        font=("Arial", 14),
                        text_color="black").grid(row=i, column=0, padx=20, pady=10, sticky="e")
            entry = ctk.CTkEntry(fields_frame, width=400, height=35,
                               font=("Arial", 14),
                               fg_color="#F0F0F0",
                               border_color="#000C1F")
            entry.grid(row=i, column=1, padx=20, pady=10, sticky="w")
            self.leitor_entries[label] = entry
        
        # Submit button
        submit_btn = ctk.CTkButton(form_frame, text="Cadastrar Leitor",
                                command=self.cadastrar_leitor,
                                font=("Arial", 16, "bold"),
                                width=200, height=45,
                                fg_color="#000C1F",
                                hover_color="#001F4D")
        submit_btn.pack(pady=30)

    def show_emprestimos_frame(self):
        self.clear_main_frame()
        self.main_frame.configure(fg_color="#E5E5E5")
        
        # Form frame
        form_frame = ctk.CTkFrame(self.main_frame, fg_color="white", corner_radius=10)
        form_frame.pack(fill="both", expand=True, padx=50, pady=50)
        
        # Title
        title_label = ctk.CTkLabel(form_frame, text="Gestão de Empréstimos",
                                font=("Arial", 24, "bold"),
                                text_color="black")
        title_label.pack(pady=30)
        
        # Form fields
        labels = ["ISBN do Livro", "ID do Leitor"]
        self.emprestimo_entries = {}
        
        fields_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        fields_frame.pack(pady=20)
        
        for i, label in enumerate(labels):
            ctk.CTkLabel(fields_frame, text=label,
                        font=("Arial", 14),
                        text_color="black").grid(row=i, column=0, padx=20, pady=10, sticky="e")
            entry = ctk.CTkEntry(fields_frame, width=400, height=35,
                               font=("Arial", 14),
                               fg_color="#F0F0F0",
                               border_color="#000C1F")
            entry.grid(row=i, column=1, padx=20, pady=10, sticky="w")
            self.emprestimo_entries[label] = entry
        
        # Buttons frame
        buttons_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        buttons_frame.pack(pady=30)
        
        # Buttons
        emprestar_btn = ctk.CTkButton(buttons_frame, text="Registrar Empréstimo",
                                   command=self.registrar_emprestimo,
                                   font=("Arial", 16, "bold"),
                                   width=200, height=45,
                                   fg_color="#000C1F",
                                   hover_color="#001F4D")
        emprestar_btn.pack(side="left", padx=10)
        
        devolver_btn = ctk.CTkButton(buttons_frame, text="Registrar Devolução",
                                  command=self.registrar_devolucao,
                                  font=("Arial", 16, "bold"),
                                  width=200, height=45,
                                  fg_color="#000C1F",
                                  hover_color="#001F4D")
        devolver_btn.pack(side="left", padx=10)

    def cadastrar_livro(self):
        try:
            livro = Livro(
                isbn=self.livro_entries["ISBN"].get(),
                titulo=self.livro_entries["Título do Livro"].get(),
                autor=self.livro_entries["Nome do Autor"].get(),
                edicao=self.livro_entries["Edição"].get(),
                qtd_exemplar=int(self.livro_entries["Qtd. Exemplares"].get())
            )
            self.lista_livros.cadastrar_livro(livro)
            self.show_message("Sucesso", "Livro cadastrado com sucesso!")
            
            # Clear entries
            for entry in self.livro_entries.values():
                entry.delete(0, 'end')
                
        except Exception as e:
            self.show_message("Erro", str(e))

    def cadastrar_leitor(self):
        try:
            leitor = Leitor(
                id_leitor=self.leitor_entries["ID Leitor"].get(),
                nome=self.leitor_entries["Nome"].get(),
                telefone=self.leitor_entries["Telefone"].get()
            )
            self.lista_leitores.cadastrarleitor(leitor)
            self.show_message("Sucesso", "Leitor cadastrado com sucesso!")
            
            # Clear entries
            for entry in self.leitor_entries.values():
                entry.delete(0, 'end')
                
        except Exception as e:
            self.show_message("Erro", str(e))

    def registrar_emprestimo(self):
        try:
            isbn = self.emprestimo_entries["ISBN do Livro"].get()
            id_leitor = self.emprestimo_entries["ID do Leitor"].get()
            
            livro = self.lista_livros.consultarlivro(isbn)
            leitor = self.lista_leitores.consultarleitor(id_leitor)
            
            if isinstance(livro, str) or isinstance(leitor, str):
                self.show_message("Erro", "Livro ou leitor não encontrado!")
                return
                
            emprestimo = Emprestimo(livro, leitor)
            resultado = emprestimo.registrar_emprestimo()
            self.show_message("Resultado", resultado)
            
            # Clear entries
            for entry in self.emprestimo_entries.values():
                entry.delete(0, 'end')
                
        except Exception as e:
            self.show_message("Erro", str(e))

    def registrar_devolucao(self):
        try:
            isbn = self.emprestimo_entries["ISBN do Livro"].get()
            id_leitor = self.emprestimo_entries["ID do Leitor"].get()
            
            livro = self.lista_livros.consultarlivro(isbn)
            leitor = self.lista_leitores.consultarleitor(id_leitor)
            
            if isinstance(livro, str) or isinstance(leitor, str):
                self.show_message("Erro", "Livro ou leitor não encontrado!")
                return
                
            emprestimo = Emprestimo(livro, leitor)
            resultado = emprestimo.registrardevolucao()
            self.show_message("Resultado", resultado)
            
            # Clear entries
            for entry in self.emprestimo_entries.values():
                entry.delete(0, 'end')
                
        except Exception as e:
            self.show_message("Erro", str(e))

    def show_message(self, title, message):
        dialog = ctk.CTkInputDialog(text=message, title=title,
                                  button_fg_color="#000C1F",
                                  button_hover_color="#001F4D",
                                  font=("Arial", 14))
        dialog.destroy()

    def run(self):
        self.app.mainloop()

if __name__ == "__main__":
    app = BibliotecaApp()
    app.run()
