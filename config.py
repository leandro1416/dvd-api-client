"""
Configurações principais do projeto DVD API Client
"""

# Configurações da API
API_BASE_URL = "https://sum.natsec.bot/api"
API_TIMEOUT = 30
API_MAX_PAGE_SIZE = 5000
API_KEY = "7cd663fefd95cb7b434c1c5ec57c4e00c5d8ca2d68163bfb095c77488c14dbc8"

# Configurações do cliente
DEFAULT_PAGE_SIZE = 100
DEFAULT_TIMEOUT = 30

# Configurações da interface web
WEB_HOST = "127.0.0.1"
WEB_PORT = 5000
WEB_DEBUG = True

# Configurações do bot Telegram
TELEGRAM_TOKEN = "8369793525:AAHjbxS_CD1dpR5D577Yeu1ld1KlndBHihI"
TELEGRAM_CHAT_ID = ""  # Configure o chat ID aqui

# Configurações de logging
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Diretórios do projeto
PROJECT_ROOT = "."
SRC_DIR = "src"
CLIENTS_DIR = "src/clients"
WEB_DIR = "src/web"
SCRIPTS_DIR = "src/scripts"
TESTS_DIR = "src/tests"
DOCS_DIR = "src/docs"
DATA_DIR = "src/data" 