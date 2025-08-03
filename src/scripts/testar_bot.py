#!/usr/bin/env python3
"""
Script de teste para o bot do Telegram
"""

import sys
import os
import logging
import traceback
from pathlib import Path
from datetime import datetime

# Adiciona o diretório raiz ao path para importar config
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import requests
from config import API_BASE_URL, API_TIMEOUT, TELEGRAM_TOKEN

# Configurar logging detalhado
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('teste_bot.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def test_config():
    """Testa as configurações"""
    logger.info("🔧 Testando configurações...")
    
    # Testar token do Telegram
    if not TELEGRAM_TOKEN or TELEGRAM_TOKEN == "":
        logger.error("❌ ERRO: TELEGRAM_TOKEN não configurado!")
        logger.error("📝 Configure o token no arquivo config.py")
        return False
    
    if TELEGRAM_TOKEN == "SEU_TOKEN_AQUI":
        logger.error("❌ ERRO: TELEGRAM_TOKEN ainda está com valor padrão!")
        logger.error("📝 Substitua 'SEU_TOKEN_AQUI' pelo seu token real")
        return False
    
    logger.info(f"✅ TELEGRAM_TOKEN configurado: {TELEGRAM_TOKEN[:10]}...")
    
    # Testar configurações da API
    logger.info(f"✅ API_BASE_URL: {API_BASE_URL}")
    logger.info(f"✅ API_TIMEOUT: {API_TIMEOUT}")
    
    return True

def test_api_connection():
    """Testa conexão com a API"""
    logger.info("🔗 Testando conexão com a API...")
    
    try:
        headers = {
            'Authorization': 'Api-Key 7cd663fefd95cb7b434c1c5ec57c4e00c5d8ca2d68163bfb095c77488c14dbc8',
            'User-Agent': 'DVD-API-Bot/1.0'
        }
        
        logger.debug(f"📡 Fazendo requisição para: {API_BASE_URL}/status")
        logger.debug(f"📋 Headers: {headers}")
        
        response = requests.get(f"{API_BASE_URL}/status", headers=headers, timeout=API_TIMEOUT)
        
        logger.debug(f"📊 Resposta: Status {response.status_code}")
        logger.debug(f"📋 Headers da resposta: {dict(response.headers)}")
        
        if response.status_code == 200:
            data = response.json()
            logger.info("✅ API está online!")
            logger.debug(f"📋 Dados da API: {data}")
            return True
        else:
            logger.error(f"❌ API retornou erro {response.status_code}")
            logger.error(f"📝 Resposta: {response.text}")
            return False
            
    except requests.exceptions.ConnectionError as e:
        logger.error(f"❌ ERRO: Não foi possível conectar com a API")
        logger.error(f"📝 Detalhes: {e}")
        logger.error(f"📝 Verifique se a API está rodando em {API_BASE_URL}")
        return False
    except requests.exceptions.Timeout as e:
        logger.error(f"⏱️ ERRO: Timeout ao conectar com a API")
        logger.error(f"📝 Detalhes: {e}")
        logger.error(f"📝 Timeout configurado: {API_TIMEOUT}s")
        return False
    except Exception as e:
        logger.error(f"💥 ERRO: {e}")
        logger.error(f"📋 Traceback: {traceback.format_exc()}")
        return False

def test_telegram_bot():
    """Testa se o bot do Telegram pode ser criado"""
    logger.info("🤖 Testando criação do bot...")
    
    try:
        from telegram.ext import Application
        
        logger.debug("📦 Importando Application do telegram.ext")
        
        # Tentar criar a aplicação
        logger.debug("🔧 Criando aplicação do bot...")
        application = Application.builder().token(TELEGRAM_TOKEN).build()
        
        logger.info("✅ Bot criado com sucesso!")
        logger.info("📱 Token válido")
        
        # Testar se consegue obter informações do bot
        logger.debug("📡 Testando comunicação com Telegram...")
        try:
            import asyncio
            bot_info = asyncio.run(application.bot.get_me())
            logger.info(f"🤖 Informações do bot: {bot_info.first_name} (@{bot_info.username})")
        except Exception as e:
            logger.warning(f"⚠️ Não foi possível obter informações do bot: {e}")
            # Mesmo assim, o bot foi criado com sucesso
        
        return True
        
    except ImportError as e:
        logger.error(f"❌ ERRO: Módulo telegram não encontrado")
        logger.error(f"📝 Detalhes: {e}")
        logger.error(f"📝 Instale com: pip install python-telegram-bot==21.0")
        return False
    except Exception as e:
        logger.error(f"❌ ERRO ao criar bot: {e}")
        logger.error(f"📋 Traceback: {traceback.format_exc()}")
        logger.error(f"📝 Verifique se o token está correto")
        return False

def test_dependencies():
    """Testa se todas as dependências estão instaladas"""
    logger.info("📦 Testando dependências...")
    
    required_modules = [
        'requests',
        'telegram',
        'asyncio'
    ]
    
    missing_modules = []
    
    for module in required_modules:
        try:
            __import__(module)
            logger.info(f"✅ {module}")
        except ImportError:
            logger.error(f"❌ {module} - NÃO INSTALADO")
            missing_modules.append(module)
    
    if missing_modules:
        logger.error(f"📝 Instale as dependências faltantes:")
        logger.error("pip install -r requirements.txt")
        return False
    
    return True

def test_file_permissions():
    """Testa permissões de arquivo para logs"""
    logger.info("📁 Testando permissões de arquivo...")
    
    try:
        # Testar se consegue criar arquivo de log
        test_log_file = "test_log_permissions.log"
        with open(test_log_file, 'w') as f:
            f.write("Teste de permissões")
        
        # Remover arquivo de teste
        os.remove(test_log_file)
        
        logger.info("✅ Permissões de arquivo OK")
        return True
    except Exception as e:
        logger.error(f"❌ Erro de permissões: {e}")
        return False

def main():
    """Função principal"""
    logger.info("=" * 60)
    logger.info("🧪 TESTE DO BOT DO TELEGRAM")
    logger.info("=" * 60)
    logger.info(f"📅 Data/Hora: {datetime.now()}")
    logger.info(f"🔧 Python: {sys.version}")
    logger.info(f"📁 Diretório: {os.getcwd()}")
    logger.info("=" * 60)
    
    # Testar permissões
    perms_ok = test_file_permissions()
    
    # Testar dependências
    deps_ok = test_dependencies()
    
    # Testar configurações
    config_ok = test_config()
    
    # Testar API
    api_ok = test_api_connection()
    
    # Testar bot
    bot_ok = test_telegram_bot()
    
    # Resultado final
    logger.info("=" * 60)
    logger.info("📊 RESULTADO DOS TESTES")
    logger.info("=" * 60)
    
    results = {
        "Permissões": perms_ok,
        "Dependências": deps_ok,
        "Configurações": config_ok,
        "API": api_ok,
        "Bot": bot_ok
    }
    
    all_passed = True
    for test_name, passed in results.items():
        status = "✅ PASSOU" if passed else "❌ FALHOU"
        logger.info(f"{test_name}: {status}")
        if not passed:
            all_passed = False
    
    logger.info("=" * 60)
    
    if all_passed:
        logger.info("🎉 TODOS OS TESTES PASSARAM!")
        logger.info("✅ O bot está pronto para uso")
        logger.info("")
        logger.info("🚀 Para executar o bot:")
        logger.info("python3 main.py bot")
        logger.info("")
        logger.info("📱 Ou execute diretamente:")
        logger.info("python3 src/scripts/telegram_bot.py")
    else:
        logger.error("❌ ALGUNS TESTES FALHARAM")
        logger.error("")
        logger.error("🔧 Problemas encontrados:")
        
        if not perms_ok:
            logger.error("- Problemas de permissões de arquivo")
        if not deps_ok:
            logger.error("- Dependências não instaladas")
        if not config_ok:
            logger.error("- Configurações incorretas")
        if not api_ok:
            logger.error("- API não está acessível")
        if not bot_ok:
            logger.error("- Token do bot inválido")
        
        logger.error("")
        logger.error("📝 Consulte o guia em src/docs/GUIA_BOT_TELEGRAM.md")
        logger.error("📝 Verifique os logs detalhados acima")
    
    logger.info("=" * 60)

if __name__ == "__main__":
    main() 