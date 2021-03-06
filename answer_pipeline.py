import openai
import os
from decouple import config
import re

openai.api_key = config('OPEN_AI')

questions = []

# Read questions file into string
with open("questions.txt") as file:
  questions = file.readlines()

# Produce answers via GPT-3
for txtfile in os.listdir(os.path.join("data", "text")):
  print("Starting: {}".format(txtfile))
  with open(os.path.join("data", "text", txtfile)) as file:
    data = file.read()
    data = re.sub(r"\s+", ' ', data)

    #Create output log file
    log_file = os.path.join("data", "log", txtfile)
    f = open(log_file, "w")

    #GPT API call
    for question in questions:
      try:
        response = openai.Completion.create(
          engine="text-davinci-002",
          prompt=data + '\n' + question,
          temperature=0,
          max_tokens=100,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0
        )

        #Write answers to output doc
        f.write(response.choices[0].text + "\n")
      except Exception as e:
        print(e)
  print("Done")