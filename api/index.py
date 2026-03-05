import sys
import os

# Add the project root to the path so we can import 'backend'
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from backend.main import app

# Vercel looks for 'app' in index.py
# If backend/main.py defines 'app', it's already imported.
