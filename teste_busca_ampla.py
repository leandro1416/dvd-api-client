#!/usr/bin/env python3
"""
Teste da busca ampla do bot
"""

import requests
import json
from urllib.parse import quote

# Configurações
API_BASE_URL = "https://sum.natsec.bot/api"
API_KEY = "7cd663fefd95cb7b434c1c5ec57c4e00c5d8ca2d68163bfb095c77488c14dbc8"

headers = {
    'Authorization': f'Api-Key {API_KEY}',
    'User-Agent': 'DVD-API-Bot/1.0'
}

def test_search_terms():
    """Testa diferentes termos de busca"""
    test_terms = ["gmail", "hotmail", "claro", "gol", "mulvipay"]
    
    print("🔍 TESTE DA BUSCA AMPLA")
    print("=" * 50)
    
    for term in test_terms:
        print(f"\n📋 Testando termo: '{term}'")
        
        # Busca por domínio
        try:
            encoded_term = quote(term)
            url = f"{API_BASE_URL}/dominio/{encoded_term}"
            response = requests.get(url, headers=headers, params={'page': 1, 'page_size': 5}, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                total = data.get('total', 0)
                results = len(data.get('data', []))
                print(f"  ✅ Domínio: {total} total, {results} resultados")
                
                # Mostrar alguns resultados
                for i, item in enumerate(data.get('data', [])[:3]):
                    print(f"    {i+1}. URL: {item.get('url', 'N/A')}")
                    print(f"       👤: {item.get('username', 'N/A')}")
                    print(f"       🔑: {item.get('password', 'N/A')}")
            else:
                print(f"  ❌ Erro {response.status_code}: {response.text}")
                
        except Exception as e:
            print(f"  ❌ Erro: {e}")
        
        # Busca por URL
        try:
            url = f"{API_BASE_URL}/url"
            response = requests.get(url, headers=headers, params={'url': term, 'page': 1, 'page_size': 5}, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                total = data.get('total', 0)
                results = len(data.get('data', []))
                print(f"  ✅ URL: {total} total, {results} resultados")
            else:
                print(f"  ❌ Erro {response.status_code}: {response.text}")
                
        except Exception as e:
            print(f"  ❌ Erro: {e}")

def test_partial_search():
    """Testa busca parcial em claro.com.br"""
    print("\n🔍 TESTE DE BUSCA PARCIAL")
    print("=" * 50)
    
    # Buscar todos os dados de claro.com.br
    try:
        url = f"{API_BASE_URL}/dominio/claro.com.br"
        response = requests.get(url, headers=headers, params={'page': 1, 'page_size': 50}, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            all_results = data.get('data', [])
            
            # Testar diferentes termos
            test_terms = ["gmail", "hotmail", "claro", "gol"]
            
            for term in test_terms:
                print(f"\n📋 Buscando '{term}' em claro.com.br:")
                filtered = []
                term_lower = term.lower()
                
                for item in all_results:
                    url_text = item.get('url', '').lower()
                    username = item.get('username', '').lower()
                    password = item.get('password', '').lower()
                    
                    if (term_lower in url_text or 
                        term_lower in username or 
                        term_lower in password):
                        filtered.append(item)
                
                print(f"  ✅ Encontrados {len(filtered)} resultados")
                
                # Mostrar alguns resultados
                for i, item in enumerate(filtered[:3]):
                    print(f"    {i+1}. URL: {item.get('url', 'N/A')}")
                    print(f"       👤: {item.get('username', 'N/A')}")
                    print(f"       🔑: {item.get('password', 'N/A')}")
                    
        else:
            print(f"❌ Erro {response.status_code}: {response.text}")
            
    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    test_search_terms()
    test_partial_search()
    print("\n✅ Teste concluído!") 