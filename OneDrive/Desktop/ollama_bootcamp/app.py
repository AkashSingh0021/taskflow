import streamlit as st
import time
import re
import os

from analyzer import analyze_resume
from pdfreader import extract_text
from reportgenerator import generate_pdf

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# LOAD CSS
# ==========================================

def load_css():
    try:
        with open("styles/style.css") as css:
            st.markdown(
                f"<style>{css.read()}</style>",
                unsafe_allow_html=True
            )
    except FileNotFoundError:
        st.warning("style.css not found.")

load_css()

# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    try:
        st.image("assets/logo.png", width=180)
    except:
        pass

    st.title("🤖 AI Resume Analyzer")

    st.markdown("---")

    st.success("✅ Local AI")
    st.success("✅ Ollama")
    st.success("✅ DeepSeek")
    st.success("✅ ATS Resume Scanner")

    st.markdown("---")

    st.subheader("👨‍💻 Developer")

    st.write("""
Akash Singh

B.Tech CSE

DevOps | AWS | Docker | Terraform
""")

    st.markdown("---")

    st.info(
        """
Upload your Resume

Get ATS Score

Improve Resume

Prepare Interview
"""
    )

# ==========================================
# HEADER
# ==========================================

st.title("📄 AI Resume Analyzer")

st.caption(
    "Professional ATS Resume Analysis using Ollama + DeepSeek AI"
)

st.markdown("---")

# ==========================================
# TWO COLUMN LAYOUT
# ==========================================

left, right = st.columns([2,1])

with left:

    uploaded_file = st.file_uploader(
        "📂 Upload Resume",
        type=["pdf"]
    )

with right:

    st.markdown("### 📌 Supported Format")

    st.write("✔ PDF")

    st.write("✔ ATS Friendly Resume")

    st.write("✔ Maximum Size : 200 MB")

st.markdown("---")

# ==========================================
# WAIT FOR FILE
# ==========================================

if uploaded_file is None:

    st.warning("📂 Please upload your Resume.")

else:

    # ======================================
    # READ PDF
    # ======================================

    with st.spinner("Reading Resume..."):

        progress = st.progress(0)

        for i in range(101):

            progress.progress(i)

            time.sleep(0.01)

        resume = extract_text(uploaded_file)

        progress.empty()

    st.success("✅ Resume Uploaded Successfully")

    with st.expander("📄 Resume Preview"):

        st.text(resume[:5000])

    st.markdown("---")
        # ======================================
    # ANALYZE BUTTON
    # ======================================

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        analyze = st.button(
            "🚀 Analyze Resume",
            use_container_width=True
        )

    # ======================================
    # START ANALYSIS
    # ======================================

    if analyze:

        st.markdown("---")

        status = st.empty()

        progress = st.progress(0)

        status.info("🤖 Initializing AI Model...")

        for i in range(20):
            progress.progress(i + 1)
            time.sleep(0.03)

        status.info("📄 Reading Resume...")

        for i in range(20,40):
            progress.progress(i + 1)
            time.sleep(0.03)

        status.info("🧠 AI is analyzing your Resume...")

        result = analyze_resume(resume)

        # ======================================
        # GENERATE PDF REPORT
        # ======================================

        os.makedirs("reports", exist_ok=True)

        pdf_path = "reports/ATS_Report.pdf"

        generate_pdf(result, pdf_path)

        for i in range(40,100):
            progress.progress(i + 1)
            time.sleep(0.02)

        progress.empty()

        status.empty()

        st.success("🎉 Resume Analysis Completed Successfully!")

        st.balloons()

        st.markdown("---")

        # ======================================
        # TRY TO EXTRACT ATS SCORE
        # ======================================

        ats_score = "N/A"

        match = re.search(r"Overall Score[: ]*([0-9]+)", result)

        if match:
            ats_score = match.group(1)

        # ======================================
        # ATS SCORE CARD
        # ======================================

        st.markdown("## 📊 ATS Score")

        c1, c2, c3 = st.columns(3)

        with c2:

            st.metric(
                label="Overall ATS Score",
                value=f"{ats_score}/100"
            )

        st.markdown("---")

        # ======================================
        # COMPLETE REPORT
        # ======================================

        st.markdown("## 📑 Complete Analysis")

        st.markdown(result)

        st.markdown("---")

        # ======================================
        # DOWNLOAD BUTTONS
        # ======================================

        d1, d2, d3 = st.columns(3)

        with d1:

            st.download_button(
                label="📥 Download TXT Report",
                data=result,
                file_name="ATS_Report.txt",
                mime="text/plain",
                use_container_width=True
            )

        with d2:

            st.download_button(
                label="📥 Download Markdown Report",
                data=result,
                file_name="ATS_Report.md",
                mime="text/markdown",
                use_container_width=True
            )

        with d3:

            with open(pdf_path, "rb") as pdf_file:
                st.download_button(
                    label="📄 Download PDF Report",
                    data=pdf_file,
                    file_name="ATS_Report.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )

        st.markdown("---")

        # ======================================
        # TIPS
        # ======================================

        st.info(
            """
### 💡 Resume Improvement Tips

✅ Add more projects.

✅ Mention measurable achievements.

✅ Add certifications.

✅ Optimize ATS keywords.

✅ Keep resume within 1-2 pages.

✅ Customize resume for every job.

✅ Include GitHub and LinkedIn profile.

✅ Highlight technical skills.
"""
        )

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.markdown(
"""
<div style='text-align:center;'>

<h4>🤖 AI Resume Analyzer</h4>

<p>Built with ❤️ using Streamlit + Ollama + DeepSeek</p>

<p>Developed by <b>Akash Singh</b></p>

</div>
""",
unsafe_allow_html=True
)