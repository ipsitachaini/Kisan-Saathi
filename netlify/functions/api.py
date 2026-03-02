import sys
import os

# Add backend directory to sys.path so we can import app and other modules
# Netlify root is the repository root.
sys.path.append(os.path.join(os.getcwd(), 'backend'))

from main import app
from mangum import Mangum

# Wrap the FastAPI app for Netlify / Lambda
handler = Mangum(app)
