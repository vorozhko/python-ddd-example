from sqlmodel import create_engine, Session, SQLModel

# SQLite database URL
DATABASE_URL = "sqlite:///movies.db"

# Create the database engine
engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    """Initialize the database by creating all tables."""
    SQLModel.metadata.create_all(engine)

def get_session() -> Session:
    """Provide a database session."""
    return Session(engine)