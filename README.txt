EXPERIMENT 3: INTELLIGENT EMAIL ASSISTANT USING OLLAMA

REQUIREMENTS
1. Python 3.10 or newer
2. Ollama installed
3. A local Ollama model (instructions below)

SETUP ON WINDOWS
1. Extract the EmailAssistant folder.
2. Open Command Prompt or PowerShell.
3. Change to the project folder, for example:
   cd Desktop\EmailAssistant
4. Install the Python dependency:
   py -m pip install requests
5. Install Ollama from https://ollama.com/download
6. In a terminal, download the model:
   ollama pull llama3.2
7. Make sure Ollama is running. If necessary, open a separate terminal and run:
   ollama serve
8. Run the project from the EmailAssistant folder:
   py main.py

IMPORTANT
- The app expects Ollama at http://localhost:11434.
- The model name is set to llama3.2 in utils.py. If you use another model,
  change MODEL_NAME to the exact model name shown by `ollama list`.
- The dataset is in data/emails.csv.
- Saved replies are appended to outputs/generated_reply.txt.
- The similarity search uses Python's built-in SequenceMatcher, so no
  machine-learning package is required.
- If Ollama is unavailable, intent detection uses a General Inquiry fallback
  and reply/summary generation uses a basic fallback response.

FUNCTIONS
Q1-Q2: Customer details input and display
Q3: Intent detection with Ollama
Q4-Q5: CSV historical email retrieval
Q6: Professional reply generation
Q7: Friendly, Formal, or Empathetic tone
Q8: Summary within 50 words
Q9: Save email, reply, intent, and date
Q10: Continuous menu system
