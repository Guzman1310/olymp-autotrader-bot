import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_IDS, ACCOUNT_MODE

def send_execution_report(action: str, asset: str, stake: float, price: float, level: int = 1, result: str = "EN CURSO", profit: float = 0.0, cycle_completed: bool = False):
    """
    Envía reporte detallado de interés compuesto a Rafael y Eduardo.
    """
    emoji = "🟢 COMPRA (ARRIBA)" if "COMPRA" in action.upper() else "🔴 VENTA (ABAJO)"
    
    if result == "EN CURSO":
        header = f"⚡ *[OPERACIÓN EN EJECUCIÓN - NIVEL {level}/4]*"
        body = f"⏳ *Estado:* Operación abierta al segundo :00 (Duración 60s)\n📈 *Estrategia:* Interés Compuesto Soros"
    elif "GANADA" in result.upper():
        if cycle_completed:
            header = f"🏆 *¡META ALCANZADA! CICLO DE 4 NIVELES COMPLETADO* 🎉"
            body = (
                f"💵 *Ganancia de esta operación:* `+${profit:.2f} USD`\n"
                f"🚀 *Resultado del Ciclo:* ¡4 de 4 operaciones ganadas consecutivas!\n"
                f"🔄 *Próxima operación:* Reiniciando a `$10.00 USD` (Nivel 1)"
            )
        else:
            header = f"🎉 *[WIN NIVEL {level}/4 GANADO]*"
            body = (
                f"💵 *Beneficio:* `+${profit:.2f} USD`\n"
                f"📈 *Siguiente Nivel ({level + 1}/4):* Próxima entrada con capital + ganancia acumulada."
            )
    else:
        header = f"❌ *[LOSS EN NIVEL {level}/4]*"
        body = (
            f"📉 *Resultado:* `-${stake:.2f} USD`\n"
            f"🔄 *Gestión de Protección:* Reiniciando inmediatamente a `$10.00 USD` (Nivel 1)."
        )

    msg = (
        f"{header}\n\n"
        f"👤 *Cuenta:* `{ACCOUNT_MODE}` (Demo Aislada)\n"
        f"📊 *Activo:* `{asset}`\n"
        f"🎯 *Dirección:* *{emoji}*\n"
        f"💰 *Importe:* `${stake:.2f} USD`\n"
        f"📍 *Precio de Entrada:* `{price}`\n"
        f"{body}\n\n"
        f"🤖 _Olymp AutoTrader Master 24/7_"
    )

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    for chat_id in TELEGRAM_CHAT_IDS:
        try:
            requests.post(url, json={"chat_id": chat_id, "text": msg, "parse_mode": "Markdown"}, timeout=5)
        except Exception as e:
            print(f"[Error enviando a {chat_id}]: {e}")
