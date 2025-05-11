FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install numpy first to avoid binary incompatibility issues
RUN pip install --no-cache-dir numpy==1.26.0

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install spaCy model directly
RUN python -m spacy download en_core_web_sm

# Create wrapper script to handle imports properly
COPY . .
RUN echo '#!/usr/bin/env python3\nimport os\nimport sys\nsys.path.insert(0, os.path.abspath("."))\nfrom src.main import main\nif __name__ == "__main__":\n    main()' > /app/run_app.py && \
    chmod +x /app/run_app.py

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Create output directory with proper permissions
RUN mkdir -p output && chmod 777 output

# Set the entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["python", "/app/run_app.py"] 