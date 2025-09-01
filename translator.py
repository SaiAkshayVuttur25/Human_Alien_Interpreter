import csv
import os

DICTIONARY_FILE = 'dictionary.csv'

def load_dictionaries():
    """
    Loads the translation dictionaries from the CSV file.
    Returns two dictionaries: one for English to Aliench, and one for Aliench to English.
    """
    eng_to_aliench = {}
    aliench_to_eng = {}
    
    if not os.path.exists(DICTIONARY_FILE):
        print(f"Error: The dictionary file '{DICTIONARY_FILE}' was not found.")
        print("Please make sure the file is in the same directory as the script.")
        return None, None

    with open(DICTIONARY_FILE, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        # Skip header row
        next(reader, None) 
        for row in reader:
            if len(row) == 2:
                english_word = row[0].strip().lower()
                aliench_word = row[1].strip().lower()
                eng_to_aliench[english_word] = aliench_word
                aliench_to_eng[aliench_word] = english_word
                
    return eng_to_aliench, aliench_to_eng

def translate_sentence(sentence, dictionary):
    """
    Translates a sentence word by word using the provided dictionary.
    If a word is not in the dictionary, it remains unchanged.
    """
    words = sentence.lower().split()
    translated_words = []
    
    for word in words:
        # Basic punctuation handling
        punctuation = ''
        if word and not word[-1].isalnum():
            punctuation = word[-1]
            word = word[:-1]
            
        # Translate the word or keep original if not found
        translated_word = dictionary.get(word, word) + punctuation
        translated_words.append(translated_word)
        
    return ' '.join(translated_words)

def main():
    """
    Main function to run the alien-human interpreter.
    """
    print("--- Alien-Human Language Interpreter ---")
    
    # Load dictionaries from the CSV file
    eng_to_aliench, aliench_to_eng = load_dictionaries()
    
    if eng_to_aliench is None:
        return # Exit if dictionaries could not be loaded

    while True:
        print("\nChoose an option:")
        print("1. Translate English to Aliench")
        print("2. Translate Aliench to English")
        print("3. Exit")
        
        choice = input("Enter your choice (1, 2, or 3): ")
        
        if choice == '1':
            sentence = input("Enter the English sentence to translate: ")
            translation = translate_sentence(sentence, eng_to_aliench)
            print(f"Translated to Aliench: {translation}")
        elif choice == '2':
            sentence = input("Enter the Aliench sentence to translate: ")
            translation = translate_sentence(sentence, aliench_to_eng)
            print(f"Translated to English: {translation}")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()