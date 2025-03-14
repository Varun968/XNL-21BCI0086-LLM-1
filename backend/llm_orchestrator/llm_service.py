from langchain.llms import OpenAI
from fastapi import FastAPI

app = FastAPI()
llm = OpenAI(model="gpt-4", api_key="YOUR_OPENAI_API_KEY")

@app.get("/analyze")
def analyze_market(text: str):
    response = llm(text)
    return {"analysis": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
