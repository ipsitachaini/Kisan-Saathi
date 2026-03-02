from fastapi.testclient import TestClient
from main import app

client = TestClient(app, raise_server_exceptions=True)

try:
    response = client.post(
        "/api/v1/auth/register",
        json={"email": "client_test@farmer.com", "password": "password123", "full_name": "Test Farmer"}
    )
    print("STATUS:", response.status_code)
    print("BODY:", response.json())
except Exception as e:
    import traceback
    traceback.print_exc()
