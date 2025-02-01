from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Налаштування браузера
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Запуск у фоновому режимі (без відображення вікна)
options.add_argument("--disable-gpu")  # Вимкнення GPU для оптимізації
options.add_argument("--no-sandbox")  # Вимкнення sandbox для хмарних середовищ

# Ініціалізація драйвера
driver = webdriver.Chrome(options=options)

try:
    # Відкриття сайту RollerCoin
    driver.get("https://rollercoin.com")
    print("Сайт успішно відкрито.")

    # Очікування завантаження сторінки
    time.sleep(5)

    # Увійти в систему (якщо потрібно)
    login_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Sign In')]")
    login_button.click()
    time.sleep(2)

    # Введення логіну та паролю
    email_input = driver.find_element(By.NAME, "email")
    password_input = driver.find_element(By.NAME, "password")

    email_input.send_keys("your_email@example.com")  # Замініть на ваш email
    password_input.send_keys("your_password")  # Замініть на ваш пароль
    password_input.send_keys(Keys.RETURN)
    print("Вхід у систему виконано.")

    # Очікування завантаження сторінки після входу
    time.sleep(5)

    # Запуск міні-гри (приклад для гри "Token Blaster")
    game_button = driver.find_element(By.XPATH, "//div[contains(text(), 'Token Blaster')]")
    game_button.click()
    print("Міні-гра відкрита.")

    # Очікування завантаження гри
    time.sleep(5)

    # Приклад дій у грі (натискання пробілу для стрільби)
    game_canvas = driver.find_element(By.TAG_NAME, "body")
    for _ in range(10):  # Виконати 10 дій
        game_canvas.send_keys(Keys.SPACE)
        time.sleep(1)  # Інтервал між діями

    print("Міні-гра завершена.")

except Exception as e:
    print(f"Сталася помилка: {e}")

finally:
    # Закриття браузера
    driver.quit()
    print("Браузер закрито.")