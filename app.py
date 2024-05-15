import os
import chainlit as cl  # Importing the chainlit library for building chatbot applications.
# from chainlit.playground.providers import ChatOpenAI  # Import statement commented out.
from dotenv import load_dotenv  # For loading environment variables from .env files.
from langchain.agents.agent_types import AgentType  # Importing agent types from langchain.
from langchain_openai import ChatOpenAI  # For integrating OpenAI's API with langchain.
from langchain_experimental.agents.agent_toolkits import create_csv_agent  # To create agents that operate based on CSV data.
import pandas as pd  # For handling data in dataframe format.

load_dotenv()  # Load environment variables from .env file.

uploaded_file = ""  # A variable to store the path of the uploaded file.

@cl.on_chat_start  # Decorator that triggers the enclosed function at the start of a user session.
async def start_chat():
    files = None
    while files == None:  # Loop to ensure a file is uploaded.
        files = await cl.AskFileMessage(
            content="Please upload a csv file to begin!", accept=["csv"]
        ).send()  # Prompt user to upload a CSV file.

    csv_file = files[0]  # Access the first uploaded file.

    with open(csv_file.path, "r", encoding="utf-8") as f:  # Open the file in read mode with UTF-8 encoding.
        text = f.read()  # Read all contents of the file.
    # Notify user of the upload success and file content size.
    await cl.Message(
        content=f"`{csv_file.name}` uploaded, it contains {len(text)} characters!"
    ).send()

    cl.user_session.set("schedule_file_path", csv_file.path)  # Store the file path in the session.

@cl.on_message  # Decorator to handle each message received from the user during the session.
async def main(message: cl.Message):
    file_path = cl.user_session.get("schedule_file_path")  # Retrieve the stored file path from the session.
    chat_file_path = "chat.csv"
    df = pd.read_csv(file_path)  # Load the CSV file into a pandas dataframe.
    uploaded_file = [file_path, chat_file_path] # Update the global variable with the current file path.
    print(uploaded_file)  # Print the file path.
    agent = create_csv_agent(
        ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0125"),
        uploaded_file,
        verbose=True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
    )  # Create an agent with specific configurations to process CSV data.
    res = agent.invoke(message.content)  # Invoke the agent with the user's message.
    print(res)  # Print the response from the agent.
    # Send the response to the user.
    await cl.Message(res["output"]).send()
