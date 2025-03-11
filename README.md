# text-processing-cli
# Text Processing CLI Tool  

A powerful Command-Line Interface (CLI) tool for text analysis, including:
- Word & Sentence Counting
- Stop-word Removal
- Stemming & Lemmatization
- Word Frequency Analysis
- Named Entity Recognition (NER)
- Interactive Menu for Easy Navigation
- SQLite Database Storage for Results

---

## Features  

- Basic Statistics (Word, Sentence, and Paragraph Count)  
- Stop-word Removal (Removes unnecessary words for cleaner analysis)  
- Stemming & Lemmatization (Reduces words to their root form)  
- Word Frequency Analysis (Finds the most common words)  
- Named Entity Recognition (NER) (Detects names, places, dates, organizations)  
- Interactive CLI (User-friendly menu for easy navigation)  
- Database Storage (Saves results in `text_analysis.db`)  

---

## Installation  

### 1. Install Python (if not installed)  
Ensure you have Python 3.x installed. You can check with:
```sh
python --version
```

### 2. Clone the Repository
```sh
git clone https://github.com/NeuralWordsmith/Text-Processing-CLI-Tool.git
cd Text-Processing-CLI-Tool
```

### 3. Install Required Dependencies
```sh
pip install nltk spacy sqlite3
python -m spacy download en_core_web_sm
```

---

## Usage  

Run the tool with a text file:  
```sh
python import.py your_text_file.txt
```

### Example Run
```sh
python import.py test_text.txt
```
You'll see the interactive menu:
```
Text Processing Tool
==================================================
1. Basic Statistics
2. Words AFTER Stop-word Removal
3. Words AFTER Stemming & Lemmatization
4. Top 10 Most Common Words
5. Named Entity Recognition (NER)
6. Save Results & Exit
==================================================
Enter your choice (1-5) to choose an option, (M) Main Menu, or (Q) Quit:
```

---

## Example Output  

**Basic Statistics:**
```
Basic Statistics
--------------------------------------------------
Total Words: 79
Total Sentences: 9
Total Paragraphs: 3
```

**Named Entity Recognition:**
```
Named Entities Recognized
--------------------------------------------------
Elon Musk → PERSON
Pretoria → GPE
South Africa → GPE
Tesla → ORG
OpenAI → ORG
Neuralink → PERSON
2023 → DATE
The New York Times → ORG
```

---

## Future Improvements  
- Export Results as JSON or CSV  
- Support for Different Languages  
- More Advanced NLP Features  

---

## Contributing  
Feel free to fork this repo and submit pull requests for improvements!  

---

## License  
This project is open-source and available under the MIT License.

