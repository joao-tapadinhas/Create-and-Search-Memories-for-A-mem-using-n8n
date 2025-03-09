# Use a lightweight Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose the port FastAPI runs on
EXPOSE 9000

# Start the FastAPI app with Uvicorn
CMD ["uvicorn", "amem_api:app", "--host", "0.0.0.0", "--port", "9000"]
