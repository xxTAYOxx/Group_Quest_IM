"""My Lists page — owned lists + lists shared with the current user."""
from __future__ import annotations

import streamlit as st

from auth import current_user, logout_user
from db import get_conn

st.set_page_config(page_title="My Lists · ListMate", page_icon="📋")

user = current_user()
if not user:
    st.warning("Please log in first.")
    st.page_link("app.py", label="← Go to login")
    st.stop()

st.sidebar.markdown(f"👤 **{user['username']}**")
if st.sidebar.button("Log out", use_container_width=True):
    logout_user()
    st.switch_page("app.py")

st.title("📋 My Lists")

with st.expander("➕ Create a new list", expanded=False):
    with st.form("new_list_form", clear_on_submit=True):
        new_name = st.text_input(
            "List name",
            max_chars=60,
            placeholder='e.g. "Groceries Tuesday"',
        )
        submitted = st.form_submit_button("Create list", use_container_width=True)
    if submitted:
        name = new_name.strip()
        if not name:
            st.error("Please give your list a name.")
        else:
            with get_conn() as conn:
                conn.execute(
                    "INSERT INTO lists (name, owner_id) VALUES (?, ?)",
                    (name, user["id"]),
                )
            st.success(f'List "{name}" created.')
            st.rerun()

with get_conn() as conn:
    owned_lists = conn.execute(
        """
        SELECT id, name, last_updated
        FROM lists
        WHERE owner_id = ?
        ORDER BY last_updated DESC
        """,
        (user["id"],),
    ).fetchall()

    shared_lists = conn.execute(
        """
        SELECT l.id, l.name, l.last_updated, u.username AS owner_username
        FROM lists l
        JOIN list_collaborators c ON c.list_id = l.id
        JOIN users u             ON u.id      = l.owner_id
        WHERE c.user_id = ?
        ORDER BY l.last_updated DESC
        """,
        (user["id"],),
    ).fetchall()

tab_owned, tab_shared = st.tabs(
    [f"My Lists ({len(owned_lists)})", f"Shared with me ({len(shared_lists)})"]
)

with tab_owned:
    if not owned_lists:
        st.info(
            "You don't have any shopping lists yet. Create your first one above ☝️"
        )
    else:
        for lst in owned_lists:
            with st.container(border=True):
                st.subheader(lst["name"])
                st.caption(f"Last updated: {lst['last_updated']}")
                if st.button(
                    "Open list",
                    key=f"open_owned_{lst['id']}",
                    use_container_width=True,
                ):
                    st.session_state["active_list_id"] = lst["id"]
                    st.switch_page("pages/02_List_Detail.py")

with tab_shared:
    if not shared_lists:
        st.info("No one has shared a list with you yet.")
    else:
        for lst in shared_lists:
            with st.container(border=True):
                st.subheader(lst["name"])
                st.caption(
                    f"Shared by **{lst['owner_username']}** · Last updated: {lst['last_updated']}"
                )
                if st.button(
                    "Open list",
                    key=f"open_shared_{lst['id']}",
                    use_container_width=True,
                ):
                    st.session_state["active_list_id"] = lst["id"]
                    st.switch_page("pages/02_List_Detail.py")
