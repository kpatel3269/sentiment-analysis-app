Here's a clean README.md you can copy and paste directly into VS Code:

```markdown
# FlowDesk AI - Intelligent Ticket Management Platform

A full-stack SaaS application for managing support tickets with AI-powered triage, multi-step approval workflows, and role-based access control.

![FlowDesk Dashboard](docs/dashboard.png)

---

## Features

- **JWT Authentication & RBAC** - Secure user authentication with role-based permissions (Admin, Agent, User)
- **Multi-Step Workflows** - Configurable approval chains (Submission → Review → Approval → Fulfillment)
- **AI Ticket Triage** - Automatic category/priority classification and response suggestions using OpenAI API
- **Async Job Processing** - Background tasks for SLA monitoring, notifications, and automation (Celery + Redis)
- **Audit Logging** - Complete activity tracking for compliance and debugging
- **Analytics Dashboard** - Real-time ticket status, priority distribution, and workflow metrics
- **Docker Compose Setup** - One-command local development environment

---

## Tech Stack

**Frontend**
- Next.js 14
- React
- TailwindCSS

**Backend**
- FastAPI
- PostgreSQL
- Redis
- Celery

**AI/ML**
- OpenAI API (GPT-4)
- Fallback: Rule-based classifier

**DevOps**
- Docker & Docker Compose
- JWT for authentication

---

## Quick Start

### Prerequisites
- Docker & Docker Compose
- OpenAI API key (optional - works with stub mode)

### 1) Clone the repository
```bash
git clone https://github.com/kpatel3269/flowdesk-ai.git
cd flowdesk-ai
```

### 2) Configure environment
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key (optional)
```

### 3) Start the stack
```bash
docker-compose up --build
```

### 4) Access the application
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

---

## Environment Variables

```bash
# Database
DATABASE_URL=postgresql://user:password@db:5432/flowdesk

# Redis
REDIS_URL=redis://redis:6379/0

# JWT
JWT_SECRET_KEY=your-secret-key-here

# AI Triage (optional)
OPENAI_API_KEY=sk-...
AI_MODE=openai  # or 'stub' for rule-based fallback
```

---

## Architecture

```
┌─────────────┐      ┌──────────────┐      ┌──────────────┐
│   Next.js   │─────▶│   FastAPI    │─────▶│  PostgreSQL  │
│  Frontend   │      │   Backend    │      │   Database   │
└─────────────┘      └──────────────┘      └──────────────┘
                            │
                            ▼
                     ┌──────────────┐      ┌──────────────┐
                     │    Redis     │◀────▶│    Celery    │
                     │    Cache     │      │    Worker    │
                     └──────────────┘      └──────────────┘
```

---

## Key Workflows

### Ticket Lifecycle
1. **Submission** - User creates ticket
2. **AI Triage** - Auto-classify category/priority
3. **Assignment** - Route to appropriate agent
4. **Approval** - Manager reviews (if required)
5. **Fulfillment** - Agent resolves ticket
6. **Closure** - Automated or manual close

### Background Jobs (Celery)
- SLA monitoring and breach alerts
- Scheduled ticket escalation
- Email notifications
- Analytics aggregation

---

## API Endpoints

### Authentication
- `POST /api/auth/register` - Create new user
- `POST /api/auth/login` - Get JWT token
- `POST /api/auth/refresh` - Refresh token

### Tickets
- `GET /api/tickets` - List tickets (filtered by role)
- `POST /api/tickets` - Create ticket
- `GET /api/tickets/{id}` - Get ticket details
- `PATCH /api/tickets/{id}` - Update ticket
- `POST /api/tickets/{id}/assign` - Assign to agent

### Admin
- `GET /api/admin/analytics` - Dashboard metrics
- `GET /api/admin/audit-logs` - Activity logs
- `POST /api/admin/users` - Manage users

Full API documentation: http://localhost:8000/docs

---

## Development

### Run without Docker
```bash
# Backend
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000

# Frontend
cd frontend
npm install
npm run dev
```

### Run tests
```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test
```

### Database migrations
```bash
cd backend
alembic revision --autogenerate -m "migration message"
alembic upgrade head
```

---

## Project Structure

```
flowdesk-ai/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── lib/
│   └── package.json
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   ├── services/
│   │   ├── tasks/          # Celery tasks
│   │   └── main.py
│   └── requirements.txt
├── docker-compose.yml
└── README.md
```

---

## Roadmap

- [ ] Email integration (IMAP/SMTP)
- [ ] Advanced analytics & reporting
- [ ] Mobile app (React Native)
- [ ] Webhook integrations (Slack, Teams)
- [ ] Multi-tenancy support
- [ ] Knowledge base & chatbot

---

## License

MIT License - See [LICENSE](LICENSE) file for details

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

---

## Contact

**Kakksh Patel**  
📧 kakshpatel2232@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/Kakkshpatel)  
💻 [GitHub](https://github.com/kakshp)
```

