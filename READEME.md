# Burger Queen

Burger Queen is a web-based chatbot built using Streamlit and powered by OpenAI's Generative AI models. It maintains conversational context and delivers an interactive user experience like
1. Takes order for burger and other add-ons(Extras, drinks etc)
2. Asks either it's pickup or delivery if it's delivery it asks for address details.
3. Summarise the order and check next if user wants to add anything else.
4. Asks for payment details and collect that.
---
#### Quick project outcome: [Click Here](https://drive.google.com/file/d/13slkAA5G-AaE9u5KrHx__orsiF3Arw69/view?usp=drive_link)

## Setup  

### 1. Create a Virtual Environment  

 > python3 -m venv .b_venv

### 2. Activate the Virtual Environment
Inside the project directory, run:

> source health_venv/bin/activate

### 3. Deactivate the Virtual Environment
To deactivate the virtual environment, use:

> deactivate

###  4. Install Dependencies
> pip install -r requirements.txt


### 5. Run the streamlit app
> streamlit run main.py


### Concepts Used

#### Generative AI Model

Utilizes OpenAI's GPT-4o-mini or GPT-3.5 Turbo for generating conversational responses.

#### Chat Completion

Maintains context of the conversation using message history, allowing the bot to remember past interactions and respond contextually.

#### Streamlit Library

A Python-based web framework used to create the interactive UI for BurgerBot.
Instructive Prompt

####  Prompt type - Instructive
Sets the initial context to guide the bot's behavior and maintain conversational flow.