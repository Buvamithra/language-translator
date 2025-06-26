# 🌍 AI-Powered Language Translator

This project is a **Language Translation Tool** built using **Artificial Intelligence and Machine Learning**. It takes a sentence or paragraph in one language and translates it into the target language using state-of-the-art NLP models.

> ✨ A simple and intelligent translator for global communication — useful for students, travelers, and cross-language learning apps.

---

## 📌 Features

- 🔄 Translates text between multiple languages
- 🧠 Powered by AI/ML (transformer-based models)
- 🎯 Accurate, fast, and easy to use
- 🖥️ Simple GUI and console interface
- 💬 Support for widely spoken languages like English, Tamil, Hindi, French, Spanish, German, etc.

---

## 🛠️ Technologies Used

- **Python**
- **Transformers (Hugging Face)**
- **TextBlob / Googletrans (Optional fallback)**
- **Tkinter** (for GUI)
- **Streamlit** (if deployed on web)
- **NLP** concepts: Tokenization, Translation APIs, Sequence-to-Sequence learning

---

## 📂 Project Structure

language-translator/
├── gui_translator.py # GUI version using Tkinter
├── console_translator.py # CLI version
├── translator_model.py # Main ML translation logic
├── requirements.txt # Python dependencies
└── README.md # You're reading it!

yaml
Copy
Edit

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/language-translator.git
cd language-translator
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Run the Console Version
bash
Copy
Edit
python console_translator.py
4. Run the GUI Version (Optional)
bash
Copy
Edit
python gui_translator.py
🎯 Example
mathematica
Copy
Edit
Input Language: English
Output Language: Tamil

Text: "How are you?"
Translation: "நீங்கள் எப்படி இருக்கிறீர்கள்?"
🧠 Model Logic
The translator uses a combination of:

transformers models (like MarianMT or M2M100) from Hugging Face

Tokenization and sequence encoding

Optional fallback to TextBlob or Googletrans for basic translations

Language codes are mapped internally

✅ Supported Languages (Examples)
Language	Code
English	en
Tamil	ta
Hindi	hi
French	fr
Spanish	es
German	de
Chinese	zh

You can add more languages easily by extending the model/language map.

🌐 Optional: Streamlit Web App (Bonus)
If you're using Streamlit, run:

bash
Copy
Edit
streamlit run app.py
A clean web interface will appear where users can select languages and translate text interactively.

🧪 Requirements
Python 3.7+

transformers

torch

sentencepiece

textblob (optional)

tkinter

streamlit (optional)

Install with:

bash
Copy
Edit
pip install transformers torch sentencepiece textblob streamlit
📬 Contact
Buvamithra Ulagarajan
📧 buvamithraulagarajan@gmail.com
🔗 LinkedIn

📄 License
This project is licensed under the MIT License. Free to use, modify, and distribute with credits.
