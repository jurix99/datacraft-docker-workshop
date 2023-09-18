# Use a more specific base image
FROM python:3.10-slim

# Create a new user to run the app
RUN addgroup --system appgroup \
    && adduser --system appuser --ingroup appgroup

# Install poetry
RUN pip install --no-cache-dir poetry

# Copy only the pyproject.toml and poetry.lock files to install dependencies
WORKDIR /app
COPY pyproject.toml poetry.lock* ./

# Install dependencies in a single layer
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Switch to the new user
USER appuser

# Copy only necessary files and change ownership to appuser
COPY --chown=appuser:appgroup ./gradio ./gradio

# Expose the necessary port
EXPOSE 8080

# Change to the application directory
WORKDIR /app/gradio

# Run the application
CMD ["gradio", "./datacraft.py"]
