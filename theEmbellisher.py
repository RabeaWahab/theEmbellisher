import openai
from dotenv import load_dotenv
import os
import csv

load_dotenv()
openAiKey = os.getenv("OPENAI_API_KEY")
print(openAiKey)

# read a file on the same directory line by line and print it out
def processFile():
    with open("keywords.csv") as csv_file:
        file = csv.reader(csv_file, delimiter=',', quotechar='"')
        # skip the first line
        next(file)
        i = 0
        for line in file:
            item = line
            print(item[3])
            result = callOpenAI(item[3], item[0])
            writeToCSVFile(item[0], item[3], result)
            if (i > 1):
                break
            i+=1

def getGPTEmbellishment(content):
    return content.split("\n")[-1]

def getGPTKeywords(content):
    return content.split("\n")[:-1]
    
# write response to csv file with the date and keywords
def writeToCSVFile(date, keywords, response):
    os.remove("results.csv")
    with open("results.csv", "a+") as csv_file:
        file = csv.writer(csv_file, delimiter=',', quotechar='"')
        file.writerow([date, "\n".join(getGPTKeywords(response["choices"][0]["message"]["content"])), getGPTEmbellishment(response["choices"][0]["message"]["content"])])
        
    

# call openai api to get the result from chatgpt-turbo-3.5 model    
def callOpenAI(text: str, date: str):
    print("Sort the following keywords based on their societal impact, choose the top 5 keywords that you think are the most impactful if they are more than 5 and use them in a summary related to the day ({date}): {keywords}".format(date=date, keywords=text))
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "content": "Sort the following keywords based on their societal impact, choose the top 5 keywords that you think are the most impactful if they are more than 5 and use them in a summary related to the day ({date}): {keywords}".format(date=date, keywords=text),
            "role": "user"
        }],
        temperature=0,
        # max_tokens=,
        # top_p=1,
        # frequency_penalty=0,
        # presence_penalty=0.6,
        # stop=["\n", " Human:", " AI:"]
    )
    return response    
    
processFile()