from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.auth import authrouter
import uvicorn

# Create the FastAPI app
app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,  
    allow_methods=["*"],  
    allow_headers=["*"]
)

app.include_router(authrouter)
# Example route
@app.get("/")
def read_root():
    return {"message": "Hello, world!"}

if __name__ == "__main__":
    uvicorn.run(app, port=8000)