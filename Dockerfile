# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy only the files needed for dependency installation to leverage Docker layer caching
COPY pyproject.toml poetry.lock ./

# Install project dependencies, creating no virtual environment in the container
RUN poetry config virtualenvs.create false && poetry install --no-root --no-dev

# Copy the rest of the application code into the container
COPY ./app /app/

# Expose the port Streamlit runs on
EXPOSE 8501

# Define the command to run your app when the container starts
CMD ["streamlit", "run", "app/main.py", "--server.port=8501", "--server.address=0.0.0.0"]