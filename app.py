from dotenv import load_dotenv
load_dotenv()# load the local variable s
import streamlit as st

from pdf import process_pdf
from analysis import analyse_profile
# create the front end 
st.header('Scan my :blue[CV.ai]',divider = 'green')
st.subheader('Tips for using the application')
notes=f"""

* Upload the resume(PDF only)
* Paste the **Job description**
* Unlesh the power of LLMs to derive insights about your resume.

"""

st.write(notes)

#sidebar
st.sidebar.subheader('Upload the resume ')
pdf_doc = st.sidebar.file_uploader('Upload the resume',type=['pdf'])
st.sidebar.write('Created by Akshay Matta')

# Job Description text Box
st.subheader("Enter the Job Description",divider=True)
job_desc = st.text_area(label="Enter the job description from job board(e.g.linkedin)",max_chars=10000)
submit = st.button(label="Get AI Powered Insights")

if submit:
    st.markdown(analyse_profile(pdf_doc=pdf_doc,job_desc=job_desc))