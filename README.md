# 🛡️ ResumeAssess - AI-Powered Resume Discrepancy Detector

ResumeAssess is a powerful AI-based Streamlit web app that analyzes resumes (PDF format) using Google's Gemini LLM and LangChain. It identifies discrepancies, detects suspicious claims, and evaluates the credibility of resumes to help HR professionals and recruiters make informed decisions.

[Live Demo](https://verifyresume.streamlit.app)  
[GitHub Repo](https://github.com/memehdi14/ResumeAssess)

---

## Features

- **Resume Parsing**: Extracts text from uploaded PDF resumes using `pdfplumber`.
- **AI Discrepancy Detection**: Uses Gemini LLM to:
  - Check for fake or exaggerated qualifications
  - Identify illogical or inconsistent employment dates
  - Flag dubious institutions and suspicious claims
  - Analyze industry/domain shifts and job tenures
  - Rate the resume's honesty and credibility out of 10
- **Embeddings + Vector Search**: FAISS-powered similarity search to contextualize resume content.
- **Streamlit Interface**: User-friendly web interface to upload and analyze resumes.

---

## 📁 Project Structure
```bash
.
├── ResumeShield.py         # Core backend logic (resume parsing + AI analysis)
├── resumeshieldapp.py      # Streamlit frontend application
├── .env                    # Environment variables (API keys)
└── README.md               # You're here!
```

---

## Technologies Used

* [Streamlit](https://streamlit.io/)
* [LangChain](https://python.langchain.com/)
* [Google Generative AI (Gemini)](https://ai.google.dev/)
* [FAISS](https://github.com/facebookresearch/faiss)
* [pdfplumber](https://github.com/jsvine/pdfplumber)
* Python 3.9+

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/memehdi14/ResumeAssess.git
cd resumeassess
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up API Keys

Create a `.env` file in the root directory and add your Google API key:

```env
GOOGLE_API_KEY=your_api_key_here
```

### 5. Run the App

```bash
streamlit run resumeshieldapp.py
```

---

## Sample Usage

1. Launch the Streamlit app.
2. Upload a resume in PDF format.
3. Let the AI analyze the file.
4. View a structured discrepancy report and an honesty rating.

---

## Example Output

* Resume parsed
* Detected overlapping job dates
* Flagged unknown university
* Suggestion to verify job claims
* Honesty Rating: **8.5 / 10**

---

## Contributors

* **Mehdi Namdar** – Developer & AI Integrator
#### About me:-
```
I’m Mehdi Namdar — passionate about AI, automation, and building meaningful tools.
If you found this project useful or have ideas to improve it, feel free to connect or contribute.
Let’s build something better together!
Drop a mail at: Namdar.Mehdi14@gmail.com
```
[GitHub](https://github.com/memehdi14) [LinkedIn](https://in.linkedin.com/in/mohammad-mehdi-namdar-042609327) [Instagram](https://www.instagram.com/mehxbot/profilecard)

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

Built with ❤️ using:

* Google Gemini
* LangChain
* Streamlit

---
