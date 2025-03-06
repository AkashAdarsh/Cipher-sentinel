

# 🛡️ CipherSentinel

> **CipherSentinel** is a next-gen AI-powered smart contract auditor and rug pull analyzer designed to protect the Ethereum ecosystem from malicious contracts and scams. Combining blockchain analytics, machine learning, and cyberpunk vibes into one modular, scalable platform.

---

## 🚀 Project Status
> 🛠️ **Status:** Pre-MVP Development (Day 2)  
> 🗓️ **Current Focus:** Backend & Frontend scaffolding, API setup, Dockerization  

---

## 🧩 Modular Structure

/CipherSentinel
/backend        → FastAPI backend (APIs, ML integration, blockchain scanner)
/frontend        → Next.js frontend (UI, dashboards, interactions)
/docs            → Architecture diagrams, specs, documentation
/docker          → Dockerfiles, docker-compose orchestration
/tests           → Unit and integration tests


---

## ⚡ Tech Stack
| Layer               | Technology                  |
|---------------------|-----------------------------|
| Frontend           | Next.js, TailwindCSS        |
| Backend            | FastAPI (Python)            |
| Blockchain Access  | Web3.py (Ethereum)          |
| ML Models          | PyTorch, Hugging Face, Scikit-learn |
| Containerization   | Docker, Docker Compose      |
| Version Control    | Git + GitHub                |

---

## 🎯 MVP Goals
✅ Analyze Ethereum smart contracts for common vulnerabilities  
✅ Detect potential rug pull patterns through behavioral analytics  
✅ Deliver transparent, actionable risk reports via a web interface  

---

## 🗂️ Features Roadmap
| Phase | Features |
|-------|----------|
| 🔹 MVP  | Health check, contract fetcher, basic ML auditor |
| 🔹 v1.0 | Rug pull detector, risk scoring, frontend dashboards |
| 🔹 v1.5 | Ethereum Mainnet live monitoring, contract history visualizations |
| 🔹 v2.0 | Multi-chain support (Solana, BSC), advanced ML insights |

---

## 🏗️ Local Development

### Backend (FastAPI)

cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload

### Frontend (Next.js)
cd frontend
npm install
npm run dev


### Docker (Full Stack)

docker-compose up --build

<<<<<<< HEAD

---
## Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
# Infura Project ID for Ethereum (Goerli Testnet)
INFURA_PROJECT_ID=your_infura_project_id

# Etherscan API Key (optional, for future use)
ETHERSCAN_API_KEY=your_etherscan_api_key

# Application Settings
DEBUG=True
PORT=8000

Install python-dotenv to load the variables:

pip install python-dotenv
=======
>>>>>>> 2a21463f6b3b67466bc6534b2f32e9217c3960e1

---

## 📄 Documentation
- [Architecture Diagram](./docs/architecture.png)
- API docs: `http://localhost:8000/docs`
- Frontend: `http://localhost:3000`

---

## 📌 Contribution Guide (Coming Soon)
- How to set up the dev environment
- Coding standards
- Issue tracking

---

## 📝 License
**Private SaaS – All rights reserved.**  
For internal or licensed use only.

---

## 🤝 Credits
Made with ❤️ by Akash Adarsh.  
Cyberpunk vibes. Real-world protection.

---

## 🔮 Future Ideas
- Real-time contract event monitoring
- Discord/Telegram alert integrations
- Community-submitted contract auditing


