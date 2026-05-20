import streamlit as st

from extractor import extract_text_from_pdf
from preprocess import preprocess_text
from vectorizer import vectorize_documents
from similarity import calculate_similarity
from gap_analysis import find_missing_keywords
from recommendation import generate_recommendations
from report_generator import generate_pdf_report
from skill_matcher import calculate_skill_match


# PAGE CONFIG
st.set_page_config(
    page_title="SkillSync AI",
    page_icon="📄",
    layout="wide"
)


# CUSTOM CSS
st.markdown(
    """
    <style>

    .main {
        background-color: #0f172a;
    }

    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        font-size: 18px;
        background-color: #2563eb;
        color: white;
        border: none;
    }

    .stButton>button:hover {
        background-color: #1d4ed8;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# HEADER
st.markdown(
    """
    <h1 style='text-align:center; color:white;'>
        📄 SkillSync AI
    </h1>

    <h3 style='text-align:center; color:lightgray;'>
        AI-Powered Resume Matcher
    </h3>
    """,
    unsafe_allow_html=True
)

st.markdown("---")


# INPUT SECTION
uploaded_resume = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=220
)


# ANALYZE BUTTON
if st.button("Analyze Resume"):

    if uploaded_resume and job_description:

        # SAVE TEMP PDF
        with open("temp_resume.pdf", "wb") as f:
            f.write(uploaded_resume.read())


        # EXTRACT TEXT
        raw_resume_text = extract_text_from_pdf(
            "temp_resume.pdf"
        )


        # PREPROCESS
        cleaned_resume = preprocess_text(
            raw_resume_text
        )

        cleaned_job_description = preprocess_text(
            job_description
        )


        # VECTORIZE
        vectors, vectorizer = vectorize_documents(
            cleaned_resume,
            cleaned_job_description
        )


        # SEMANTIC SCORE
        semantic_score = calculate_similarity(
            vectors
        )


        # SKILL MATCH SCORE
        skill_score, matched_skills = calculate_skill_match(
            cleaned_resume,
            cleaned_job_description
        )


        # FINAL SCORE
        match_score = (
            (skill_score * 0.8) +
            (semantic_score * 0.2)
        )


        # MISSING SKILLS
        missing_skills = find_missing_keywords(
            vectorizer,
            cleaned_resume,
            cleaned_job_description
        )


        # RECOMMENDATIONS
        recommendations = generate_recommendations(
            missing_skills
        )


        # CANDIDATE NAME
        candidate_name = raw_resume_text.split("\n")[0]


        # GENERATE PDF
        pdf_file = generate_pdf_report(
            candidate_name,
            match_score,
            missing_skills,
            recommendations
        )


        # SCORE COLOR
        score_color = "#ef4444"

        if match_score >= 75:
            score_color = "#22c55e"

        elif match_score >= 50:
            score_color = "#f59e0b"


        # SCORE CARD
        st.markdown(
            f"""
            <div style="
                background-color:{score_color};
                padding:20px;
                border-radius:15px;
                text-align:center;
                color:white;
                font-size:32px;
                font-weight:bold;
                margin-bottom:25px;
            ">
                Resume Match Score: {match_score:.2f}%
            </div>
            """,
            unsafe_allow_html=True
        )


        # RESULTS SECTION
        col1, col2 = st.columns(2)


        # MATCHING SKILLS
        with col1:

            st.subheader("✅ Matching Skills")

            if matched_skills:

                for skill in matched_skills:

                    st.markdown(f"- {skill}")

            else:

                st.warning("No matching skills found.")


        # MISSING SKILLS
        with col2:

            st.subheader("❌ Missing Skills")

            if missing_skills:

                for skill in missing_skills:

                    st.markdown(f"- {skill}")

            else:

                st.success("No missing skills found!")


        st.markdown("---")


        # RECOMMENDATIONS
        st.subheader("💡 Recommendations")

        for recommendation in recommendations:

            st.markdown(
                f"""
                <div style="
                    background-color:#1e293b;
                    padding:12px;
                    border-radius:10px;
                    margin-bottom:10px;
                    border-left:5px solid #3b82f6;
                    color:white;
                ">
                    ✅ {recommendation}
                </div>
                """,
                unsafe_allow_html=True
            )


        st.markdown("---")


        # DOWNLOAD REPORT
        with open(pdf_file, "rb") as pdf:

            st.download_button(
                label="📥 Download Professional PDF Report",
                data=pdf,
                file_name="SkillSync_Professional_Report.pdf",
                mime="application/pdf"
            )


        st.success(
            "Analysis Completed Successfully!"
        )

    else:

        st.warning(
            "Please upload a resume and enter a job description."
        )