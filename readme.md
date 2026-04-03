# 🎬 Movie Show Tracker (District Alert Bot)

## 🚀 Real Problem → Real Solution

I wanted to watch *Project Hail Mary* on release day, but in my city (Muzaffarpur), all theatre screens were occupied by another high-demand movie.

Manually checking again and again was frustrating.

So instead of waiting, I built a system that checks for me.

---

## 💡 What this project does

This project automatically monitors movie availability in Muzaffarpur using District (by Zomato) and sends alerts when a specific movie appears.

✔ Checks availability every 10 minutes
✔ Runs automatically on cloud (GitHub Actions)
✔ Sends instant alerts via Telegram and Email

---

## ⚙️ How it works

1. GitHub Actions runs the script every 10 minutes
2. Script fetches District movies page for Muzaffarpur
3. Scans page content for the target movie
4. If found → sends alert

---

## 🧠 Tech Stack

* Python
* Requests (lightweight scraping)
* GitHub Actions (automation & scheduling)
* Telegram Bot API (instant alerts)
* SMTP (email notifications)

---

## 🔔 Features

* Fully automated (runs in background)
* Works even when laptop is OFF
* No Selenium / browser dependency
* More reliable than traditional scraping
* Real-time alert system

---

## 🧪 Example Use Case

> Tracking availability of "Project Hail Mary" in Muzaffarpur when theatres were initially dominated by another movie.

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
* Detect show timings (not just listing)
* Prevent duplicate alerts
* Multi-movie tracking
* Add UI/dashboard

---

## 🧠 Key Insight

Initially, I tried scraping BookMyShow using Selenium, but it was blocked due to bot detection.

Instead of forcing a solution, I switched to a better data source (District), which made the system simpler and more reliable.

> Sometimes the best fix is not better code — it's choosing the right source.

---

## 📎 Repository

Feel free to explore, use, or improve this project.

---

## 🙌 Final Note

Built this for a real personal need, and it turned into a great learning experience in automation, scraping strategy, and system design.

---
