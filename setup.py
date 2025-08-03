#!/usr/bin/env python3
"""
Script de setup para o cliente DVD API
"""

import subprocess
import sys
import os

def verificar_python():
    """Verifica se o Python está instalado"""
    print("Verificando versão do Python...")
    try:
        version = sys.version_info
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} encontrado")
        return True
    except Exception as e:
        print(f"❌ Erro ao verificar Python: {e}")
        return False

def instalar_dependencias():
    """Instala as dependências do projeto"""
    print("\nInstalando dependências...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependências instaladas com sucesso!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao instalar dependências: {e}")
        return False
    except FileNotFoundError:
        print("❌ pip não encontrado. Verifique se o Python está instalado corretamente.")
        return False

def testar_tkinter():
    """Testa se o tkinter está disponível"""
    print("\nTestando tkinter...")
    try:
        import tkinter
        print("✅ tkinter está disponível")
        return True
    except ImportError:
        print("❌ tkinter não está disponível")
        print("   No Ubuntu/Debian: sudo apt-get install python3-tk")
        print("   No CentOS/RHEL: sudo yum install tkinter")
        print("   No macOS: tkinter vem com o Python")
        return False

def criar_arquivo_config():
    """Cria um arquivo de configuração de exemplo"""
    config_content = """# Configuração da API DVD
# Substitua pelos seus valores reais

API_KEY = "SUA_API_KEY_AQUI"
BASE_URL = "https://sum.natsec.bot/api"

# Exemplo de uso:
# from dvd_api_client import DVDAPIClient
# client = DVDAPIClient(API_KEY, BASE_URL)
# status = client.check_status()
"""
    
    try:
        with open("config.py", "w", encoding="utf-8") as f:
            f.write(config_content)
        print("✅ Arquivo config.py criado")
        return True
    except Exception as e:
        print(f"❌ Erro ao criar config.py: {e}")
        return False

def mostrar_instrucoes():
    """Mostra instruções de uso"""
    print("\n" + "="*60)
    print("🎉 INSTALAÇÃO CONCLUÍDA!")
    print("="*60)
    
    print("\n📋 COMO USAR:")
    print("\n1. Interface Gráfica (Recomendado):")
    print("   python dvd_api_client.py")
    
    print("\n2. Linha de Comando:")
    print("   python simple_client.py status SUA_API_KEY")
    print("   python simple_client.py domain SUA_API_KEY exemplo.com.br")
    
    print("\n3. Teste de Conectividade:")
    print("   python teste_conexao.py SUA_API_KEY")
    
    print("\n4. Exemplos de Uso:")
    print("   python exemplo_uso.py")
    
    print("\n📁 ARQUIVOS CRIADOS:")
    print("   - dvd_api_client.py: Cliente com interface gráfica")
    print("   - simple_client.py: Cliente de linha de comando")
    print("   - teste_conexao.py: Script de teste")
    print("   - exemplo_uso.py: Exemplos de uso")
    print("   - config.py: Arquivo de configuração")
    print("   - requirements.txt: Dependências")
    print("   - README.md: Documentação completa")
    
    print("\n⚠️  PRÓXIMOS PASSOS:")
    print("1. Certifique-se de que a API está rodando em https://sum.natsec.bot")
    print("2. Substitua 'SUA_API_KEY_AQUI' pela sua API Key real")
    print("3. Execute 'python teste_conexao.py SUA_API_KEY' para testar")
    print("4. Execute 'python dvd_api_client.py' para usar a interface gráfica")
    
    print("\n📖 DOCUMENTAÇÃO:")
    print("   Leia o arquivo README.md para instruções detalhadas")
    
    print("\n" + "="*60)

def main():
    """Função principal do setup"""
    print("🚀 Setup do Cliente DVD API")
    print("="*40)
    
    # Verificar Python
    if not verificar_python():
        print("❌ Python não encontrado. Instale o Python 3.7+ primeiro.")
        return False
    
    # Instalar dependências
    if not instalar_dependencias():
        print("❌ Falha ao instalar dependências.")
        return False
    
    # Testar tkinter
    if not testar_tkinter():
        print("⚠️  tkinter não está disponível. A interface gráfica pode não funcionar.")
    
    # Criar arquivo de configuração
    criar_arquivo_config()
    
    # Mostrar instruções
    mostrar_instrucoes()
    
    return True

if __name__ == "__main__":
    try:
        sucesso = main()
        if sucesso:
            print("\n✅ Setup concluído com sucesso!")
        else:
            print("\n❌ Setup falhou. Verifique os erros acima.")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nSetup cancelado pelo usuário.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        sys.exit(1) 