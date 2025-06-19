# Use Alpine-based Python image
FROM python:3.12-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the local app.py to the container's /app directory
COPY ./app.py /app/

# Install Flask dependency
RUN pip install flask

# Expose port 5000 for the application
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
