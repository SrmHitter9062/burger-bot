from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
# Set open api key
client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)


def get_assistance(input):
    print("getting assistance")
    # model="gpt-4o-mini",  
    # messages=[{"role": "system", "content": "You are a compassionate mental health counselor."},
    #            {"role": "user", "content": message}]
    #        )
    # Call OpenAI API
    response = client.chat.completions.create(
        # model="gpt-3.5",
        model="gpt-4o-mini",
        messages=input,
        max_tokens=100,
        temperature=0.7
    )    
    print("response2:", response.choices[0].message)
    bot_reply = response.choices[0].message.content    
    return bot_reply