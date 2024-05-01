import json
# from dotenv import load_dotenv
from openai import OpenAI

openai_keys = json.load(open('C:/shared/content/config/api-keys/hackathon_openai_keys.json'))
my_openai_key = openai_keys['team_1']

file = open("D:/AS2-e44125884bd0217c/My Files/Home Folder/demoApp/data.txt","r")
data = file.read()

openAI_client = OpenAI(
    api_key=my_openai_key,
)

response = openAI_client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role":"user",
            "content":"can you check which has max engagement score"+data,
        },
    ],
)
print(response.choices[0].message.content)