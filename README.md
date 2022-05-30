# Computer Network Project: Diverting in Socially (Ir)responsible ISP

Final Publication Artifact: https://docs.google.com/document/d/1GvsGTeLyuy8OWV8tfBA9YP4aLPyZyUCXU_mntvX3t4w/edit?usp=sharing

## Requirements:
- Python >3.6

## Installations:
- Clone the repository:
```
git clone https://github.com/ckjones818/isp-responsibility.git
```
- Create a virtual environment (optional but recommended) for this project
- Download dependencies:
```
pip install -r requirements.txt
```
- Create an environment file (to store API keys):
```
touch .env
```
- Get an API key from [OPENAI](https://openai.com/blog/openai-api/) and [ECFS](https://www.fcc.gov/ecfs/help/public_api) and put it in the .env file by replacing YOUR_API_KEY with your actual key:
```
echo "OPEN_AI='YOUR_API_KEY'\nECFS='YOUR_API_KEY'" > .env
```

## How to use:
- scraper.py: download all the relevant documents regarding ISP's stance on various social responsibilities.
```
python scraper.py
```
- text-parser.py: parse all pdfs and doc(s) files into text files
```
python text_parser.py
```
- rating_pipeline.py: parses text files and answers questions in questions.txt with GPT's API
```
python rating_pipeline.py
```
- answer_pipeline.py: parses answers from rating_pipeline.py and answers questions in rating_prompt.txt with GPT's API
```
python answer_pipeline.py
```
