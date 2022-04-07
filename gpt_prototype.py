import openai

openai.api_key = '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'

print('Enter a question:')
input = input()


response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=input,
  temperature=0,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response.choices[0].text)