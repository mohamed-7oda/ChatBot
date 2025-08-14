from fastapi import FastAPI
from pydantic import BaseModel
import os
from langchain_cohere import ChatCohere
from langchain.schema import HumanMessage, AIMessage

app = FastAPI()

# De Class 3a4an a3mel verification en el rad el men el model lazem yeb2a string
class ChatResponse(BaseModel):
    answer: str

# De Class 3a4an a3mel verification en el prombt el men el user lazem yeb2a string
class ChatRequest(BaseModel):
    prombt: str
    session_id: str  # to identify conversation

# Initialize LangChain's updated Cohere chat model
llm = ChatCohere(
    cohere_api_key=os.getenv("TOGETHER_API_KEY") or "ORpQXJdhHU93VMRqEAiwtXQqIXuxqTaZdcBEUxL8",
    model="command-a-03-2025"
)


# Store chat history in memory (key: session_id, value: list of messages)
chat_histories = {}

# ba2olo el response men no3 ChatbResponse el hwa lazem yeb2a string
@app.post("/chat", response_model=ChatResponse)
async def chat_with_cohere(request: ChatRequest):
    """
    Receives a prompt from the user, sends it to the Cohere model via LangChain,
    and returns the model's response.
    """

    # Get the history for this session (or start empty)
    history = chat_histories.get(request.session_id, [])

    # Add the user's message
    history.append(HumanMessage(content=request.prombt))

    # Call the model with the full conversation history
    response = llm.invoke(history)

    # Add the AI's reply to the history
    history.append(AIMessage(content=response.content))

    # Save updated history
    chat_histories[request.session_id] = history

    return ChatResponse(answer=response.content)

# to run: uvicorn main:app
