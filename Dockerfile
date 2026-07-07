FROM ubuntu:22.04

# Install dependencies, Python, and curl
RUN apt-get update && apt-get install -y \
    curl \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install LM Studio Headless Core (llmster)
RUN curl -fsSL https://lmstudio.ai/install.sh | bash

# Ensure lms CLI is in path
ENV PATH="/root/.cache/lm-studio/bin:${PATH}"

# Install the Python SDK
RUN pip3 install lmstudio

# Create a work directory
WORKDIR /app

# Copy your Python application script (e.g., app.py)
COPY . /app

# Expose LM Studio default server port
EXPOSE 1234

# Start the server and run your python process
CMD ["sh", "-x", "-c", "lms server start --port 1234 & python3 app.py"]

