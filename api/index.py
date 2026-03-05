import sys
import os

# Root as usual
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root not in sys.path:
    sys.path.insert(0, root)

# Import the actual FastAPI app
# BUILD_VERSION_FINAL: 1845_STABLE_REBUILD
from backend.main import app
