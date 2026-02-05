import os
import time

print("🤖 Bot Polymarket iniciado")

MARKET_ID = os.getenv("MARKET_ID")
SIDE = os.getenv("SIDE")
BUY_PRICE = os.getenv("BUY_PRICE")
SELL_PRICE = os.getenv("SELL_PRICE")
ORDER_SIZE = os.getenv("ORDER_SIZE")

while True:
    print("🟢 Bot rodando...")
    print("Mercado:", MARKET_ID)
    print("Lado:", SIDE)
    print("Compra:", BUY_PRICE)
    print("Venda:", SELL_PRICE)
    print("Tamanho:", ORDER_SIZE)
    time.sleep(30)
