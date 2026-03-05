import sys
import os

# Add the project root to the path so we can import 'backend'
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if path not in sys.path:
    sys.path.insert(0, path)

from backend.main import app
