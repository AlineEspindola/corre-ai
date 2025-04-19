# import requests
# from bs4 import BeautifulSoup

# url = "https://centraldacorrida.com.br/evento/ii-corrida-de-conscientiza%C3%A7%C3%A3o-mundial-do-autismo"

# response = requests.get(url)

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Accept-Language": "en-US,en;q=0.5",
#     "Connection": "keep-alive",
#     "Upgrade-Insecure-Requests": "1",
#     "TE": "Trailers"
# }

# print(f"response: {response}")

# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     print(f"soup: {soup}")
# else:
#     print("Erro ao acessar a página")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tempfile

temp_user_data_dir = tempfile.mkdtemp()

options = Options()
options.add_argument("--headless") 
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument(f"--user-data-dir={temp_user_data_dir}")

driver = webdriver.Chrome(options=options)

print("[INFO] Acessando site...")
driver.get("https://minhasinscricoes.com.br/pt-br/calendario")

print(f"[INFO] Título da página: {driver.title}")

try:
    print("[INFO] Aguardando eventos aparecerem...")
    elements = WebDriverWait(driver, 20).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, 'titulo-destaque'))
    )
    print(f"[INFO] Eventos encontrados: {len(elements)}")
    for i, element in enumerate(elements, 1):
        print(f"{i}. {element.text}")
except Exception as e:
    print("[ERRO] Nenhum evento encontrado ou erro ao renderizar página.")
    print(f"Detalhes: {e}")

driver.quit()
