import requests
import re

def extrair_id_limpo(dado):
    if not dado:
        return None
    if isinstance(dado, list) and len(dado) > 0:
        dado = dado[0]
    match = re.search(r"\d{30,}", str(dado))
    return match.group(0) if match else None

slug = "bitcoin-up-or-down-on-february-7"
url = f"https://gamma-api.polymarket.com/events?slug={slug}"

print(f"🔍 Consultando API para slug: {slug}")
resp = requests.get(url).json()

for event in resp:
    for m in event.get("markets", []):
        print("Pergunta:", m.get("question"))
        print("clobTokenIds bruto:", m.get("clobTokenIds"))
        print("Token limpo:", extrair_id_limpo(m.get("clobTokenIds")))
