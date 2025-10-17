class Tarefa:
    def __init__(self, descricao: str):
        self.descricao = descricao
        self.concluida = False

    def concluir(self):
        self.concluida = True

    def __str__(self):
        status = "Concluída" if self.concluida else "Pendente"
        return f"Tarefa: {self.descricao} | Status: {status}"


class ListaTarefas:
    def __init__(self, nome_lista: str):
        self.nome_lista = nome_lista
        self.tarefas = []

    def adicionar_tarefa(self, tarefa: Tarefa):
        self.tarefas.append(tarefa)

    def concluir_tarefa(self, descricao: str):
        for i in self.tarefas:
            if i.descricao == descricao:
                i.concluir()

    def listar_tarefas(self):
        return [str(i) for i in self.tarefas]

    def listar_pendentes(self):
        return [str(i) for i in self.tarefas if not i.concluida]

    def salvar_em_arquivo(self):
        nome_arquivo = f"{self.nome_lista}.txt"
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            for i in self.tarefas:
                status = "Concluída" if i.concluida else "Pendente"
                arquivo.write(f"{i.descricao} = {status}\n")
