from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
	return {"This is frist APP using FastAPI by Jimi"}
