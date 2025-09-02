import csv
import os

DICTIONARY_FILE = "dictionary.csv"

# Load dictionary
def load_dictionary():
    eng_to_alien = {}
    alien_to_eng = {}
    
    if not os.path.exists(DICTIONARY_FILE):
        with open(DICTIONARY_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["english", "aliench"])  # header row

    with open(DICTIONARY_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            eng = row["english"].strip().lower()
            alien = row["aliench"].strip().lower()
            eng_to_alien[eng] = alien
            alien_to_eng[alien] = eng
    return eng_to_alien, alien_to_eng

# Add new word
def add_word(english, alien):
    with open(DICTIONARY_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([english.lower(), alien.lower()])
    print(f"Added word: {english} -> {alien}")

# Translate text
def translate(text, eng_to_alien, alien_to_eng, direction="eng_to_alien"):
    words = text.lower().split()
    result = []
    
    for word in words:
        if direction == "eng_to_alien":
            result.append(eng_to_alien.get(word, word))
        else:
            result.append(alien_to_eng.get(word, word))
    
    return " ".join(result)

# Translate input file -> output file
def translate_file(input_file, output_file, eng_to_alien, alien_to_eng, direction):
    with open(input_file, "r") as f:
        text = f.read()
    translated_text = translate(text, eng_to_alien, alien_to_eng, direction)
    
    with open(output_file, "w") as f:
        f.write(translated_text)
    print(f"Translated file saved as {output_file}")

# Main menu
def main():
    eng_to_alien, alien_to_eng = load_dictionary()
    
    while True:
        print("\n--- Alien-Human Interpreter ---")
        print("1. Translate English → Aliench")
        print("2. Translate Aliench → English")
        print("3. Add new word to dictionary")
        print("4. Translate input file to output file")
        print("5. Exit")
        
        choice = input("Enter choice: ").strip()
        
        if choice == "1":
            text = input("Enter English text: ")
            print("Translated:", translate(text, eng_to_alien, alien_to_eng, "eng_to_alien"))
        elif choice == "2":
            text = input("Enter Aliench text: ")
            print("Translated:", translate(text, eng_to_alien, alien_to_eng, "alien_to_eng"))
        elif choice == "3":
            eng = input("Enter English word: ")
            alien = input("Enter Aliench word: ")
            add_word(eng, alien)
            eng_to_alien, alien_to_eng = load_dictionary()  # reload dictionary
        elif choice == "4":
            infile = input("Enter input filename: ")
            outfile = input("Enter output filename: ")
            direction = input("Translate direction (eng_to_alien / alien_to_eng): ").strip()
            translate_file(infile, outfile, eng_to_alien, alien_to_eng, direction)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")

if _name_ == "_main_":
    main()