# Dockerfile for Streamlit
FROM python:3.9

WORKDIR /app

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Expose Streamlit's default port
EXPOSE 8501

# Run Streamlit
CMD ["streamlit", "run", "upload_to_pg.py", "--server.port=8501", "--server.address=0.0.0.0"]