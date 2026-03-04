import sys
import os

# Add backend directory to sys.path so we can import app and other modules
# Netlify root is the repository root.
# Get the absolute path of the repository root
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(base_dir, 'backend'))

from main import app
from mangum import Mangum

# Wrap the FastAPI app for Netlify / Lambda
handler = Mangum(app)
