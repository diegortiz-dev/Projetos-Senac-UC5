from conexao import conectar_banco

def setup_database():
    """Configura o banco de dados criando as tabelas necessárias"""
    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()
        
        # Criar tabela de livros
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS livros (
                numero_isbn VARCHAR(20) PRIMARY KEY,
                titulo VARCHAR(255) NOT NULL,
                autor VARCHAR(255) NOT NULL,
                edicao VARCHAR(50),
                quantidade_exemplares INT DEFAULT 0,
                capa_path VARCHAR(500)
            )
        """)
        
        # Criar tabela de leitores
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS leitores (
                id INT PRIMARY KEY AUTO_INCREMENT,
                nome VARCHAR(255) NOT NULL,
                telefone VARCHAR(20)
            )
        """)
        
        # Criar tabela de empréstimos
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS emprestimos (
                id INT PRIMARY KEY AUTO_INCREMENT,
                leitor_id INT,
                livro_isbn VARCHAR(20),
                data_emprestimo DATE NOT NULL,
                data_devolucao DATE NULL,
                FOREIGN KEY (leitor_id) REFERENCES leitores(id) ON DELETE CASCADE,
                FOREIGN KEY (livro_isbn) REFERENCES livros(numero_isbn) ON DELETE CASCADE
            )
        """)
        
        # Verificar se a coluna capa_path existe, se não, adicionar
        try:
            cursor.execute("ALTER TABLE livros ADD COLUMN capa_path VARCHAR(500)")
        except:
            pass  # Coluna já existe
        
        # Criar índices
        try:
            cursor.execute("CREATE INDEX idx_emprestimos_leitor ON emprestimos(leitor_id)")
        except:
            pass
            
        try:
            cursor.execute("CREATE INDEX idx_emprestimos_livro ON emprestimos(livro_isbn)")
        except:
            pass
            
        try:
            cursor.execute("CREATE INDEX idx_emprestimos_devolucao ON emprestimos(data_devolucao)")
        except:
            pass
        
        conexao.commit()
        cursor.close()
        conexao.close()
        
        print("Banco de dados configurado com sucesso!")
        
    except Exception as e:
        print(f"Erro ao configurar banco de dados: {e}")

if __name__ == "__main__":
    setup_database()