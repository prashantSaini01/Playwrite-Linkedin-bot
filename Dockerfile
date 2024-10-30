# Base image with Playwright
FROM mcr.microsoft.com/playwright:v1.42.1-focal

# Set working directory
WORKDIR /app

# Install Python and pip
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Install Playwright browsers
RUN playwright install chromium
RUN playwright install-deps

# Copy application code
COPY . .

# Create directory for CSV files
RUN mkdir -p /app/data && chmod 777 /app/data

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright

# Default port for Render
ENV PORT=5000

# Use a non-root user
RUN useradd -m myuser && chown -R myuser:myuser /app
USER myuser

# Command to run the application
CMD ["python3", "app.py"]