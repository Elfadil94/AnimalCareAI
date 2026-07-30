import streamlit as st

from utils.ai import analyze_pet
from utils.image_ai import analyze_pet_image

st.set_page_config(
    page_title="AnimalCare AI",
    page_icon="🐾",
    layout="wide",
)

st.title("🐾 AnimalCare AI")

st.markdown("""
AI-powered educational assistant for pet owners.

Upload a pet photo and describe the symptoms to receive educational guidance.

⚠️ This application does **not** replace a licensed veterinarian.
""")

# ============================
# Pet Information
# ============================

col1, col2 = st.columns(2)

with col1:
    pet = st.selectbox(
        "Pet Type",
        [
            "Dog 🐶",
            "Cat 🐱",
            "Rabbit 🐰",
            "Bird 🐦"
        ]
    )

with col2:
    age = st.number_input(
        "Age (Years)",
        min_value=0.0,
        max_value=50.0,
        value=1.0,
        step=0.5
    )

uploaded_image = st.file_uploader(
    "📷 Upload a photo (Optional)",
    type=["jpg", "jpeg", "png"]
)

if uploaded_image:
    st.image(uploaded_image, width=350)

symptoms = st.text_area(
    "Describe your pet's symptoms",
    height=180,
    placeholder="Example:\nMy dog has been coughing for two days and refuses to eat."
)

if st.button("🔍 Analyze", use_container_width=True):

    if symptoms.strip() == "":
        st.warning("Please describe the symptoms.")
        st.stop()

    image_report = ""

    # =====================================
    # Analyze Image
    # =====================================

    if uploaded_image is not None:

        with st.spinner("Analyzing image..."):

            try:
                image_report = analyze_pet_image(uploaded_image)

                st.success("Image analyzed successfully.")

                with st.expander("Image Analysis"):

                    st.write(image_report)

            except Exception as e:

                st.warning("Image analysis failed.")

                st.exception(e)

    # =====================================
    # Analyze Symptoms
    # =====================================

    final_symptoms = symptoms

    if image_report:

        final_symptoms = f"""
Image observations:

{image_report}

----------------------------

Reported symptoms:

{symptoms}
"""

    with st.spinner("Analyzing symptoms..."):

        try:

            result = analyze_pet(
                pet=pet,
                age=age,
                symptoms=final_symptoms,
            )

        except Exception as e:

            st.error("AI analysis failed.")

            st.exception(e)

            st.stop()

    st.success("Analysis Complete ✅")

    st.divider()

    left, right = st.columns(2)

    with left:

        st.subheader("Possible Causes")

        for cause in result["possible_causes"]:
            st.write("•", cause)

        st.subheader("Risk Level")

        risk = result["risk_level"].lower()

        if risk == "low":
            st.success(result["risk_level"])

        elif risk == "medium":
            st.warning(result["risk_level"])

        else:
            st.error(result["risk_level"])

    with right:

        st.subheader("Recommendations")

        for item in result["recommendations"]:
            st.write("•", item)

        st.subheader("Veterinary Advice")

        st.info(result["visit_vet"])

    st.divider()

    if result["emergency"]:
        st.error("🚨 This may be an emergency. Seek veterinary care immediately.")

    st.caption(result["disclaimer"])