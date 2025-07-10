import streamlit as st

# for centre placement of title 
# instead of using title we use markdowm which has an access to html code too
st.markdown(
    """
    <h1 style='text-align: center;'>Talent Align AI</h1>
    """,
    unsafe_allow_html=True
)

#creating a resume button and 
resume_state = st.button("Resume")
jd_state = st.button("Job description")
st.write(resume_state)
st.write(jd_state)
 


