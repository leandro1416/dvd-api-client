# 📊 Logs Detalhados - Bot do Telegram

## ✅ Logs Implementados

O bot agora possui **logs detalhados** para facilitar a correção de problemas e monitoramento.

## 📁 Arquivos de Log

### 1. `bot_telegram.log`
- **Arquivo:** Log principal do bot
- **Conteúdo:** Todas as atividades do bot
- **Nível:** DEBUG (máximo detalhamento)

### 2. `teste_bot.log`
- **Arquivo:** Log dos testes
- **Conteúdo:** Resultados dos testes de configuração
- **Nível:** DEBUG

## 🔍 Tipos de Logs

### 📱 Logs do Bot
```
2025-08-02 22:30:15,123 - __main__ - INFO - 🤖 INICIANDO BOT DO TELEGRAM
2025-08-02 22:30:15,124 - __main__ - INFO - 📱 Token: 8369793525...
2025-08-02 22:30:15,125 - __main__ - INFO - 🔗 API Base URL: http://127.0.0.1:8002/api
2025-08-02 22:30:15,126 - __main__ - INFO - ⏱️ Timeout: 30s
2025-08-02 22:30:15,127 - __main__ - INFO - 📅 Data/Hora: 2025-08-02 22:30:15
```

### 👤 Logs de Usuários
```
2025-08-02 22:30:20,123 - __main__ - INFO - 👤 Usuário 123456789 (João) iniciou o bot
2025-08-02 22:30:25,456 - __main__ - INFO - 👤 Usuário 123456789 clicou em botão: search
2025-08-02 22:30:30,789 - __main__ - INFO - 👤 Usuário 123456789 escolheu tipo: domain
2025-08-02 22:30:35,012 - __main__ - INFO - 🔍 Usuário 123456789 iniciando busca: domain = 'claro.com.br'
```

### 🔗 Logs de API
```
2025-08-02 22:30:35,123 - __main__ - INFO - 🔍 Verificando status da API...
2025-08-02 22:30:35,124 - __main__ - DEBUG - 📡 Fazendo requisição para: http://127.0.0.1:8002/api/status
2025-08-02 22:30:35,125 - __main__ - DEBUG - 📊 Resposta: Status 200
2025-08-02 22:30:35,126 - __main__ - INFO - ✅ API está online
```

### ❌ Logs de Erros
```
2025-08-02 22:30:35,127 - __main__ - ERROR - ❌ Erro de conexão: HTTPConnectionPool(host='127.0.0.1', port=8002): Max retries exceeded
2025-08-02 22:30:35,128 - __main__ - ERROR - 📋 Traceback: Traceback (most recent call last):
  File "telegram_bot.py", line 123, in check_status
    response = requests.get(url, headers=self.headers, timeout=API_TIMEOUT)
```

## 🎯 Informações Logadas

### ✅ Informações Básicas
- **Inicialização do bot**
- **Configurações carregadas**
- **Token do bot**
- **URL da API**
- **Timeout configurado**

### 👤 Atividades de Usuários
- **Usuários que iniciam o bot**
- **Comandos executados**
- **Botões clicados**
- **Termos de busca**
- **Tipos de busca escolhidos**

### 🔗 Comunicação com API
- **URLs das requisições**
- **Headers enviados**
- **Status das respostas**
- **Dados recebidos**
- **Erros de conexão**

### ❌ Tratamento de Erros
- **Erros de conexão**
- **Timeouts**
- **Erros de API**
- **Exceções inesperadas**
- **Tracebacks completos**

## 🔧 Como Usar os Logs

### 1. Verificar Logs em Tempo Real
```bash
# Acompanhar logs do bot
tail -f bot_telegram.log

# Acompanhar logs de teste
tail -f teste_bot.log
```

### 2. Buscar por Erros
```bash
# Buscar erros no log do bot
grep "ERROR" bot_telegram.log

# Buscar erros de conexão
grep "ConnectionError" bot_telegram.log
```

### 3. Buscar por Usuário
```bash
# Buscar atividades de um usuário específico
grep "Usuário 123456789" bot_telegram.log
```

### 4. Buscar por Comando
```bash
# Buscar comandos /start
grep "/start" bot_telegram.log

# Buscar buscas por domínio
grep "Buscando por domínio" bot_telegram.log
```

## 🐛 Troubleshooting com Logs

### Problema: Bot não responde
```bash
# Verificar se o bot está rodando
grep "Bot iniciado" bot_telegram.log

# Verificar erros de inicialização
grep "ERROR" bot_telegram.log | head -10
```

### Problema: API não funciona
```bash
# Verificar tentativas de conexão
grep "Fazendo requisição" bot_telegram.log

# Verificar erros de API
grep "API retornou erro" bot_telegram.log
```

### Problema: Usuário não consegue buscar
```bash
# Verificar se o usuário está sendo logado
grep "iniciando busca" bot_telegram.log

# Verificar erros durante busca
grep "Erro na busca" bot_telegram.log
```

## 📊 Exemplos de Logs

### ✅ Bot Funcionando Normalmente
```
2025-08-02 22:30:15,123 - __main__ - INFO - 🤖 INICIANDO BOT DO TELEGRAM
2025-08-02 22:30:15,124 - __main__ - INFO - ✅ Aplicação criada com sucesso
2025-08-02 22:30:15,125 - __main__ - INFO - ✅ Handlers registrados com sucesso
2025-08-02 22:30:15,126 - __main__ - INFO - ✅ Bot iniciado! Envie /start para começar.
2025-08-02 22:30:20,123 - __main__ - INFO - 👤 Usuário 123456789 (João) iniciou o bot
2025-08-02 22:30:20,124 - __main__ - INFO - ✅ Mensagem de boas-vindas enviada para usuário 123456789
```

### ❌ Bot com Problemas
```
2025-08-02 22:30:15,123 - __main__ - INFO - 🤖 INICIANDO BOT DO TELEGRAM
2025-08-02 22:30:15,124 - __main__ - ERROR - ❌ Erro fatal ao iniciar bot: Invalid token
2025-08-02 22:30:15,125 - __main__ - ERROR - 📋 Traceback: Traceback (most recent call last):
  File "telegram_bot.py", line 456, in main
    application = Application.builder().token(TELEGRAM_TOKEN).build()
```

### 🔗 API Offline
```
2025-08-02 22:30:35,123 - __main__ - INFO - 🔍 Verificando status da API...
2025-08-02 22:30:35,124 - __main__ - DEBUG - 📡 Fazendo requisição para: http://127.0.0.1:8002/api/status
2025-08-02 22:30:35,125 - __main__ - ERROR - ❌ Erro de conexão: HTTPConnectionPool(host='127.0.0.1', port=8002): Max retries exceeded
2025-08-02 22:30:35,126 - __main__ - WARNING - ⚠️ API offline para usuário 123456789: Erro de conexão: HTTPConnectionPool...
```

## 🎯 Benefícios dos Logs

### ✅ Para Desenvolvimento
- **Identificar problemas rapidamente**
- **Rastrear comportamento de usuários**
- **Monitorar performance da API**
- **Debugar erros específicos**

### ✅ Para Produção
- **Monitorar uso do bot**
- **Detectar problemas antes que afetem usuários**
- **Analisar padrões de uso**
- **Manter histórico de atividades**

### ✅ Para Suporte
- **Ajudar usuários com problemas**
- **Identificar causas de erros**
- **Fornecer informações detalhadas**
- **Rastrear problemas específicos**

## 🔧 Configuração de Logs

### Níveis de Log
- **DEBUG:** Máximo detalhamento (desenvolvimento)
- **INFO:** Informações gerais (produção)
- **WARNING:** Avisos (problemas não críticos)
- **ERROR:** Erros (problemas críticos)

### Arquivos de Log
- **bot_telegram.log:** Log principal do bot
- **teste_bot.log:** Log dos testes
- **Console:** Logs também aparecem no terminal

### Rotação de Logs
Para evitar arquivos muito grandes, você pode configurar rotação:
```python
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler('bot_telegram.log', maxBytes=1024*1024, backupCount=5)
```

## 📊 Monitoramento

### Comandos Úteis
```bash
# Ver tamanho dos logs
ls -lh *.log

# Ver últimas linhas
tail -20 bot_telegram.log

# Buscar erros recentes
grep "$(date +%Y-%m-%d)" bot_telegram.log | grep ERROR

# Contar usuários únicos
grep "Usuário" bot_telegram.log | cut -d' ' -f8 | sort | uniq | wc -l
```

---

**🎉 Agora você tem logs detalhados para monitorar e corrigir problemas facilmente!** 