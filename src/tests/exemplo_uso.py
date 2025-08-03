#!/usr/bin/env python3
"""
Exemplo de uso da API DVD
Este script demonstra como usar a API programaticamente
"""

from dvd_api_client import DVDAPIClient
import json

def exemplo_completo():
    """Exemplo completo de uso da API"""
    
    # Configuração
    API_KEY = "SUA_API_KEY_AQUI"  # Substitua pela sua API Key
    BASE_URL = "https://sum.natsec.bot/api"
    
    # Criar cliente
    client = DVDAPIClient(API_KEY, BASE_URL)
    
    print("=== Exemplo de Uso da API DVD ===\n")
    
    # 1. Verificar status da API
    print("1. Verificando status da API...")
    status = client.check_status()
    if status and "error" not in status:
        print(f"✅ API funcionando!")
        print(f"   Status: {status.get('status', 'N/A')}")
        print(f"   Usuário: {status.get('usuario', 'N/A')}")
        print(f"   Consultas restantes: {status.get('consultas_restantes', 'N/A')}")
        print(f"   Limite diário: {status.get('limite_diario', 'N/A')}")
    else:
        print("❌ Erro ao conectar com a API")
        return
    
    print("\n" + "="*50 + "\n")
    
    # 2. Buscar por domínio
    print("2. Buscando credenciais por domínio...")
    dominio = "exemplo.com.br"
    result_domain = client.search_by_domain(dominio)
    
    if result_domain and "error" not in result_domain:
        print(f"✅ Encontradas {result_domain.get('total', 0)} credenciais para {dominio}")
        print(f"   Página {result_domain.get('page', 1)} de {result_domain.get('pages', 1)}")
        
        # Mostrar primeiras 3 credenciais
        for i, cred in enumerate(result_domain.get('data', [])[:3]):
            print(f"   Credencial {i+1}:")
            print(f"     URL: {cred.get('url', 'N/A')}")
            print(f"     Usuário: {cred.get('username', 'N/A')}")
            print(f"     Senha: {cred.get('password', 'N/A')}")
    else:
        print(f"❌ Nenhuma credencial encontrada para {dominio}")
    
    print("\n" + "="*50 + "\n")
    
    # 3. Buscar por senha
    print("3. Buscando credenciais por senha...")
    senha = "123456"
    result_password = client.search_by_password(senha)
    
    if result_password and "error" not in result_password:
        print(f"✅ Encontradas {result_password.get('total', 0)} credenciais com senha '{senha}'")
        print(f"   Página {result_password.get('page', 1)} de {result_password.get('pages', 1)}")
        
        # Mostrar primeiras 3 credenciais
        for i, cred in enumerate(result_password.get('data', [])[:3]):
            print(f"   Credencial {i+1}:")
            print(f"     URL: {cred.get('url', 'N/A')}")
            print(f"     Usuário: {cred.get('username', 'N/A')}")
            print(f"     Senha: {cred.get('password', 'N/A')}")
    else:
        print(f"❌ Nenhuma credencial encontrada com senha '{senha}'")
    
    print("\n" + "="*50 + "\n")
    
    # 4. Buscar por usuário
    print("4. Buscando credenciais por usuário...")
    usuario = "admin@empresa.com"
    result_user = client.search_by_user(usuario)
    
    if result_user and "error" not in result_user:
        print(f"✅ Encontradas {result_user.get('total', 0)} credenciais para usuário '{usuario}'")
        print(f"   Página {result_user.get('page', 1)} de {result_user.get('pages', 1)}")
        
        # Mostrar primeiras 3 credenciais
        for i, cred in enumerate(result_user.get('data', [])[:3]):
            print(f"   Credencial {i+1}:")
            print(f"     URL: {cred.get('url', 'N/A')}")
            print(f"     Usuário: {cred.get('username', 'N/A')}")
            print(f"     Senha: {cred.get('password', 'N/A')}")
    else:
        print(f"❌ Nenhuma credencial encontrada para usuário '{usuario}'")
    
    print("\n" + "="*50 + "\n")
    
    # 5. Buscar por URL
    print("5. Buscando credenciais por URL...")
    url = "https://exemplo.com.br/login"
    result_url = client.search_by_url(url)
    
    if result_url and "error" not in result_url:
        print(f"✅ Encontradas {result_url.get('total', 0)} credenciais para URL '{url}'")
        print(f"   Página {result_url.get('page', 1)} de {result_url.get('pages', 1)}")
        
        # Mostrar primeiras 3 credenciais
        for i, cred in enumerate(result_url.get('data', [])[:3]):
            print(f"   Credencial {i+1}:")
            print(f"     URL: {cred.get('url', 'N/A')}")
            print(f"     Usuário: {cred.get('username', 'N/A')}")
            print(f"     Senha: {cred.get('password', 'N/A')}")
    else:
        print(f"❌ Nenhuma credencial encontrada para URL '{url}'")
    
    print("\n" + "="*50 + "\n")
    
    # 6. Mapear rotas de domínio
    print("6. Mapeando rotas de domínio...")
    dominio_mapear = "exemplo.com.br"
    result_routes = client.map_domain_routes(dominio_mapear)
    
    if result_routes and "error" not in result_routes:
        print(f"✅ Encontradas {result_routes.get('total', 0)} rotas para {dominio_mapear}")
        print(f"   Página {result_routes.get('page', 1)} de {result_routes.get('pages', 1)}")
        
        # Mostrar primeiras 5 rotas
        for i, route in enumerate(result_routes.get('rotas', [])[:5]):
            print(f"   Rota {i+1}: {route.get('url', 'N/A')}")
    else:
        print(f"❌ Nenhuma rota encontrada para {dominio_mapear}")
    
    print("\n" + "="*50 + "\n")
    print("✅ Exemplo concluído!")

def exemplo_paginacao():
    """Exemplo de como buscar todas as páginas"""
    
    API_KEY = "SUA_API_KEY_AQUI"  # Substitua pela sua API Key
    client = DVDAPIClient(API_KEY)
    
    print("=== Exemplo de Paginação ===\n")
    
    dominio = "exemplo.com.br"
    todas_credenciais = []
    page = 1
    
    print(f"Buscando todas as credenciais para {dominio}...")
    
    while True:
        print(f"Buscando página {page}...")
        result = client.search_by_domain(dominio, page, 500)
        
        if not result or "error" in result:
            print(f"Erro na página {page} ou fim dos resultados")
            break
        
        credenciais_pagina = result.get('data', [])
        todas_credenciais.extend(credenciais_pagina)
        
        print(f"   Encontradas {len(credenciais_pagina)} credenciais na página {page}")
        
        if page >= result.get('pages', 1):
            print("   Última página alcançada")
            break
        
        page += 1
    
    print(f"\n✅ Total de credenciais encontradas: {len(todas_credenciais)}")
    
    # Mostrar algumas credenciais
    for i, cred in enumerate(todas_credenciais[:5]):
        print(f"\nCredencial {i+1}:")
        print(f"  URL: {cred.get('url', 'N/A')}")
        print(f"  Usuário: {cred.get('username', 'N/A')}")
        print(f"  Senha: {cred.get('password', 'N/A')}")

def exemplo_exportar_json():
    """Exemplo de como exportar resultados para JSON"""
    
    API_KEY = "SUA_API_KEY_AQUI"  # Substitua pela sua API Key
    client = DVDAPIClient(API_KEY)
    
    print("=== Exemplo de Exportação JSON ===\n")
    
    # Buscar credenciais
    result = client.search_by_domain("exemplo.com.br")
    
    if result and "error" not in result:
        # Salvar em arquivo JSON
        with open('credenciais_exportadas.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Exportadas {len(result.get('data', []))} credenciais para 'credenciais_exportadas.json'")
        print("   Arquivo salvo com sucesso!")
    else:
        print("❌ Erro ao buscar credenciais para exportação")

if __name__ == "__main__":
    print("Escolha um exemplo:")
    print("1. Exemplo completo")
    print("2. Exemplo de paginação")
    print("3. Exemplo de exportação JSON")
    
    try:
        escolha = input("\nDigite sua escolha (1-3): ").strip()
        
        if escolha == "1":
            exemplo_completo()
        elif escolha == "2":
            exemplo_paginacao()
        elif escolha == "3":
            exemplo_exportar_json()
        else:
            print("Escolha inválida. Executando exemplo completo...")
            exemplo_completo()
    
    except KeyboardInterrupt:
        print("\n\nOperação cancelada pelo usuário.")
    except Exception as e:
        print(f"\nErro: {e}")
        print("\nDica: Verifique se a API está rodando e se a API Key está correta.") 