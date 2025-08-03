#!/usr/bin/env python3
"""
Bot do Telegram para a API DVD
"""

import sys
import os
from pathlib import Path

# Adiciona o diretório raiz ao path para importar config
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import requests
import json
from urllib.parse import quote
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters
import asyncio
import logging
import traceback
from datetime import datetime
from config import API_BASE_URL, API_TIMEOUT, TELEGRAM_TOKEN, API_KEY

# Configuração da API DVD

# Verificar se o token do Telegram está configurado
if not TELEGRAM_TOKEN or TELEGRAM_TOKEN == "SEU_TOKEN_AQUI":
    print("❌ ERRO: Token do Telegram não configurado!")
    print("📝 Configure o TELEGRAM_TOKEN no arquivo config.py")
    print("🔗 Obtenha o token em: https://t.me/BotFather")
    sys.exit(1)

# Configurar logging detalhado
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot_telegram.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Log de inicialização
logger.info("=" * 50)
logger.info("🤖 INICIANDO BOT DO TELEGRAM")
logger.info("=" * 50)
logger.info(f"📱 Token: {TELEGRAM_TOKEN[:10]}...")
logger.info(f"🔗 API Base URL: {API_BASE_URL}")
logger.info(f"⏱️ Timeout: {API_TIMEOUT}s")
logger.info(f"📅 Data/Hora: {datetime.now()}")
logger.info("=" * 50)

headers = {
    'Authorization': f'Api-Key {API_KEY}',
    'User-Agent': 'DVD-API-Bot/1.0'
}

class DVDAPIClient:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            'Authorization': f'Api-Key {api_key}',
            'User-Agent': 'DVD-API-Bot/1.0'
        }
        logger.info(f"🔧 Cliente API inicializado: {base_url}")
    
    def check_status(self):
        """Verifica o status da API"""
        logger.info("🔍 Verificando status da API...")
        try:
            url = f"{self.base_url}/status"
            logger.debug(f"📡 Fazendo requisição para: {url}")
            
            response = requests.get(url, headers=self.headers, timeout=API_TIMEOUT)
            logger.debug(f"📊 Resposta: Status {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                logger.info("✅ API está online")
                logger.debug(f"📋 Dados da API: {data}")
                return data
            else:
                error_msg = f"Erro {response.status_code}: {response.text}"
                logger.error(f"❌ API retornou erro: {error_msg}")
                return {"error": error_msg}
        except requests.exceptions.ConnectionError as e:
            error_msg = f"Erro de conexão: {e}"
            logger.error(f"❌ {error_msg}")
            return {"error": error_msg}
        except requests.exceptions.Timeout as e:
            error_msg = f"Timeout: {e}"
            logger.error(f"⏱️ {error_msg}")
            return {"error": error_msg}
        except Exception as e:
            error_msg = f"Erro inesperado: {e}"
            logger.error(f"💥 {error_msg}")
            logger.error(f"📋 Traceback: {traceback.format_exc()}")
            return {"error": error_msg}
    
    def search_by_domain(self, domain, page=1, page_size=50):
        """Busca credenciais por domínio"""
        logger.info(f"🔍 Buscando por domínio: {domain} (página {page})")
        try:
            encoded_domain = quote(domain)
            params = {'page': page, 'page_size': page_size}
            url = f"{self.base_url}/dominio/{encoded_domain}"
            
            logger.debug(f"📡 URL: {url}")
            logger.debug(f"📋 Parâmetros: {params}")
            
            response = requests.get(url, headers=self.headers, params=params, timeout=API_TIMEOUT)
            logger.debug(f"📊 Resposta: Status {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                logger.info(f"✅ Busca por domínio concluída: {len(data.get('data', []))} resultados")
                return data
            else:
                error_msg = f"Erro {response.status_code}: {response.text}"
                logger.error(f"❌ Erro na busca por domínio: {error_msg}")
                return {"error": error_msg}
        except Exception as e:
            error_msg = f"Erro de busca por domínio: {e}"
            logger.error(f"❌ {error_msg}")
            logger.error(f"📋 Traceback: {traceback.format_exc()}")
            return {"error": error_msg}
    
    def search_by_password(self, password, page=1, page_size=50):
        """Busca credenciais por senha"""
        logger.info(f"🔍 Buscando por senha: {password} (página {page})")
        try:
            encoded_password = quote(password)
            params = {'page': page, 'page_size': page_size}
            url = f"{self.base_url}/senha/{encoded_password}"
            
            logger.debug(f"📡 URL: {url}")
            
            response = requests.get(url, headers=self.headers, params=params, timeout=API_TIMEOUT)
            logger.debug(f"📊 Resposta: Status {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                logger.info(f"✅ Busca por senha concluída: {len(data.get('data', []))} resultados")
                return data
            else:
                error_msg = f"Erro {response.status_code}: {response.text}"
                logger.error(f"❌ Erro na busca por senha: {error_msg}")
                return {"error": error_msg}
        except Exception as e:
            error_msg = f"Erro de busca por senha: {e}"
            logger.error(f"❌ {error_msg}")
            logger.error(f"📋 Traceback: {traceback.format_exc()}")
            return {"error": error_msg}
    
    def search_by_user(self, username, page=1, page_size=50):
        """Busca credenciais por usuário"""
        logger.info(f"🔍 Buscando por usuário: {username} (página {page})")
        try:
            encoded_username = quote(username)
            params = {'page': page, 'page_size': page_size}
            url = f"{self.base_url}/usuario/{encoded_username}"
            
            logger.debug(f"📡 URL: {url}")
            
            response = requests.get(url, headers=self.headers, params=params, timeout=API_TIMEOUT)
            logger.debug(f"📊 Resposta: Status {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                logger.info(f"✅ Busca por usuário concluída: {len(data.get('data', []))} resultados")
                return data
            else:
                error_msg = f"Erro {response.status_code}: {response.text}"
                logger.error(f"❌ Erro na busca por usuário: {error_msg}")
                return {"error": error_msg}
        except Exception as e:
            error_msg = f"Erro de busca por usuário: {e}"
            logger.error(f"❌ {error_msg}")
            logger.error(f"📋 Traceback: {traceback.format_exc()}")
            return {"error": error_msg}
    
    def search_by_url(self, url, page=1, page_size=50):
        """Busca credenciais por URL"""
        logger.info(f"🔍 Buscando por URL: {url} (página {page})")
        try:
            params = {'url': url, 'page': page, 'page_size': page_size}
            api_url = f"{self.base_url}/url"
            
            logger.debug(f"📡 URL: {api_url}")
            logger.debug(f"📋 Parâmetros: {params}")
            
            response = requests.get(api_url, headers=self.headers, params=params, timeout=API_TIMEOUT)
            logger.debug(f"📊 Resposta: Status {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                logger.info(f"✅ Busca por URL concluída: {len(data.get('data', []))} resultados")
                return data
            else:
                error_msg = f"Erro {response.status_code}: {response.text}"
                logger.error(f"❌ Erro na busca por URL: {error_msg}")
                return {"error": error_msg}
        except Exception as e:
            error_msg = f"Erro de busca por URL: {e}"
            logger.error(f"❌ {error_msg}")
            logger.error(f"📋 Traceback: {traceback.format_exc()}")
            return {"error": error_msg}
    
    def map_domain_routes(self, domain, page=1, page_size=50):
        """Mapeia rotas de um domínio"""
        logger.info(f"🗺️ Mapeando rotas do domínio: {domain} (página {page})")
        try:
            encoded_domain = quote(domain)
            params = {'page': page, 'page_size': page_size}
            url = f"{self.base_url}/mapear-site/{encoded_domain}"
            
            logger.debug(f"📡 URL: {url}")
            
            response = requests.get(url, headers=self.headers, params=params, timeout=API_TIMEOUT)
            logger.debug(f"📊 Resposta: Status {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                logger.info(f"✅ Mapeamento de rotas concluído: {len(data.get('rotas', []))} rotas")
                return data
            else:
                error_msg = f"Erro {response.status_code}: {response.text}"
                logger.error(f"❌ Erro no mapeamento de rotas: {error_msg}")
                return {"error": error_msg}
        except Exception as e:
            error_msg = f"Erro de mapeamento de rotas: {e}"
            logger.error(f"❌ {error_msg}")
            logger.error(f"📋 Traceback: {traceback.format_exc()}")
            return {"error": error_msg}
    
    def search_all_domains(self, search_term, page=1, page_size=100):
        """Busca em todos os domínios disponíveis"""
        logger.info(f"🔍 Buscando em todos os domínios: {search_term}")
        try:
            # Primeiro, vamos buscar por domínio específico
            domain_result = self.search_by_domain(search_term, page, page_size)
            
            # Se não encontrou nada, vamos buscar por URL
            if not domain_result.get('data') or len(domain_result.get('data', [])) == 0:
                logger.info(f"🔍 Tentando busca por URL: {search_term}")
                url_result = self.search_by_url(search_term, page, page_size)
                if url_result.get('data') and len(url_result.get('data', [])) > 0:
                    return url_result
            
            # Se ainda não encontrou, vamos buscar por termo parcial em claro.com.br
            if not domain_result.get('data') or len(domain_result.get('data', [])) == 0:
                logger.info(f"🔍 Tentando busca por termo parcial em claro.com.br: {search_term}")
                # Buscar em claro.com.br com o termo
                partial_result = self.search_by_domain("claro.com.br", page, page_size * 2)
                if partial_result.get('data'):
                    # Filtrar resultados que contenham o termo de busca
                    filtered_data = []
                    search_term_lower = search_term.lower()
                    for item in partial_result.get('data', []):
                        url = item.get('url', '').lower()
                        username = item.get('username', '').lower()
                        password = item.get('password', '').lower()
                        
                        if (search_term_lower in url or 
                            search_term_lower in username or 
                            search_term_lower in password):
                            filtered_data.append(item)
                    
                    if filtered_data:
                        partial_result['data'] = filtered_data
                        partial_result['total'] = len(filtered_data)
                        partial_result['dominio_pesquisado'] = search_term
                        logger.info(f"✅ Encontrados {len(filtered_data)} resultados com termo parcial")
                        return partial_result
            
            return domain_result
        except Exception as e:
            error_msg = f"Erro na busca ampla: {e}"
            logger.error(f"💥 {error_msg}")
            logger.error(f"📋 Traceback: {traceback.format_exc()}")
            return {"error": error_msg}

# Criar cliente
client = DVDAPIClient(API_KEY, API_BASE_URL)

# Dicionário para armazenar estado dos usuários
user_states = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /start"""
    user_id = update.effective_user.id
    user_name = update.effective_user.first_name
    logger.info(f"👤 Usuário {user_id} ({user_name}) iniciou o bot")
    
    welcome_message = """
🔍 *DVD API Bot*

Bem-vindo ao bot da API DVD! 

*Comandos disponíveis:*
/start - Mostra esta mensagem
/status - Verifica status da API
/search - Inicia busca
/help - Ajuda

*Tipos de busca:*
🌐 Por Domínio (ex: claro.com.br)
🔑 Por Senha (ex: 123456)
👤 Por Usuário (ex: admin)
🔗 Por URL (ex: https://exemplo.com/login)
🗺️ Mapear Rotas (ex: exemplo.com.br)

*Como usar:*
1. Digite /search
2. Escolha o tipo de busca
3. Digite o termo
4. Veja os resultados!

*Exemplo:*
/search
🌐 Por Domínio
claro.com.br
    """
    
    keyboard = [
        [InlineKeyboardButton("🔍 Buscar", callback_data="search")],
        [InlineKeyboardButton("📊 Status", callback_data="status")],
        [InlineKeyboardButton("❓ Ajuda", callback_data="help")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    try:
        await update.message.reply_text(welcome_message, parse_mode='Markdown', reply_markup=reply_markup)
        logger.info(f"✅ Mensagem de boas-vindas enviada para usuário {user_id}")
    except Exception as e:
        logger.error(f"❌ Erro ao enviar mensagem de boas-vindas: {e}")
        logger.error(f"📋 Traceback: {traceback.format_exc()}")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /status"""
    user_id = update.effective_user.id
    logger.info(f"👤 Usuário {user_id} solicitou status da API")
    
    try:
        await update.message.reply_text("🔍 Verificando status da API...")
        
        result = client.check_status()
        if result.get("error"):
            status_message = f"❌ *API Offline*\n\nErro: {result['error']}"
            logger.warning(f"⚠️ API offline para usuário {user_id}: {result['error']}")
        else:
            status_message = f"✅ *API Online*\n\nStatus: {result.get('status', 'N/A')}\nTimestamp: {result.get('timestamp', 'N/A')}"
            logger.info(f"✅ API online - status enviado para usuário {user_id}")
        
        await update.message.reply_text(status_message, parse_mode='Markdown')
    except Exception as e:
        error_msg = f"Erro ao verificar status: {e}"
        logger.error(f"❌ {error_msg}")
        logger.error(f"📋 Traceback: {traceback.format_exc()}")
        await update.message.reply_text(f"❌ Erro interno: {error_msg}")

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /search"""
    user_id = update.effective_user.id
    logger.info(f"👤 Usuário {user_id} iniciou busca")
    
    try:
        user_states[user_id] = {"step": "choosing_type"}
        
        keyboard = [
            [InlineKeyboardButton("🌐 Por Domínio", callback_data="type_domain")],
            [InlineKeyboardButton("🔑 Por Senha", callback_data="type_password")],
            [InlineKeyboardButton("👤 Por Usuário", callback_data="type_user")],
            [InlineKeyboardButton("🔗 Por URL", callback_data="type_url")],
            [InlineKeyboardButton("🗺️ Mapear Rotas", callback_data="type_routes")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text("🔍 Escolha o tipo de busca:", reply_markup=reply_markup)
        logger.info(f"✅ Menu de busca enviado para usuário {user_id}")
    except Exception as e:
        error_msg = f"Erro ao mostrar menu de busca: {e}"
        logger.error(f"❌ {error_msg}")
        logger.error(f"📋 Traceback: {traceback.format_exc()}")
        await update.message.reply_text(f"❌ Erro interno: {error_msg}")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /help"""
    user_id = update.effective_user.id
    logger.info(f"👤 Usuário {user_id} solicitou ajuda")
    
    try:
        help_message = """
❓ *Ajuda - DVD API Bot*

*Comandos:*
/start - Inicia o bot
/status - Verifica status da API
/search - Inicia busca
/help - Mostra esta ajuda

*Tipos de Busca:*

🌐 *Por Domínio*
Busca todas as credenciais de um domínio
Exemplo: claro.com.br

🔑 *Por Senha*
Busca credenciais que usam uma senha específica
Exemplo: 123456

👤 *Por Usuário*
Busca todas as credenciais de um usuário
Exemplo: admin

🔗 *Por URL*
Busca credenciais para uma URL específica
Exemplo: https://exemplo.com/login

🗺️ *Mapear Rotas*
Lista todas as URLs de um domínio
Exemplo: exemplo.com.br

*Dicas:*
• Use termos específicos para melhores resultados
• O bot mostra até 50 resultados por vez
• Use paginação para ver mais resultados
        """
        
        await update.message.reply_text(help_message, parse_mode='Markdown')
        logger.info(f"✅ Ajuda enviada para usuário {user_id}")
    except Exception as e:
        error_msg = f"Erro ao enviar ajuda: {e}"
        logger.error(f"❌ {error_msg}")
        logger.error(f"📋 Traceback: {traceback.format_exc()}")
        await update.message.reply_text(f"❌ Erro interno: {error_msg}")

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para botões inline"""
    query = update.callback_query
    user_id = query.from_user.id
    data = query.data
    
    logger.info(f"👤 Usuário {user_id} clicou em botão: {data}")
    
    try:
        await query.answer()
        
        if data == "search":
            user_states[user_id] = {"step": "choosing_type"}
            keyboard = [
                [InlineKeyboardButton("🌐 Por Domínio", callback_data="type_domain")],
                [InlineKeyboardButton("🔑 Por Senha", callback_data="type_password")],
                [InlineKeyboardButton("👤 Por Usuário", callback_data="type_user")],
                [InlineKeyboardButton("🔗 Por URL", callback_data="type_url")],
                [InlineKeyboardButton("🗺️ Mapear Rotas", callback_data="type_routes")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await query.edit_message_text("🔍 Escolha o tipo de busca:", reply_markup=reply_markup)
            logger.info(f"✅ Menu de busca enviado para usuário {user_id}")
        
        elif data == "status":
            await query.edit_message_text("🔍 Verificando status da API...")
            result = client.check_status()
            if result.get("error"):
                status_message = f"❌ *API Offline*\n\nErro: {result['error']}"
                logger.warning(f"⚠️ API offline para usuário {user_id}: {result['error']}")
            else:
                status_message = f"✅ *API Online*\n\nStatus: {result.get('status', 'N/A')}\nTimestamp: {result.get('timestamp', 'N/A')}"
                logger.info(f"✅ API online - status enviado para usuário {user_id}")
            await query.edit_message_text(status_message, parse_mode='Markdown')
        
        elif data == "help":
            help_message = """
❓ *Ajuda - DVD API Bot*

*Comandos:*
/start - Inicia o bot
/status - Verifica status da API
/search - Inicia busca
/help - Mostra esta ajuda

*Tipos de Busca:*

🌐 *Por Domínio*
Busca todas as credenciais de um domínio
Exemplo: claro.com.br

🔑 *Por Senha*
Busca credenciais que usam uma senha específica
Exemplo: 123456

👤 *Por Usuário*
Busca todas as credenciais de um usuário
Exemplo: admin

🔗 *Por URL*
Busca credenciais para uma URL específica
Exemplo: https://exemplo.com/login

🗺️ *Mapear Rotas*
Lista todas as URLs de um domínio
Exemplo: exemplo.com.br

*Dicas:*
• Use termos específicos para melhores resultados
• O bot mostra até 50 resultados por vez
• Use paginação para ver mais resultados
            """
            await query.edit_message_text(help_message, parse_mode='Markdown')
            logger.info(f"✅ Ajuda enviada para usuário {user_id}")
        
        elif data.startswith("type_"):
            search_type = data.replace("type_", "")
            user_states[user_id] = {"step": "entering_term", "type": search_type}
            
            type_names = {
                "domain": "🌐 Por Domínio",
                "password": "🔑 Por Senha", 
                "user": "👤 Por Usuário",
                "url": "🔗 Por URL",
                "routes": "🗺️ Mapear Rotas"
            }
            
            await query.edit_message_text(f"🔍 {type_names[search_type]}\n\nDigite o termo de busca:")
            logger.info(f"✅ Usuário {user_id} escolheu tipo: {search_type}")
        
        elif data.startswith("download_"):
            # Handler para download de arquivos
            parts = data.split("_")
            if len(parts) >= 4:
                search_type = parts[1]
                search_term = parts[2]
                page = int(parts[3])
                
                logger.info(f"📁 Usuário {user_id} solicitou download: {search_type} = '{search_term}' página {page}")
                
                # Executar busca novamente para obter dados
                try:
                    if search_type == "domain":
                        result = client.search_all_domains(search_term, page)
                    elif search_type == "password":
                        result = client.search_by_password(search_term, page)
                    elif search_type == "user":
                        result = client.search_by_user(search_term, page)
                    elif search_type == "url":
                        result = client.search_by_url(search_term, page)
                    else:
                        await query.answer("❌ Tipo de busca inválido para download")
                        return
                    
                    if result.get("error"):
                        await query.answer(f"❌ Erro: {result['error']}")
                        return
                    
                    # Criar arquivo JSON
                    import json
                    import tempfile
                    import os
                    
                    filename = f"resultados_{search_type}_{search_term}_p{page}.json"
                    filepath = os.path.join(tempfile.gettempdir(), filename)
                    
                    with open(filepath, 'w', encoding='utf-8') as f:
                        json.dump(result, f, ensure_ascii=False, indent=2)
                    
                    # Enviar arquivo
                    with open(filepath, 'rb') as f:
                        await context.bot.send_document(
                            chat_id=user_id,
                            document=f,
                            filename=filename,
                            caption=f"📁 Resultados da busca\nTipo: {search_type}\nTermo: {search_term}\nPágina: {page}"
                        )
                    
                    # Limpar arquivo temporário
                    os.remove(filepath)
                    
                    await query.answer("✅ Arquivo enviado!")
                    logger.info(f"✅ Arquivo enviado para usuário {user_id}")
                    
                except Exception as e:
                    error_msg = f"Erro ao gerar arquivo: {e}"
                    logger.error(f"❌ {error_msg}")
                    logger.error(f"📋 Traceback: {traceback.format_exc()}")
                    await query.answer(f"❌ {error_msg}")
    
    except Exception as e:
        error_msg = f"Erro no handler de botões: {e}"
        logger.error(f"❌ {error_msg}")
        logger.error(f"📋 Traceback: {traceback.format_exc()}")
        try:
            await query.edit_message_text(f"❌ Erro interno: {error_msg}")
        except:
            pass

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para mensagens de texto"""
    user_id = update.effective_user.id
    message_text = update.message.text
    
    logger.info(f"👤 Usuário {user_id} enviou mensagem: {message_text[:50]}...")
    
    if user_id not in user_states:
        logger.info(f"👤 Usuário {user_id} não tem estado - enviando instrução")
        await update.message.reply_text("Use /search para iniciar uma busca!")
        return
    
    state = user_states[user_id]
    
    if state["step"] == "entering_term":
        search_type = state["type"]
        search_term = message_text.strip()
        
        logger.info(f"🔍 Usuário {user_id} iniciando busca: {search_type} = '{search_term}'")
        
        if not search_term:
            logger.warning(f"⚠️ Usuário {user_id} enviou termo vazio")
            await update.message.reply_text("❌ Por favor, digite um termo de busca válido.")
            return
        
        # Mostrar loading
        loading_message = await update.message.reply_text("🔍 Buscando...")
        
        try:
            # Executar busca baseada no tipo
            if search_type == "domain":
                result = client.search_all_domains(search_term)  # Usar busca ampla
            elif search_type == "password":
                result = client.search_by_password(search_term)
            elif search_type == "user":
                result = client.search_by_user(search_term)
            elif search_type == "url":
                result = client.search_by_url(search_term)
            elif search_type == "routes":
                result = client.map_domain_routes(search_term)
            else:
                logger.error(f"❌ Tipo de busca inválido: {search_type}")
                await loading_message.edit_text("❌ Tipo de busca inválido")
                return
            
            if result.get("error"):
                error_msg = f"Erro na busca: {result['error']}"
                logger.error(f"❌ {error_msg}")
                await loading_message.edit_text(f"❌ {error_msg}")
            else:
                # Formatar resultados
                await format_and_send_results(loading_message, result, search_type, search_term, user_id)
        
        except Exception as e:
            error_msg = f"Erro interno: {str(e)}"
            logger.error(f"❌ {error_msg}")
            logger.error(f"📋 Traceback: {traceback.format_exc()}")
            await loading_message.edit_text(f"❌ {error_msg}")
        
        # Limpar estado do usuário
        del user_states[user_id]
        logger.info(f"✅ Estado do usuário {user_id} limpo")

async def format_and_send_results(message, result, search_type, search_term, user_id):
    """Formata e envia resultados"""
    logger.info(f"📊 Formatando resultados para usuário {user_id}")
    
    try:
        total = result.get("total", 0)
        page = result.get("page", 1)
        pages = result.get("pages", 1)
        
        # Cabeçalho
        header = f"🔍 *Resultados da Busca*\n\n"
        header += f"*Tipo:* {search_type}\n"
        header += f"*Termo:* `{search_term}`\n"
        header += f"*Total:* {total}\n"
        header += f"*Página:* {page} de {pages}\n\n"
        
        if search_type == "routes":
            # Mostrar rotas
            routes = result.get("rotas", [])
            if routes:
                header += "*Rotas encontradas:*\n"
                for i, route in enumerate(routes[:20]):  # Limitar a 20 rotas
                    header += f"• {route.get('url', 'N/A')}\n"
                if len(routes) > 20:
                    header += f"\n... e mais {len(routes) - 20} rotas"
                logger.info(f"✅ {len(routes)} rotas encontradas para usuário {user_id}")
            else:
                header += "❌ Nenhuma rota encontrada"
                logger.info(f"⚠️ Nenhuma rota encontrada para usuário {user_id}")
        else:
            # Mostrar credenciais
            data = result.get("data", [])
            if data:
                header += "*Credenciais encontradas:*\n"
                for i, cred in enumerate(data[:10]):  # Limitar a 10 credenciais
                    header += f"• URL: `{cred.get('url', 'N/A')}`\n"
                    header += f"  Usuário: `{cred.get('username', 'N/A')}`\n"
                    header += f"  Senha: `{cred.get('password', 'N/A')}`\n\n"
                if len(data) > 10:
                    header += f"... e mais {len(data) - 10} credenciais"
                logger.info(f"✅ {len(data)} credenciais encontradas para usuário {user_id}")
            else:
                header += "❌ Nenhuma credencial encontrada"
                logger.info(f"⚠️ Nenhuma credencial encontrada para usuário {user_id}")
        
        # Botões de navegação se houver mais páginas
        keyboard = []
        if pages > 1:
            if page > 1:
                keyboard.append([InlineKeyboardButton("⬅️ Anterior", callback_data=f"page_{search_type}_{search_term}_{page-1}")])
            if page < pages:
                keyboard.append([InlineKeyboardButton("Próxima ➡️", callback_data=f"page_{search_type}_{search_term}_{page+1}")])
        
        # Adicionar botão para download se houver dados
        if search_type != "routes" and result.get("data"):
            keyboard.append([InlineKeyboardButton("📁 Baixar JSON", callback_data=f"download_{search_type}_{search_term}_{page}")])
        
        keyboard.append([InlineKeyboardButton("🔍 Nova Busca", callback_data="search")])
        
        reply_markup = InlineKeyboardMarkup(keyboard) if keyboard else None
        
        await message.edit_text(header, parse_mode='Markdown', reply_markup=reply_markup)
        logger.info(f"✅ Resultados enviados para usuário {user_id}")
    
    except Exception as e:
        error_msg = f"Erro ao formatar resultados: {e}"
        logger.error(f"❌ {error_msg}")
        logger.error(f"📋 Traceback: {traceback.format_exc()}")
        await message.edit_text(f"❌ Erro ao formatar resultados: {error_msg}")

async def page_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para paginação"""
    query = update.callback_query
    user_id = query.from_user.id
    data = query.data
    
    logger.info(f"👤 Usuário {user_id} solicitou página: {data}")
    
    try:
        await query.answer()
        
        if data.startswith("page_"):
            parts = data.split("_")
            search_type = parts[1]
            search_term = parts[2]
            page = int(parts[3])
            
            logger.info(f"🔍 Usuário {user_id} navegando para página {page}")
            
            # Executar busca com nova página
            loading_message = await query.edit_message_text("🔍 Carregando página...")
            
            try:
                if search_type == "domain":
                    result = client.search_by_domain(search_term, page)
                elif search_type == "password":
                    result = client.search_by_password(search_term, page)
                elif search_type == "user":
                    result = client.search_by_user(search_term, page)
                elif search_type == "url":
                    result = client.search_by_url(search_term, page)
                elif search_type == "routes":
                    result = client.map_domain_routes(search_term, page)
                
                if result.get("error"):
                    error_msg = f"Erro na busca: {result['error']}"
                    logger.error(f"❌ {error_msg}")
                    await loading_message.edit_text(f"❌ {error_msg}")
                else:
                    await format_and_send_results(loading_message, result, search_type, search_term, user_id)
            
            except Exception as e:
                error_msg = f"Erro interno: {str(e)}"
                logger.error(f"❌ {error_msg}")
                logger.error(f"📋 Traceback: {traceback.format_exc()}")
                await loading_message.edit_text(f"❌ {error_msg}")
    
    except Exception as e:
        error_msg = f"Erro no handler de paginação: {e}"
        logger.error(f"❌ {error_msg}")
        logger.error(f"📋 Traceback: {traceback.format_exc()}")
        try:
            await query.edit_message_text(f"❌ Erro interno: {error_msg}")
        except:
            pass

def main():
    """Função principal"""
    logger.info("🤖 Iniciando Bot do Telegram...")
    logger.info(f"🔗 API Base URL: {API_BASE_URL}")
    logger.info(f"📱 Token: {TELEGRAM_TOKEN[:10]}...")
    logger.info("📱 Para parar: Ctrl+C")
    
    try:
        # Criar aplicação
        application = Application.builder().token(TELEGRAM_TOKEN).build()
        logger.info("✅ Aplicação criada com sucesso")
        
        # Adicionar handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("status", status))
        application.add_handler(CommandHandler("search", search))
        application.add_handler(CommandHandler("help", help_command))
        application.add_handler(CallbackQueryHandler(button_handler))
        application.add_handler(CallbackQueryHandler(page_handler, pattern="^page_"))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
        
        logger.info("✅ Handlers registrados com sucesso")
        
        # Iniciar bot
        logger.info("✅ Bot iniciado! Envie /start para começar.")
        application.run_polling()
        
    except Exception as e:
        logger.error(f"❌ Erro fatal ao iniciar bot: {e}")
        logger.error(f"📋 Traceback: {traceback.format_exc()}")
        sys.exit(1)

if __name__ == "__main__":
    main() 