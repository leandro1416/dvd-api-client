#!/usr/bin/env python3
"""
DVD API Client - Arquivo principal
Permite executar diferentes componentes do projeto
"""

import sys
import os
import argparse
from pathlib import Path

# Adiciona o diretório src ao path
sys.path.insert(0, str(Path(__file__).parent / "src"))

def main():
    parser = argparse.ArgumentParser(description="DVD API Client - Interface principal")
    parser.add_argument("component", choices=["gui", "web", "bot", "test"], 
                       help="Componente a ser executado")
    parser.add_argument("--api-key", help="Sua API Key")
    parser.add_argument("--host", default="127.0.0.1", help="Host para servidor web")
    parser.add_argument("--port", type=int, default=5000, help="Porta para servidor web")
    
    args = parser.parse_args()
    
    if args.component == "gui":
        print("Iniciando interface gráfica...")
        from clients.dvd_api_client import main as gui_main
        gui_main()
        
    elif args.component == "web":
        print(f"Iniciando servidor web em http://{args.host}:{args.port}")
        from web.app_web_optimized import app
        app.run(host=args.host, port=args.port, debug=True)
        
    elif args.component == "bot":
        print("Iniciando bot do Telegram...")
        from scripts.telegram_bot import main as bot_main
        bot_main()
        
    elif args.component == "test":
        print("Executando testes...")
        from tests.teste_conexao import main as test_main
        test_main()

if __name__ == "__main__":
    main() 