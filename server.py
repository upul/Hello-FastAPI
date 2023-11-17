from fastapi import FastAPI

app = FastAPI()

def fib(n):
    if n < 0:
        return "n must be a positive integer"
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    

@app.get("/api/v1/ping")
async def root():
    return {"message": "server is running"}

# endpoint for calculating the fibonacci number. write the as a POST method
@app.post("/api/v1/fibonacci")
async def fibonacci(n: int):
        return {"message": fib(n)}
