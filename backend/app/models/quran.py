from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base_class import Base


class QuranSurah(Base):
    __tablename__ = "quran_surahs"

    number = Column(Integer, primary_key=True, index=True)
    name_simple = Column(String, index=True)
    name_arabic = Column(String)
    revelation_place = Column(String)
    revelation_order = Column(Integer)
    verses_count = Column(Integer)

    verses = relationship("QuranVerse", back_populates="surah")


class QuranVerse(Base):
    __tablename__ = "quran_verses"

    id = Column(Integer, primary_key=True, index=True)
    surah_number = Column(Integer, ForeignKey("quran_surahs.number"), index=True)
    verse_number = Column(Integer, index=True)
    verse_key = Column(String, index=True)  # "1:1"
    text_uthmani = Column(Text)
    text_indopak = Column(Text, nullable=True)
    juz_number = Column(Integer)
    hizb_number = Column(Integer)
    page_number = Column(Integer)
    sajdah_number = Column(Integer, nullable=True)

    surah = relationship("QuranSurah", back_populates="verses")
    translations = relationship("QuranTranslation", back_populates="verse")
    read_history = relationship("VerseReadHistory", back_populates="verse")


class QuranTranslation(Base):
    __tablename__ = "quran_translations"

    id = Column(Integer, primary_key=True, index=True)
    verse_id = Column(Integer, ForeignKey("quran_verses.id"), index=True)
    language_code = Column(String, index=True)
    translator_name = Column(String)
    text = Column(Text)

    verse = relationship("QuranVerse", back_populates="translations")


class ReadingSession(Base):
    __tablename__ = "reading_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    start_time = Column(DateTime(timezone=True), server_default=func.now())
    end_time = Column(DateTime(timezone=True), nullable=True)
    duration_seconds = Column(Integer, default=0)
    verses_read_count = Column(Integer, default=0)
    hasanat_earned = Column(Integer, default=0)

    user = relationship("User", back_populates="reading_sessions")


class VerseReadHistory(Base):
    __tablename__ = "verse_read_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    verse_id = Column(Integer, ForeignKey("quran_verses.id"), index=True)
    read_at = Column(DateTime(timezone=True), server_default=func.now())
    session_id = Column(Integer, ForeignKey("reading_sessions.id"), nullable=True)

    user = relationship("User", back_populates="verse_history")
    verse = relationship("QuranVerse", back_populates="read_history")
