import requests
import json
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from urllib.parse import quote
import threading
from datetime import datetime

class DVDAPIClient:
    def __init__(self, api_key, base_url="https://sum.natsec.bot/api"):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            'Authorization': f'Api-Key {api_key}'
        }
    
    def check_status(self):
        """Verifica o status da API"""
        try:
            response = requests.get(f"{self.base_url}/status", headers=self.headers, timeout=30)
            return response.json() if response.status_code == 200 else None
        except Exception as e:
            return {"error": str(e)}
    
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
            return response.json() if response.status_code == 200 else None
        except Exception as e:
            return {"error": str(e)}
    
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
            return response.json() if response.status_code == 200 else None
        except Exception as e:
            return {"error": str(e)}
    
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
            return response.json() if response.status_code == 200 else None
        except Exception as e:
            return {"error": str(e)}
    
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
            return response.json() if response.status_code == 200 else None
        except Exception as e:
            return {"error": str(e)}
    
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
            return response.json() if response.status_code == 200 else None
        except Exception as e:
            return {"error": str(e)}

class DVDAPIGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("DVD API Client")
        self.root.geometry("1000x700")
        self.root.configure(bg='#f0f0f0')
        
        self.api_client = None
        self.setup_ui()
    
    def setup_ui(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configuração da API
        config_frame = ttk.LabelFrame(main_frame, text="Configuração da API", padding="10")
        config_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        ttk.Label(config_frame, text="API Key:").grid(row=0, column=0, sticky=tk.W)
        self.api_key_entry = ttk.Entry(config_frame, width=50, show="*")
        self.api_key_entry.grid(row=0, column=1, padx=(10, 0))
        
        ttk.Label(config_frame, text="Base URL:").grid(row=1, column=0, sticky=tk.W, pady=(10, 0))
        self.base_url_entry = ttk.Entry(config_frame, width=50)
        self.base_url_entry.insert(0, "https://sum.natsec.bot/api")
        self.base_url_entry.grid(row=1, column=1, padx=(10, 0), pady=(10, 0))
        
        ttk.Button(config_frame, text="Testar Conexão", command=self.test_connection).grid(row=2, column=1, pady=(10, 0), sticky=tk.W)
        
        # Frame de busca
        search_frame = ttk.LabelFrame(main_frame, text="Buscar Credenciais", padding="10")
        search_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Tipo de busca
        ttk.Label(search_frame, text="Tipo de Busca:").grid(row=0, column=0, sticky=tk.W)
        self.search_type = tk.StringVar(value="domain")
        search_types = [
            ("Por Domínio", "domain"),
            ("Por Senha", "password"),
            ("Por Usuário", "user"),
            ("Por URL", "url"),
            ("Mapear Rotas", "routes")
        ]
        
        for i, (text, value) in enumerate(search_types):
            ttk.Radiobutton(search_frame, text=text, variable=self.search_type, value=value).grid(row=0, column=i+1, padx=(10, 0))
        
        # Campo de busca
        ttk.Label(search_frame, text="Termo de Busca:").grid(row=1, column=0, sticky=tk.W, pady=(10, 0))
        self.search_entry = ttk.Entry(search_frame, width=60)
        self.search_entry.grid(row=1, column=1, columnspan=4, padx=(10, 0), pady=(10, 0), sticky=(tk.W, tk.E))
        
        # Paginação
        ttk.Label(search_frame, text="Página:").grid(row=2, column=0, sticky=tk.W, pady=(10, 0))
        self.page_entry = ttk.Entry(search_frame, width=10)
        self.page_entry.insert(0, "1")
        self.page_entry.grid(row=2, column=1, padx=(10, 0), pady=(10, 0))
        
        ttk.Label(search_frame, text="Itens por página:").grid(row=2, column=2, sticky=tk.W, pady=(10, 0), padx=(20, 0))
        self.page_size_entry = ttk.Entry(search_frame, width=10)
        self.page_size_entry.insert(0, "500")
        self.page_size_entry.grid(row=2, column=3, padx=(10, 0), pady=(10, 0))
        
        ttk.Button(search_frame, text="Buscar", command=self.search).grid(row=2, column=4, padx=(20, 0), pady=(10, 0))
        
        # Resultados
        results_frame = ttk.LabelFrame(main_frame, text="Resultados", padding="10")
        results_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        
        # Treeview para resultados
        self.tree = ttk.Treeview(results_frame, columns=("url", "username", "password"), show="headings")
        self.tree.heading("url", text="URL")
        self.tree.heading("username", text="Usuário")
        self.tree.heading("password", text="Senha")
        self.tree.column("url", width=300)
        self.tree.column("username", width=200)
        self.tree.column("password", width=150)
        
        # Scrollbar para treeview
        tree_scroll = ttk.Scrollbar(results_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=tree_scroll.set)
        
        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        tree_scroll.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Informações da busca
        self.info_label = ttk.Label(results_frame, text="")
        self.info_label.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 0))
        
        # Configurar grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(2, weight=1)
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(0, weight=1)
    
    def test_connection(self):
        """Testa a conexão com a API"""
        api_key = self.api_key_entry.get().strip()
        base_url = self.base_url_entry.get().strip()
        
        if not api_key:
            messagebox.showerror("Erro", "Por favor, insira a API Key")
            return
        
        self.api_client = DVDAPIClient(api_key, base_url)
        
        def test_thread():
            try:
                result = self.api_client.check_status()
                if result and "error" not in result:
                    messagebox.showinfo("Sucesso", f"API conectada com sucesso!\n\nStatus: {result.get('status', 'N/A')}\nUsuário: {result.get('usuario', 'N/A')}\nConsultas restantes: {result.get('consultas_restantes', 'N/A')}")
                else:
                    error_msg = result.get("error", "Erro desconhecido") if result else "Erro de conexão"
                    messagebox.showerror("Erro", f"Falha na conexão: {error_msg}")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao conectar: {str(e)}")
        
        threading.Thread(target=test_thread, daemon=True).start()
    
    def search(self):
        """Executa a busca baseada no tipo selecionado"""
        if not self.api_client:
            messagebox.showerror("Erro", "Por favor, teste a conexão primeiro")
            return
        
        search_term = self.search_entry.get().strip()
        if not search_term:
            messagebox.showerror("Erro", "Por favor, insira um termo de busca")
            return
        
        try:
            page = int(self.page_entry.get())
            page_size = int(self.page_size_entry.get())
        except ValueError:
            messagebox.showerror("Erro", "Página e itens por página devem ser números")
            return
        
        search_type = self.search_type.get()
        
        def search_thread():
            try:
                result = None
                
                if search_type == "domain":
                    result = self.api_client.search_by_domain(search_term, page, page_size)
                elif search_type == "password":
                    result = self.api_client.search_by_password(search_term, page, page_size)
                elif search_type == "user":
                    result = self.api_client.search_by_user(search_term, page, page_size)
                elif search_type == "url":
                    result = self.api_client.search_by_url(search_term, page, page_size)
                elif search_type == "routes":
                    result = self.api_client.map_domain_routes(search_term, page, page_size)
                
                self.root.after(0, lambda: self.display_results(result, search_type))
                
            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror("Erro", f"Erro na busca: {str(e)}"))
        
        threading.Thread(target=search_thread, daemon=True).start()
    
    def display_results(self, result, search_type):
        """Exibe os resultados na interface"""
        # Limpar resultados anteriores
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        if not result or "error" in result:
            error_msg = result.get("error", "Nenhum resultado encontrado") if result else "Erro na busca"
            self.info_label.config(text=f"Erro: {error_msg}")
            return
        
        # Exibir informações da busca
        if search_type == "routes":
            total = result.get("total", 0)
            pages = result.get("pages", 0)
            domain = result.get("dominio", "")
            self.info_label.config(text=f"Domínio: {domain} | Total de rotas: {total} | Páginas: {pages}")
            
            # Para rotas, mostrar apenas URLs
            for route in result.get("rotas", []):
                self.tree.insert("", "end", values=(route.get("url", ""), "", ""))
        else:
            total = result.get("total", 0)
            pages = result.get("pages", 0)
            current_page = result.get("page", 1)
            self.info_label.config(text=f"Total: {total} | Página {current_page} de {pages}")
            
            # Para credenciais, mostrar URL, usuário e senha
            for cred in result.get("data", []):
                self.tree.insert("", "end", values=(
                    cred.get("url", ""),
                    cred.get("username", ""),
                    cred.get("password", "")
                ))

def main():
    root = tk.Tk()
    app = DVDAPIGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 