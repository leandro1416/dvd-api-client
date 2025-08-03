#!/usr/bin/env python3
"""
Script para testar o bot do Telegram
"""

import requests
import json
from urllib.parse import quote

# Configuração da API DVD
API_KEY = "7cd663fefd95cb7b434c1c5ec57c4e00c5d8ca2d68163bfb095c77488c14dbc8"
BASE_URL = "https://sum.natsec.bot/api"

headers = {
    'Authorization': f'Bearer {API_KEY}',
    'User-Agent': 'DVD-API-Bot/1.0'
}

def testar_api():
    """Testa a API DVD"""
    print("🔍 Testando API DVD...")
    
    try:
        # Testar status
        response = requests.get(f"{BASE_URL}/status", headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ API funcionando!")
            print(f"   Status: {data.get('status', 'N/A')}")
            print(f"   Timestamp: {data.get('timestamp', 'N/A')}")
        else:
            print(f"❌ Erro na API: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Erro de conexão: {e}")
        return False
    
    return True

def testar_busca():
    """Testa uma busca simples"""
    print("\n🔍 Testando busca...")
    
    try:
        # Buscar por domínio
        domain = "claro.com.br"
        encoded_domain = quote(domain)
        response = requests.get(
            f"{BASE_URL}/dominio/{encoded_domain}",
            headers=headers,
            params={'page': 1, 'page_size': 5},
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            total = data.get("total", 0)
            print(f"✅ Busca funcionando!")
            print(f"   Total de credenciais: {total}")
            print(f"   Resultados na primeira página: {len(data.get('data', []))}")
        else:
            print(f"❌ Erro na busca: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Erro na busca: {e}")
        return False
    
    return True

def verificar_token():
    """Verifica se o token do bot está configurado"""
    print("\n🤖 Verificando configuração do bot...")
    
    try:
        with open('telegram_bot.py', 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'SEU_TOKEN_AQUI' in content:
            print("❌ Token do bot não configurado!")
            print("   Edite o arquivo telegram_bot.py e substitua SEU_TOKEN_AQUI pelo seu token real")
            return False
        else:
            print("✅ Token do bot configurado!")
            return True
    except Exception as e:
        print(f"❌ Erro ao verificar token: {e}")
        return False

def mostrar_instrucoes():
    """Mostra instruções para configurar o bot"""
    print("\n" + "="*60)
    print("🤖 CONFIGURAÇÃO DO BOT TELEGRAM")
    print("="*60)
    
    print("\n📋 Passos para configurar:")
    print("1. Abra o Telegram e procure por @BotFather")
    print("2. Envie: /newbot")
    print("3. Digite o nome: DVD API Bot")
    print("4. Digite o username: dvd_api_bot")
    print("5. Copie o token recebido")
    print("6. Edite telegram_bot.py e substitua SEU_TOKEN_AQUI pelo token")
    print("7. Execute: python3 telegram_bot.py")
    
    print("\n📱 Para testar o bot:")
    print("1. Procure seu bot no Telegram")
    print("2. Envie: /start")
    print("3. Clique em '🔍 Buscar'")
    print("4. Escolha '🌐 Por Domínio'")
    print("5. Digite: claro.com.br")
    print("6. Veja os resultados!")
    
    print("\n📁 Arquivos criados:")
    print("   - telegram_bot.py: Bot do Telegram")
    print("   - GUIA_BOT_TELEGRAM.md: Guia completo")
    print("   - testar_bot.py: Script de teste")
    
    print("\n🎯 Funcionalidades do bot:")
    print("   - Interface com botões inline")
    print("   - Busca por domínio, senha, usuário, URL e rotas")
    print("   - Paginação automática")
    print("   - Formatação bonita com Markdown")
    print("   - Tratamento de erros robusto")

def main():
    """Função principal"""
    print("🚀 Testando Bot do Telegram para API DVD")
    print("="*50)
    
    # Testar API
    if not testar_api():
        print("\n❌ API não está funcionando. Verifique a conexão.")
        return
    
    # Testar busca
    if not testar_busca():
        print("\n❌ Busca não está funcionando. Verifique a API.")
        return
    
    # Verificar token
    token_ok = verificar_token()
    
    # Mostrar instruções
    mostrar_instrucoes()
    
    if token_ok:
        print("\n🎉 Tudo pronto! Execute: python3 telegram_bot.py")
    else:
        print("\n⚠️ Configure o token antes de executar o bot!")

if __name__ == "__main__":
    main() 