# Database Schema - Al-Huda

This document describes the database schema and relationships for the Al-Huda Quran Habit Builder.

## Overview
Al-Huda uses **PostgreSQL** with **SQLAlchemy 2.0 (Async)** and **Alembic** for migrations.

## Tables

### Users & Authentication

#### `users`
Core authentication and account information.
- `id` (Integer, Primary Key): Unique identifier.
- `email` (String, Unique, Index): User's email address.
- `username` (String, Unique, Index): User's display handle.
- `hashed_password` (String): Bcrypt hashed password.
- `is_active` (Boolean): Default True.
- `created_at` (DateTime): Timestamp of account creation.
- `updated_at` (DateTime): Timestamp of last update.

#### `user_profiles`
Extended profile information for a user.
- `id` (Integer, Primary Key): Unique identifier.
- `user_id` (Integer, ForeignKey): Relationship to `users`.
- `display_name` (String): User's chosen name for display.
- `bio` (Text): User's short biography.
- `avatar_url` (String): URL to the user's profile picture.
- `privacy_level` (Enum): PUBLIC, PRIVATE, FRIENDS_ONLY.

#### `user_locations`
- `id`, `user_id`, `latitude`, `longitude`, `city`, `country`, `timezone`.

### Quran Data

#### `quran_surahs`
- `id`, `number`, `name_simple`, `name_complex`, `name_arabic`, `revelation_order`, `revelation_place`, `verses_count`.

#### `quran_verses`
- `id`, `surah_number`, `verse_number`, `verse_key`, `text_uthmani`.

#### `quran_translations`
- `id`, `verse_id` (FK to `quran_verses`), `language_code`, `text`.

### Progress & Tracking

#### `user_goals`
- `id`, `user_id`, `type` (VERSES, TIME, PAGES), `target`, `frequency`.

#### `user_stats`
- `id`, `user_id`, `current_streak`, `longest_streak`, `total_verses_read`, `total_reading_time`.

#### `reading_sessions`
- `id`, `user_id`, `start_time`, `end_time`.

#### `verse_read_history`
- `id`, `user_id`, `verse_id`, `reading_session_id`, `timestamp`.

## Relationships
- **User -> Profile:** One-to-One.
- **User -> Goals:** One-to-Many.
- **User -> History:** One-to-Many.
- **Surah -> Verse:** One-to-Many.
- **Verse -> Translation:** One-to-Many.
