# Use a more specific base image
FROM python:3.10-slim

# Install poetry
RUN pip install --no-cache-dir poetry

# Copy only the pyproject.toml and poetry.lock files to install dependencies
COPY pyproject.toml poetry.lock* /app/
WORKDIR /app

# Install dependencies in a single layer
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Copy only necessary files
COPY ./gradio ./app

# Expose the necessary port
EXPOSE 8080
WORKDIR /app/gradio

# Run the application
CMD ["poetry","run","gradio", "./datacraft.py"]
