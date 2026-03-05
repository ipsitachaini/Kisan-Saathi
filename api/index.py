import sys
import os
import traceback
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

try:
    from backend.main import app
except Exception as e:
    err_str = str(e)
    tb_str = traceback.format_exc()
    
    # A raw ASGI application that doesn't rely on FastAPI, 
    # ensuring we get the error as JSON even if zero libraries are installed!
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
            'status': 500,
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
