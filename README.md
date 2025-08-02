# Stock-messaging-logic-using-API System with News & WhatsApp Integration

This Python project monitors Tesla Inc. (TSLA) stock prices using the **Alpha Vantage API** and sends **news alerts via WhatsApp** (using **Twilio**) if the stock changes significantly (more than 5%) between two consecutive days. News articles are fetched from the **NewsAPI**.

---

## 🔧 Features

- Fetch daily stock prices from Alpha Vantage.
- Compare closing prices of the last two days.
- Fetch top 3 news articles related to Tesla Inc. using NewsAPI.
- Send automated alerts via WhatsApp using Twilio if price fluctuation exceeds 5%.

---

## 📦 Dependencies

- Python 3.x
- `requests`
- `twilio`
- `datetime`

Install required packages:

```bash
pip install requests twilio
