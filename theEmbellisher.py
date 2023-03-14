import openai
from dotenv import load_dotenv
import os

load_dotenv()

openAiKey = os.getenv("OPENAI_API_KEY")
print(openAiKey)

# read a file on the same directory line by line and print it out
def process_file():
    file = open("keywords.csv", "r")
    # skip the first line
    next(file)
    for line in file:
        item = returnLine(line)
        print(item[3])
        result = callOpenAI(item[3])
        print(result)
        break
    file.close()

# return a line as a tuple
def returnLine(line):
    line = line.split(",")
    return line

# call openai api to get the result from chatgpt-turbo-3.5 model    
def callOpenAI(text: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "content": "what is the latest on inflation in the united states?",
            "role": "user"
        }],
        temperature=0,
        # max_tokens=150,
        # top_p=1,
        # frequency_penalty=0,
        # presence_penalty=0.6,
        # stop=["\n", " Human:", " AI:"]
    )
    print(response)






process_file()