from sqlalchemy import (
    Column, Integer, String, Boolean, DateTime, ForeignKey, Float
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base_class import Base
import enum


class GoalType(str, enum.Enum):
    VERSE = "verse"
    TIME = "time"
    PAGE = "page"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    profile = relationship("UserProfile", back_populates="user", uselist=False)
    location = relationship("UserLocation", back_populates="user", uselist=False)
    goals = relationship("UserGoal", back_populates="user")
    stats = relationship("UserStats", back_populates="user", uselist=False)
    reading_sessions = relationship("ReadingSession", back_populates="user")
    verse_history = relationship("VerseReadHistory", back_populates="user")


class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    display_name = Column(String)
    bio = Column(String)
    profile_picture_url = Column(String)
    privacy_level = Column(String, default="public")

    user = relationship("User", back_populates="profile")


class UserLocation(Base):
    __tablename__ = "user_locations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    city = Column(String)
    country = Column(String)
    timezone = Column(String)

    user = relationship("User", back_populates="location")


class UserGoal(Base):
    __tablename__ = "user_goals"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    goal_type = Column(String, nullable=False)  # verse, time, page
    target_value = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="goals")


class UserStats(Base):
    __tablename__ = "user_stats"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    current_streak = Column(Integer, default=0)
    longest_streak = Column(Integer, default=0)
    total_verses_read = Column(Integer, default=0)
    total_hasanat = Column(Integer, default=0)
    last_read_at = Column(DateTime(timezone=True))

    user = relationship("User", back_populates="stats")
