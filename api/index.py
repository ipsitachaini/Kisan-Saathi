import sys
import os

# Root as usual
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root not in sys.path:
    sys.path.insert(0, root)

# Direct import - we've already confirmed absolute paths work
from backend.main import app
