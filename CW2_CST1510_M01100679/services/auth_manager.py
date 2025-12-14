import bcrypt
from typing import Optional
from models.user import User
from services.database_manager import DatabaseManager


class SimpleHasher:
    """
    Handles password hashing and checking.
    We use bcrypt because it is secure and recommended.
    """

    def hash_password(password: str) -> str:       # now using bcrypt, not text-file system
        """
        Turn a normal password into a safe, hashed version.
        This is what gets stored in the database.
        """
        bytes_pw = password.encode("utf-8")
        hashed = bcrypt.hashpw(bytes_pw, bcrypt.gensalt())
        return hashed.decode("utf-8")

    def check_password(password: str, stored_hash: str) -> bool:   # New password check logic
        """
        Compare a typed password with the hashed password from the database.
        Returns True if they match.
        """
        return bcrypt.checkpw(password.encode("utf-8"), stored_hash.encode("utf-8"))


class AuthManager:
    """
    Handles everything related to user accounts:
    - registering new users
    - logging in existing users
    """

    def __init__(self, db: DatabaseManager):
        self._db = db   #using DatabaseManager instead of text files

    def register_user(self, username: str, password: str, role: str = "user") -> bool:
        """
        Register a new user.
        Steps:
        1. Check if username already exists
        2. Hash the password
        3. Save username + hashed password in the database
        """

        existing = self._db.fetch_one(       #  check username in SQLite DB
            "SELECT username FROM users WHERE username = ?",
            (username,),
        )

        if existing is not None:
            return False

        hashed_pw = SimpleHasher.hash_password(password)    # hashing with bcrypt

        self._db.execute_query(  # save user in SQLite instead of writing to users.txt
            "INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
            (username, hashed_pw, role),
        )

        return True

    def login_user(self, username: str, password: str) -> Optional[User]:
        """
        Try to log a user in.
        Steps:
        1. Look up user in the DB
        2. Compare entered password with stored hashed password
        3. If match → return User object
        4. If not → return None
        """

        row = self._db.fetch_one(              #fetch login info from SQLite
            "SELECT id,username, password_hash, role FROM users WHERE username = ?",
            (username,),
        )

        if row is None:
            return None

        id_db, username_db, password_hash_db, role_db = row

        if SimpleHasher.check_password(password, password_hash_db):
            return User(id_db, username_db, password_hash_db, role_db)

        return None