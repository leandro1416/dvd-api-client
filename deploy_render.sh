#!/bin/bash

# 🚀 Script de Deploy Automático no Render.com
# Este script automatiza todo o processo de deploy

echo "🚀 Iniciando deploy automático no Render.com..."

# Verificar se o GitHub CLI está logado
if ! gh auth status > /dev/null 2>&1; then
    echo "❌ GitHub CLI não está logado. Execute: gh auth login"
    exit 1
fi

# Verificar se o Render CLI está logado
if ! render whoami > /dev/null 2>&1; then
    echo "❌ Render CLI não está logado. Execute: render login"
    exit 1
fi

echo "✅ GitHub e Render CLIs logados"

# Verificar se o repositório existe
if ! gh repo view leandro1416/dvd-api-client > /dev/null 2>&1; then
    echo "📦 Criando repositório no GitHub..."
    gh repo create dvd-api-client --public --description "DVD API Client - Web Interface" --source=. --remote=origin --push
else
    echo "✅ Repositório já existe no GitHub"
fi

# Fazer push das últimas mudanças
echo "📤 Fazendo push das mudanças..."
git add .
git commit -m "🚀 Deploy update - $(date)" || true
git push origin main

echo ""
echo "🎯 Próximos passos:"
echo "1. Acesse: https://dashboard.render.com"
echo "2. Clique em 'New +' → 'Web Service'"
echo "3. Conecte GitHub (se ainda não conectou)"
echo "4. Selecione o repositório: leandro1416/dvd-api-client"
echo "5. Configure:"
echo "   - Name: dvd-api-client"
echo "   - Environment: Python"
echo "   - Build Command: pip install -r requirements.txt"
echo "   - Start Command: python3 main.py web"
echo "   - Health Check Path: /api/status"
echo "6. Clique em 'Create Web Service'"
echo ""
echo "📖 Para instruções completas, veja: INSTRUCOES_DEPLOY.md"

echo ""
echo "🔗 Repositório GitHub: https://github.com/leandro1416/dvd-api-client"
echo "🌐 Render Dashboard: https://dashboard.render.com" 