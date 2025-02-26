# Sentiment Analysis with Google Gemini AI

## Project Overview
This project is a **Sentiment Analysis Web Application** that utilizes **Google Gemini AI** for sentiment classification. The application is built with **Flask** for the backend and containerized using **Docker** for easy deployment.

## Chosen Prompt
The prompt used for sentiment analysis:
> "Analyze the sentiment of the following Tweets and classify them as POSITIVE, NEGATIVE, or NEUTRAL."

## Steps to Complete the Assignment
### 1. Obtaining the Code
- The Flask application was developed to handle user input and send requests to the Google Gemini AI API.
- The frontend (optional) was created to interact with the backend.
- API calls were structured based on the Google AI Studio prompt.

### 2. Setting Up the Docker Container
#### a) Create a `Dockerfile`
```dockerfile
FROM python:3.9-slim

# Set working directory
WORKDIR /medify

# Copy files to container
COPY . /medify

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Start the Flask application
CMD ["python", "main.py"]
```

#### b) Create `requirements.txt`
```
Flask
google-generativeai
```

### 3. Running the Code Locally Using Docker
#### a) Build the Docker Image
Run the following command in the terminal inside the project directory:
```bash
docker build -t sentiment-analyzer .
```

#### b) Run the Container
```bash
docker run -p 5000:5000 -e GEMINI_API_KEY=your_api_key sentiment-analyzer
```

### 4. Accessing the Application
- Once the container is running, open a web browser and go to:
  ```
http://localhost:5000
  ```
- You can enter a sentence to analyze its sentiment.

### 5. GitHub Repository & Screenshot
- A screenshot of the application running successfully on `http://localhost:5000` should be included in your repository.
- The repository should contain:
  - `main.py` (Flask Backend)
  - `Dockerfile`
  - `requirements.txt`
  - `README.md`
  - Screenshot (`screenshot.png` or `.jpg`)

## Troubleshooting
- If you encounter a **KeyError** for `GEMINI_API_KEY`, ensure you set the environment variable correctly before running the container.
- Ensure that `google-generativeai` is installed inside the container using `pip list`.
- If Docker fails to run, try restarting the Docker service and ensure port `5000` is not in use.

## Conclusion
This project helped in understanding **Flask API development**, **Google Gemini AI integration**, and **Docker containerization**. It provides a functional AI-powered sentiment analysis tool that runs efficiently in a containerized environment.

