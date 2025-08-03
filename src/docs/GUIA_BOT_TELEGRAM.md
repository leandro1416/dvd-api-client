# 🤖 Guia Completo do Bot do Telegram

## 📋 Pré-requisitos

1. **Python 3.7+** instalado
2. **Dependências** instaladas:
   ```bash
   pip install -r requirements.txt
   ```

## 🔧 Configuração do Bot

### 1. Criar o Bot no Telegram

1. **Acesse o BotFather:**
   - Abra o Telegram
   - Procure por `@BotFather`
   - Clique em "Start"

2. **Crie um novo bot:**
   ```
   /newbot
   ```

3. **Configure o bot:**
   - Digite um nome para o bot (ex: "DVD API Bot")
   - Digite um username (ex: "dvd_api_bot")
   - O BotFather retornará um token como:
   ```
   1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
   ```

4. **Copie o token** e guarde-o

### 2. Configurar o Token

1. **Edite o arquivo `config.py`:**
   ```python
   # Configurações do bot Telegram
   TELEGRAM_TOKEN = "SEU_TOKEN_AQUI"  # Substitua pelo token real
   TELEGRAM_CHAT_ID = ""  # Opcional: para notificações
   ```

2. **Substitua `SEU_TOKEN_AQUI`** pelo token que você recebeu do BotFather

### 3. Configurações Opcionais

No arquivo `config.py`, você pode configurar:

```python
# Configurações do bot Telegram
TELEGRAM_TOKEN = "1234567890:ABCdefGHIjklMNOpqrsTUVwxyz"
TELEGRAM_CHAT_ID = "123456789"  # Seu chat ID para notificações

# Configurações da API
API_BASE_URL = "http://127.0.0.1:8002/api"
API_TIMEOUT = 30
```

## 🚀 Como Executar

### Método 1: Usando main.py (Recomendado)
```bash
python3 main.py bot
```

### Método 2: Execução Direta
```bash
python3 src/scripts/telegram_bot.py
```

### Método 3: Com Configurações Específicas
```bash
# Edite config.py primeiro, depois execute:
python3 src/scripts/telegram_bot.py
```

## 📱 Como Usar o Bot

### 1. Iniciar o Bot
- Abra o Telegram
- Procure pelo seu bot (username que você definiu)
- Clique em "Start" ou digite `/start`

### 2. Comandos Disponíveis

#### `/start` - Inicia o bot
Mostra a mensagem de boas-vindas e menu principal

#### `/status` - Verifica status da API
Verifica se a API DVD está online

#### `/search` - Inicia busca
Abre o menu de tipos de busca

#### `/help` - Ajuda
Mostra informações de ajuda

### 3. Tipos de Busca

#### 🌐 Por Domínio
Busca todas as credenciais de um domínio
```
Exemplo: claro.com.br
```

#### 🔑 Por Senha
Busca credenciais que usam uma senha específica
```
Exemplo: 123456
```

#### 👤 Por Usuário
Busca todas as credenciais de um usuário
```
Exemplo: admin
```

#### 🔗 Por URL
Busca credenciais para uma URL específica
```
Exemplo: https://exemplo.com/login
```

#### 🗺️ Mapear Rotas
Lista todas as URLs de um domínio
```
Exemplo: exemplo.com.br
```

## 🔍 Exemplo de Uso

1. **Inicie o bot:**
   ```
   /start
   ```

2. **Clique em "🔍 Buscar"** ou digite `/search`

3. **Escolha o tipo de busca:**
   - Clique em "🌐 Por Domínio"

4. **Digite o termo:**
   ```
   claro.com.br
   ```

5. **Veja os resultados!**

## ⚙️ Configurações Avançadas

### 1. Personalizar Mensagens

Edite o arquivo `src/scripts/telegram_bot.py` para personalizar:

- Mensagens de boas-vindas
- Textos de ajuda
- Formatação dos resultados

### 2. Adicionar Novos Comandos

Para adicionar novos comandos:

1. **Crie a função:**
   ```python
   async def novo_comando(update: Update, context: ContextTypes.DEFAULT_TYPE):
       await update.message.reply_text("Sua mensagem aqui")
   ```

2. **Registre o handler:**
   ```python
   application.add_handler(CommandHandler("comando", novo_comando))
   ```

### 3. Configurar Logs

Para ativar logs detalhados:

```python
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG  # Mude para DEBUG
)
```

## 🐛 Troubleshooting

### Problema: "Token do Telegram não configurado"
**Solução:** Configure o `TELEGRAM_TOKEN` no arquivo `config.py`

### Problema: "ModuleNotFoundError: No module named 'telegram'"
**Solução:** Instale as dependências:
```bash
pip install python-telegram-bot==20.7
```

### Problema: "Bot não responde"
**Solução:**
1. Verifique se o token está correto
2. Verifique se o bot está rodando
3. Verifique se a API está online

### Problema: "Erro de conexão"
**Solução:**
1. Verifique se a API está rodando
2. Verifique a URL no `config.py`
3. Verifique a conectividade de rede

## 🔒 Segurança

### 1. Proteger o Token
- Nunca compartilhe o token do bot
- Não commite o token no Git
- Use variáveis de ambiente em produção

### 2. Limitar Acesso
Para limitar o acesso ao bot:

```python
# Lista de usuários autorizados
AUTHORIZED_USERS = [123456789, 987654321]

async def check_auth(update: Update):
    user_id = update.effective_user.id
    if user_id not in AUTHORIZED_USERS:
        await update.message.reply_text("❌ Acesso negado!")
        return False
    return True
```

### 3. Rate Limiting
Para evitar spam:

```python
from collections import defaultdict
import time

user_requests = defaultdict(list)

def check_rate_limit(user_id, limit=10, window=60):
    now = time.time()
    user_requests[user_id] = [req for req in user_requests[user_id] if now - req < window]
    
    if len(user_requests[user_id]) >= limit:
        return False
    
    user_requests[user_id].append(now)
    return True
```

## 📊 Monitoramento

### 1. Logs de Atividade
O bot gera logs automáticos:
```
2024-01-15 10:30:15 - INFO - Bot iniciado!
2024-01-15 10:30:20 - INFO - Usuário 123456789 iniciou busca
```

### 2. Estatísticas
Para adicionar estatísticas:

```python
# Contadores
stats = {
    'total_searches': 0,
    'successful_searches': 0,
    'failed_searches': 0
}

async def log_search(success=True):
    stats['total_searches'] += 1
    if success:
        stats['successful_searches'] += 1
    else:
        stats['failed_searches'] += 1
```

## 🚀 Deploy em Produção

### 1. Usando systemd (Linux)
Crie `/etc/systemd/system/dvd-bot.service`:

```ini
[Unit]
Description=DVD API Telegram Bot
After=network.target

[Service]
Type=simple
User=seu_usuario
WorkingDirectory=/caminho/para/projeto
ExecStart=/usr/bin/python3 main.py bot
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

### 2. Usando Docker
Crie `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "main.py", "bot"]
```

### 3. Usando PM2 (Node.js)
```bash
npm install -g pm2
pm2 start "python3 main.py bot" --name "dvd-bot"
pm2 save
pm2 startup
```

## 📞 Suporte

Para problemas ou dúvidas:

1. **Verifique os logs** do bot
2. **Teste a API** separadamente
3. **Verifique a configuração** no `config.py`
4. **Consulte a documentação** da API DVD

## 🎯 Próximos Passos

1. **Configure o token** no `config.py`
2. **Teste o bot** com `/start`
3. **Faça uma busca** de teste
4. **Monitore os logs** para problemas
5. **Personalize** conforme necessário

---

**🎉 Seu bot está pronto para uso!** 