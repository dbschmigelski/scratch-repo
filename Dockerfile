FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
COPY low_level_mcp.py .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Entrypoint
CMD ["python", "low_level_mcp.py"]
