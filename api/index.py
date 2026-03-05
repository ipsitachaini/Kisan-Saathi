import sys
import os

# Root of the repo
root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# The backend folder where actual code lives
backend = os.path.join(root, 'backend')

if root not in sys.path:
    sys.path.insert(0, root)
if backend not in sys.path:
    sys.path.insert(0, backend)

from backend.main import app
