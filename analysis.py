import streamlit as st
import google.generativeai as genai
from pdf import process_pdf
import os 
from dotenv import load_dotenv
load_dotenv()

# configure genai and model 
genai.configure(api_key = os.getenv("api_key"))
model = genai.GenerativeModel("gemini-1.5-flash")

def analyse_profile(pdf_doc,job_desc):
    if pdf_doc is not None:
        pdf=process_pdf(pdf_doc)
        st.sidebar.markdown("Upload Success")
    else:
        st.warning("Upload the Resume")

    good_fit = model.generate_content(f''' Compare the {job_desc} with resume{pdf} and suggest Am i a good 
                                        fit for the role  ''')
    ats_scores = model.generate_content(f''' Compare the {job_desc} with resume{pdf} and suggest the ATS
                                        score of the resume ''')
    probability = model.generate_content(f''' Compare the {job_desc} with resume{pdf} and suggest the probability
                                        of getting selected in percentage  ''')
    
    keywords = model.generate_content(f''' Compare the {job_desc} with resume{pdf} and give me a list of
                                        keywords shown in job description but missing from the resume ''')
    swot = model.generate_content(f''' Compare the {job_desc} with resume{pdf} and give me a list of SWOT 
                                           analysis followed by actionable insights in bullets points ''')
    
    projects = model.generate_content(f''' Compare the {job_desc} with resume{pdf} and give me a list of ML 
                                      competition or Projects that are aligned with job description & the role 
                                      in bullet points along with chances of getting selected in percentage ''') 

    return(st.write(good_fit.text),
           st.write(ats_scores.text),
           st.write(probability.text),
           st.write(swot.text),
           st.write(keywords.text),
           st.write(projects.text))                                               