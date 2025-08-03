# 🚀 Deploy no Render.com - Instruções Completas

## 📋 Pré-requisitos

1. **Conta no GitHub** (gratuita)
2. **Conta no Render.com** (gratuita)
3. **Projeto configurado** ✅ (já está pronto!)

## 🔧 Arquivos de Configuração Criados

✅ `render.yaml` - Configuração do Render.com
✅ `requirements.txt` - Dependências Python
✅ `Procfile` - Para Heroku (backup)
✅ `.gitignore` - Arquivos ignorados
✅ `DEPLOY_RENDER.md` - Guia detalhado

## 🚀 Passo a Passo Completo

### **1. Criar Repositório no GitHub**

1. **Acesse:** https://github.com
2. **Faça login** na sua conta
3. **Clique em "New"** (botão verde)
4. **Configure o repositório:**
   - **Repository name:** `dvd-api-client`
   - **Description:** `DVD API Client - Web Interface`
   - **Visibility:** Public ou Private (sua escolha)
   - **NÃO marque** "Add a README file"
   - **NÃO marque** "Add .gitignore"
   - **NÃO marque** "Choose a license"
5. **Clique em "Create repository"**

### **2. Conectar o Projeto ao GitHub**

Execute estes comandos no terminal:

```bash
# Adicionar o repositório remoto (SUBSTITUA SEU_USUARIO)
git remote add origin https://github.com/SEU_USUARIO/dvd-api-client.git

# Fazer push do código
git branch -M main
git push -u origin main
```

### **3. Deploy no Render.com**

1. **Acesse:** https://render.com
2. **Clique em "Sign Up"** (use GitHub para login)
3. **Clique em "New +"** → **"Web Service"**
4. **Conecte GitHub** (se ainda não conectou)
5. **Selecione o repositório:** `dvd-api-client`
6. **Configure o serviço:**

#### **Configurações Básicas:**
- **Name:** `dvd-api-client`
- **Environment:** `Python`
- **Region:** Escolha a mais próxima (ex: US East)
- **Branch:** `main`

#### **Configurações de Build:**
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `python3 main.py web`

#### **Configurações Avançadas:**
- **Health Check Path:** `/api/status`
- **Auto-Deploy:** ✅ Ativado

### **4. Variáveis de Ambiente (Opcional)**

Se quiser configurar manualmente, adicione estas variáveis:

```
PYTHON_VERSION=3.13.3
API_KEY=7cd663fefd95cb7b434c1c5ec57c4e00c5d8ca2d68163bfb095c77488c14dbc8
API_BASE_URL=https://sum.natsec.bot/api
TELEGRAM_TOKEN=8369793525:AAHjbxS_CD1dpR5D577Yeu1ld1KlndBHihI
```

### **5. Finalizar Deploy**

1. **Clique em "Create Web Service"**
2. **Aguarde o build** (2-5 minutos)
3. **Verifique os logs** se houver erro
4. **Acesse a URL** fornecida pelo Render

## 🎯 URLs Esperadas

- **URL do Render:** `https://dvd-api-client.onrender.com`
- **URL alternativa:** `https://seu-app-name.onrender.com`

## ✅ Verificação do Deploy

Após o deploy, teste:

1. **Status da API:** `https://sua-url.onrender.com/api/status`
2. **Interface Web:** `https://sua-url.onrender.com/`
3. **Busca de teste:** Use "claro.com.br" para testar

## 🔧 Troubleshooting

### **Se o deploy falhar:**

1. **Verifique os logs** no Render
2. **Confirme** que todos os arquivos estão no GitHub
3. **Teste localmente** primeiro: `python3 main.py web`
4. **Verifique** se o `requirements.txt` está correto

### **Se a API não responder:**

1. **Verifique** se a URL da API está correta
2. **Teste** a API externa diretamente
3. **Confirme** as variáveis de ambiente

## 🎉 Sucesso!

Após o deploy bem-sucedido, você terá:

✅ **URL pública** acessível de qualquer lugar
✅ **Interface web** moderna e responsiva
✅ **API funcional** conectada ao banco de dados
✅ **Deploy automático** quando atualizar o GitHub

## 📞 Suporte

Se precisar de ajuda:
1. **Verifique os logs** no Render
2. **Teste localmente** primeiro
3. **Confirme** todas as configurações 