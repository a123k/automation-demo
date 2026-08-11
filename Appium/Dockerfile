# Use a lightweight Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set environment variables (if needed)
ENV PYTHONUNBUFFERED=1

# Command to run the tests
# We use -v for verbose output and --tb=short for cleaner error messages
CMD ["pytest", "tests/", "-v", "--tb=short"]
