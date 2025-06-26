from googletrans import Translator

# Create a translator object
translator = Translator()

# Input text and target language
text = input("Enter text to translate: ")
target_lang = input("Enter target language (e.g., 'en' for English, 'ta' for Tamil): ")

# Perform translation
translated = translator.translate(text, dest=target_lang)

# Show result
print(f"Translated text: {translated.text}")
