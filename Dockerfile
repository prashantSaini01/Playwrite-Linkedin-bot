# Use the Playwright Python image, which has everything pre-installed
FROM mcr.microsoft.com/playwright/python:v1.30.0-focal

# Install Flask (since it's specific to your project)
RUN pip install --no-cache-dir flask

# Set the working directory inside the container
WORKDIR /app

# Copy project files to the container
COPY . .

# Expose the Flask app's port (5000)
EXPOSE 5000

# Set the default command to run the Flask app
CMD ["python", "app.py"]
