from selenium import webdriver
from selenium.common.exceptions import TimeoutException
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
driver.get("https://www.runningland.com.br/calendario?page=1") 

print(f"[INFO] Título da página: {driver.title}")

try:
    accept_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "adopt-accept-all-button"))
    )
    accept_button.click()
    print("[INFO] Botão de aceite de cookies clicado.")
except TimeoutException:
    print("[INFO] Botão de aceite de cookies não encontrado. Continuando...")

try:
    wait = WebDriverWait(driver, 10)
    
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "eventCard-name-1Ln")))
    events = driver.find_elements(By.CLASS_NAME, "eventCard-name-1Ln")
    
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[class^='eventCard-region']")))
    regions = driver.find_elements(By.CSS_SELECTOR, "[class^='eventCard-region']")
    
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[class^='eventCard-modality-2Rl']")))
    distances = driver.find_elements(By.CSS_SELECTOR, "[class^='eventCard-modality-2Rl']")
    
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[class^='eventCard-eventDay-2H5']")))
    days = driver.find_elements(By.CSS_SELECTOR, "[class^='eventCard-eventDay-2H5']")
    
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[class^='eventCard-eventDay-2H5']")))
    months = driver.find_elements(By.CSS_SELECTOR, "[class^='eventCard-eventMonth-24f']")
    
    for i in range(len(events)):
      print(f"{i + 1} Corrida: {events[i].text}")
      
      spansLocals = regions[i].find_elements(By.TAG_NAME, "span")
      if spansLocals:
        print(f"Local: {spansLocals[1].text}")
        
      spansDistances = distances[i].find_elements(By.TAG_NAME, "span")
      if spansDistances:
        print(f"Distância: {spansDistances[1].text}")
        
      print(f"Data: {days[i].text} {months[i].text}")
        
      print("--------------------------------------------------------------------")

except Exception as e:
    print("[ERRO] Não conseguiu encontrar os eventos:", e)

driver.quit()