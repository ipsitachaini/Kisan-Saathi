import sys
import os

# Add the 'backend' folder to the python path so imports inside FastAPI work correctly
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))

from backend.main import app
