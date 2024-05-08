# Welcome to Time Coordinator! 🚀🤖

![alt text](CrossTimeCoordinator.png)

This project consists of an asynchronous chatbot application that processes CSV files uploaded by users. The chatbot provides real-time interaction to manage and process data from the CSV files.

## Features

- **File Upload**: Prompts users to upload a CSV file at the start of a session.
- **Character Count**: Notifies the user of the number of characters in the uploaded CSV file.
- **Data Processing**: Processes messages using the content of the uploaded CSV file to generate responses.

## Getting Started

### Prerequisites

Ensure you have Python installed on your system. This project uses asynchronous features that require Python 3.7 or newer.

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/Mona3087/time-coordinator.git
cd time-coordinator
pip install -w requirements.txt
#Run Locally
chainlit run app.py -w 
```

Build Docker Container

```bash
docker build -t jira-app .
docker run -p 7860:7860 jira-app

