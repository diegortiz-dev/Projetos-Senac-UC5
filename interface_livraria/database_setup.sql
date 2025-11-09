-- Script para criar/atualizar as tabelas do banco de dados da livraria

-- Criar tabela de livros (se não existir)
CREATE TABLE IF NOT EXISTS livros (
    numero_isbn VARCHAR(20) PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    autor VARCHAR(255) NOT NULL,
    edicao VARCHAR(50),
    quantidade_exemplares INT DEFAULT 0,
    capa_path VARCHAR(500)
);

-- Criar tabela de leitores (se não existir)
CREATE TABLE IF NOT EXISTS leitores (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    telefone VARCHAR(20)
);

-- Criar tabela de empréstimos (se não existir)
CREATE TABLE IF NOT EXISTS emprestimos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    leitor_id INT,
    livro_isbn VARCHAR(20),
    data_emprestimo DATE NOT NULL,
    data_devolucao DATE NULL,
    FOREIGN KEY (leitor_id) REFERENCES leitores(id) ON DELETE CASCADE,
    FOREIGN KEY (livro_isbn) REFERENCES livros(numero_isbn) ON DELETE CASCADE
);

-- Adicionar coluna capa_path se ela não existir na tabela livros
ALTER TABLE livros ADD COLUMN IF NOT EXISTS capa_path VARCHAR(500);

-- Índices para melhor performance
CREATE INDEX IF NOT EXISTS idx_emprestimos_leitor ON emprestimos(leitor_id);
CREATE INDEX IF NOT EXISTS idx_emprestimos_livro ON emprestimos(livro_isbn);
CREATE INDEX IF NOT EXISTS idx_emprestimos_devolucao ON emprestimos(data_devolucao);