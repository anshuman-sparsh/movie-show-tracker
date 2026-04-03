import os
import time
import smtplib
import requests
import undetected_chromedriver as uc
from email.mime.text import MIMEText

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


URL = "https://in.bookmyshow.com/explore/movies-muzaffarpur"


def check_movie():
    options = Options()
    is_github = os.environ.get("GITHUB_ACTIONS") == "true"

    if is_github:
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
    else:
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )

    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    

    driver = uc.Chrome(
    version_main=146,
    headless=True
)
    driver.get(URL)

    time.sleep(5)


    for _ in range(3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    
    elements = driver.find_elements(By.XPATH, "//*[text()]")

    for el in elements[:50]:
        print("TEXT:", el.text)

    target_keywords = ["hail mary"]

    for el in elements:
        try:
            text = el.text.lower().strip()
            if any(keyword in text for keyword in target_keywords):
                driver.quit()
                return True
        except:
            continue

    driver.quit()
    return False


def send_telegram(message):
    token = os.environ["BOT_TOKEN"]
    chat_id = os.environ["CHAT_ID"]

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.post(url, data={"chat_id": chat_id, "text": message})


def send_email(message):
    email = os.environ["EMAIL"]
    password = os.environ["PASSWORD"]

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)

    msg = MIMEText(message)
    msg["Subject"] = "🚨 Movie Alert"
    msg["From"] = email
    msg["To"] = email

    server.send_message(msg)
    server.quit()


if __name__ == "__main__":
    if check_movie():
        alert_msg = "🚨 Project Hail Mary is LIVE in Muzaffarpur! Book now!"
        send_telegram(alert_msg)
        send_email(alert_msg)
        print("ALERT SENT")
    else:
        print("Not available yet")