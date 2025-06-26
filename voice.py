from googletrans import Translator, LANGUAGES
from gtts import gTTS
import playsound
import os

# Display supported languages
print("Supported languages:")
for code, name in LANGUAGES.items():
    print(f"{code} → {name}")

# Create translator
translator = Translator()

# Get user input
text = input("\nEnter text to translate: ")
target_lang = input("Enter target language code (e.g., 'en', 'ta', 'hi'): ")

# Translate the text
translated = translator.translate(text, dest=target_lang)
translated_text = translated.text

# Output
print("\n========== TRANSLATION ==========")
print(f"Original text     : {text}")
print(f"Target Language   : {LANGUAGES.get(target_lang, 'Unknown')}")
print(f"Translated text   : {translated_text}")
print("=================================")

# Convert to speech using gTTS
tts = gTTS(text=translated_text, lang=target_lang)
audio_file = "translated_audio.mp3"
tts.save(audio_file)

# Play the translated audio
playsound.playsound(audio_file)

# Clean up the audio file
os.remove(audio_file)
