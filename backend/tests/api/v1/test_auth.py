import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from app.core import security
from app.core.config import settings

@pytest.mark.asyncio
async def test_register_user(client: AsyncClient):
    data = {
        "email": "test@example.com",
        "username": "testuser",
        "password": "Password123!"
    }
    response = await client.post(f"{settings.API_V1_STR}/auth/register", json=data)
    assert response.status_code == 200
    content = response.json()
    assert content["email"] == data["email"]
    assert content["username"] == data["username"]
    assert "id" in content


@pytest.mark.asyncio
async def test_register_user_weak_password(client: AsyncClient):
    data = {
        "email": "weak@example.com",
        "username": "weakuser",
        "password": "password"
    }
    response = await client.post(f"{settings.API_V1_STR}/auth/register", json=data)
    assert response.status_code == 422  # Pydantic validation error


@pytest.mark.asyncio
async def test_login_access_token(client: AsyncClient, db: AsyncSession):
    # Register first
    data = {
        "email": "login@example.com",
        "username": "loginuser",
        "password": "Password123!"
    }
    await client.post(f"{settings.API_V1_STR}/auth/register", json=data)

    # Login
    login_data = {
        "username": data["email"],
        "password": data["password"]
    }
    response = await client.post(
        f"{settings.API_V1_STR}/auth/login/access-token",
        data=login_data
    )
    assert response.status_code == 200
    content = response.json()
    assert "access_token" in content
    assert "refresh_token" in content
    assert content["token_type"] == "bearer"


@pytest.mark.asyncio
async def test_read_users_me(client: AsyncClient, db: AsyncSession):
    # Register and login to get token
    data = {
        "email": "me@example.com",
        "username": "meuser",
        "password": "Password123!"
    }
    await client.post(f"{settings.API_V1_STR}/auth/register", json=data)
    
    login_data = {
        "username": data["email"],
        "password": data["password"]
    }
    login_response = await client.post(
        f"{settings.API_V1_STR}/auth/login/access-token",
        data=login_data
    )
    token = login_response.json()["access_token"]

    # Access /me
    headers = {"Authorization": f"Bearer {token}"}
    response = await client.get(f"{settings.API_V1_STR}/users/me", headers=headers)
    assert response.status_code == 200
    content = response.json()
    assert content["email"] == data["email"]
    assert content["username"] == data["username"]
