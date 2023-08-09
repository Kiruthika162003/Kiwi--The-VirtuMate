class KiwiAssistant:
    def __init__(self):
        self.chatbot = pipeline("conversational")
        self.expenses = []
        self.budgets = {}
    
    def communicate(self, user_input):
        conv = Conversation([{"role": "system", "content": "I am Kiwi, your helpful assistant."}, {"role": "user", "content": user_input}])
        response = self.chatbot(conv)[-1]["generated"]["text"]
        return response
    
    def track_expense(self, category, amount):
        self.expenses.append({"category": category, "amount": amount})
        return f"Expense of ${amount} in the {category} category has been tracked."
    
    def create_budget(self, category, amount):
        self.budgets[category] = amount
        return f"Budget of ${amount} has been set for the {category} category."
    
    def get_expense_summary(self):
        total_expenses = sum(expense["amount"] for expense in self.expenses)
        summary = f"Total expenses: ${total_expenses}\n"
        for category, budget in self.budgets.items():
            spent = sum(expense["amount"] for expense in self.expenses if expense["category"] == category)
            remaining = budget - spent
            summary += f"{category.capitalize()} budget: ${budget} | Spent: ${spent} | Remaining: ${remaining}\n"
        return summary
    
def main():
    print("Kiwi: Hello! I'm Kiwi, your advanced virtual assistant.")
    print("Kiwi: How can I assist you today? Feel free to ask or command. Type 'exit' to end the conversation.")

    kiwi = KiwiAssistant()
    user_input = input("You: ")

    while user_input.lower() != "exit":
        if "track expense" in user_input:
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            expense_response = kiwi.track_expense(category, amount)
            print(f"Kiwi: {expense_response}")
        elif "create budget" in user_input:
            category = input("Enter budget category: ")
            amount = float(input("Enter budget amount: "))
            budget_response = kiwi.create_budget(category, amount)
            print(f"Kiwi: {budget_response}")
        elif "expense summary" in user_input:
            summary = kiwi.get_expense_summary()
            print(f"Kiwi: {summary}")
        else:
            kiwi_response = kiwi.communicate(user_input)
            print("Kiwi:", kiwi_response)

        user_input = input("You: ")

    print("Kiwi: Goodbye! Have a wonderful day.")

if __name__ == "__main__":
    main()
