from __future__ import annotations

import streamlit as st

import models

from database.session import session_scope
from services.ai_report_service import AIReportService
from services.ai_service import AIService
from services.image_service import ImageService
from services.pet_service import PetService

st.set_page_config(
    page_title="AI Analysis",
    page_icon="🤖",
    layout="wide",
)

st.title("🤖 AI Veterinary Analysis")

# =====================================================
# Load Pets
# =====================================================

with session_scope() as db:
    pets = PetService.get_all_pets(db)

if not pets:
    st.warning("No pets found.")
    st.stop()

pet_options = {
    f"{pet.name} — {pet.owner.first_name} {pet.owner.last_name}": pet
    for pet in pets
}

selected_pet_name = st.selectbox(
    "Select Pet",
    list(pet_options.keys()),
)

selected_pet = pet_options[selected_pet_name]

# =====================================================
# Load Images
# =====================================================

with session_scope() as db:
    images = ImageService.get_pet_images(
        db,
        selected_pet.id,
    )

if not images:
    st.info("This pet has no uploaded images.")
    st.stop()

image_options = {
    f"Image #{img.id} ({img.image_type})": img
    for img in images
}

selected_image_name = st.selectbox(
    "Select Image",
    list(image_options.keys()),
)

selected_image = image_options[selected_image_name]

st.image(
    selected_image.image_path,
    caption=selected_image.image_path,
    use_container_width=True,
)

# =====================================================
# Symptoms
# =====================================================

symptoms = st.text_area(
    "Owner Reported Symptoms",
    placeholder="Example: Red eyes, itching, vomiting, loss of appetite...",
)

# =====================================================
# Analyze
# =====================================================

if st.button("🔬 Analyze with Gemini", type="primary"):

    with session_scope() as db:

        with st.spinner("Analyzing image..."):

            try:

                report = AIService.analyze_image(
                    db=db,
                    pet_id=selected_pet.id,
                    pet_image_id=selected_image.id,
                    image_path=selected_image.image_path,
                    symptoms=symptoms,
                )

                st.success("Analysis completed successfully.")

                st.markdown(report)

            except Exception as ex:

                st.error(str(ex))

# =====================================================
# Previous Reports
# =====================================================

st.divider()

st.subheader("Previous Reports")

with session_scope() as db:

    reports = AIReportService.get_reports_for_pet(
        db,
        selected_pet.id,
    )

if reports:

    for report in reports:

        with st.expander(
            f"Report #{report.id} - {report.created_at}"
        ):

            st.caption(f"Model: {report.model_name}")

            if report.confidence:
                st.info(f"Confidence: {report.confidence}")

            if report.symptoms:
                st.write("### Symptoms")
                st.write(report.symptoms)

            st.write("### AI Report")
            st.markdown(report.report)

else:

    st.info("No AI reports available.")