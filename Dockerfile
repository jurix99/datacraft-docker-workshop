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
COPY ./app ./app

# Expose the necessary port
EXPOSE 8080

# Run the application
CMD ["python", "app/datacraft.py"]
