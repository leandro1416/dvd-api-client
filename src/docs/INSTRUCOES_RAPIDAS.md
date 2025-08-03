# 🚀 Instruções Rápidas - Cliente DVD API

## ⚡ Começar em 3 Passos

### 1. Ativar o Ambiente
```bash
./ativar.sh
```

### 2. Testar a Conexão
```bash
python teste_conexao.py SUA_API_KEY
```

### 3. Usar a Interface Gráfica
```bash
python dvd_api_client.py
```

## 📋 Comandos Principais

### Interface Gráfica (Recomendado)
```bash
python dvd_api_client.py
```
- Abre uma interface gráfica completa
- Teste de conexão integrado
- Busca por domínio, senha, usuário, URL e rotas
- Paginação automática

### Linha de Comando
```bash
# Testar conexão
python simple_client.py status SUA_API_KEY

# Buscar por domínio
python simple_client.py domain SUA_API_KEY exemplo.com.br

# Buscar por senha
python simple_client.py password SUA_API_KEY 123456

# Buscar por usuário
python simple_client.py user SUA_API_KEY admin@empresa.com

# Buscar por URL
python simple_client.py url SUA_API_KEY "https://exemplo.com.br/login"

# Mapear rotas
python simple_client.py routes SUA_API_KEY exemplo.com.br
```

### Teste de Conectividade
```bash
python teste_conexao.py SUA_API_KEY
```

### Exemplos de Uso
```bash
python exemplo_uso.py
```

## 🔧 Configuração

### API Key
Substitua `SUA_API_KEY` pela sua chave real da API.

### Base URL
A API deve estar rodando em: `http://127.0.0.1:8002`

## 📁 Arquivos Importantes

- `dvd_api_client.py` - Interface gráfica completa
- `simple_client.py` - Cliente de linha de comando
- `teste_conexao.py` - Script de teste
- `exemplo_uso.py` - Exemplos de uso
- `ativar.sh` - Script para ativar ambiente
- `README.md` - Documentação completa

## ❗ Solução de Problemas

### Erro: "API não encontrada"
- Verifique se a API está rodando em `http://127.0.0.1:8002`

### Erro: "API Key inválida"
- Verifique se a API Key está correta

### Erro: "tkinter não encontrado"
- No macOS: tkinter já vem com Python
- No Linux: `sudo apt-get install python3-tk`

### Erro: "Ambiente virtual não ativado"
- Execute: `source venv/bin/activate`

## 🎯 Exemplo Rápido

```bash
# 1. Ativar ambiente
./ativar.sh

# 2. Testar conexão
python teste_conexao.py MINHA_API_KEY

# 3. Usar interface gráfica
python dvd_api_client.py
```

## 📖 Documentação Completa

Para instruções detalhadas, leia o arquivo `README.md`. 