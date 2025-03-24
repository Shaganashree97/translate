from deep_translator import GoogleTranslator

def translate_text(text, target_language='fr'):
    translator = GoogleTranslator(source='auto', target=target_language)
    return translator.translate(text)

if __name__ == "__main__":
    text = input("Enter text to translate: ")
    target_lang = input("Enter target language code (e.g., 'fr' for French, 'es' for Spanish): ")
    translated_text = translate_text(text, target_lang)
    print(f"Translated text: {translated_text}")
