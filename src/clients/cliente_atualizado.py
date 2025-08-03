#!/usr/bin/env python3
"""
Cliente atualizado para a API DVD com endereço correto
"""

import requests
import json
import sys
from urllib.parse import quote

class DVDAPIClient:
    def __init__(self, api_key, base_url="https://sum.natsec.bot/api"):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            'Authorization': f'Bearer {api_key}'  # Usando Bearer em vez de Api-Key
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

def main():
    # API Key fornecida
    API_KEY = "7cd663fefd95cb7b434c1c5ec57c4e00c5d8ca2d68163bfb095c77488c14dbc8"
    
    # Criar cliente
    client = DVDAPIClient(API_KEY)
    
    print("🎉 Cliente DVD API - Conectado!")
    print("="*50)
    
    # Testar conexão
    print("1. Testando conexão...")
    status = client.check_status()
    if status:
        print(f"✅ API funcionando!")
        print(f"   Status: {status.get('status', 'N/A')}")
        print(f"   Timestamp: {status.get('timestamp', 'N/A')}")
    else:
        print("❌ Erro ao conectar com a API")
        return
    
    print("\n" + "="*50)
    
    # Menu interativo
    while True:
        print("\n📋 Escolha uma opção:")
        print("1. Buscar por domínio")
        print("2. Buscar por senha")
        print("3. Buscar por usuário")
        print("4. Buscar por URL")
        print("5. Mapear rotas de domínio")
        print("6. Testar conexão novamente")
        print("0. Sair")
        
        try:
            opcao = input("\nDigite sua escolha (0-6): ").strip()
            
            if opcao == "0":
                print("👋 Até logo!")
                break
            elif opcao == "1":
                dominio = input("Digite o domínio (ex: exemplo.com.br): ").strip()
                if dominio:
                    result = client.search_by_domain(dominio)
                    if result:
                        print(f"\n✅ Encontradas {result.get('total', 0)} credenciais para {dominio}")
                        for i, cred in enumerate(result.get('data', [])[:5]):
                            print(f"\nCredencial {i+1}:")
                            print(f"  URL: {cred.get('url', 'N/A')}")
                            print(f"  Usuário: {cred.get('username', 'N/A')}")
                            print(f"  Senha: {cred.get('password', 'N/A')}")
                    else:
                        print("❌ Nenhuma credencial encontrada")
            elif opcao == "2":
                senha = input("Digite a senha: ").strip()
                if senha:
                    result = client.search_by_password(senha)
                    if result:
                        print(f"\n✅ Encontradas {result.get('total', 0)} credenciais com senha '{senha}'")
                        for i, cred in enumerate(result.get('data', [])[:5]):
                            print(f"\nCredencial {i+1}:")
                            print(f"  URL: {cred.get('url', 'N/A')}")
                            print(f"  Usuário: {cred.get('username', 'N/A')}")
                            print(f"  Senha: {cred.get('password', 'N/A')}")
                    else:
                        print("❌ Nenhuma credencial encontrada")
            elif opcao == "3":
                usuario = input("Digite o usuário: ").strip()
                if usuario:
                    result = client.search_by_user(usuario)
                    if result:
                        print(f"\n✅ Encontradas {result.get('total', 0)} credenciais para usuário '{usuario}'")
                        for i, cred in enumerate(result.get('data', [])[:5]):
                            print(f"\nCredencial {i+1}:")
                            print(f"  URL: {cred.get('url', 'N/A')}")
                            print(f"  Usuário: {cred.get('username', 'N/A')}")
                            print(f"  Senha: {cred.get('password', 'N/A')}")
                    else:
                        print("❌ Nenhuma credencial encontrada")
            elif opcao == "4":
                url = input("Digite a URL: ").strip()
                if url:
                    result = client.search_by_url(url)
                    if result:
                        print(f"\n✅ Encontradas {result.get('total', 0)} credenciais para URL '{url}'")
                        for i, cred in enumerate(result.get('data', [])[:5]):
                            print(f"\nCredencial {i+1}:")
                            print(f"  URL: {cred.get('url', 'N/A')}")
                            print(f"  Usuário: {cred.get('username', 'N/A')}")
                            print(f"  Senha: {cred.get('password', 'N/A')}")
                    else:
                        print("❌ Nenhuma credencial encontrada")
            elif opcao == "5":
                dominio = input("Digite o domínio para mapear rotas: ").strip()
                if dominio:
                    result = client.map_domain_routes(dominio)
                    if result:
                        print(f"\n✅ Encontradas {result.get('total', 0)} rotas para {dominio}")
                        for i, route in enumerate(result.get('rotas', [])[:10]):
                            print(f"  Rota {i+1}: {route.get('url', 'N/A')}")
                    else:
                        print("❌ Nenhuma rota encontrada")
            elif opcao == "6":
                status = client.check_status()
                if status:
                    print(f"✅ API funcionando! Status: {status.get('status', 'N/A')}")
                else:
                    print("❌ Erro ao conectar com a API")
            else:
                print("❌ Opção inválida")
                
        except KeyboardInterrupt:
            print("\n\n👋 Até logo!")
            break
        except Exception as e:
            print(f"❌ Erro: {e}")

if __name__ == "__main__":
    main() 