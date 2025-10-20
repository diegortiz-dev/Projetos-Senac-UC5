import datetime


class Leitor:
    def __init__(self, id_leitor, nome, telefone):
        self.id_leitor = id_leitor
        self.nome = nome
        self.telefone = telefone

    def __str__(self):
        return "Nome:{} ID:{} Telefone:{}".format(self.nome, self.id_leitor, self.telefone)


class Livro:
    def __init__(self, isbn, titulo, autor, edicao, qtd_exemplar):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.edicao = edicao
        self.qtd_exemplar = qtd_exemplar

    def __str__(self):
        return "Titulo:{} Autor:{} Exemplares Disponiveis:{}".format(self.titulo, self.autor, self.qtd_exemplar)


class Emprestimo:
    def __init__(self, livro: Livro, leitor: Leitor):
        self.livro = livro
        self.leitor = leitor
        self.datadev = None
        self.dataempr = None

    def registrar_emprestimo(self):
        if self.livro.qtd_exemplar > 0:
            self.dataempr = datetime.date.today()
            self.livro.qtd_exemplar -= 1
            return "Devoluçao registrada:{} Pegou o livro {} no dia {}".format(self.leitor, self.livro, self.dataempr)
        else:
            return "Sem exemplares para emprestimo"

    def registrardevolucao(self):
        self.datadev = datetime.date.today()
        self.livro.qtd_exemplar += 1
        return "Devoluçao registrada:{} devolveu o livro {} no dia {}".format(self.leitor, self.livro, self.datadev)


class ListaLeitores:
    def __init__(self, nome_livraria):
        self.nome_livraria = nome_livraria
        self.listaleitores = []

    def cadastrarleitor(self, leitor: Leitor):
        self.listaleitores.append(leitor)

    def atualizarleitor(self, id_leitor, novo_telefone=None, novo_nome=None):
        for i in self.listaleitores:
            if i.id_leitor == id_leitor:
                if novo_telefone != None:
                    i.telefone = novo_telefone
                if novo_nome != None:
                    i.nome = novo_nome
                return 'Telefone do Leitor {} atualizado para {}'.format(id_leitor, novo_telefone)
        return 'Leitor nao encontrado'

    def deletarleitor(self, id_leitor):
        for i in self.listaleitores:
            if i.id_leitor == id_leitor:
                del self.listaleitores[i]

    def consultarleitor(self, id_leitor):
        for i in self.listaleitores:
            if i.id_leitor == id_leitor:
                return i
        return "Leitor nao encontrado"


class ListaLivros:
    def __init__(self, nome_livraria):
        self.nome_livraria = nome_livraria
        self.listalivros = []

    def cadastrar_livro(self, livro: Livro):
        self.listalivros.append(livro)

    def atualizar_livro(self, isbn, qtd_exemplar_add):
        for i in self.listalivros:
            if i.isbn == isbn:
                i.qtd_exemplar = qtd_exemplar_add

    def deletar_livro(self, isbn):
        for i in self.listalivros:
            if i.isbn == isbn:
                del self.listalivros[i]

    def consultarlivro(self, isbn):
        for i in self.listalivros:
            if i.isbn == isbn:
                return i
        return "Livro nao encontrado"

    def verificar_disponibilidade(self, isbn):
        for i in self.listalivros:
            if i.qtd_exemplar > 0 and i.isbn == isbn:
                return 'Livro Disponivel'
        return 'Livro Indisponivel'


lista_leitores = ListaLeitores("Livraria Central")
lista_livros = ListaLivros("Livraria Central")

leitor1 = Leitor(1, "Diego", "1111-1111")
leitor2 = Leitor(2, "Duda amor", "2222-2222")

lista_leitores.cadastrarleitor(leitor1)
lista_leitores.cadastrarleitor(leitor2)

livro1 = Livro(3, 'Arte da guerra', 'Sun Tzu', 'edicao top', 2)
lista_livros.cadastrar_livro(livro1)

emprestimo1=Emprestimo(livro1,leitor1)
emprestimo1.registrar_emprestimo()
emprestimo1.registrardevolucao()
emprestimo1.registrardevolucao()
emprestimo1.registrardevolucao()
emprestimo1.registrardevolucao()
emprestimo1.registrardevolucao()
print(lista_livros.consultarlivro(3))