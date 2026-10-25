# 🎧 commentate-API

A fast and lightweight micro service API made to transform boring text into high energy football commentary.

## 🚀 How it works?
1. **The Server:** A high performance Go web server that listens to incoming HTTP POST requests.
2. **The Pipeline:** When it gets data, the Go server calls a python worker: `python3 worker.py "{data}"`
3. **The AI:** The python worker grabs the data using `sys.argv[1]` and immediately sends a request to Groq's cloud for talking with open source openai models.

## 📦 Why I built it this way
Render and other free cloud servers give you tiny RAM limits, so I built this to be super lightweight and ready to run. 

I am young teenager from Morocco, so I don't have a credit card for cloud servers. Because of that, this project is built to run easily and locally wherever you want.
### how to make the post request when running:
- use this command and replace "the+cat.." with your prompt:
```bash
curl "http://localhost:8080/?prompt=the+cat+saved+a+missel+shot"
```
for a better guide go to the release page it has the latest documentary and releases.

Thank you very much for checking out my API, and I hope you enjoy it! ⚽🔥
