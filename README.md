# resume_analysis
# Project Synopsis
Here you can check your resume with the job description and get the score and insights such as:
* ATS Score of the resume
* Probability of getting hired
* Keyword analysis
* SWOT Analysis
* Suggestions for overall improvement

## Steps for creating the project
1. Create the virtual environment - `python -m venv .venv`
2. Activate the virtual environment - `source .venv/bin/activate`
3. Create the .env file to store the api key.
4. Create the requirements.txt file and add the libraries for installation - `pip install -r requirements.txt`


# Architecture 
* app.py:front end creation and output of the genai model 
it will have the feature of capturing info such as Resume and JD 
* info we are capturing is "Resume.pdf" and 'job_desc'.
*pdf.py that will process the info in pdf and thats why we have installed 'pypdf
* analysis.py that will triganulate the pdf info and the JD and will provde insights and next step 