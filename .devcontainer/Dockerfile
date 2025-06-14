FROM mcr.microsoft.com/vscode/devcontainers/base:ubuntu-22.04

# Install dependencies for VNC and Docker
RUN apt-get update && apt-get install -y \
    docker.io \
    xvfb \
    x11vnc \
    fluxbox \
    && rm -rf /var/lib/apt/lists/*