---
license: apache-2.0
title: Chatbot-with_OpenAI
sdk: streamlit
emoji: 🏆
colorFrom: red
colorTo: green
short_description: Chatbot-with_OpenAI
---


# Chatbot-with-OpenAI
An end-to-end GEN AI chatbot application built using OpenAI's language models (gpt-4, gpt-4-turbo, gpt-4o). This Streamlit-based web application was deployed in Hugging face spaces

## Features
- Interactive chat interface
- Customizable OpenAI model selection
- Adjustable response parameters (temperature and max tokens)
- Secure API key input
# Installation
To run the project:
- Install python
- Install dependencies from requirements.txt
```bash
pip install -r requirments.txt
```
# Usage
- Ensure you have an OpenAI API key
- Run the Streamlit app:
```bash
streamlit run app.py
```
- Open your web browser and go to the URL provided by Streamlit.
- Enter your OpenAI API key in the sidebar.
- Select the desired OpenAI model and adjust the response parameters.
- Type your question in the input field and receive answers from the chatbot
#  Configuration
The application allows you to configure:
- OpenAI API Key (required)
- OpenAI model selection (gpt-4, gpt-4-turbo, gpt-4o)
- Temperature (0.0 to 1.0)
- Max tokens (50 to 300)
# Dependencies
- python-dotenv
- langchain_community
- langchain-openai
- openai
- streamlit

