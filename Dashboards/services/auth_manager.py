import bcrypt
from typing import Optional
from models.user import User
from services.database_manager import DatabaseManager


class BcryptHasher:
    """Password hashing using bcrypt."""

    @staticmethod
    def hash_password(plain: str) -> str:
        hashed = bcrypt.hashpw(plain.encode("utf-8"), bcrypt.gensalt())
        return hashed.decode("utf-8")

    @staticmethod
    def check_password(plain: str, hashed: str) -> bool:
        return bcrypt.checkpw(plain.encode("utf-8"), hashed.encode("utf-8"))


class AuthManager:
    """Handles user registration and login."""

    def __init__(self, db: DatabaseManager):
        self._db = db
        self._hasher = BcryptHasher()

    def register_user(self, username: str, password: str, role: str = "user"):
        existing = self._db.fetch_one(
            "SELECT username FROM users WHERE username = ?",
            (username,),
        )
        if existing:
            return False, "Username already exists."

        password_hash = self._hasher.hash_password(password)
        self._db.execute_query(
            "INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
            (username, password_hash, role),
        )
        return True, "User registered successfully."

    def login_user(self, username: str, password: str) -> Optional[User]:
        row = self._db.fetch_one(
            "SELECT username, password_hash, role FROM users WHERE username = ?",
            (username,),
        )
        if row is None:
            return None

        username_db, password_hash_db, role_db = row
        if self._hasher.check_password(password, password_hash_db):
            return User(username_db, password_hash_db, role_db)

        return None