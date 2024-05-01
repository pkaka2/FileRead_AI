import pandas as pd
import json
from openai import OpenAI

openai_keys = json.load(open('C:/shared/content/config/api-keys/hackathon_openai_keys.json'))
my_openai_key = openai_keys['team_1']

# file = open("D:/AS2-e44125884bd0217c/My Files/Home Folder/demoApp/data.txt","r")
# data = file.read()

client = OpenAI(
    api_key=my_openai_key,
)

client.files.create(
    file = open("D:/AS2-e44125884bd0217c/My Files/Home Folder/demoApp/data.txt","rb"),
    purpose = 'assistants',
)

response = client.beta.assistants.create(
    model="gpt-3.5-turbo",
    instructions="can you check which poid has max engagement score",
    tools=[{"type":"retrieval"}]
)
print(client)
