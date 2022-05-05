import openai
import os
from decouple import config
import re

openai.api_key = config('OPEN_AI')

#read questions from file
with open("rating_prompt.txt") as file:
    rating_prompt = file.read()

for txtfile in os.listdir(os.path.join("data", "log")):
    print("Starting: {}".format(txtfile))
    with open(os.path.join("data", "log", txtfile)) as file:
        data = file.read()
    
    input = data + rating_prompt

    #create output log file
    log_file = os.path.join("data", "rating_log", txtfile)
    f = open(log_file, "w")

    #gpt3 api call
    try:
        response = openai.Completion.create(
          engine="text-davinci-002",
          prompt=input,
          temperature=0,
          max_tokens=100,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0
        )

        #write to output
        f.write(response.choices[0].text)
    except Exception as e:
        print(e)
print("Done")