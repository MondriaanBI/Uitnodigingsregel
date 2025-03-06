# Pull the base python image + uv | Note: this repository needs python 3.9
FROM ghcr.io/astral-sh/uv:latest

# Copy the project into the image
ADD . /app

# Set the working directory
WORKDIR /app

ENV UV_LINK_MODE=copy

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync