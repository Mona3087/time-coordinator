# JIRA Time Coordinator
![alt text](CrossTimeCoordinator.png)

Welcome to Time Coordinator, an asynchronous chatbot application designed to help you manage and process data from CSV files. This project enables real-time interaction with users, offering tools to upload files, count characters, and dynamically generate responses based on the processed data.

## Features

- **File Upload**: Allows users to upload CSV files directly within the chat interface.
- **Character Count**: Automatically calculates and displays the number of characters in the uploaded CSV file.
- **Data Processing**: Utilizes the data within the uploaded CSV to tailor responses and provide meaningful interaction.

## Prerequisites

Before you begin, ensure you have Python 3.7 or newer installed on your machine. This project utilizes asynchronous features supported by newer versions of Python.

OPENAI_API_KEY= ""

tabulate==0.9.0
pandas==2.2.1
chainlit==0.7.700
python-dotenv==1.0.0
langchain==0.1.16
langchain-community==0.0.34
langchain-openai==0.1.3
langchain_experimental==0.0.57

## Installation

Follow these steps to get Time Coordinator up and running on your local machine:

### Clone the Repository

```bash
git clone https://github.com/Mona3087/time-coordinator.git
cd time-coordinator
pip install -w requirements.txt
```

Run Locally
Use Streamlit to run the application:

```bash
streamlit run app.py -w
Build and Run with Docker
```
Alternatively, you can build and run the application using Docker:

```bash
docker build -t time-coordinator-app .
docker run -p 7860:7860 time-coordinator-app
```

## Usage

After installation, start the application using one of the methods above. The interface will prompt you to upload a CSV file. Once uploaded, the application will display the number of characters in the file and begin processing the data to interact with you based on the content.

## Supported CSV Formats
Ensure your CSV files are formatted correctly for optimal performance. The application expects headers with specific names based on its processing logic.

## Troubleshooting

If you encounter issues during installation or while using the application, ensure that all prerequisites are met and that your CSV file is formatted correctly. For Docker users, verify that Docker is running correctly on your machine.

## Contributing

Contributions to Time Coordinator are welcome! Please feel free to fork the repository, make your changes, and submit a pull request.
