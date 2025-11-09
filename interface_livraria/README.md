# Sistema de Livraria - TELivraria

Sistema de gerenciamento de livraria com interface gráfica desenvolvido em Python usando CustomTkinter.

## Funcionalidades

- ✅ Cadastro, edição e exclusão de livros
- ✅ Cadastro, edição e exclusão de leitores  
- ✅ Registro e controle de empréstimos
- ✅ Upload de capas de livros
- ✅ Pesquisa de livros, leitores e empréstimos
- ✅ Integração completa com banco de dados MySQL

## Configuração do Banco de Dados

### 1. Criar arquivo .env
Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```
DB_HOST=localhost
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_NAME=nome_do_banco
```

### 2. Configurar o banco de dados
Execute o script de configuração para criar as tabelas:

```bash
python setup_database.py
```

Ou execute manualmente o arquivo `database_setup.sql` no seu MySQL.

### 3. Estrutura das Tabelas

#### Tabela `livros`
- `numero_isbn` (VARCHAR(20)) - Chave primária
- `titulo` (VARCHAR(255)) - Título do livro
- `autor` (VARCHAR(255)) - Nome do autor
- `edicao` (VARCHAR(50)) - Edição do livro
- `quantidade_exemplares` (INT) - Quantidade disponível
- `capa_path` (VARCHAR(500)) - Caminho da imagem da capa

#### Tabela `leitores`
- `id` (INT) - Chave primária auto incremento
- `nome` (VARCHAR(255)) - Nome do leitor
- `telefone` (VARCHAR(20)) - Telefone do leitor

#### Tabela `emprestimos`
- `id` (INT) - Chave primária auto incremento
- `leitor_id` (INT) - ID do leitor (FK)
- `livro_isbn` (VARCHAR(20)) - ISBN do livro (FK)
- `data_emprestimo` (DATE) - Data do empréstimo
- `data_devolucao` (DATE) - Data da devolução (NULL se não devolvido)

## Dependências

```bash
pip install customtkinter
pip install pillow
pip install mysql-connector-python
pip install python-dotenv
```

## Como usar

1. Configure o banco de dados conforme instruções acima
2. Execute o arquivo principal:
```bash
python app.py
```

## Funcionalidades Implementadas

### Livros
- Cadastro com upload de capa
- Edição de informações
- Exclusão com confirmação
- Pesquisa por título, autor ou ISBN
- Controle de quantidade de exemplares

### Leitores
- Cadastro com ID automático
- Edição de informações
- Exclusão com confirmação
- Pesquisa por nome ou ID

### Empréstimos
- Registro de empréstimo com validação
- Controle automático de quantidade
- Devolução com atualização de estoque
- Visualização de empréstimos ativos
- Pesquisa por leitor ou livro

## Correções Implementadas

✅ **Conexão de empréstimos ao banco de dados**: Agora todos os empréstimos são salvos e carregados do banco

✅ **Campo capa_path para livros**: Adicionado suporte completo para salvar e carregar capas dos livros

✅ **Correções de pequenos erros**: 
- Limpeza correta das listas ao carregar do banco
- Inicialização adequada da aplicação
- Geração de IDs baseada no banco de dados
- Atualização automática de quantidades nos empréstimos e devoluções

## Estrutura de Arquivos

```
interface_livraria/
├── app.py              # Arquivo principal da aplicação
├── main.py             # Classes do modelo de dados
├── conexao.py          # Configuração da conexão com banco
├── setup_database.py   # Script de configuração do banco
├── database_setup.sql  # Script SQL das tabelas
├── .env               # Variáveis de ambiente (criar)
├── assets/            # Pasta com imagens da interface
└── README.md          # Este arquivo
```