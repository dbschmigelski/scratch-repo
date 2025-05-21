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

# uv is a Rust-based package manager – we assume it's used as a CLI tool
# Install uvx from uv (requires Rust toolchain)
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y \
    && . $HOME/.cargo/env \
    && cargo install uv \
    && ln -s /root/.cargo/bin/uvx /usr/local/bin/uvx

# Entrypoint
CMD ["python", "low_level_mcp.py"]
