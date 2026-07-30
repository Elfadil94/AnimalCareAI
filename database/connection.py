from __future__ import annotations

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from config.settings import DATABASE_URL

# ==========================================================
# SQLAlchemy Engine
# ==========================================================

engine: Engine = create_engine(
    DATABASE_URL,
    echo=False,          # اجعلها True أثناء تصحيح الأخطاء إذا أردت
    future=True,
)

# ==========================================================
# Helper
# ==========================================================

def get_engine() -> Engine:
    """
    Return the SQLAlchemy engine.
    """
    return engine