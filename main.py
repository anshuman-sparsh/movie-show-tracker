import os
import time
import smtplib
import requests
from email.mime.text import MIMEText

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


URL = "https://in.bookmyshow.com/explore/movies-muzaffarpur"


def check_movie():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(URL)


    time.sleep(5)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)


    try:
        movies = driver.find_elements(By.TAG_NAME, "h3")

        for movie in movies:
            text = movie.text.lower()
            if "hail mary" in text:
                driver.quit()
                return True
    except Exception as e:
        print("Element detection error:", e)


    page = driver.page_source.lower()
    driver.quit()

    keywords = ["project hail mary", "hail mary"]
    return any(keyword in page for keyword in keywords)


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