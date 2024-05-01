import json
from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)


openai_keys = json.load(open('C:/shared/content/config/api-keys/hackathon_openai_keys.json'))
my_openai_key = openai_keys['team_1']

file = open("D:/AS2-9d5cdd2100752e76/My Files/Home Folder/demoApp/data.txt","r")
data = file.read()

openAI_client = OpenAI(
    api_key=my_openai_key,
)

@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/home",methods=['POST'])
def getValue():
    searchString = request.form['searchString']
    response = openAI_client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role":"user",
            "content":searchString+' '+data,
        },
    ],
)
    response_data = response.choices[0].message.content
    print(response_data)
    return render_template('index.html',responseString=response_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)