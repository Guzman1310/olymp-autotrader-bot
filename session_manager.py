"""
Motor de Inicio de Sesión y Persistencia de Sesión Segura para Olymp Trade.
Utiliza Playwright con navegación stealth para guardar cookies y sesión activa.
"""
import time
import os
from playwright.sync_api import sync_playwright
from reporter import send_execution_report

try:
    from credentials import OLYMP_USER_EMAIL, OLYMP_USER_PASSWORD
except ImportError:
    try:
        from credentials import OLYMP_USER_EMAIL, OLYMP_USER_PASSWORD
    except Exception:
        # Import desde archivo oculto
        import importlib.util
        cred_path = os.path.join(os.path.dirname(__file__), ".credentials.py")
        spec = importlib.util.spec_from_file_location("credentials", cred_path)
        creds = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(creds)
        OLYMP_USER_EMAIL = creds.OLYMP_USER_EMAIL
        OLYMP_USER_PASSWORD = creds.OLYMP_USER_PASSWORD

USER_DATA_DIR = os.path.join(os.path.dirname(__file__), "browser_session")

def start_safe_session():
    """
    Inicia una ventana de navegador segura para que el usuario verifique
    el inicio de sesión en Olymp Trade y resuelva cualquier captcha inicial.
    Una vez iniciada la sesión, queda guardada para siempre.
    """
    print("="*65)
    print("🤖 INICIANDO SESIÓN SEGURA DE OLYMP TRADE (AUTOTRADER)")
    print(f"📧 Correo configurado: {OLYMP_USER_EMAIL}")
    print("="*65)
    
    with sync_playwright() as p:
        # Lanzamos Chromium con perfil persistente
        browser = p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=False, # Modo visible para que veas el proceso
            args=[
                "--disable-blink-features=AutomationControlled",
                "--start-maximized"
            ],
            viewport=None
        )
        
        page = browser.pages[0] if browser.pages else browser.new_page()
        print("[+] Abriendo plataforma Olymp Trade...")
        page.goto("https://olymptrade.com/platform", timeout=60000)
        
        time.sleep(5)
        
        # Verificar si ya está logueado o requiere login
        if "platform" in page.url and ("trade" in page.content().lower() or "deposit" in page.content().lower()):
            print("[✓] ¡Sesión ya iniciada y activa en la plataforma!")
        else:
            print("[*] En la página de login...")
            try:
                # Intentar auto-rellenar correo si existe el campo
                email_input = page.query_selector('input[type="email"], input[name="email"]')
                if email_input:
                    email_input.fill(OLYMP_USER_EMAIL)
                    time.sleep(1)
                    pass_input = page.query_selector('input[type="password"], input[name="password"]')
                    if pass_input:
                        pass_input.fill(OLYMP_USER_PASSWORD)
                        print("[*] Credenciales ingresadas automáticamente.")
            except Exception as e:
                print(f"[!] Nota de login: {e}")
                
        print("\n" + "="*65)
        print("IMPORTANTE: Revisa la ventana del navegador que se acaba de abrir.")
        print("Si te pide resolver un captcha o código 2FA, resuélvelo manualmente.")
        print("Una vez dentro de la plataforma, la sesión quedará guardada.")
        print("="*65)
        
        # Mantener abierto para que el usuario confirme
        for _ in range(60):
            time.sleep(1)
            
        browser.close()
        print("[✓] Proceso de sesión finalizado.")

if __name__ == "__main__":
    start_safe_session()
