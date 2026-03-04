import sys
import os

# Get the absolute path of the repository root
# functions/api.py -> parent is root
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
backend_path = os.path.join(base_dir, 'backend')
if backend_path not in sys.path:
    sys.path.append(backend_path)

from main import app
from mangum import Mangum

# Wrap the FastAPI app for Netlify / Lambda
handler = Mangum(app)
