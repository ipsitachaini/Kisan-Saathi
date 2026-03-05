import sys
import os
import traceback
import json

# Absolute path to root
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if path not in sys.path:
    sys.path.insert(0, path)

try:
    from backend.main import app
except Exception as e:
    err_msg = str(e)
    tb = traceback.format_exc()
    
    # Simple direct ASGI app to bypass Vercel 500
    async def app(scope, receive, send):
        if scope['type'] != 'http': return
        body = json.dumps({
            "status": "error", 
            "message": "Backend initialization failed", 
            "error": err_msg,
            "traceback": tb
        }).encode()
        await send({'type': 'http.response.start', 'status': 200, 'headers': [(b'content-type', b'application/json')]})
        await send({'type': 'http.response.body', 'body': body})
