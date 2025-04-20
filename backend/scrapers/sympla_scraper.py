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
driver.get("https://www.sympla.com.br/eventos?s=corrida")

print(f"[INFO] Título da página: {driver.title}")

try:
    wait = WebDriverWait(driver, 10)
    
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "pn67h18")))
    events = driver.find_elements(By.CLASS_NAME, "pn67h18")
   
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "qtfy413")))
    dates = driver.find_elements(By.CLASS_NAME, "qtfy413")
   
    for i in range(len(events)):
      print(f"{i + 1} Corrida: {events[i].text}")
        
      print(f"Data: {dates[i].text}")
        
      print("--------------------------------------------------------------------")

except Exception as e:
    print("[ERRO] Não conseguiu encontrar os eventos:", e)

driver.quit()