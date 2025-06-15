# Chrome Docker Codespace

This repository contains a development environment setup for running Google Chrome in a Docker container, accessible via a noVNC interface, hosted on GitHub Codespaces. It provides a pre-configured environment for testing and development with Chrome, leveraging Docker and a virtual display.

## Overview

- **Purpose**: Provides a Dockerized Chrome instance with a noVNC web interface, ideal for browser testing or development in a cloud-based Codespace.
- **Base Image**: Ubuntu 20.04.
- **Services**: 
  - `chrome`: Runs Google Chrome with Xvfb and x11vnc for virtual display and remote access.
  - `novnc`: Provides a web-based VNC client to access the Chrome instance.
- **Access**: Available at `https://<codespace>-6080.app.github.dev/vnc.html` after setup.

## Prerequisites

- A GitHub account with Codespaces enabled.
- Basic familiarity with Docker and Git.

## Setup Instructions

1. **Clone the Repository**:
   - Fork or clone this repository to your GitHub account.
   - Use GitHub Codespaces to create a new Codespace from the repository.

2. **Automatic Configuration**:
   - The `.devcontainer/devcontainer.json` file configures the environment automatically upon Codespace creation.
   - The `postCreateCommand` builds and starts the Docker services using `docker-compose`.

3. **Access the Environment**:
   - Once the Codespace is ready, open `https://<codespace>-6080.app.github.dev/vnc.html` in your browser (replace `<codespace>` with your Codespace name).
   - Log in to Chrome or use it for testing as needed.

## Files and Structure

- `.devcontainer/devcontainer.json`: Defines the devcontainer configuration, including the Dockerfile and post-creation commands.
- `.devcontainer/Dockerfile.chrome`: Specifies the Ubuntu 20.04-based image with Chrome, Xvfb, x11vnc, and required dependencies.
- `docker-compose.yaml`: Configures the `chrome` and `novnc` services, pointing to the Dockerfile for building.
- `README.md`: This file, providing setup and usage instructions.

## Troubleshooting

- **Build Fails with tzdata Prompt**:
  - Ensured non-interactive timezone configuration in `Dockerfile.chrome` with `DEBIAN_FRONTEND=noninteractive` and default UTC.
- **Dockerfile Not Found**:
  - Verify `Dockerfile.chrome` is in `.devcontainer/` and `docker-compose.yaml` references it with `context: ./.devcontainer`.
- **postCreateCommand Fails**:
  - Check for missing `docker-compose` or permission issues. Ensure `Dockerfile.chrome` installs `docker-compose` and `sudo chmod 666 /var/run/docker.sock` is effective.
- **No VNC Access**:
  - Confirm ports 5900 and 6080 are forwarded, and services are running with `docker ps`.

## Known Issues and Workarounds

- **Compatibility**: Uses `docker-compose` v1.29.2 to avoid SSL version issues with older `pip`-installed versions.
- **Permissions**: The `postCreateCommand` adjusts Docker socket permissions; ensure it executes successfully.

## Contributing

Feel free to submit issues or pull requests to improve this setup. Ensure changes are tested in a Codespace environment.

## License

[Add your preferred license here, e.g., MIT] - Default is no license unless specified.

## Acknowledgments

- Built with assistance from xAI's Grok 3.
- Utilizes Docker, Google Chrome, and noVNC open-source projects.