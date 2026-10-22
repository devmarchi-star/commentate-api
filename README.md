# 🎧 commentate-API
A fast and lightweight, micro service API made to transform boring text into high energy football commentary.
## 🚀 How it works?
1. **the API** its a high performance web server that listen to incoming HTTP POST requests.
2. **The execution pipeline** when getting data the API uses it to call `python worker.py {HTTP POST data here}`
3. **The python worker execution** the data transforms to the python worker with the help of `sys.argv[1]` and immediately send a request to groqs open source models hosted by them and for this i used the open source model ``
## 📦 infrastructure
* **Containerization**because renders cloud server are tiny "the free version" i containerize it to be lightweight and ready to be deployed to the cloud
# how to send to it
if you are in Linux you gonna use ``

so thank you for seeing and using this API. I hope you enjoy it.
