import streamlit as st

# Centered title
st.markdown(
    "<h1 style='text-align: center;'>Talent Align AI</h1>",
    unsafe_allow_html=True
)

# Function to display resume content
def resume_print(uploaded_file):
    if uploaded_file is not None:
        file_content = uploaded_file.read().decode("utf-8", errors="ignore")
        st.text_area("Resume content:", file_content, height=300)
    else:
        st.warning("No file uploaded.")

# Sidebar or main area toggle
option = st.radio("Select an option:", ("Resume", "Job Description"))

if option == "Resume":
    resume_file = st.file_uploader("Upload your resume here:")
    resume_print(resume_file)

elif option == "Job Description":
    jd_file = st.file_uploader("Upload job description here:")
    if jd_file is not None:
        jd_content = jd_file.read().decode("utf-8", errors="ignore")
        st.text_area("Job Description content:", jd_content, height=300)
    else:
        st.warning("No file uploaded.")
