import sys, subprocess, requests, time

cwd = r"c:\Users\ipsit\OneDrive\Documents\smart-agri-platform\backend"
p = subprocess.Popen([sys.executable, "-m", "uvicorn", "main:app", "--port", "8001"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=cwd)
time.sleep(4)

try:
    res = requests.post(
        "http://127.0.0.1:8001/api/v1/auth/register", 
        json={"email": "debug@farmer.com", "password": "password123", "full_name": "Debug Farmer"}
    )
    print("HTTP STATUS:", res.status_code)
    print("HTTP RESPONSE:", res.text)
except Exception as e:
    print("Request failed:", e)

p.terminate()
stdout, _ = p.communicate()

print("\n--- UVICORN LOG ---")
print(stdout.decode('utf-8', errors='replace'))
