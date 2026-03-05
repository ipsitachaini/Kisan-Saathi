import sys, subprocess, requests, time

import os
# Get the repository root (one level up from the backend directory where this script resides)
cwd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p = subprocess.Popen([sys.executable, "-m", "uvicorn", "backend.main:app", "--port", "8001"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=cwd)


time.sleep(4)

try:
    # Check version
    v_res = requests.get("http://127.0.0.1:8001/api/v1")
    print("VERSION CHECK:", v_res.text)

    res = requests.post(
        "http://127.0.0.1:8001/api/v1/auth/register", 
        json={"email": "debug@farmer.com", "password": "[PASSWORD]", "full_name": "Debug Farmer"}
    )
    print("HTTP STATUS:", res.status_code)
    print("HTTP RESPONSE:", res.text)

except Exception as e:
    print("Request failed:", e)

p.terminate()
stdout, _ = p.communicate()

print("\n--- UVICORN LOG ---")
print(stdout.decode('utf-8', errors='replace'))
