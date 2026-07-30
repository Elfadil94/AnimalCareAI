from __future__ import annotations

import streamlit as st

import models

from database.session import session_scope
from services.dashboard_service import DashboardService

st.set_page_config(
    page_title="AnimalCare AI",
    page_icon="🐾",
    layout="wide",
)

st.title("🐾 AnimalCare AI")

st.markdown(
    """
    ### Welcome to AnimalCare AI

    Manage pets, owners and AI-powered veterinary reports.
    """
)

# ==========================================================
# Load Dashboard Data
# ==========================================================

with session_scope() as db:
    stats = DashboardService.get_statistics(db)

# ==========================================================
# Metrics
# ==========================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "👤 Owners",
        stats["owners"],
    )

with col2:
    st.metric(
        "🐾 Pets",
        stats["pets"],
    )

with col3:
    st.metric(
        "🐶 Species",
        stats["species"],
    )

st.divider()

# ==========================================================
# Latest Pets
# ==========================================================

st.subheader("🐾 Latest Registered Pets")

if stats["latest_pets"]:

    table = []

    for pet in stats["latest_pets"]:

        table.append(
            {
                "ID": pet.id,
                "Pet": pet.name,
                "Owner": (
                    f"{pet.owner.first_name} "
                    f"{pet.owner.last_name}"
                ),
                "Species": pet.species.name,
                "Gender": pet.gender,
                "Weight (kg)": pet.weight_kg,
            }
        )

    st.dataframe(
        table,
        use_container_width=True,
        hide_index=True,
    )

else:

    st.info("No pets registered yet.")

st.divider()

st.success("✅ Database connected successfully.")