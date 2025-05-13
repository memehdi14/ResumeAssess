import os
import pdfplumber
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.vectorstores import Chroma
from langchain.chains.question_answering import load_qa_chain
from dotenv import load_dotenv

load_dotenv()

def parse_resume(pdf_path):
    """Extract text from a PDF resume."""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            resume_text = ""
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    resume_text += text + "\n"
        return resume_text
    except Exception as e:
        return f"Error parsing PDF: {str(e)}"

def analyze_resume_with_llm(resume_text):
    """Use LLM to detect falsification or discrepancies in the resume."""
    try:
        # Initialize Gemini model and vectorstore
        model = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash", temperature=0)
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        vectorstore = Chroma.from_texts([resume_text], embeddings)

        # Similarity search
        docs = vectorstore.similarity_search("Check for resume discrepancies and potential falsification.")

        # QA Chain for analysis
        chain = load_qa_chain(model, chain_type="stuff")
        llm_response = chain.run(input_documents=docs, question=f"""
        You are a resume verification expert.

        Analyze the following resume for:
        - Fabricated or exaggerated qualifications (fake degrees, fake jobs)
        - Inconsistent or illogical dates (e.g. start > end, overlaps, gaps)
        - Dubious or unrecognized institutions
        - Unusual, Suspicious, Exxagerated claims (e.g. multiple degrees in overlapping timeframes)
        - Verify the skilllset with Job Expirience
        -Career Breaks
        - Analyse statistically,
                                 1) Job Change Frequency (Calculate and Display the Average tenure at single job)
                                 2) Industry Domain Changes(Mention the Industries worked on and Calculate avegrage tenure for each industry)
       Provide a detailed structured report based on above queries, highlighting extree red flags and providing suggestions to verify. Rate the resume out of 10 on its honesty and credibility based on your analysis ignoring the need for human verification.
        Note: A person can work alongside their graduation , format it properly don't use too much of asterisks
        Resume:
        {resume_text}
        """)

        return {
            "resume_text": resume_text,
            "llm_analysis": llm_response
        }

    except Exception as e:
        return {"error": f"LLM analysis failed: {str(e)}"}

def process_resume(pdf_path):
    resume_text = parse_resume(pdf_path)
    if "Error" in resume_text:
        return {"error": resume_text}
    
    return analyze_resume_with_llm(resume_text)

result = process_resume("path_to_resume.pdf")

if "error" in result:
    print(result["error"])
else:
    print("LLM Discrepancy Analysis Report:\n")
    print(result["llm_analysis"])