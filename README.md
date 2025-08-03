# DVD API Client

Cliente Python para conectar com a API DVD, permitindo buscar credenciais por domínio, senha, usuário, URL e mapear rotas de sites.

## 🚀 Funcionalidades

- ✅ Interface gráfica com tkinter
- ✅ Interface web com Flask
- ✅ Cliente de linha de comando
- ✅ Bot do Telegram
- ✅ Teste de conexão com a API
- ✅ Busca por domínio
- ✅ Busca por senha
- ✅ Busca por usuário
- ✅ Busca por URL
- ✅ Mapeamento de rotas de domínio
- ✅ Paginação automática
- ✅ Tratamento de erros
- ✅ Timeout configurável

## 📁 Estrutura do Projeto

```
Claud DVD/
├── main.py                 # Arquivo principal para execução
├── config.py              # Configurações centralizadas
├── requirements.txt        # Dependências do projeto
├── setup.py              # Script de instalação
├── README.md             # Este arquivo
├── .gitignore            # Arquivos ignorados pelo Git
└── src/                  # Código fonte organizado
    ├── __init__.py
    ├── clients/          # Clientes da API
    │   ├── __init__.py
    │   ├── dvd_api_client.py
    │   ├── simple_client.py
    │   └── cliente_atualizado.py
    ├── web/              # Interface web
    │   ├── __init__.py
    │   ├── app_web.py
    │   ├── app_web_optimized.py
    │   └── templates/
    │       ├── index.html
    │       └── index_optimized.html
    ├── scripts/          # Scripts utilitários
    │   ├── __init__.py
    │   ├── buscar_claro.py
    │   ├── telegram_bot.py
    │   └── ativar.sh
    ├── tests/            # Testes
    │   ├── __init__.py
    │   ├── testar_bot.py
    │   ├── testar_enderecos.py
    │   ├── teste_conexao.py
    │   └── exemplo_uso.py
    ├── docs/             # Documentação
    │   ├── __init__.py
    │   ├── GUIA_BOT_TELEGRAM.md
    │   └── INSTRUCOES_RAPIDAS.md
    └── data/             # Dados
        ├── __init__.py
        └── resultados_claro_20250802_160625.json
```

## 🛠️ Instalação

1. Clone ou baixe os arquivos do projeto
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

## 🚀 Como Usar

### Método 1: Arquivo Principal (Recomendado)

Use o arquivo `main.py` para executar diferentes componentes:

```bash
# Interface gráfica
python main.py gui

# Interface web
python main.py web --host 127.0.0.1 --port 5000

# Bot do Telegram
python main.py bot

# Testes
python main.py test
```

### Método 2: Execução Direta

#### 1. Interface Gráfica (Recomendado)

```bash
python src/clients/dvd_api_client.py
```

**Como usar:**
1. Insira sua API Key no campo "API Key"
2. Clique em "Testar Conexão" para verificar se está funcionando
3. Selecione o tipo de busca (domínio, senha, usuário, URL ou rotas)
4. Digite o termo de busca
5. Configure a página e itens por página (opcional)
6. Clique em "Buscar"

#### 2. Interface Web

```bash
python src/web/app_web_optimized.py
```

Acesse: http://127.0.0.1:5000

#### 3. Linha de Comando

```bash
python src/clients/simple_client.py <comando> <API_KEY> [parâmetros]
```

**Comandos disponíveis:**

##### Testar conexão:
```bash
python src/clients/simple_client.py status SUA_API_KEY
```

##### Buscar por domínio:
```bash
python src/clients/simple_client.py domain SUA_API_KEY exemplo.com.br
```

##### Buscar por senha:
```bash
python src/clients/simple_client.py password SUA_API_KEY 123456
```

##### Buscar por usuário:
```bash
python src/clients/simple_client.py user SUA_API_KEY admin@empresa.com
```

##### Buscar por URL:
```bash
python src/clients/simple_client.py url SUA_API_KEY "https://exemplo.com.br/login"
```

##### Mapear rotas de domínio:
```bash
python src/clients/simple_client.py routes SUA_API_KEY exemplo.com.br
```

## ⚙️ Configuração

### Arquivo de Configuração

Edite o arquivo `config.py` para personalizar as configurações:

```python
# Configurações da API
API_BASE_URL = "http://127.0.0.1:8002/api"
API_TIMEOUT = 30
API_MAX_PAGE_SIZE = 5000

# Configurações do bot Telegram
TELEGRAM_TOKEN = "seu_token_aqui"
TELEGRAM_CHAT_ID = "seu_chat_id_aqui"
```

## 📚 Documentação

- **Guia do Bot Telegram:** `src/docs/GUIA_BOT_TELEGRAM.md`
- **Instruções Rápidas:** `src/docs/INSTRUCOES_RAPIDAS.md`

## 🔧 Endpoints da API

### 1. Status da API
- **URL:** `GET /status`
- **Descrição:** Verifica se a API está funcionando
- **Resposta:** Status, usuário, limites e consultas restantes

### 2. Buscar por Domínio
- **URL:** `GET /dominio/{dominio_nome}`
- **Parâmetros:** `page`, `page_size`
- **Descrição:** Retorna credenciais de um domínio específico

### 3. Buscar por Senha
- **URL:** `GET /senha/{senha_valor}`
- **Parâmetros:** `page`, `page_size`
- **Descrição:** Encontra credenciais que usam uma senha específica

### 4. Buscar por Usuário
- **URL:** `GET /usuario/{usuario_valor}`
- **Parâmetros:** `page`, `page_size`
- **Descrição:** Retorna credenciais de um usuário específico

### 5. Buscar por URL
- **URL:** `GET /url`
- **Parâmetros:** `url`, `page`, `page_size`
- **Descrição:** Encontra credenciais para uma URL específica

### 6. Mapear Rotas
- **URL:** `GET /mapear-site/{dominio}`
- **Parâmetros:** `page`, `page_size`
- **Descrição:** Lista todas as URLs de um domínio

## 🔒 Configuração da API

- **Base URL:** `http://127.0.0.1:8002/api`
- **Autenticação:** Header `Authorization: Api-Key SUA_API_KEY`
- **Timeout:** 30 segundos
- **Paginação:** Máximo 5000 itens por página

## ⚠️ Tratamento de Erros

### Códigos de Erro:
- **401:** API Key inválida ou não fornecida
- **404:** Recurso não encontrado
- **429:** Limite de requisições excedido

### Exemplos de Resposta de Erro:
```json
{
  "detail": "Invalid API key"
}
```

```json
{
  "error": "Not found"
}
```

```json
{
  "error": "Limite de requisições excedido"
}
```

## 💡 Exemplos de Uso

### Exemplo 1: Verificar Status
```python
from src.clients.dvd_api_client import DVDAPIClient

client = DVDAPIClient("SUA_API_KEY")
status = client.check_status()
print(f"Status: {status['status']}")
print(f"Consultas restantes: {status['consultas_restantes']}")
```

### Exemplo 2: Buscar Credenciais por Domínio
```python
result = client.search_by_domain("exemplo.com.br")
for cred in result['data']:
    print(f"URL: {cred['url']}")
    print(f"Usuário: {cred['username']}")
    print(f"Senha: {cred['password']}")
```

### Exemplo 3: Buscar Todas as Páginas
```python
def buscar_todas_credenciais(dominio, api_key):
    client = DVDAPIClient(api_key)
    todas_credenciais = []
    page = 1
    
    while True:
        result = client.search_by_domain(dominio, page, 500)
        if not result:
            break
            
        todas_credenciais.extend(result['data'])
        
        if page >= result['pages']:
            break
            
        page += 1
    
    return todas_credenciais
```

## 🔧 Características Técnicas

- **Codificação URL:** Caracteres especiais são automaticamente codificados
- **Case Sensitive:** Usernames e senhas são sensíveis a maiúsculas/minúsculas
- **Threading:** Interface gráfica usa threads para não travar
- **Timeout:** 30 segundos para evitar travamentos
- **Error Handling:** Tratamento robusto de erros de rede e API

## 🐛 Troubleshooting

### Problema: "Erro de conexão"
**Solução:** Verifique se a API está rodando em `http://127.0.0.1:8002`

### Problema: "Invalid API key"
**Solução:** Verifique se a API Key está correta

### Problema: "Limite de requisições excedido"
**Solução:** Aguarde um pouco antes de fazer novas requisições

### Problema: Interface não abre
**Solução:** Verifique se o tkinter está instalado:
```bash
python -c "import tkinter; print('tkinter OK')"
```

### Problema: Módulos não encontrados
**Solução:** Execute a partir da raiz do projeto ou use o `main.py`:
```bash
python main.py gui
```

## 🤝 Contribuição

Para contribuir com o projeto:
1. Faça um fork do repositório
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto é de uso livre para fins educacionais e de pesquisa.

## 🆘 Suporte

Para dúvidas ou problemas:
1. Verifique a documentação da API
2. Teste a conexão primeiro
3. Verifique os logs de erro
4. Consulte os exemplos de uso 