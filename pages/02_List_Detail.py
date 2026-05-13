"""List Detail page — add, check off, and delete items. Owner can invite collaborators."""
from __future__ import annotations

import streamlit as st

from auth import current_user, logout_user
from db import get_conn

CATEGORIES = ["Other", "Dairy", "Produce", "Bakery", "Meat", "Drinks", "Household"]

st.set_page_config(page_title="List · ListMate", page_icon="📝")

user = current_user()
if not user:
    st.warning("Please log in first.")
    st.page_link("app.py", label="← Go to login")
    st.stop()

st.sidebar.markdown(f"👤 **{user['username']}**")
if st.sidebar.button("Log out", use_container_width=True):
    logout_user()
    st.switch_page("app.py")

list_id = st.session_state.get("active_list_id")
if not list_id:
    st.warning("No list selected.")
    st.page_link("pages/01_My_Lists.py", label="← Back to My Lists")
    st.stop()

with get_conn() as conn:
    lst = conn.execute(
        """
        SELECT l.id, l.name, l.owner_id, u.username AS owner_username
        FROM lists l
        JOIN users u ON u.id = l.owner_id
        WHERE l.id = ? AND (
            l.owner_id = ?
            OR EXISTS (
                SELECT 1 FROM list_collaborators
                WHERE list_id = l.id AND user_id = ?
            )
        )
        """,
        (list_id, user["id"], user["id"]),
    ).fetchone()

if not lst:
    st.error("List not found or you don't have access.")
    st.page_link("pages/01_My_Lists.py", label="← Back to My Lists")
    st.stop()

is_owner = lst["owner_id"] == user["id"]

with get_conn() as conn:
    collaborators = conn.execute(
        """
        SELECT u.id, u.username
        FROM list_collaborators c
        JOIN users u ON u.id = c.user_id
        WHERE c.list_id = ?
        ORDER BY u.username
        """,
        (list_id,),
    ).fetchall()

st.sidebar.markdown("---")
st.sidebar.markdown("**👥 Members**")
owner_marker = " *(you)*" if is_owner else ""
st.sidebar.markdown(f"- **{lst['owner_username']}** _(owner)_{owner_marker}")
for c in collaborators:
    you_marker = " *(you)*" if c["id"] == user["id"] else ""
    st.sidebar.markdown(f"- {c['username']}{you_marker}")

st.page_link("pages/01_My_Lists.py", label="← Back to My Lists")
st.title(f"📝 {lst['name']}")
if not is_owner:
    st.caption(f"Shared with you by **{lst['owner_username']}**")

feedback = st.session_state.pop("invite_feedback", None)
if feedback:
    kind, msg = feedback
    if kind == "success":
        st.success(msg)
    else:
        st.error(msg)

if is_owner:
    with st.expander("👥 Invite collaborator", expanded=False):
        with st.form("invite_form", clear_on_submit=True):
            invite_username = st.text_input(
                "Username to invite",
                placeholder="e.g. anna",
            )
            invite_submit = st.form_submit_button(
                "Send invitation", use_container_width=True
            )
        if invite_submit:
            uname = invite_username.strip()
            if not uname:
                st.session_state["invite_feedback"] = ("error", "Please enter a username.")
            elif uname.lower() == user["username"].lower():
                st.session_state["invite_feedback"] = (
                    "error",
                    "You can't add yourself as a collaborator.",
                )
            else:
                with get_conn() as conn:
                    target = conn.execute(
                        "SELECT id, username FROM users WHERE LOWER(username) = LOWER(?)",
                        (uname,),
                    ).fetchone()
                    if not target:
                        st.session_state["invite_feedback"] = (
                            "error",
                            f"No user named '{uname}' exists.",
                        )
                    else:
                        already = conn.execute(
                            "SELECT 1 FROM list_collaborators WHERE list_id = ? AND user_id = ?",
                            (list_id, target["id"]),
                        ).fetchone()
                        if already:
                            st.session_state["invite_feedback"] = (
                                "error",
                                f"'{target['username']}' is already a collaborator.",
                            )
                        else:
                            conn.execute(
                                """
                                INSERT INTO list_collaborators (list_id, user_id, invited_by)
                                VALUES (?, ?, ?)
                                """,
                                (list_id, target["id"], user["id"]),
                            )
                            st.session_state["invite_feedback"] = (
                                "success",
                                f"Invited '{target['username']}' to this list.",
                            )
            st.rerun()

with st.expander("➕ Add item", expanded=False):
    with st.form("add_item_form", clear_on_submit=True):
        new_name = st.text_input("Item name", placeholder='e.g. "Milk 1L"')
        new_qty = st.text_input(
            "Quantity / unit (optional)", placeholder='e.g. "2x" or "500g"'
        )
        new_cat = st.selectbox("Category", options=CATEGORIES, index=0)
        add_submitted = st.form_submit_button("Add item", use_container_width=True)
    if add_submitted:
        name = new_name.strip()
        if not name:
            st.error("Item name is required.")
        else:
            with get_conn() as conn:
                next_pos = conn.execute(
                    "SELECT COALESCE(MAX(position), -1) + 1 AS p FROM items WHERE list_id = ?",
                    (list_id,),
                ).fetchone()["p"]
                conn.execute(
                    """
                    INSERT INTO items (list_id, name, quantity, category, added_by, position)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (
                        list_id,
                        name,
                        new_qty.strip() or None,
                        new_cat.strip() or "Other",
                        user["id"],
                        next_pos,
                    ),
                )
                conn.execute(
                    "UPDATE lists SET last_updated = CURRENT_TIMESTAMP WHERE id = ?",
                    (list_id,),
                )
            st.success(f'Added "{name}".')
            st.rerun()

with get_conn() as conn:
    items = conn.execute(
        """
        SELECT i.id, i.name, i.quantity, i.category, i.checked,
               i.added_by, u.username AS added_by_username
        FROM items i
        JOIN users u ON u.id = i.added_by
        WHERE i.list_id = ?
        ORDER BY i.checked ASC, i.position ASC
        """,
        (list_id,),
    ).fetchall()

if not items:
    st.info("This list is empty. Add your first item above ☝️")
else:
    checked_count = sum(1 for i in items if i["checked"])
    st.caption(f"**{len(items)}** item(s) — {checked_count} checked off.")

    for item in items:
        cols = st.columns([1, 8, 1], vertical_alignment="center")
        with cols[0]:
            new_state = st.checkbox(
                "checked",
                value=bool(item["checked"]),
                key=f"chk_{item['id']}",
                label_visibility="collapsed",
            )
            if new_state != bool(item["checked"]):
                with get_conn() as conn:
                    if new_state:
                        conn.execute(
                            "UPDATE items SET checked = 1, checked_at = CURRENT_TIMESTAMP WHERE id = ?",
                            (item["id"],),
                        )
                    else:
                        conn.execute(
                            "UPDATE items SET checked = 0, checked_at = NULL WHERE id = ?",
                            (item["id"],),
                        )
                    conn.execute(
                        "UPDATE lists SET last_updated = CURRENT_TIMESTAMP WHERE id = ?",
                        (list_id,),
                    )
                st.rerun()

        with cols[1]:
            name_md = f"~~{item['name']}~~" if item["checked"] else f"**{item['name']}**"
            qty = f" · {item['quantity']}" if item["quantity"] else ""
            cat = (
                f" · _{item['category']}_"
                if item["category"] and item["category"] != "Other"
                else ""
            )
            added_by = (
                f" · _added by {item['added_by_username']}_"
                if item["added_by"] != user["id"]
                else ""
            )
            st.markdown(f"{name_md}{qty}{cat}{added_by}")

        with cols[2]:
            if st.button("🗑️", key=f"del_{item['id']}", help="Delete item"):
                with get_conn() as conn:
                    conn.execute("DELETE FROM items WHERE id = ?", (item["id"],))
                    conn.execute(
                        "UPDATE lists SET last_updated = CURRENT_TIMESTAMP WHERE id = ?",
                        (list_id,),
                    )
                st.rerun()
