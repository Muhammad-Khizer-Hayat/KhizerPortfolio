"""
Vercel serverless entrypoint.

Vercel's Python runtime (@vercel/python) auto-detects an ASGI/WSGI
app object named `app` in this file and wraps it as a serverless
function. Static assets (frontend/, static/) are served directly by
Vercel's CDN via vercel.json routes, so they never hit this function.
"""
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from backend.main import app  # noqa: E402

# Vercel looks for a module-level variable called `app`
__all__ = ["app"]
