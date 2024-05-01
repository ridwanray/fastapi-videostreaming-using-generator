# FastAPI Video Streaming Service using Generators
FastAPI Video Streaming Service using Generators

## Running In a Virtual Env

Create a virtual environment using python3.10:
```
python3 -m venv venv
```

```
pip install -r requirements.txt
```

Run the server locally using:

```
uvicorn main:app --reload
```

Access docs:
```sh
http://127.0.0.1:8000/docs/
```
## Run via docker
Alternatively, you can use docker to run the app as a container.
1. Build the image :
```sh
docker build -t fastapi-video-streaming . // This assumes you are in the directory where the dockerfile is located
```
2. Run the container
```sh
docker run -itd --name <name> <image tag> // Replace "<name>" and "<image tag>" with the container name and image name respectively
```  
