import streamlit as st

# for centre placement of title 
# instead of using title we use markdowm which has an access to html code too
st.markdown(
    """
    <h1 style='text-align: center;'>Talent Align AI</h1>
    """,
    unsafe_allow_html=True
)
col1, col2, col3, col4 = st.columns(4)
#creating a resume button and 
with col1 :
    resume_state = st.button("Resume")
    st.write(resume_state)
with col4 :
    jd_state = st.button("Job description")
    st.write(jd_state)




 

