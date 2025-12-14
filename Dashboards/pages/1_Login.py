import streamlit as st

from services.database_manager import DatabaseManager
from services.auth_manager import AuthManager

st.title("🔐 Login")

# Initialize database + auth manager
db = DatabaseManager("database/platform.db")
auth = AuthManager(db)

# Input fields
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Login button
if st.button("Login"):
    user = auth.login_user(username, password)

    if user is None:
        st.error("Invalid username or password")
    else:
        st.success(f"Welcome {user.get_username()}!")

        # Save user info in session state
        st.session_state["current_user"] = user.get_username()
        st.session_state["current_role"] = user.get_role()

        st.info("You are now logged in. Use the sidebar to navigate.")