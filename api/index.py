import sys
import os
import traceback
import json

# Absolute path to root to ensure backend can be imported
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

try:
    from backend.main import app
except Exception as e:
    err_str = str(e)
    tb_str = traceback.format_exc()
    
    # Raw ASGI app catching import errors, returning an intentionally 200 OK
    # to bypass Vercel's 500 "An API error occurred" filter and show the raw error.
    async def app(scope, receive, send):
        if scope['type'] != 'http':
            return
            
        error_data = {
            "error": "Backend Startup Failed", 
            "message": err_str, 
            "traceback": tb_str
        }
        body = json.dumps(error_data).encode("utf-8")
        
        await send({
            'type': 'http.response.start',
            'status': 200,  # 200 forces Vercel to pass the payload through unaltered!
            'headers': [
                (b'content-type', b'application/json'),
                (b'content-length', str(len(body)).encode("utf-8")),
                (b'access-control-allow-origin', b'*')
            ]
        })
        await send({
            'type': 'http.response.body',
            'body': body
        })
