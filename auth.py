"""Authentication helpers: register, login, logout, session access."""
from __future__ import annotations

import bcrypt
import streamlit as st

from db import get_conn

MIN_PASSWORD_LENGTH = 8


def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def verify_password(password: str, password_hash: bytes) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), password_hash)


def register_user(username: str, email: str, password: str) -> tuple[bool, str]:
    username = username.strip()
    email = email.strip().lower()
    if not username or not email:
        return False, "Username and email are required."
    if len(password) < MIN_PASSWORD_LENGTH:
        return False, f"Password must be at least {MIN_PASSWORD_LENGTH} characters."
    with get_conn() as conn:
        clash = conn.execute(
            "SELECT 1 FROM users WHERE username = ? OR email = ?",
            (username, email),
        ).fetchone()
        if clash:
            return False, "Username or email is already taken."
        conn.execute(
            "INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
            (username, email, hash_password(password)),
        )
    return True, ""


def login_user(username: str, password: str) -> tuple[bool, str]:
    username = username.strip()
    with get_conn() as conn:
        row = conn.execute(
            "SELECT id, username, password_hash FROM users WHERE username = ?",
            (username,),
        ).fetchone()
    if not row or not verify_password(password, row["password_hash"]):
        return False, "Invalid username or password."
    st.session_state["user"] = {"id": row["id"], "username": row["username"]}
    return True, ""


def logout_user() -> None:
    st.session_state.pop("user", None)


def current_user() -> dict | None:
    return st.session_state.get("user")
