import asyncio
from typing import AsyncGenerator

import pytest
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.api.deps import get_db
from app.core.config import settings
from app.db.base import Base

# Test database URL
TEST_SQLALCHEMY_DATABASE_URI = settings.SQLALCHEMY_DATABASE_URI + "_test"

@pytest.fixture(scope="session", autouse=True)
async def setup_test_db():
    """Create test database tables once per session."""
    engine = create_async_engine(TEST_SQLALCHEMY_DATABASE_URI, future=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await engine.dispose()

@pytest.fixture
async def db() -> AsyncGenerator[AsyncSession, None]:
    """Create a new session for each test."""
    engine = create_async_engine(TEST_SQLALCHEMY_DATABASE_URI, future=True)
    session_factory = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with session_factory() as session:
        yield session
        await session.rollback()
        await session.close()
    await engine.dispose()

@pytest.fixture
async def client(db: AsyncSession) -> AsyncGenerator[AsyncClient, None]:
    """Create a test client with the test database session overridden."""
    async def _get_test_db():
        yield db

    app.dependency_overrides[get_db] = _get_test_db
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        yield ac
    app.dependency_overrides.clear()
