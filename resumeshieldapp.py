import streamlit as st
from ResumeShield import process_resume
import tempfile

st.set_page_config(page_title="ResumeAssesment", layout="centered")

# ----- Title & Header -----
st.markdown("<h1 style='text-align: center; color:green;'>🛡 ResumeAssess</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>AI-Powered Resume Discrepancy Detector</p>", unsafe_allow_html=True)
st.markdown("---")

# ----- Feature Summary -----
st.markdown("""
*What this tool does:*  
- Checks for *inconsistent date ranges*  
- Detects *suspicious or fake education claims*  
- Flags *unrecognized institutions*  
- Uses *LLM* to review overall content for *discrepancies*
""")

# ----- File Upload -----
uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    with st.spinner("Analyzing resume with AI..."):
        result = process_resume(tmp_path)

    if "error" in result:
        st.error(result["error"])
    else:
        st.success("Analysis complete!")
        st.subheader("AI Discrepancy Report")
        st.text_area("AI Review Output", result["llm_analysis"], height=300)

st.markdown("---")
st.caption("Built with LangChain + Gemini | by Mehdi Namdar")
