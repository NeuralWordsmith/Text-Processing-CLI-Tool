import sys
import string
import re
import nltk
import spacy
import sqlite3
import time
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Load Spacy model for Named Entity Recognition
nlp = spacy.load("en_core_web_sm")

# Initialize NLP tools
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
stop_words = set(stopwords.words("english"))

# Loading animation function
def loading_animation():
    spinner = ["|", "/", "-", "\\"]
    for _ in range(2):  # Rotate 2 times
        for symbol in spinner:
            print(f"\rProcessing {symbol}", end="", flush=True)
            time.sleep(0.2)  # Adjust speed if needed
    print("\rProcessing complete!    ")  # Clear last spinner frame

if len(sys.argv) > 1:
    filename = sys.argv[1]
    print("Filename received:", filename)

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

            # 🔹 Remove punctuation
            clean_content = content.translate(str.maketrans('', '', string.punctuation))

            # 🔹 Tokenize words
            words = clean_content.split()

            # 🔹 Count Sentences
            sentences = re.split(r'[.!?]+', content)
            sentences = [s.strip() for s in sentences if s.strip()]

            # 🔹 Count Paragraphs
            paragraphs = content.split("\n\n")
            paragraphs = [p.strip() for p in paragraphs if p.strip()]

            # 🔹 Stop-word Removal
            filtered_words = [word for word in words if word.lower() not in stop_words]

            # 🔹 Stemming
            stemmed_words = [stemmer.stem(word) for word in filtered_words]

            # 🔹 Lemmatization
            lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]

            # 🔹 Word Frequency Analysis
            word_counts = Counter(lemmatized_words)
            most_common_words = word_counts.most_common(10)

            # 🔹 Named Entity Recognition (NER)
            doc = nlp(content)
            entities = [(ent.text, ent.label_) for ent in doc.ents]

            print("✅ Analysis stored in SQLite database: text_analysis.db")

            # 🔹 INTERACTIVE MENU FOR USER INPUT
            def display_menu():
                print("\n📄 TEXT PROCESSING TOOL")
                print("=" * 50)
                print("1️⃣ Basic Statistics")
                print("2️⃣ Words AFTER Stop-word Removal")
                print("3️⃣ Words AFTER Stemming & Lemmatization")
                print("4️⃣ Top 10 Most Common Words")
                print("5️⃣ Named Entity Recognition (NER)")
                print("6️⃣ Save Results & Exit")
                print("=" * 50)

            display_menu()  # Show the full menu once

            while True:
                choice = input("\n🔹 Enter your choice (1-5) to choose an option, (M) Main Menu, or (Q) Quit: ").strip().lower()

                if choice in ["1", "2", "3", "4", "5"]:
                    loading_animation()

                if choice == "1":
                    print("\n📝 Basic Statistics")
                    print("-" * 50)
                    print(f"Total Words: {len(words)}")
                    print(f"Total Sentences: {len(sentences)}")
                    print(f"Total Paragraphs: {len(paragraphs)}")
                elif choice == "2":
                    print("\n🚫 Words AFTER Stop-word Removal")
                    print("-" * 50)
                    print(" ".join(filtered_words))
                elif choice == "3":
                    print("\n🌱 Words AFTER Stemming & Lemmatization")
                    print("-" * 50)
                    print("Stemming: " + " ".join(stemmed_words))
                    print("Lemmatization: " + " ".join(lemmatized_words))
                elif choice == "4":
                    print("\n📊 Top 10 Most Common Words")
                    print("-" * 50)
                    for word, count in most_common_words:
                        print(f"{word}: {count} times")
                elif choice == "5":
                    print("\n🏷 Named Entities Recognized")
                    print("-" * 50)
                    for entity, label in entities:
                        print(f"{entity} → {label}")
                elif choice == "6" or choice == "q":
                    print("\n🔹 Exiting program. Goodbye! 👋")
                    break
                elif choice == "m":
                    display_menu()
                else:
                    print("\n❌ Invalid choice. Returning to options...")

    except FileNotFoundError:
        print(f"\n❌ Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")

else:
    print("No filename provided.")
