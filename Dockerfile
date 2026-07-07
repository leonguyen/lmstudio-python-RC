# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY Requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r Requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port Render expects
EXPOSE 10000

# Run the application using gunicorn for production stability
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "app:app"]

