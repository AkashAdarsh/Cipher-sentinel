# 🛡️ CipherSentinel

> **CipherSentinel** is a next-gen AI-powered smart contract auditor and rug pull analyzer designed to protect the Ethereum ecosystem from malicious contracts and scams. Combining blockchain analytics, machine learning, and cyberpunk vibes into one modular, scalable platform.

---

## 🚀 Project Status
> 🛠️ **Status:** Pre-MVP Development (27% Complete)  
> 🗓️ **Current Focus:** Contract Analysis Pipeline & ML Infrastructure

### Component Progress
- Backend: 45% Complete
- Frontend: 15% Complete
- ML Infrastructure: 5% Complete
- DevOps: 40% Complete
- Documentation: 30% Complete

---

## 🧩 Project Structure
```
CipherSentinel/
├── app/                    # FastAPI backend
│   ├── models/            # Data models
│   ├── services/          # Business logic
│   ├── tasks/             # Celery tasks
│   └── utils/             # Utilities
├── frontend/              # Next.js frontend
│   └── src/              # Frontend source
├── ml/                    # ML infrastructure
│   ├── models/           # ML models
│   └── inference/        # Model inference
├── docs/                 # Documentation
└── tests/               # Test suites
```

## ⚡ Tech Stack
| Layer               | Technology                  | Status    |
|---------------------|-----------------------------|-----------|
| Frontend           | Next.js 15, TailwindCSS     | Setup     |
| Backend            | FastAPI, Celery, Redis      | In Progress|
| Blockchain         | Web3.py, Slither            | In Progress|
| ML Models          | PyTorch, Hugging Face       | Planned   |
| Database           | Redis                       | Setup     |
| Containerization   | Docker, Docker Compose      | Setup     |

---

## 🎯 Current Features
✅ Health check endpoint  
✅ Contract bytecode fetcher  
✅ Basic vulnerability scanner  
✅ Async task processing  
✅ Contract risk scoring  
✅ Gas analysis  

## 🚧 In Development
- ML-based contract analysis
- Real-time monitoring
- Frontend dashboard
- WebSocket updates
- Enhanced security checks

---

## 🏗️ Local Development

### Prerequisites
- Python 3.11+
- Node.js 18+
- Redis
- Docker (optional)

### Backend Setup
```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # Unix
.venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Start Redis server
redis-server

# Start FastAPI server
uvicorn app.main:app --reload

# Start Celery worker (in new terminal)
celery -A app.tasks.audit_tasks worker --loglevel=info
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

### Docker Setup
```bash
# Start all services
docker-compose up --build

# Start specific service
docker-compose up redis -d
```

---

## 🔧 Environment Variables
Create a `.env` file in the root directory:
```env
# Required
INFURA_PROJECT_ID=your_infura_project_id
ETHERSCAN_API_KEY=your_etherscan_api_key

# Optional
DEBUG=True
PORT=8000
REDIS_URL=redis://localhost:6379/0
ML_MODEL_PATH=/path/to/models
```

---

## 📚 API Documentation
- OpenAPI docs: `http://localhost:8000/docs`
- Frontend: `http://localhost:3000`

### Key Endpoints
- `GET /health` - Service health check
- `POST /audit` - Submit contract for analysis
- `GET /audit/{task_id}` - Get analysis results

---

## 🧪 Testing
```bash
# Backend tests
pytest

# Frontend tests
cd frontend && npm test
```

---

## 📈 Roadmap

### Phase 1: MVP (Current)
- [x] Basic contract analysis
- [x] Async task processing
- [ ] ML model integration
- [ ] Frontend dashboard

### Phase 2: v1.0
- [ ] Enhanced rug pull detection
- [ ] Real-time monitoring
- [ ] User authentication
- [ ] Advanced analytics

### Phase 3: v1.5
- [ ] Multi-chain support
- [ ] API marketplace
- [ ] Community features
- [ ] Mobile app

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


