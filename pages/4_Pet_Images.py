from __future__ import annotations

import streamlit as st

import models

from database.session import session_scope
from services.image_service import ImageService
from services.pet_service import PetService

st.set_page_config(
    page_title="Pet Images",
    page_icon="📸",
    layout="wide",
)

st.title("📸 Pet Images")

# =====================================================
# Load Pets
# =====================================================

with session_scope() as db:
    pets = PetService.get_all_pets(db)

if not pets:
    st.warning("Please add at least one Pet first.")
    st.stop()

pet_options = {
    f"{pet.name} (#{pet.id})": pet.id
    for pet in pets
}

# =====================================================
# Upload Form
# =====================================================

with st.form("upload_image_form"):

    pet_name = st.selectbox(
        "Pet",
        list(pet_options.keys()),
    )

    uploaded_files = st.file_uploader(
        "Choose Image(s)",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True,
    )

    submitted = st.form_submit_button("📤 Upload")

# =====================================================
# Save Images
# =====================================================

if submitted:

    if not uploaded_files:

        st.error("Please select at least one image.")

    else:

        with session_scope() as db:

            for file in uploaded_files:

                ImageService.add_image(
                    db=db,
                    pet_id=pet_options[pet_name],
                    uploaded_file=file,
                )

        st.success("Images uploaded successfully.")

        st.rerun()

# =====================================================
# Show Images
# =====================================================

st.divider()

st.subheader("Uploaded Images")

selected_pet = st.selectbox(
    "Select Pet",
    list(pet_options.keys()),
    key="view_pet",
)

with session_scope() as db:

    images = ImageService.get_pet_images(
        db,
        pet_options[selected_pet],
    )

if images:

    cols = st.columns(3)

    for index, image in enumerate(images):

        with cols[index % 3]:

            st.image(
                image.image_path,
                use_container_width=True,
            )

            st.caption(image.image_type)

            if image.ai_analyzed:
                st.success("AI Analyzed")
            else:
                st.info("Not analyzed")

            if st.button(
                "🗑 Delete Image",
                key=f"delete_image_{image.id}",
                type="secondary",
            ):

                try:

                    with session_scope() as db:

                        ImageService.delete_image(
                            db=db,
                            image_id=image.id,
                        )

                    st.success("Image deleted successfully.")
                    st.rerun()

                except Exception as ex:

                    st.error(f"Cannot delete image: {ex}")

else:

    st.info("No images uploaded for this pet.")