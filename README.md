# Docker Swarm Voting App

A beginner-to-advanced **Docker Swarm practice project**.  
This stack demonstrates container orchestration with **Flask**, **Redis**, **Postgres**, **Worker**, **Node.js**, and **Nginx Reverse Proxy**.

---

## 🚀 Features
- **Frontend Voting App (Flask + Redis)** → users vote for Cats or Dogs  
- **Worker (Python)** → consumes votes from Redis and stores them in Postgres  
- **Result App (Node.js)** → shows voting results in real time  
- **Postgres DB** → persistent storage of votes  
- **Redis** → fast queue for temporary vote storage  
- **Nginx (inside Swarm)** → reverse proxy serving apps via domain `aitrack.tech`

---

## 📂 Project Structure
docker-swarm-voting-app/
│── vote/ # Flask voting app
│── worker/ # Worker that moves data from Redis → Postgres
│── result/ # Node.js result app
│── nginx.conf # Reverse proxy configuration
│── swarm-stack.yml# Swarm deployment file
│── docker-compose.yml # For local testing
│── README.md

---

## 🔧 Deployment Instructions

### 1. Clone Repo
```bash
git clone git@github.com:faisalthecoder/voting_app

