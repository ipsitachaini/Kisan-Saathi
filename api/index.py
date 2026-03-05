import sys
import os

# Absolute path to the project root
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root not in sys.path:
    sys.path.insert(0, root)

# Import the actual FastAPI app
from backend.main import app
