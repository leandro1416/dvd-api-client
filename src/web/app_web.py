#!/usr/bin/env python3
"""
Cliente Web para a API DVD
Acesse no browser: http://localhost:5000
"""

from flask import Flask, render_template, request, jsonify
import requests
from urllib.parse import quote
import json

app = Flask(__name__)

# Configuração da API
API_KEY = "7cd663fefd95cb7b434c1c5ec57c4e00c5d8ca2d68163bfb095c77488c14dbc8"
BASE_URL = "https://sum.natsec.bot/api"

class DVDAPIClient:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            'Authorization': f'Bearer {api_key}'
        }
    
    def check_status(self):
        """Verifica o status da API"""
        try:
            response = requests.get(f"{self.base_url}/status", headers=self.headers, timeout=30)
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
            response = requests.get(
                f"{self.base_url}/dominio/{encoded_domain}",
                headers=self.headers,
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
            response = requests.get(
                f"{self.base_url}/senha/{encoded_password}",
                headers=self.headers,
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
            response = requests.get(
                f"{self.base_url}/usuario/{encoded_username}",
                headers=self.headers,
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
            response = requests.get(
                f"{self.base_url}/url",
                headers=self.headers,
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
            response = requests.get(
                f"{self.base_url}/mapear-site/{encoded_domain}",
                headers=self.headers,
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
    return render_template('index.html')

@app.route('/api/status')
def api_status():
    """Endpoint para verificar status da API"""
    result = client.check_status()
    return jsonify(result)

@app.route('/api/search', methods=['POST'])
def api_search():
    """Endpoint para buscar credenciais"""
    data = request.get_json()
    search_type = data.get('type')
    search_term = data.get('term')
    page = data.get('page', 1)
    page_size = data.get('page_size', 500)
    
    if not search_term:
        return jsonify({"error": "Termo de busca é obrigatório"})
    
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

if __name__ == '__main__':
    print("🌐 Iniciando servidor web...")
    print("📱 Acesse: http://localhost:5000")
    print("🔄 Para parar: Ctrl+C")
    app.run(debug=True, host='0.0.0.0', port=5000) 