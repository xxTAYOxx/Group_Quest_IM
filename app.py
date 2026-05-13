"""ListMate — collaborative shopping list app. Entry point."""
import streamlit as st

from auth import current_user, login_user, logout_user, register_user
from db import init_db

st.set_page_config(page_title="ListMate", page_icon="🛒", layout="centered")

init_db()


def render_sidebar(username: str) -> None:
    st.sidebar.markdown(f"👤 **{username}**")
    if st.sidebar.button("Log out", use_container_width=True):
        logout_user()
        st.rerun()


def render_login_view() -> None:
    st.title("🛒 ListMate")
    st.caption("Your collaborative shopping list.")

    tab_login, tab_register = st.tabs(["Log in", "Register"])

    with tab_login:
        with st.form("login_form", clear_on_submit=False):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Log in", use_container_width=True)
        if submitted:
            ok, msg = login_user(username, password)
            if ok:
                st.rerun()
            else:
                st.error(msg)

    with tab_register:
        with st.form("register_form", clear_on_submit=False):
            r_username = st.text_input("Username", key="reg_username")
            r_email = st.text_input("Email", key="reg_email")
            r_password = st.text_input(
                "Password (min. 8 characters)", type="password", key="reg_password"
            )
            r_confirm = st.text_input(
                "Confirm password", type="password", key="reg_confirm"
            )
            submitted = st.form_submit_button("Create account", use_container_width=True)
        if submitted:
            if r_password != r_confirm:
                st.error("Passwords do not match.")
            else:
                ok, msg = register_user(r_username, r_email, r_password)
                if ok:
                    login_user(r_username, r_password)
                    st.rerun()
                else:
                    st.error(msg)


def render_home_view(user: dict) -> None:
    render_sidebar(user["username"])
    st.title("🛒 ListMate")
    st.success(f"Welcome back, **{user['username']}**!")
    st.markdown(
        "Open **📋 My Lists** from the sidebar to create or view your shopping lists."
    )


def main() -> None:
    user = current_user()
    if user:
        render_home_view(user)
    else:
        render_login_view()


main()
