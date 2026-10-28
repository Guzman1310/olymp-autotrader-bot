# CONFIGURACIÓN DEL AUTOTRADER CON INTERÉS COMPUESTO (SOROS 4 NIVELES)
TELEGRAM_BOT_TOKEN = "9053099301:AAFX6HNWpVfzwqBiZIqXMSZpGtCc7jwD-60"

# Receptores de reportes en vivo (Rafael & Eduardo)
TELEGRAM_CHAT_IDS = [
    "1028358282",  # Rafael Guzmán
    "7797844191"   # Eduardo Rivera
]

# Modo de Operación: "DEMO" obligatorio para pruebas
ACCOUNT_MODE = "DEMO"

# GESTIÓN DE CAPITAL: INTERÉS COMPUESTO (SOROS)
INITIAL_STAKE = 10.00          # Base inicial de $10.00 USD
MAX_COMPOUND_CYCLES = 4        # Meta de 4 operaciones consecutivas ganadas
PAYOUT_RATE = 0.85             # 85% de retorno promedio por operación
TIMEFRAME = "1m"               # 60 segundos por operación

# Si se pierde una operación en cualquier nivel, se reinicia inmediatamente a $10.00 USD
RESET_ON_LOSS = True

# 22 Mercados Permitidos
WATCHLIST = [
    "Metal Composite Index",
    "Oil Composite Index",
    "BNB OTC",
    "Bitcoin OTC",
    "Gold OTC",
    "Asia Composite Index",
    "BrasIndex",
    "Cafeina Index",
    "Compound Index",
    "Crypto Composite Index",
    "Dogecoin OTC",
    "Ethereum OTC",
    "Europe Composite Index",
    "Global Overview of Athletic Leagues Index",
    "Latam Index",
    "Pepe OTC",
    "Ripple OTC",
    "Shiba OTC",
    "Silver OTC",
    "Stable Tick Index",
    "Solana OTC",
    "Litecoin OTC"
]
