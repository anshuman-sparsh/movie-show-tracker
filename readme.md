# 🎬 Movie Show Tracker (BookMyShow Alert Bot)

## 🚀 Real Problem → Real Solution

I wanted to watch *Project Hail Mary* on release day, but in my city (Muzaffarpur), all theatres were occupied by another high-demand movie.

Instead of manually checking again and again, I built a simple automation system that does it for me.

---

## 💡 What this project does

This project automatically monitors BookMyShow for a specific movie in Muzaffarpur and sends alerts when it becomes available.

✔ Checks movie availability every 10 minutes
✔ Runs automatically on cloud (no laptop required)
✔ Sends instant alerts via Telegram and Email

---

## ⚙️ How it works

1. GitHub Actions runs the script every 10 minutes
2. Selenium opens BookMyShow (Muzaffarpur page)
3. Script searches for the movie name
4. If found → sends alert

---

## 🧠 Tech Stack

* Python
* Selenium (browser automation)
* GitHub Actions (automation & scheduling)
* Telegram Bot API (instant alerts)
* SMTP (email notifications)

---

## 🔔 Features

* Fully automated (runs in background)
* Works even when laptop is OFF
* Real-time alert system
* Built for a real-world personal use case

---

## 🧪 Example Use Case

> Tracking availability of "Project Hail Mary" in Muzaffarpur where theatre screens were limited due to another movie dominating all shows.

---

## 🔐 Environment Variables (GitHub Secrets)

The project uses secure environment variables:

* `BOT_TOKEN` → Telegram bot token
* `CHAT_ID` → Telegram chat ID
* `EMAIL` → Gmail address
* `PASSWORD` → Gmail app password

---

## 📌 Future Improvements

* Track specific theatres (Cinepolis, Eylex, etc.)
* Detect actual show timings
* Prevent duplicate alerts
* Multi-movie tracking

---

## 🧠 Key Insight

This project is a simple example of how automation can solve small real-life problems efficiently.

Instead of repeatedly checking manually, a system can monitor and notify you instantly.

---

## 📎 Repository

Feel free to explore, use, or improve this project.

---

## 🙌 Final Note

Built this for myself, but it turned out to be a great learning experience in automation, scraping, and cloud-based workflows.

---
