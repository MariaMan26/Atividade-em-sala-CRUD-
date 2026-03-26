# 🎮 Inventário de Jogos — API REST

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-API-black)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey)
![SENAI](https://img.shields.io/badge/SENAI-CTTI-red)

> 📚 **Atividade de sala de aula** — SENAI CTTI  
> Implementação de uma API REST com operações CRUD utilizando Flask e SQLite.  

API REST desenvolvida com **Flask** e **SQLite** para gerenciamento de um inventário de jogos, com suporte a múltiplas plataformas por jogo via relacionamento N:N.

---

## 📌 Sobre o projeto

Esta aplicação implementa um CRUD completo seguindo padrões REST, permitindo:

- Cadastrar jogos com informações detalhadas
- Listar todos os jogos ou buscar por ID
- Atualizar dados de um jogo existente
- Remover jogos do inventário
- Associar múltiplas plataformas a cada jogo

> 💡 A aplicação possui uma **documentação visual** disponível na rota `/`, acessível pelo navegador após iniciar o servidor.

---

## 📁 Estrutura do projeto

```
.
├── app.py                  # Aplicação Flask com todas as rotas da API
├── init_db.py              # Script de criação do banco de dados e tabelas
├── seed_db.py              # Script de população inicial com dados de exemplo
├── inventario_jogos.db     # Banco de dados SQLite (gerado automaticamente)
├── requirements.txt        # Dependências do projeto
├── templates/
│   └── index.html          # Documentação visual da API
└── README.md
```

---

## 🗄️ Modelo de dados

O banco possui 3 tabelas com relacionamento N:N entre jogos e plataformas:

```
jogos                    jogo_plataforma         plataformas
─────────────────        ───────────────         ───────────────
id (PK)                  jogo_id (FK)            id (PK)
nome                     plataforma_id (FK)      nome (UNIQUE)
ano_lancamento
descricao
desenvolvedora
genero
preco
quantidade
```

Um jogo pode estar disponível em várias plataformas, e uma plataforma pode ter vários jogos.

---

## 🚀 Tecnologias utilizadas

- **Python 3.x**
- **Flask** — framework web para a API
- **SQLite** — banco de dados relacional embutido

---

## ⚙️ Como executar o projeto

### 1. Clone o repositório

```cmd
git clone https://github.com/MariaMan26/Atividade-em-sala-CRUD-.git
cd Atividade-em-sala-CRUD-
```

### 2. Crie e ative o ambiente virtual

```cmd
python -m venv venv
venv\Scripts\activate
```

> Linux/Mac: `source venv/bin/activate`

### 3. Instale as dependências

```cmd
pip install -r requirements.txt
```

### 4. Crie o banco de dados

```cmd
python init_db.py
```

### 5. Popule com dados iniciais (opcional)

```cmd
python seed_db.py
```

Insere 4 jogos de exemplo: Bloodborne, Horizon Forbidden West, Ghost of Tsushima e FIFA 23.

### 6. Inicie o servidor

```cmd
python app.py
```

Acesse `http://localhost:5000` no navegador para ver a documentação visual da API.

---

## 📡 Endpoints

| Método | Rota | Descrição | Status |
|--------|------|-----------|--------|
| GET | /jogos | Lista todos os jogos | 200 |
| GET | /jogos/\<id\> | Busca um jogo por ID | 200 / 404 |
| POST | /jogos | Insere um novo jogo | 201 / 400 |
| PUT | /jogos/\<id\> | Atualiza um jogo existente | 204 / 404 |
| DELETE | /jogos/\<id\> | Remove um jogo | 204 / 404 |

---

## 📋 Campos do jogo

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|:-----------:|-----------|
| nome | string | ✅ | Nome do jogo |
| preco | number | ✅ | Preço em reais |
| quantidade | integer | ✅ | Quantidade em estoque |
| ano_lancamento | integer | ❌ | Ano de lançamento |
| descricao | string | ❌ | Descrição do jogo |
| desenvolvedora | string | ❌ | Empresa desenvolvedora |
| genero | string | ❌ | Gênero do jogo |
| plataformas | array | ❌ | Lista de nomes: `["PS5", "PC"]` |

---

## 🧪 Roteiro de testes com curl

> ⚠️ Mantenha o servidor rodando em um terminal e execute os comandos em outro.
> Os exemplos abaixo usam a sintaxe do **Windows CMD**.

---

### 1. Listar todos os jogos

```cmd
curl http://localhost:5000/jogos
```

**Resposta esperada (200):**
```json
[
  {
    "id": 1,
    "nome": "Bloodborne",
    "ano_lancamento": 2015,
    "desenvolvedora": "FromSoftware",
    "genero": "RPG",
    "preco": 99.9,
    "quantidade": 5,
    "plataformas": ["PS4", "PS5"]
  },
  ...
]
```

---

### 2. Buscar jogo por ID

```cmd
curl http://localhost:5000/jogos/1
```

**Resposta esperada (200):**
```json
{
  "id": 1,
  "nome": "Bloodborne",
  "ano_lancamento": 2015,
  "descricao": "RPG de ação com ambientação gótica e sombria...",
  "desenvolvedora": "FromSoftware",
  "genero": "RPG",
  "preco": 99.9,
  "quantidade": 5,
  "plataformas": ["PS4", "PS5"]
}
```

---

### 3. Buscar ID inexistente

```cmd
curl http://localhost:5000/jogos/999
```

**Resposta esperada (404):**
```json
{
  "erro": "Jogo não encontrado"
}
```

---

### 4. Inserir novo jogo

**Opção A — inline (CMD):**
```cmd
curl -X POST http://localhost:5000/jogos -H "Content-Type: application/json" -d "{\"nome\": \"Elden Ring\", \"ano_lancamento\": 2022, \"descricao\": \"RPG de mundo aberto desafiador\", \"desenvolvedora\": \"FromSoftware\", \"genero\": \"RPG\", \"preco\": 249.90, \"quantidade\": 7, \"plataformas\": [\"PS5\", \"PC\", \"Xbox Series X\"]}"
```

**Opção B — via arquivo JSON (recomendado):**

Crie um arquivo `novo_jogo.json`:
```json
{
  "nome": "Elden Ring",
  "ano_lancamento": 2022,
  "descricao": "RPG de mundo aberto desafiador",
  "desenvolvedora": "FromSoftware",
  "genero": "RPG",
  "preco": 249.90,
  "quantidade": 7,
  "plataformas": ["PS5", "PC", "Xbox Series X"]
}
```

```cmd
curl -X POST http://localhost:5000/jogos -H "Content-Type: application/json" -d @novo_jogo.json
```

**Resposta esperada (201):**
```json
{
  "id": 5,
  "nome": "Elden Ring",
  "ano_lancamento": 2022,
  "descricao": "RPG de mundo aberto desafiador",
  "desenvolvedora": "FromSoftware",
  "genero": "RPG",
  "preco": 249.9,
  "quantidade": 7,
  "plataformas": ["PS5", "PC", "Xbox Series X"]
}
```

---

### 5. Atualizar jogo

Envia apenas os campos que deseja alterar. Os demais são mantidos.

**Opção A — inline (CMD):**
```cmd
curl -X PUT http://localhost:5000/jogos/5 -H "Content-Type: application/json" -d "{\"preco\": 199.90, \"quantidade\": 3}"
```

**Opção B — via arquivo JSON:**

Crie um arquivo `update.json`:
```json
{
  "preco": 199.90,
  "quantidade": 3
}
```

```cmd
curl -X PUT http://localhost:5000/jogos/5 -H "Content-Type: application/json" -d @update.json
```

**Resposta esperada:** `204 No Content` (sem body)

---

### 6. Confirmar atualização

```cmd
curl http://localhost:5000/jogos/5
```

**Resposta esperada (200):** jogo com `preco: 199.9` e `quantidade: 3`

---

### 7. Remover jogo

```cmd
curl -X DELETE http://localhost:5000/jogos/5
```

**Resposta esperada:** `204 No Content` (sem body)

---

### 8. Confirmar remoção

```cmd
curl http://localhost:5000/jogos/5
```

**Resposta esperada (404):**
```json
{
  "erro": "Jogo não encontrado"
}
```

---

## ⚠️ Códigos de status

| Código | Significado | Quando ocorre |
|--------|-------------|---------------|
| 200 | OK | GET bem-sucedido |
| 201 | Created | POST bem-sucedido |
| 204 | No Content | PUT ou DELETE bem-sucedido |
| 400 | Bad Request | Campo obrigatório ausente no POST |
| 404 | Not Found | ID não encontrado |
| 500 | Internal Server Error | Erro inesperado no servidor |

---

## 📌 Observações

- O banco de dados é criado automaticamente ao rodar `app.py` ou `init_db.py`
- Não é necessário instalar nenhum banco externo — SQLite é embutido no Python
- O campo `plataformas` aceita nomes livres — novas plataformas são criadas automaticamente se não existirem
- O PUT é não-destrutivo: campos não enviados mantêm seus valores originais
- Use `@arquivo.json` no curl para evitar problemas com aspas no CMD

---

## 👨‍💻 Autor

Caio Gomes de Oliveira
