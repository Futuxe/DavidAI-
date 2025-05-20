# README.md
# DavidAI - AI Code Generator

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/Python-3.9+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/React-18+-61DAFB.svg" alt="React">
</p>

## 🚀 Quick Start

```bash
# Clone and setup
git clone https://github.com/rjewi/DavidAI.git
cd DavidAI

# Backend setup
cd davidai
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
pip install -r requirements.txt

# Frontend setup
cd ../frontend
npm install

# Run backend (in first terminal)
cd ../davidai
uvicorn main:app --reload

# Run frontend (in second terminal)
cd ../frontend
npm run dev
```
🔧 Configuration
Create .env file in davidai/:

```bash
SUPABASE_URL=your-project-url.supabase.co
SUPABASE_KEY=your-anon-key
```
Set up Supabase tables:
```bash
sql
-- Run in SQL Editor
CREATE TABLE api_usage (
  api_key TEXT PRIMARY KEY,
  count INTEGER NOT NULL,
  last_reset DATE NOT NULL
);
```
CREATE TABLE generations 
```bash
(
  id SERIAL PRIMARY KEY,
  api_key TEXT REFERENCES api_usage(api_key),
  prompt TEXT NOT NULL,
  language TEXT NOT NULL,
  generated_code TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```
🌐 Deployment
Deploy to Vercel
📖 API Usage
```bash
curl -X POST http://localhost:8000/generate/ \
  -H "X-API-KEY: RJW(80)OP" \
  -H "Content-Type: application/json" \
  -d '{"prompt":"write a fibonacci function","language":"python"}'
```
📜 License
MIT License - Copyright (c) 2025 futuxe (rjewi)

👨‍💻 Developer
Original Developer: rjewi (futuxe)

Contributions Welcome! Fork and submit PRs
