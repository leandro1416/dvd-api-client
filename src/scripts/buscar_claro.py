#!/usr/bin/env python3
"""
Script para buscar por claro.com.br e salvar resultados
"""

import requests
import json
from urllib.parse import quote
from datetime import datetime

# Configuração da API
API_KEY = "7cd663fefd95cb7b434c1c5ec57c4e00c5d8ca2d68163bfb095c77488c14dbc8"
BASE_URL = "https://sum.natsec.bot/api"

headers = {
    'Authorization': f'Bearer {API_KEY}',
    'User-Agent': 'DVD-API-Client/1.0'
}

def buscar_por_dominio(dominio):
    """Busca credenciais por domínio"""
    try:
        encoded_dominio = quote(dominio)
        response = requests.get(
            f"{BASE_URL}/dominio/{encoded_dominio}",
            headers=headers,
            timeout=30
        )
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Erro {response.status_code}: {response.text}"}
    except Exception as e:
        return {"error": f"Erro de busca: {e}"}

def buscar_por_url(url):
    """Busca credenciais por URL"""
    try:
        params = {'url': url}
        response = requests.get(
            f"{BASE_URL}/url",
            headers=headers,
            params=params,
            timeout=30
        )
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Erro {response.status_code}: {response.text}"}
    except Exception as e:
        return {"error": f"Erro de busca: {e}"}

def mapear_rotas(dominio):
    """Mapeia rotas de um domínio"""
    try:
        encoded_dominio = quote(dominio)
        response = requests.get(
            f"{BASE_URL}/mapear-site/{encoded_dominio}",
            headers=headers,
            timeout=30
        )
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Erro {response.status_code}: {response.text}"}
    except Exception as e:
        return {"error": f"Erro de busca: {e}"}

def salvar_resultados(resultados, nome_arquivo):
    """Salva resultados em arquivo JSON"""
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            json.dump(resultados, f, indent=2, ensure_ascii=False)
        print(f"✅ Resultados salvos em: {nome_arquivo}")
        return True
    except Exception as e:
        print(f"❌ Erro ao salvar arquivo: {e}")
        return False

def main():
    dominio = "claro.com.br"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_arquivo = f"resultados_claro_{timestamp}.json"
    
    print("🔍 Iniciando busca por claro.com.br...")
    print("="*50)
    
    resultados = {
        "dominio": dominio,
        "timestamp_busca": datetime.now().isoformat(),
        "buscas": {}
    }
    
    # 1. Buscar por domínio
    print("1. Buscando por domínio...")
    resultado_dominio = buscar_por_dominio(dominio)
    resultados["buscas"]["por_dominio"] = resultado_dominio
    
    if resultado_dominio.get("error"):
        print(f"❌ Erro na busca por domínio: {resultado_dominio['error']}")
    else:
        total = resultado_dominio.get("total", 0)
        print(f"✅ Encontradas {total} credenciais por domínio")
    
    # 2. Buscar por URL específica
    print("\n2. Buscando por URL específica...")
    url_especifica = f"https://{dominio}/login"
    resultado_url = buscar_por_url(url_especifica)
    resultados["buscas"]["por_url_login"] = resultado_url
    
    if resultado_url.get("error"):
        print(f"❌ Erro na busca por URL: {resultado_url['error']}")
    else:
        total = resultado_url.get("total", 0)
        print(f"✅ Encontradas {total} credenciais para {url_especifica}")
    
    # 3. Buscar por outras URLs comuns
    urls_comuns = [
        f"https://{dominio}/admin",
        f"https://{dominio}/portal",
        f"https://{dominio}/acesso",
        f"https://{dominio}/user",
        f"https://{dominio}/account"
    ]
    
    print("\n3. Buscando por URLs comuns...")
    resultados["buscas"]["por_urls_comuns"] = {}
    
    for url in urls_comuns:
        print(f"   Buscando: {url}")
        resultado = buscar_por_url(url)
        resultados["buscas"]["por_urls_comuns"][url] = resultado
        
        if resultado.get("error"):
            print(f"   ❌ Erro: {resultado['error']}")
        else:
            total = resultado.get("total", 0)
            print(f"   ✅ Encontradas {total} credenciais")
    
    # 4. Mapear rotas do domínio
    print("\n4. Mapeando rotas do domínio...")
    resultado_rotas = mapear_rotas(dominio)
    resultados["buscas"]["mapeamento_rotas"] = resultado_rotas
    
    if resultado_rotas.get("error"):
        print(f"❌ Erro no mapeamento: {resultado_rotas['error']}")
    else:
        total = resultado_rotas.get("total", 0)
        print(f"✅ Encontradas {total} rotas")
    
    # 5. Resumo dos resultados
    print("\n" + "="*50)
    print("📊 RESUMO DOS RESULTADOS:")
    print("="*50)
    
    total_credenciais = 0
    total_rotas = 0
    
    # Contar credenciais por domínio
    if "por_dominio" in resultados["buscas"] and not resultados["buscas"]["por_dominio"].get("error"):
        total_credenciais += resultados["buscas"]["por_dominio"].get("total", 0)
        print(f"🌐 Por domínio: {resultados['buscas']['por_dominio'].get('total', 0)} credenciais")
    
    # Contar credenciais por URLs
    if "por_url_login" in resultados["buscas"] and not resultados["buscas"]["por_url_login"].get("error"):
        total_credenciais += resultados["buscas"]["por_url_login"].get("total", 0)
        print(f"🔗 Por URL login: {resultados['buscas']['por_url_login'].get('total', 0)} credenciais")
    
    # Contar credenciais por URLs comuns
    if "por_urls_comuns" in resultados["buscas"]:
        for url, resultado in resultados["buscas"]["por_urls_comuns"].items():
            if not resultado.get("error"):
                total_credenciais += resultado.get("total", 0)
                print(f"🔗 {url}: {resultado.get('total', 0)} credenciais")
    
    # Contar rotas
    if "mapeamento_rotas" in resultados["buscas"] and not resultados["buscas"]["mapeamento_rotas"].get("error"):
        total_rotas = resultados["buscas"]["mapeamento_rotas"].get("total", 0)
        print(f"🗺️ Total de rotas: {total_rotas}")
    
    print(f"\n📈 TOTAL GERAL:")
    print(f"   Credenciais encontradas: {total_credenciais}")
    print(f"   Rotas mapeadas: {total_rotas}")
    
    # Salvar resultados
    print(f"\n💾 Salvando resultados...")
    if salvar_resultados(resultados, nome_arquivo):
        print(f"✅ Busca concluída! Arquivo salvo: {nome_arquivo}")
    else:
        print("❌ Erro ao salvar arquivo")

if __name__ == "__main__":
    main() 