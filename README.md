# 🔒 Web Security Header Scanner

Um scanner simples de cabeçalhos de segurança em sites, feito em Python.  
Esse projeto verifica se um site utiliza os principais **HTTP Security Headers**, que ajudam a proteger aplicações web contra ataques como **XSS**, **clickjacking**, entre outros.

## 🚀 Como usar

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/web-security-header-scanner.git
cd web-security-header-scanner

### 2. Crie e ative um ambiente virtual

Linux/Mac:
```bash
python3 -m venv venv
source venv/bin/activate

Windows:
```bash
python -m venv venv
venv\Scripts\activate

### 3. Instale as dependências
```bash
pip install -r requirements.txt

### 4. Execute o scanner
```bash
python scanner_headers.py

O programa pedirá para você digitar a URL de um site. Exemplo:
```less
Digite a URL do site (ex: https://exemplo.com): https://google.com

## 🛡️ Cabeçalhos Verificados
- Content-Security-Policy

- X-Frame-Options

- X-Content-Type-Options

- Strict-Transport-Security

- Referrer-Policy

- Permissions-Policy

Esses headers são boas práticas recomendadas por organizações como OWASP para aumentar a segurança de aplicações web.

### 📂 Estrutura do Projeto
```bash
web_security_header_scanner/
├── scanner_headers.py
├── requirements.txt
└── README.md

### 🧰 Tecnologias

- Python 3.x

- requests

### 🤝 Contribuindo
Contribuições são bem-vindas!
Você pode:

- Criar um fork

- Sugerir melhorias

- Reportar bugs

- Abrir um Pull Request
