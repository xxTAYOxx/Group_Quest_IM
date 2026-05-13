"""List Detail page — add, check off, and delete items on a shopping list."""
from __future__ import annotations

import streamlit as st

from auth import current_user, logout_user
from db import get_conn

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
        "SELECT id, name FROM lists WHERE id = ? AND owner_id = ?",
        (list_id, user["id"]),
    ).fetchone()

if not lst:
    st.error("List not found or you don't have access.")
    st.page_link("pages/01_My_Lists.py", label="← Back to My Lists")
    st.stop()

st.page_link("pages/01_My_Lists.py", label="← Back to My Lists")
st.title(f"📝 {lst['name']}")

with st.expander("➕ Add item", expanded=False):
    with st.form("add_item_form", clear_on_submit=True):
        new_name = st.text_input("Item name", placeholder='e.g. "Milk 1L"')
        new_qty = st.text_input(
            "Quantity / unit (optional)", placeholder='e.g. "2x" or "500g"'
        )
        new_cat = st.text_input(
            "Category (optional)", placeholder='e.g. "Dairy"', value="Other"
        )
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
        SELECT id, name, quantity, category, checked
        FROM items
        WHERE list_id = ?
        ORDER BY position ASC
        """,
        (list_id,),
    ).fetchall()

if not items:
    st.info("This list is empty. Add your first item above ☝️")
else:
    checked_count = sum(1 for i in items if i["checked"])
    st.caption(f"**{len(items)}** item(s) — {checked_count} checked off.")

    for item in items:
        cols = st.columns([1, 8, 1])
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
            st.markdown(f"{name_md}{qty}{cat}")

        with cols[2]:
            if st.button("🗑️", key=f"del_{item['id']}", help="Delete item"):
                with get_conn() as conn:
                    conn.execute("DELETE FROM items WHERE id = ?", (item["id"],))
                    conn.execute(
                        "UPDATE lists SET last_updated = CURRENT_TIMESTAMP WHERE id = ?",
                        (list_id,),
                    )
                st.rerun()
