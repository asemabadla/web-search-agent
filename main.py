from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class QueryRequest(BaseModel):
    query: str
@app.get("/")
def read_root():
    return {"status": "Web Search Agent is active and ready"}
@app.post("/invoke")
def invoke_agent(request: QueryRequest):
    return {"response": f"Summary for: {request.query}"}