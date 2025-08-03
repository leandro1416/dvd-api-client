#!/usr/bin/env python3
"""
Script de teste para verificar a conectividade com a API DVD
"""

import requests
import sys
import time

def testar_conexao_api(api_key, base_url="https://sum.natsec.bot/api"):
    """Testa a conexão com a API"""
    
    print("=== Teste de Conectividade da API DVD ===\n")
    
    headers = {
        'Authorization': f'Api-Key {api_key}'
    }
    
    # Teste 1: Verificar se a API está acessível
    print("1. Testando conectividade básica...")
    try:
        response = requests.get(f"{base_url}/status", headers=headers, timeout=10)
        if response.status_code == 200:
            print("✅ API está acessível")
            data = response.json()
            print(f"   Status: {data.get('status', 'N/A')}")
            print(f"   Usuário: {data.get('usuario', 'N/A')}")
            print(f"   Consultas restantes: {data.get('consultas_restantes', 'N/A')}")
        elif response.status_code == 401:
            print("❌ API Key inválida")
            return False
        elif response.status_code == 404:
            print("❌ Endpoint não encontrado")
            return False
        else:
            print(f"❌ Erro {response.status_code}: {response.text}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Não foi possível conectar com a API")
        print("   Verifique se a API está rodando em:", base_url)
        return False
    except requests.exceptions.Timeout:
        print("❌ Timeout na conexão")
        return False
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return False
    
    print("\n" + "="*50 + "\n")
    
    # Teste 2: Verificar endpoints
    print("2. Testando endpoints...")
    
    endpoints = [
        ("/dominio/exemplo.com.br", "Busca por domínio"),
        ("/senha/123456", "Busca por senha"),
        ("/usuario/admin", "Busca por usuário"),
        ("/url?url=https://exemplo.com.br/login", "Busca por URL"),
        ("/mapear-site/exemplo.com.br", "Mapeamento de rotas")
    ]
    
    for endpoint, descricao in endpoints:
        try:
            print(f"   Testando {descricao}...")
            response = requests.get(f"{base_url}{endpoint}", headers=headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                total = data.get('total', 0)
                print(f"   ✅ {descricao}: OK (Total: {total})")
            elif response.status_code == 404:
                print(f"   ⚠️  {descricao}: Nenhum resultado encontrado")
            elif response.status_code == 401:
                print(f"   ❌ {descricao}: API Key inválida")
            else:
                print(f"   ❌ {descricao}: Erro {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ {descricao}: Erro - {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Teste 3: Verificar limites
    print("3. Testando limites da API...")
    
    try:
        # Testar com página grande
        response = requests.get(
            f"{base_url}/dominio/exemplo.com.br",
            headers=headers,
            params={'page': 1, 'page_size': 10000},  # Acima do limite
            timeout=10
        )
        
        if response.status_code == 200:
            print("✅ API aceita requisições com parâmetros")
        else:
            print(f"⚠️  API retornou erro {response.status_code} para página grande")
            
    except Exception as e:
        print(f"❌ Erro ao testar limites: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Teste 4: Performance
    print("4. Testando performance...")
    
    start_time = time.time()
    try:
        response = requests.get(f"{base_url}/status", headers=headers, timeout=10)
        end_time = time.time()
        
        if response.status_code == 200:
            tempo = (end_time - start_time) * 1000  # Converter para milissegundos
            print(f"✅ Tempo de resposta: {tempo:.2f}ms")
            
            if tempo < 1000:
                print("   ⚡ Resposta rápida")
            elif tempo < 3000:
                print("   🐌 Resposta lenta")
            else:
                print("   🐌 Resposta muito lenta")
        else:
            print("❌ Erro ao testar performance")
            
    except Exception as e:
        print(f"❌ Erro no teste de performance: {e}")
    
    print("\n" + "="*50 + "\n")
    print("✅ Teste de conectividade concluído!")
    return True

def main():
    if len(sys.argv) < 2:
        print("Uso: python teste_conexao.py <API_KEY>")
        print("Exemplo: python teste_conexao.py SUA_API_KEY_AQUI")
        return
    
    api_key = sys.argv[1]
    
    print("Iniciando teste de conectividade...")
    print("Certifique-se de que a API está rodando em https://sum.natsec.bot")
    print()
    
    sucesso = testar_conexao_api(api_key)
    
    if sucesso:
        print("\n🎉 Todos os testes passaram! A API está funcionando corretamente.")
        print("\nPróximos passos:")
        print("1. Execute 'python dvd_api_client.py' para usar a interface gráfica")
        print("2. Execute 'python simple_client.py status SUA_API_KEY' para teste rápido")
        print("3. Execute 'python exemplo_uso.py' para ver exemplos de uso")
    else:
        print("\n❌ Alguns testes falharam. Verifique:")
        print("1. Se a API está rodando em https://sum.natsec.bot")
        print("2. Se a API Key está correta")
        print("3. Se não há firewall bloqueando a conexão")

if __name__ == "__main__":
    main() 