FROM python:3.13-slim

WORKDIR /app

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"
# 激活虚拟环境
ENV PATH="/app/.venv/bin/:$PATH"

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


# Download the latest uv installer
ADD https://astral.sh/uv/install.sh /uv-installer.sh

# Run the uv installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh \
    && git clone https://github.com/jiyongfeng/llm-examples.git . \
    && uv sync --frozen


EXPOSE 8501

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8501/ || exit 1

ENTRYPOINT ["streamlit", "run", "Chatbot.py", "--server.port=8501", "--server.address=0.0.0.0"]
