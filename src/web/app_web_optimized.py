#!/usr/bin/env python3
"""
Cliente Web Otimizado para a API DVD
Acesse no browser: http://localhost:8080
"""

from flask import Flask, render_template, request, jsonify, send_from_directory
import requests
from urllib.parse import quote
import json
import time
import threading
from functools import wraps
import os

app = Flask(__name__)

# Configuração da API
API_KEY = "7cd663fefd95cb7b434c1c5ec57c4e00c5d8ca2d68163bfb095c77488c14dbc8"
BASE_URL = "https://sum.natsec.bot/api"

# Cache para melhorar performance
cache = {}
cache_timeout = 300  # 5 minutos

def cache_result(func):
    """Decorator para cache de resultados"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = f"{func.__name__}_{hash(str(args) + str(kwargs))}"
        current_time = time.time()
        
        if cache_key in cache:
            result, timestamp = cache[cache_key]
            if current_time - timestamp < cache_timeout:
                return result
        
        result = func(*args, **kwargs)
        cache[cache_key] = (result, current_time)
        return result
    return wrapper

class DVDAPIClient:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'User-Agent': 'DVD-API-Client/1.0'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
    
    @cache_result
    def check_status(self):
        """Verifica o status da API com cache"""
        try:
            response = self.session.get(f"{self.base_url}/status", timeout=10)
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"Erro {response.status_code}: {response.text}"}
        except Exception as e:
            return {"error": f"Erro de conexão: {e}"}
    
    def search_by_domain(self, domain, page=1, page_size=500):
        """Busca credenciais por domínio"""
        try:
            encoded_domain = quote(domain)
            params = {'page': page, 'page_size': page_size}
            response = self.session.get(
                f"{self.base_url}/dominio/{encoded_domain}",
                params=params,
                timeout=30
            )
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"Erro {response.status_code}: {response.text}"}
        except Exception as e:
            return {"error": f"Erro de busca: {e}"}
    
    def search_by_password(self, password, page=1, page_size=500):
        """Busca credenciais por senha"""
        try:
            encoded_password = quote(password)
            params = {'page': page, 'page_size': page_size}
            response = self.session.get(
                f"{self.base_url}/senha/{encoded_password}",
                params=params,
                timeout=30
            )
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"Erro {response.status_code}: {response.text}"}
        except Exception as e:
            return {"error": f"Erro de busca: {e}"}
    
    def search_by_user(self, username, page=1, page_size=500):
        """Busca credenciais por usuário"""
        try:
            encoded_username = quote(username)
            params = {'page': page, 'page_size': page_size}
            response = self.session.get(
                f"{self.base_url}/usuario/{encoded_username}",
                params=params,
                timeout=30
            )
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"Erro {response.status_code}: {response.text}"}
        except Exception as e:
            return {"error": f"Erro de busca: {e}"}
    
    def search_by_url(self, url, page=1, page_size=500):
        """Busca credenciais por URL"""
        try:
            params = {'url': url, 'page': page, 'page_size': page_size}
            response = self.session.get(
                f"{self.base_url}/url",
                params=params,
                timeout=30
            )
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"Erro {response.status_code}: {response.text}"}
        except Exception as e:
            return {"error": f"Erro de busca: {e}"}
    
    def map_domain_routes(self, domain, page=1, page_size=500):
        """Mapeia rotas de um domínio"""
        try:
            encoded_domain = quote(domain)
            params = {'page': page, 'page_size': page_size}
            response = self.session.get(
                f"{self.base_url}/mapear-site/{encoded_domain}",
                params=params,
                timeout=30
            )
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"Erro {response.status_code}: {response.text}"}
        except Exception as e:
            return {"error": f"Erro de busca: {e}"}

# Criar cliente
client = DVDAPIClient(API_KEY, BASE_URL)

@app.route('/')
def index():
    """Página principal"""
    return render_template('index_optimized.html')

@app.route('/favicon.ico')
def favicon():
    """Favicon para evitar 404"""
    return '', 204

@app.route('/api/status')
def api_status():
    """Endpoint para verificar status da API"""
    result = client.check_status()
    return jsonify(result)

@app.route('/api/search', methods=['POST'])
def api_search():
    """Endpoint para buscar credenciais"""
    try:
        data = request.get_json()
        search_type = data.get('type')
        search_term = data.get('term')
        page = data.get('page', 1)
        page_size = data.get('page_size', 500)
        
        if not search_term:
            return jsonify({"error": "Termo de busca é obrigatório"})
        
        # Validar parâmetros
        if page < 1:
            page = 1
        if page_size < 1 or page_size > 5000:
            page_size = 500
        
        if search_type == 'domain':
            result = client.search_by_domain(search_term, page, page_size)
        elif search_type == 'password':
            result = client.search_by_password(search_term, page, page_size)
        elif search_type == 'user':
            result = client.search_by_user(search_term, page, page_size)
        elif search_type == 'url':
            result = client.search_by_url(search_term, page, page_size)
        elif search_type == 'routes':
            result = client.map_domain_routes(search_term, page, page_size)
        else:
            return jsonify({"error": "Tipo de busca inválido"})
        
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": f"Erro interno: {str(e)}"}), 500

@app.route('/api/stats')
def api_stats():
    """Endpoint para estatísticas do sistema"""
    return jsonify({
        "cache_size": len(cache),
        "cache_timeout": cache_timeout,
        "api_status": "online" if not client.check_status().get("error") else "offline"
    })

@app.route('/api/clear-cache')
def clear_cache():
    """Endpoint para limpar cache"""
    cache.clear()
    return jsonify({"message": "Cache limpo com sucesso"})

@app.errorhandler(404)
def not_found(error):
    """Handler para páginas não encontradas"""
    return jsonify({"error": "Página não encontrada"}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handler para erros internos"""
    return jsonify({"error": "Erro interno do servidor"}), 500

def cleanup_cache():
    """Limpa cache expirado periodicamente"""
    while True:
        time.sleep(60)  # Executar a cada minuto
        current_time = time.time()
        expired_keys = []
        
        for key, (result, timestamp) in cache.items():
            if current_time - timestamp > cache_timeout:
                expired_keys.append(key)
        
        for key in expired_keys:
            del cache[key]

# Iniciar thread de limpeza de cache
cache_cleanup_thread = threading.Thread(target=cleanup_cache, daemon=True)
cache_cleanup_thread.start()

if __name__ == '__main__':
    print("🚀 Iniciando servidor web otimizado...")
    print("📱 Acesse: http://localhost:8080")
    print("⚡ Cache ativado para melhor performance")
    print("🔄 Para parar: Ctrl+C")
    
    # Configuração para produção
    port = int(os.environ.get('PORT', 8080))
    debug = os.environ.get('FLASK_ENV') == 'development'
    
    app.run(debug=debug, host='0.0.0.0', port=port, threaded=True) 