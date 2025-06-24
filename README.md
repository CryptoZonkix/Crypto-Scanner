
# Crypto Scanner 📡

AI-powered crypto project intelligence dashboard built with:

- 🔥 Flask backend (data ingestion, NLP, sentiment, scam detection)
- ⚛️ React frontend (charts, dashboards, alerts)
- 🐘 PostgreSQL, ⚙️ Redis, 🔁 Kafka
- 🐳 Dockerized stack (`docker-compose`)

---

## 📦 Project Structure

```
crypto-scanner/
├── frontend/   # React + Chart UI
├── backend/    # Flask + Kafka + DB
├── docker-compose.yml
├── .env.example (both frontend and backend)
```

---

## 🚀 Quick Start (Docker)

1. Clone repo
2. Add `.env` files based on provided `.env.example`
3. Run:

```bash
docker-compose up --build
```

---

## 🔧 Environment Setup

### backend/.env

```
SECRET_KEY=your_secret_key
DATABASE_URL=postgresql://user:password@localhost:5432/crypto_scanner_db
KAFKA_BOOTSTRAP_SERVERS=localhost:9092
REDIS_URL=redis://localhost:6379/0
```

### frontend/.env

```
REACT_APP_API_BASE_URL=http://localhost:5000/api
REACT_APP_SOCKET_IO_URL=http://localhost:5000
```

---

## 📊 Features

- Real-time alerts via WebSockets
- Scam & NLP risk detection
- Funding + investor visualization
- Fully dockerized setup
