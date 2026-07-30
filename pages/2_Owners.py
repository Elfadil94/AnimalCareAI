from __future__ import annotations

import streamlit as st

# مهم جداً: تحميل جميع الـ Models
import models

from database.session import session_scope
from services.owner_service import OwnerService

st.set_page_config(
    page_title="Owners",
    page_icon="👤",
    layout="wide",
)

st.title("👤 Owners")

# ==========================================================
# Owner Form
# ==========================================================

with st.form("owner_form"):

    col1, col2 = st.columns(2)

    with col1:
        first_name = st.text_input("First Name")
        email = st.text_input("Email")
        country = st.text_input("Country")
        address = st.text_input("Address")

    with col2:
        last_name = st.text_input("Last Name")
        phone = st.text_input("Phone")
        city = st.text_input("City")
        postal_code = st.text_input("Postal Code")

    submitted = st.form_submit_button("💾 Save Owner")

# ==========================================================
# Save Owner
# ==========================================================

if submitted:

    if not first_name.strip():
        st.error("First Name is required.")

    elif not last_name.strip():
        st.error("Last Name is required.")

    else:

        with session_scope() as db:

            OwnerService.create_owner(
                db=db,
                first_name=first_name,
                last_name=last_name,
                email=email or None,
                phone=phone or None,
                country=country or None,
                city=city or None,
                address=address or None,
                postal_code=postal_code or None,
            )

        st.success("✅ Owner added successfully.")
        st.rerun()

# ==========================================================
# Owners Table
# ==========================================================

st.divider()

st.subheader("Registered Owners")

with session_scope() as db:

    owners = OwnerService.get_all(db)

if owners:

    table = []

    for owner in owners:

        table.append(
            {
                "ID": owner.id,
                "First Name": owner.first_name,
                "Last Name": owner.last_name,
                "Email": owner.email,
                "Phone": owner.phone,
                "Country": owner.country,
                "City": owner.city,
            }
        )

    st.dataframe(
        table,
        use_container_width=True,
        hide_index=True,
    )

else:

    st.info("No owners found.")