try:
    from backend.main import app
except Exception as e:
    import traceback
    import json
    err_msg = str(e)
    tb = traceback.format_exc()
    
    # Direct ASGI fallback to show TRUE error instead of Vercel 500
    async def app(scope, receive, send):
        if scope['type'] != 'http': return
        body = json.dumps({
            "status": "error", 
            "message": "Initialization crash", 
            "error": err_msg,
            "traceback": tb
        }).encode()
        await send({'type': 'http.response.start', 'status': 200, 'headers': [(b'content-type', b'application/json')]})
        await send({'type': 'http.response.body', 'body': body})
