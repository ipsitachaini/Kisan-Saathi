import sys
import os

# Root directory
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Backend directory
backend = os.path.join(root, 'backend')

if root not in sys.path:
    sys.path.insert(0, root)
if backend not in sys.path:
    sys.path.insert(0, backend)

from backend.main import app
