# 🚀 Deploy no Render.com

## 📋 Pré-requisitos

1. **Conta no GitHub** com o código do projeto
2. **Conta no Render.com** (gratuita)
3. **Projeto configurado** com os arquivos necessários

## 🔧 Arquivos de Configuração

O projeto já está configurado com:
- ✅ `render.yaml` - Configuração do Render
- ✅ `requirements.txt` - Dependências Python
- ✅ `main.py` - Arquivo principal
- ✅ `Procfile` - Para Heroku (backup)

## 🚀 Passo a Passo

### 1. **Acesse o Render.com**
```
https://render.com
```

### 2. **Crie uma conta gratuita**
- Clique em "Sign Up"
- Use GitHub para login

### 3. **Crie um novo Web Service**
- Clique em "New +"
- Selecione "Web Service"
- Conecte seu GitHub

### 4. **Configure o Repositório**
- **Repository:** Selecione seu repositório
- **Name:** `dvd-api-client`
- **Environment:** `Python`
- **Region:** Escolha a mais próxima

### 5. **Configurações de Build**
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `python3 main.py web`

### 6. **Variáveis de Ambiente**
Adicione estas variáveis no painel do Render:

```
API_KEY=7cd663fefd95cb7b434c1c5ec57c4e00c5d8ca2d68163bfb095c77488c14dbc8
API_BASE_URL=https://sum.natsec.bot/api
TELEGRAM_TOKEN=8369793525:AAHjbxS_CD1dpR5D577Yeu1ld1KlndBHihI
PYTHON_VERSION=3.13.3
```

### 7. **Deploy**
- Clique em "Create Web Service"
- Aguarde o build (2-5 minutos)
- URL será gerada automaticamente

## 🌐 URLs

Após o deploy, você terá:
- **URL Principal:** `https://dvd-api-client.onrender.com`
- **Health Check:** `https://dvd-api-client.onrender.com/api/status`

## 🔍 Verificação

1. **Acesse a URL** do seu app
2. **Teste a busca** com "claro.com.br"
3. **Verifique os logs** no painel do Render

## 📊 Monitoramento

- **Logs:** Disponível no painel do Render
- **Métricas:** Uptime e performance
- **Deploy:** Automático ao fazer push no GitHub

## 🛠️ Troubleshooting

### Se o deploy falhar:
1. **Verifique os logs** no painel
2. **Confirme as variáveis** de ambiente
3. **Teste localmente** primeiro
4. **Verifique o requirements.txt**

### Se o app não responder:
1. **Verifique o health check**
2. **Aguarde 2-3 minutos** após deploy
3. **Verifique as variáveis** de ambiente

## 📞 Suporte

- **Render Docs:** https://render.com/docs
- **Status:** https://status.render.com
- **Community:** https://community.render.com 