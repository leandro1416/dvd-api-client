#!/usr/bin/env python3
"""
Script para testar diferentes endereços da API DVD
"""

import requests
import sys

def testar_endereco(base_url, api_key):
    """Testa um endereço específico da API"""
    headers = {
        'Authorization': f'Api-Key {api_key}'
    }
    
    try:
        response = requests.get(f"{base_url}/status", headers=headers, timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ API encontrada em: {base_url}")
            print(f"   Status: {data.get('status', 'N/A')}")
            print(f"   Usuário: {data.get('usuario', 'N/A')}")
            print(f"   Consultas restantes: {data.get('consultas_restantes', 'N/A')}")
            return True
        else:
            print(f"❌ {base_url} - Erro {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print(f"❌ {base_url} - Conexão recusada")
        return False
    except requests.exceptions.Timeout:
        print(f"❌ {base_url} - Timeout")
        return False
    except Exception as e:
        print(f"❌ {base_url} - Erro: {e}")
        return False

def main():
    api_key = "7cd663fefd95cb7b434c1c5ec57c4e00c5d8ca2d68163bfb095c77488c14dbc8"
    
    print("🔍 Testando diferentes endereços da API DVD...")
    print("="*50)
    
    # Lista de endereços para testar
    enderecos = [
        "https://sum.natsec.bot/api",
        "http://localhost:8002/api",
        "http://127.0.0.1:8000/api",
        "http://localhost:8000/api",
        "http://127.0.0.1:3000/api",
        "http://localhost:3000/api",
        "http://127.0.0.1:5000/api",
        "http://localhost:5000/api",
        "http://127.0.0.1:8080/api",
        "http://localhost:8080/api",
        "http://127.0.0.1:8888/api",
        "http://localhost:8888/api"
    ]
    
    encontrado = False
    
    for endereco in enderecos:
        if testar_endereco(endereco, api_key):
            encontrado = True
            print(f"\n🎉 API encontrada! Use este endereço: {endereco}")
            break
        print()
    
    if not encontrado:
        print("\n❌ API não encontrada nos endereços testados.")
        print("\n💡 Verifique:")
        print("1. Se a API está rodando")
        print("2. Se está usando a porta correta")
        print("3. Se não há firewall bloqueando")
        print("\n📋 Para usar quando a API estiver rodando:")
        print("python3 simple_client.py status SUA_API_KEY")
        print("python3 simple_client.py domain SUA_API_KEY exemplo.com.br")

if __name__ == "__main__":
    main() 