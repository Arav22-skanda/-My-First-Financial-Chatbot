# Financial Chatbot

This is a simple rule-based chatbot built in Python that answers common financial questions using predefined responses. It is designed to help users quickly retrieve basic financial information such as revenue, expenses, net income, profit margin, and cash position.

## How It Works

The chatbot compares the user’s input to a list of exact, predefined questions using if-else conditions. If the input matches one of these questions, it returns a fixed answer. If the input does not match any known question, it shows a default message:  
*"Sorry, I can only provide information on predefined queries."*

## Supported Questions

The chatbot currently supports the following five questions:

- **What is the total revenue?**  
  → The total revenue is $1.5 million.

- **How has net income changed over the last year?**  
  → Net income increased by $200,000 compared to last year.

- **What are the total expenses?**  
  → Total expenses are $1.1 million.

- **What is the profit margin?**  
  → The profit margin is 26.7%.

- **How much cash does the company have?**  
  → The company has $500,000 in cash.

Note: The chatbot only recognizes these questions exactly as written. It will not understand reworded or similar questions.

## How to Run

1. Make sure you have Python installed (version 3.13.7 or any recent Python 3.x version).
2. Open a terminal or command prompt.
3. Navigate to the folder containing the chatbot files.
4. Run the following command in command prompt:

```bash
python Mychatbot.py
```

5. Type one of the supported questions, or type `exit` to quit.

## Technologies Used

- Python 3.13.7
- Built-in `input()` and `print()` functions (no external libraries required)
- Can be extended later with Flask or other tools for web-based use

## Files Included

- `Mychatbot.py` – Main Python script containing the chatbot logic
- `Chatbot documentation.txt` – This documentation file

## Limitations

- Only responds to exact predefined questions (case-sensitive).
- Cannot understand variations, synonyms, or natural language phrasing.
- Uses static data—no connection to a real database or live financial system.
- No support for real-time updates or user-specific data.

## Possible Improvements

- Add support for similar or paraphrased questions using fuzzy matching.
- Load answers from a data file (like JSON or CSV) instead of hardcoding them.
- Create a web interface using Flask or Streamlit.
- Add more financial metrics or support multiple companies.

---

This project is intended for learning and demonstration purposes. Feel free to use, modify, and build upon it!
