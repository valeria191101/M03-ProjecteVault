from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import sys


# Configurar opcions de Chrome
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")


passwords = ['1234', 'qwerty', 'admin', 'password123', 'letmein']


try:
    driver = webdriver.Chrome(options=chrome_options)
    
    # IMPORTANT: Canvia aquesta ruta per la teva ruta exacta
    ruta_completa = "/home/isard/M03-ProjecteVault/login.html"
    print(f"Accedint a: file://{ruta_completa}")
    
    driver.get(f"file://{ruta_completa}")
    time.sleep(3)  # Donar més temps per carregar
    
    # Atac
    driver.find_element(By.ID, 'username').send_keys('admin')
    
    for pwd in passwords:
        print(f"Provant: {pwd}")
        
        driver.find_element(By.ID, 'password').clear()
        driver.find_element(By.ID, 'password').send_keys(pwd)
        driver.find_element(By.ID, 'loginBtn').click()
        time.sleep(1)
        
        if "ACCESS_GRANTED" in driver.find_element(By.ID, 'message').text:
            print(f"VULNERABILITAT TROBADA! Contrasenya: {pwd}")
            sys.exit(1)
            driver.save_screenshot('hacked.png')
            break
    
except Exception as e:
    print(f"Error: {e}")


finally:
    time.sleep(5)
    driver.quit()
