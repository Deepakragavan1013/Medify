FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /medify

# Copy files to the container
COPY main.py /medify/
COPY requirements.txt /medify/

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port for Flask
EXPOSE 5000

# Run the Flask app
CMD ["python", "main.py"]

