import requests

def verificar_headers(url):
    try:
        resposta = requests.get(url)
        headers = resposta.headers

        print(f"\n[+] Verificando headers de segurança em: {url}\n")

        headers_esperados = [
            "Content-Security-Policy",
            "X-Frame-Options",
            "X-Content-Type-Options",
            "Strict-Transport-Security",
            "Referrer-Policy",
            "Permissions-Policy"
        ]

        for header in headers_esperados:
            if header in headers:
                print(f"[OK] {header}: {headers[header]}")
            else:
                print(f"[FALTA] {header} não encontrado.")

    except Exception as e:
        print(f"Erro ao acessar o site: {e}")

# Exemplo de uso
url = input("Digite a URL (ex: https://exemplo.com): ")
verificar_headers(url)
