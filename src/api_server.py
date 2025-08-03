#!/usr/bin/env python3
"""
Servidor Mock da API DVD
Fornece endpoints da API usando dados locais
"""

import json
import os
from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
import logging

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)  # Permitir CORS

# Carregar dados
def load_data():
    """Carrega os dados do arquivo JSON"""
    try:
        data_file = os.path.join(os.path.dirname(__file__), 'data', 'resultados_claro_20250802_160625.json')
        with open(data_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Erro ao carregar dados: {e}")
        return None

# Carregar dados uma vez
DATA = load_data()

# API Key válida
VALID_API_KEY = "7cd663fefd95cb7b434c1c5ec57c4e00c5d8ca2d68163bfb095c77488c14dbc8"

def check_auth():
    """Verifica se a API Key é válida"""
    auth_header = request.headers.get('Authorization', '')
    if not auth_header.startswith('Api-Key '):
        return False
    api_key = auth_header.replace('Api-Key ', '')
    return api_key == VALID_API_KEY

@app.route('/api/status', methods=['GET'])
def status():
    """Endpoint de status da API"""
    logger.info("📊 Requisição de status recebida")
    
    if not check_auth():
        return jsonify({"detail": "Invalid API key"}), 401
    
    return jsonify({
        "status": "API está funcionando",
        "timestamp": datetime.now().isoformat(),
        "usuario": "João Silva",
        "limite_diario": 10000,
        "consultas_hoje": 250,
        "consultas_restantes": 9750
    })

@app.route('/api/dominio/<domain>', methods=['GET'])
def search_by_domain(domain):
    """Busca credenciais por domínio"""
    logger.info(f"🔍 Busca por domínio: {domain}")
    
    if not check_auth():
        return jsonify({"detail": "Invalid API key"}), 401
    
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 500))
    
    if not DATA:
        return jsonify({"error": "Dados não disponíveis"}), 500
    
    # Filtrar dados por domínio
    all_data = DATA.get("buscas", {}).get("por_dominio", {}).get("data", [])
    
    # Filtrar por domínio (case insensitive)
    filtered_data = [
        item for item in all_data 
        if domain.lower() in item.get("url", "").lower()
    ]
    
    # Paginação
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    paginated_data = filtered_data[start_idx:end_idx]
    
    total = len(filtered_data)
    pages = (total + page_size - 1) // page_size
    
    logger.info(f"✅ Encontrados {total} resultados para domínio {domain}")
    
    return jsonify({
        "total": total,
        "page": page,
        "pages": pages,
        "dominio": domain,
        "dominio_pesquisado": domain,
        "data": paginated_data
    })

@app.route('/api/senha/<password>', methods=['GET'])
def search_by_password(password):
    """Busca credenciais por senha"""
    logger.info(f"🔍 Busca por senha: {password}")
    
    if not check_auth():
        return jsonify({"detail": "Invalid API key"}), 401
    
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 500))
    
    if not DATA:
        return jsonify({"error": "Dados não disponíveis"}), 500
    
    # Filtrar dados por senha
    all_data = DATA.get("buscas", {}).get("por_dominio", {}).get("data", [])
    
    # Filtrar por senha (case insensitive)
    filtered_data = [
        item for item in all_data 
        if password.lower() in item.get("password", "").lower()
    ]
    
    # Paginação
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    paginated_data = filtered_data[start_idx:end_idx]
    
    total = len(filtered_data)
    pages = (total + page_size - 1) // page_size
    
    logger.info(f"✅ Encontrados {total} resultados para senha {password}")
    
    return jsonify({
        "total": total,
        "page": page,
        "pages": pages,
        "data": paginated_data
    })

@app.route('/api/usuario/<username>', methods=['GET'])
def search_by_user(username):
    """Busca credenciais por usuário"""
    logger.info(f"🔍 Busca por usuário: {username}")
    
    if not check_auth():
        return jsonify({"detail": "Invalid API key"}), 401
    
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 500))
    
    if not DATA:
        return jsonify({"error": "Dados não disponíveis"}), 500
    
    # Filtrar dados por usuário
    all_data = DATA.get("buscas", {}).get("por_dominio", {}).get("data", [])
    
    # Filtrar por usuário (case insensitive)
    filtered_data = [
        item for item in all_data 
        if username.lower() in item.get("username", "").lower()
    ]
    
    # Paginação
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    paginated_data = filtered_data[start_idx:end_idx]
    
    total = len(filtered_data)
    pages = (total + page_size - 1) // page_size
    
    logger.info(f"✅ Encontrados {total} resultados para usuário {username}")
    
    return jsonify({
        "total": total,
        "page": page,
        "pages": pages,
        "data": paginated_data
    })

@app.route('/api/url', methods=['GET'])
def search_by_url():
    """Busca credenciais por URL"""
    url = request.args.get('url', '')
    logger.info(f"🔍 Busca por URL: {url}")
    
    if not check_auth():
        return jsonify({"detail": "Invalid API key"}), 401
    
    if not url:
        return jsonify({"error": "Parâmetro 'url' é obrigatório"}), 400
    
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 500))
    
    if not DATA:
        return jsonify({"error": "Dados não disponíveis"}), 500
    
    # Filtrar dados por URL
    all_data = DATA.get("buscas", {}).get("por_dominio", {}).get("data", [])
    
    # Filtrar por URL (case insensitive)
    filtered_data = [
        item for item in all_data 
        if url.lower() in item.get("url", "").lower()
    ]
    
    # Paginação
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    paginated_data = filtered_data[start_idx:end_idx]
    
    total = len(filtered_data)
    pages = (total + page_size - 1) // page_size
    
    logger.info(f"✅ Encontrados {total} resultados para URL {url}")
    
    return jsonify({
        "total": total,
        "page": page,
        "pages": pages,
        "data": paginated_data
    })

@app.route('/api/mapear-site/<domain>', methods=['GET'])
def map_domain_routes(domain):
    """Mapeia rotas de um domínio"""
    logger.info(f"🗺️ Mapeando rotas do domínio: {domain}")
    
    if not check_auth():
        return jsonify({"detail": "Invalid API key"}), 401
    
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 500))
    
    if not DATA:
        return jsonify({"error": "Dados não disponíveis"}), 500
    
    # Filtrar dados por domínio
    all_data = DATA.get("buscas", {}).get("por_dominio", {}).get("data", [])
    
    # Filtrar por domínio e extrair URLs únicas
    domain_urls = set()
    for item in all_data:
        url = item.get("url", "")
        if domain.lower() in url.lower():
            domain_urls.add(url)
    
    # Converter para lista e paginar
    routes_list = list(domain_urls)
    routes_list.sort()
    
    # Paginação
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    paginated_routes = routes_list[start_idx:end_idx]
    
    total = len(routes_list)
    pages = (total + page_size - 1) // page_size
    
    # Formatar rotas conforme documentação
    routes = [{"url": route, "credenciais": []} for route in paginated_routes]
    
    logger.info(f"✅ Encontradas {total} rotas para domínio {domain}")
    
    return jsonify({
        "total": total,
        "page": page,
        "pages": pages,
        "dominio": domain,
        "rotas": routes
    })

@app.route('/api/health', methods=['GET'])
def health():
    """Endpoint de health check"""
    return jsonify({"status": "healthy", "timestamp": datetime.now().isoformat()})

@app.route('/', methods=['GET'])
def root():
    """Página inicial"""
    return jsonify({
        "message": "DVD API Server",
        "version": "1.0.0",
        "endpoints": [
            "/api/status",
            "/api/dominio/{domain}",
            "/api/senha/{password}",
            "/api/usuario/{username}",
            "/api/url?url={url}",
            "/api/mapear-site/{domain}",
            "/api/health"
        ]
    })

if __name__ == '__main__':
    logger.info("🚀 Iniciando servidor da API DVD...")
    logger.info(f"📊 Dados carregados: {len(DATA.get('buscas', {}).get('por_dominio', {}).get('data', [])) if DATA else 0} registros")
    logger.info("🌐 Servidor rodando em https://sum.natsec.bot")
    app.run(host='127.0.0.1', port=8002, debug=True) 