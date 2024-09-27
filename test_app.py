import os
from fastapi.testclient import TestClient
from mini_groq import app 

from dotenv import load_dotenv
load_dotenv()

client = TestClient(app)

def test_get_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"message": "OK"}

def test_post_chat():
    response = client.post(
        "/chat",
        json={"prompt": "What is a LLM?"}
    )
    assert response.status_code == 200
    assert "response" in response.json()

def test_post_chat_rate_limit_exceeded(mocker):
    mocker.patch('groq.Groq.chat.completions.create', side_effect=groq.RateLimitError)

    response = client.post(
        "/chat",
        json={"prompt": "What is a LLM?"}
    )
    assert response.status_code == 429
    assert response.json() == {"detail": "Rate Limit Exceeded"}
