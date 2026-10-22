import requests
import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Error: No prompt provided")
        return
    content = sys.argv[1]

    apikey = os.environ.get("GROQ_API_KEY")
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {apikey}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "openai/gpt-oss-120b",
        "messages": [
            {"role": "user", "content": f"convert this text into football commentary text: {content}"}
        ]
    }
    print("now sending...")
    response = requests.post(url, json=payload, headers=headers)
    print(response.status_code)
    data = response.json()
    aimessage = data['choices'][0]['message']['content']
    print(aimessage)

if __name__ == "__main__":
    main()
