from __future__ import annotations

from contextlib import contextmanager

from sqlalchemy.orm import Session, sessionmaker

from database.connection import engine

# ==========================================================
# Session Factory
# ==========================================================

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


# ==========================================================
# Create Session
# ==========================================================

def get_session() -> Session:
    """
    Returns a new SQLAlchemy session.
    """
    return SessionLocal()


# ==========================================================
# Context Manager
# ==========================================================

@contextmanager
def session_scope():
    """
    Automatically commits or rolls back transactions.
    """

    session = SessionLocal()

    try:
        yield session
        session.commit()

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()