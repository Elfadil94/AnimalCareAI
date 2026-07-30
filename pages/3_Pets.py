from __future__ import annotations

import streamlit as st

import models

from database.session import session_scope
from services.pet_service import PetService

st.set_page_config(
    page_title="Pets",
    page_icon="🐾",
    layout="wide",
)

st.title("🐾 Pets")

# =====================================================
# Load Data
# =====================================================

with session_scope() as db:
    owners = PetService.get_all_owners(db)
    species = PetService.get_all_species(db)

if not owners:
    st.warning("Please add at least one Owner first.")
    st.stop()

if not species:
    st.warning("Species table is empty.")
    st.stop()

owner_options = {
    f"{o.first_name} {o.last_name}": o.id
    for o in owners
}

species_options = {
    s.name: s.id
    for s in species
}

# =====================================================
# Form
# =====================================================

with st.form("pet_form"):

    pet_name = st.text_input("Pet Name")

    owner_name = st.selectbox(
        "Owner",
        list(owner_options.keys())
    )

    species_name = st.selectbox(
        "Species",
        list(species_options.keys())
    )

    gender = st.selectbox(
        "Gender",
        [
            "Male",
            "Female",
        ]
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=0.0,
        value=0.0,
        step=0.1,
    )

    color = st.text_input("Color")

    submitted = st.form_submit_button("💾 Save Pet")

# =====================================================
# Save
# =====================================================

if submitted:

    if not pet_name.strip():

        st.error("Pet name is required.")

    else:

        with session_scope() as db:

            PetService.create_pet(
                db=db,
                name=pet_name,
                owner_id=owner_options[owner_name],
                species_id=species_options[species_name],
                gender=gender,
                weight_kg=weight,
                color=color or None,
            )

        st.success("Pet added successfully.")
        st.rerun()

# =====================================================
# Table
# =====================================================

st.divider()

st.subheader("Registered Pets")

with session_scope() as db:

    pets = PetService.get_all_pets(db)

if pets:

    table = []

    for pet in pets:

        table.append(
            {
                "ID": pet.id,
                "Name": pet.name,
                "Owner": f"{pet.owner.first_name} {pet.owner.last_name}",
                "Species": pet.species.name,
                "Gender": pet.gender,
                "Weight": pet.weight_kg,
                "Color": pet.color,
            }
        )

    st.dataframe(
        table,
        use_container_width=True,
        hide_index=True,
    )

else:

    st.info("No pets found.")