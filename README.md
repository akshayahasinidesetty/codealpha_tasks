CodeAlpha Python Programming Internship

Overview

This repository contains four beginner-friendly Python projects created for the CodeAlpha Python Programming Internship. The projects practise Python fundamentals, problem-solving, user input, and file handling.
Projects
1. Hangman Game — Guess a randomly selected word with up to six incorrect guesses.
2. Stock Portfolio Tracker — Calculate the total value of selected stocks using predefined sample prices. Optionally export the results to CSV.
3. Task Automation — Extract unique email addresses from input.txt and save them to emails_found.txt.
4. Basic Chatbot — Chat with a simple rule-based bot that responds to predefined messages.

Technologies

- Python 3
- Built-in modules: random, csv, re, pathlib, and datetime
- Git and GitHub
No third-party packages are required.
Project Structure

CodeAlpha_Python_Internship/
├── Hangman_Game/
│   └── hangman.py
├── Stock_Portfolio_Tracker/
│   └── stock_tracker.py
├── Task_Automation/
│   ├── email_extractor.py
│   └── input.txt
├── Basic_Chatbot/
│   └── chatbot.py
├── README.md
└── SUBMISSION_CHECKLIST.md

How to Run
Make sure Python is installed. Check the version:
python --version
Run each script from its project directory:

Hangman Game
python hangman.py
Stock Portfolio Tracker
python stock_tracker.py
Task Automation
python email_extractor.py
Place the text you want to scan in input.txt in the same directory as email_extractor.py. The extracted addresses will be saved in emails_found.txt.

Basic Chatbot
python chatbot.py
On Windows, you may use py instead of python if required.
Concepts Practised
- Variables, strings, lists, dictionaries, and sets
- Conditional statements and loops
- Functions and input validation
- Basic arithmetic
- File handling and CSV output
- Regular expressions and text processing
- Simple rule-based interaction
Learning Outcomes
These projects provide practical experience in writing and testing Python programs, organizing code, handling user input, processing text files, and automating simple tasks.
Future Improvements
Possible enhancements include adding difficulty levels to Hangman, supporting live stock-price data, automating additional file operations, adding chatbot intents, and writing automated tests.
Author
Akshaya Hasini Desetty
GitHub: akshayahasinidesetty
Acknowledgment
Project ideas are based on the task list supplied for the CodeAlpha Python Programming Internship. These projects are intended for educational purposes.
Note: Stock prices in this project are hardcoded sample values, not live market data or financial advice.
