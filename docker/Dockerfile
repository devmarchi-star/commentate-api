FROM python:3.11-slim
RUN apt-get update && apt-get install -y golang && rm -rf /var/lib/apt/lists/*
WORKDIR /app
RUN pip install --no-cache-dir requests
COPY . . 
RUN go build -o server main.go
EXPOSE 8080
CMD [ "./server" ]
