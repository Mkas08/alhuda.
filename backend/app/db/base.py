from app.db.base_class import Base  # noqa: F401

# Import all models here for Alembic to detect them
# noqa: F401
from app.models.user import User, UserProfile, UserLocation, UserGoal, UserStats  # noqa
from app.models.quran import QuranSurah, QuranVerse, QuranTranslation, ReadingSession, VerseReadHistory  # noqa
