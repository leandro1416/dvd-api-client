#!/usr/bin/env python3
"""
Cliente simples para a API DVD
Uso: python simple_client.py
"""

import requests
import json
import sys
from urllib.parse import quote

class SimpleDVDClient:
    def __init__(self, api_key, base_url="https://sum.natsec.bot/api"):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            'Authorization': f'Api-Key {api_key}'
        }
    
    def check_status(self):
        """Verifica o status da API"""
        try:
            response = requests.get(f"{self.base_url}/status", headers=self.headers, timeout=30)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Erro {response.status_code}: {response.text}")
                return None
        except Exception as e:
            print(f"Erro de conexão: {e}")
            return None
    
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
                print(f"Erro {response.status_code}: {response.text}")
                return None
        except Exception as e:
            print(f"Erro de busca: {e}")
            return None
    
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
                print(f"Erro {response.status_code}: {response.text}")
                return None
        except Exception as e:
            print(f"Erro de busca: {e}")
            return None
    
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
                print(f"Erro {response.status_code}: {response.text}")
                return None
        except Exception as e:
            print(f"Erro de busca: {e}")
            return None
    
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
                print(f"Erro {response.status_code}: {response.text}")
                return None
        except Exception as e:
            print(f"Erro de busca: {e}")
            return None
    
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
                print(f"Erro {response.status_code}: {response.text}")
                return None
        except Exception as e:
            print(f"Erro de busca: {e}")
            return None

def print_help():
    """Exibe a ajuda do programa"""
    print("""
Cliente DVD API - Uso:

1. Testar conexão:
   python simple_client.py status <API_KEY>

2. Buscar por domínio:
   python simple_client.py domain <API_KEY> <DOMINIO>

3. Buscar por senha:
   python simple_client.py password <API_KEY> <SENHA>

4. Buscar por usuário:
   python simple_client.py user <API_KEY> <USUARIO>

5. Buscar por URL:
   python simple_client.py url <API_KEY> <URL>

6. Mapear rotas de domínio:
   python simple_client.py routes <API_KEY> <DOMINIO>

Exemplos:
   python simple_client.py status SUA_API_KEY
   python simple_client.py domain SUA_API_KEY exemplo.com.br
   python simple_client.py password SUA_API_KEY 123456
   python simple_client.py user SUA_API_KEY admin@empresa.com
   python simple_client.py url SUA_API_KEY "https://exemplo.com.br/login"
   python simple_client.py routes SUA_API_KEY exemplo.com.br
""")

def main():
    if len(sys.argv) < 3:
        print_help()
        return
    
    command = sys.argv[1].lower()
    api_key = sys.argv[2]
    
    client = SimpleDVDClient(api_key)
    
    if command == "status":
        result = client.check_status()
        if result:
            print("=== Status da API ===")
            print(f"Status: {result.get('status', 'N/A')}")
            print(f"Usuário: {result.get('usuario', 'N/A')}")
            print(f"Consultas restantes: {result.get('consultas_restantes', 'N/A')}")
            print(f"Timestamp: {result.get('timestamp', 'N/A')}")
    
    elif command == "domain":
        if len(sys.argv) < 4:
            print("Erro: Domínio não especificado")
            return
        domain = sys.argv[3]
        result = client.search_by_domain(domain)
        if result:
            print(f"=== Busca por Domínio: {domain} ===")
            print(f"Total: {result.get('total', 0)}")
            print(f"Página: {result.get('page', 1)} de {result.get('pages', 1)}")
            print("\nCredenciais encontradas:")
            for cred in result.get('data', []):
                print(f"URL: {cred.get('url', 'N/A')}")
                print(f"Usuário: {cred.get('username', 'N/A')}")
                print(f"Senha: {cred.get('password', 'N/A')}")
                print("-" * 50)
    
    elif command == "password":
        if len(sys.argv) < 4:
            print("Erro: Senha não especificada")
            return
        password = sys.argv[3]
        result = client.search_by_password(password)
        if result:
            print(f"=== Busca por Senha: {password} ===")
            print(f"Total: {result.get('total', 0)}")
            print(f"Página: {result.get('page', 1)} de {result.get('pages', 1)}")
            print("\nCredenciais encontradas:")
            for cred in result.get('data', []):
                print(f"URL: {cred.get('url', 'N/A')}")
                print(f"Usuário: {cred.get('username', 'N/A')}")
                print(f"Senha: {cred.get('password', 'N/A')}")
                print("-" * 50)
    
    elif command == "user":
        if len(sys.argv) < 4:
            print("Erro: Usuário não especificado")
            return
        username = sys.argv[3]
        result = client.search_by_user(username)
        if result:
            print(f"=== Busca por Usuário: {username} ===")
            print(f"Total: {result.get('total', 0)}")
            print(f"Página: {result.get('page', 1)} de {result.get('pages', 1)}")
            print("\nCredenciais encontradas:")
            for cred in result.get('data', []):
                print(f"URL: {cred.get('url', 'N/A')}")
                print(f"Usuário: {cred.get('username', 'N/A')}")
                print(f"Senha: {cred.get('password', 'N/A')}")
                print("-" * 50)
    
    elif command == "url":
        if len(sys.argv) < 4:
            print("Erro: URL não especificada")
            return
        url = sys.argv[3]
        result = client.search_by_url(url)
        if result:
            print(f"=== Busca por URL: {url} ===")
            print(f"Total: {result.get('total', 0)}")
            print(f"Página: {result.get('page', 1)} de {result.get('pages', 1)}")
            print("\nCredenciais encontradas:")
            for cred in result.get('data', []):
                print(f"URL: {cred.get('url', 'N/A')}")
                print(f"Usuário: {cred.get('username', 'N/A')}")
                print(f"Senha: {cred.get('password', 'N/A')}")
                print("-" * 50)
    
    elif command == "routes":
        if len(sys.argv) < 4:
            print("Erro: Domínio não especificado")
            return
        domain = sys.argv[3]
        result = client.map_domain_routes(domain)
        if result:
            print(f"=== Mapeamento de Rotas: {domain} ===")
            print(f"Total: {result.get('total', 0)}")
            print(f"Página: {result.get('page', 1)} de {result.get('pages', 1)}")
            print("\nRotas encontradas:")
            for route in result.get('rotas', []):
                print(f"URL: {route.get('url', 'N/A')}")
                print("-" * 30)
    
    else:
        print(f"Comando desconhecido: {command}")
        print_help()

if __name__ == "__main__":
    main() 