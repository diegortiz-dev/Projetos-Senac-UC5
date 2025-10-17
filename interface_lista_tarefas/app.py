import customtkinter
 
janela=customtkinter.CTk()
janela.geometry('400x700')
janela.title("Todolist")
janela.resizable(False,False)
janela.iconbitmap("iconelista.ico")
janela.configure(fg_color="#1d2866")
entrada_nome_lista=customtkinter.CTkEntry(janela,text_color="white",placeholder_text="Nome da Lista",placeholder_text_color="white",justify="center",corner_radius=20,fg_color="#b4b4b4",width=380,height=40,font=("League Spartan",30,"bold"))
entrada_nome_lista.grid(row=1,column=0,columnspan=2,padx=10,pady=5)
entrada_nome_tarefa=customtkinter.CTkEntry(janela,text_color="white",placeholder_text="Adicionar Tarefa",placeholder_text_color="white",justify="center",corner_radius=20,fg_color="#b4b4b4",width=300,height=40,font=("League Spartan",30,"bold"))
entrada_nome_tarefa.grid(row=3,column=0,padx=10,pady=5)
botao_adicionar=customtkinter.CTkButton(janela,text="+",fg_color="#b4b4b4",hover_color="#c2c2c2",width=50,height=50,corner_radius=20,font=("League Spartan",40,"bold"),command=lambda: adicionar_tarefa())
botao_adicionar.grid(row=3,column=1,padx=10,pady=5)
lista_tarefas = customtkinter.CTkScrollableFrame(janela, width=350, height=350, corner_radius=10, fg_color="#b4b4b4")
lista_tarefas.grid(row=4,column=0,columnspan=2,pady=20)
botao_pendentes=customtkinter.CTkButton(janela,text="Ver Pendentes",fg_color="#b4b4b4",hover_color="#b4b4b4",width=380,height=40,corner_radius=20,font=("League Spartan",30,"bold"),command=lambda: ver_pendentes())
botao_pendentes.grid(row=5,column=0,columnspan=2,padx=5,pady=5)
botao_salvar=customtkinter.CTkButton(janela,text="Salvar lista",fg_color="#46c143",hover_color="#023809",width=380,height=40,corner_radius=20,font=("League Spartan",30,"bold"),command=lambda: salvar_lista())
botao_salvar.grid(row=6,column=0,columnspan=2,padx=10,pady=5)
 
 
def adicionar_tarefa():
    tarefa = entrada_nome_tarefa.get().strip()
    if tarefa != "":
        criar_tarefa(tarefa)
        entrada_nome_tarefa.delete(0, "end")
 
def criar_tarefa(tarefa):
    tarefa_frame = customtkinter.CTkFrame(lista_tarefas, fg_color="#b4b4b4", corner_radius=10)
    tarefa_frame.grid(pady=5, padx=5, sticky="ew")
    tarefa_label = customtkinter.CTkLabel(tarefa_frame,text=tarefa,anchor="w",text_color="white",font=("Segoe UI", 20,"bold"))
    tarefa_label.grid(row=0, column=1, sticky="w", padx=(10, 0))
    botao_concluir = customtkinter.CTkButton(tarefa_frame,text="✔",width=35,height=30,fg_color="#46c143",hover_color="#1c4d1b",corner_radius=8,command=lambda: alternar_status(tarefa_label, botao_concluir, tarefa_frame))
    botao_concluir.grid(row=0, column=0, sticky="e", padx=(5, 10))
 
def alternar_status(tarefa_label, botao_concluir, tarefa_frame):
    if tarefa_label.cget("text_color") == "white":
        tarefa_label.configure(text_color="gray50")  
        botao_concluir.configure(text="X", fg_color="#d11818")  
    else:
        tarefa_label.configure(text_color="white")  
        botao_concluir.configure(text="✔", fg_color="#1f631e")
 
def ver_pendentes():
    for tarefa_frame in lista_tarefas.winfo_children():
            tarefa_label = tarefa_frame.winfo_children()[0]
            if tarefa_label.cget("text_color") == "gray50":
                tarefa_frame.grid_remove() 
            else:
                tarefa_frame.grid()
    botao_pendentes.configure(text="Ver todas",command=ver_todas)

def ver_todas():
    for tarefa_frame in lista_tarefas.winfo_children():
        tarefa_frame.grid()
    botao_pendentes.configure(text="Ver pendentes",command=ver_pendentes)

 
def salvar_lista():
    nome_arquivo = f"{entrada_nome_lista.get().strip()}.txt"
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for tarefa_frame in lista_tarefas.winfo_children():
            tarefa_label = tarefa_frame.winfo_children()[0]
            descricao = tarefa_label.cget("text")
            status = "Concluída" if tarefa_label.cget("text_color") == "gray50" else "Pendente"
            arquivo.write(f"{descricao} = {status}\n")
 
 
janela.mainloop()