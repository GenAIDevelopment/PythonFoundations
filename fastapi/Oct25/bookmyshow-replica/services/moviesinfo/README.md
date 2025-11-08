# Movies Info Service

## Local Development

### Using Docker Compose
```bash
docker-compose up -d
```

### Manual Setup
1. Install dependencies:
```bash
git clone https://github.com/GenAIDevelopment/PythonFoundations.git
cd ./PythonFoundations/fastapi/Oct25/bookmyshow-replica/services/moviesinfo
uv sync
```

2. Start the service:
```bash
uv run moviesinfo
```

### Environment Variables
Configure in `.env` file:
- `POSTGRES_DB` - Database name
- `POSTGRES_USER` - Database user
- `POSTGRES_PASSWORD` - Database password
- `DATABASE_URL` - Full database connection string
- `HOST` - Service host (default: 0.0.0.0)
- `MOVIES_SVC_PORT` - Service port (default: 8000)

## API Endpoints
- `GET /` - Health check
- `GET /items/{item_id}` - Get item by ID

* The service docs can be accessed by url `http://localhost:18000/docs`