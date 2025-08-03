#!/bin/bash
# Script para ativar o ambiente virtual e executar o cliente

echo "🚀 Ativando ambiente virtual..."
source venv/bin/activate

echo "✅ Ambiente virtual ativado!"
echo ""
echo "📋 Comandos disponíveis:"
echo ""
echo "1. Interface gráfica:"
echo "   python dvd_api_client.py"
echo ""
echo "2. Linha de comando:"
echo "   python simple_client.py status SUA_API_KEY"
echo "   python simple_client.py domain SUA_API_KEY exemplo.com.br"
echo ""
echo "3. Teste de conectividade:"
echo "   python teste_conexao.py SUA_API_KEY"
echo ""
echo "4. Exemplos de uso:"
echo "   python exemplo_uso.py"
echo ""
echo "5. Para desativar o ambiente:"
echo "   deactivate"
echo ""

# Verificar se foi passado um comando
if [ $# -eq 0 ]; then
    echo "💡 Dica: Execute 'python dvd_api_client.py' para usar a interface gráfica"
    echo "💡 Dica: Execute 'python teste_conexao.py SUA_API_KEY' para testar a conexão"
else
    echo "Executando: $@"
    python "$@"
fi 