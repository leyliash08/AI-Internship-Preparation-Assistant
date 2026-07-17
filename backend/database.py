from sqlalchemy import DateTime, Integer, String, Text, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from datetime import datetime

DATABASE_URL = 'sqlite:///./internship_requests.db'

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

class Analysis(Base):
    __tablename__ = 'analysis'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    internship_goal: Mapped[str] = mapped_column(Text, nullable=False)
    required_skills: Mapped[str] = mapped_column(Text, nullable=False)
    learning_plan: Mapped[str] = mapped_column(Text, nullable=False)
    skill_gaps: Mapped[str] = mapped_column(Text, nullable=False)
    next_steps: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

Base.metadata.create_all(bind=engine)