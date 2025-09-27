# Mychatbot.py

def simple_chatbot(user_query):
    if user_query == "What is the total revenue?":
        return "The total revenue is $1.5 million."
    elif user_query == "How has net income changed over the last year?":
        return "Net income increased by $200,000 compared to last year."
    elif user_query == "What are the total expenses?":
        return "Total expenses are $1.1 million."
    elif user_query == "What is the profit margin?":
        return "The profit margin is 26.7%."
    elif user_query == "How much cash does the company have?":
        return "The company has $500,000 in cash."
    else:
        return "Sorry, I can only provide information on predefined queries."

# Chatbot interface
if __name__ == "__main__":
    print("Welcome to the Financial Chatbot!")
    while True:
        user_input = input("Ask a financial question (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = simple_chatbot(user_input)
        print(response)
