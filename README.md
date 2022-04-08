# Computer Network Project: Diverting in Socially (Ir)responsible ISP

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
- gpt_protocol.py: initialize gpt3 to be used on the command line
```
python gpt_protocol.py
```