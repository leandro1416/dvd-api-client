#!/bin/bash

# 🚀 Script de Deploy para Render.com
# Este script facilita o processo de deploy

echo "🚀 Iniciando processo de deploy para Render.com..."

# Verificar se o git está configurado
if ! git config --get user.name > /dev/null 2>&1; then
    echo "❌ Git não está configurado. Configure primeiro:"
    echo "git config --global user.name 'Seu Nome'"
    echo "git config --global user.email 'seu@email.com'"
    exit 1
fi

# Verificar se há mudanças para commitar
if [[ -n $(git status --porcelain) ]]; then
    echo "📝 Há mudanças não commitadas. Fazendo commit..."
    git add .
    git commit -m "🚀 Deploy update - $(date)"
fi

# Verificar se o remote está configurado
if ! git remote get-url origin > /dev/null 2>&1; then
    echo "❌ Remote 'origin' não configurado."
    echo "Configure com: git remote add origin https://github.com/SEU_USUARIO/dvd-api-client.git"
    exit 1
fi

# Fazer push
echo "📤 Fazendo push para GitHub..."
git push origin main

if [ $? -eq 0 ]; then
    echo "✅ Push realizado com sucesso!"
    echo ""
    echo "🎯 Próximos passos:"
    echo "1. Acesse: https://render.com"
    echo "2. Crie um novo Web Service"
    echo "3. Conecte seu GitHub"
    echo "4. Selecione o repositório: dvd-api-client"
    echo "5. Configure:"
    echo "   - Build Command: pip install -r requirements.txt"
    echo "   - Start Command: python3 main.py web"
    echo "6. Clique em 'Create Web Service'"
    echo ""
    echo "📖 Para instruções completas, veja: INSTRUCOES_DEPLOY.md"
else
    echo "❌ Erro no push. Verifique suas configurações do Git."
fi 