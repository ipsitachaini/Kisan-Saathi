FROM python:3.10-slim

WORKDIR /app

# Copy backend requirements and install
COPY backend/requirements.txt ./backend/requirements.txt
RUN pip install --no-cache-dir -r ./backend/requirements.txt

# Copy source code
COPY backend/ ./backend/
COPY frontend/ ./frontend/

# Set environment variables
ENV PYTHONPATH=/app/backend

# Provide a default port but allow Render to override it via $PORT
ENV PORT=8000
EXPOSE $PORT

# Start the application
CMD uvicorn backend.main:app --host 0.0.0.0 --port $PORT
