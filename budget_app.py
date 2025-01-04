# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Category:
    
    def __init__(self, budget): 
        self.budget = budget
        self.ledger = []
  
    def deposit(self, amount, description = None):
        if description is None:
            self.description = []
            self.ledger.append({'amount': amount, 'description': ''})
        else:
            self.ledger.append({'amount': amount, 'description': description})
    
    def withdraw(self, amount, description = None):
        if self.check_funds(amount):
            if description is None:
                self.description = []
                self.ledger.append({'amount': -amount, 'description': ''})
            else:
                self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        current_balance = 0
        for item in self.ledger:
            current_balance += item['amount']
        return current_balance 
    
    def transfer(self, amount, another_budget):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {another_budget.budget}")
            another_budget.deposit(amount, f"Transfer from {self.budget}")
            return True
        return False

    def check_funds(self, amount):
        if (amount > self.get_balance()):
            return False
        return True

    def __str__(self):
        title = f"{self.budget:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + "\n"
            total += item['amount']
        return title + items + 'Total: ' + str(total)
    
def create_spend_chart(categories):

    def withdrawals(category): #A function to get total withdrawals for each budget category
        individual = 0 
        for item in category.ledger:
            if item['amount'] < 0:
                individual += item['amount']
        return individual
    
    total_spent = sum(withdrawals(i) for i in categories) 
     # Calculate spending percentages for each category
    percentages = []
    for i in categories:
        one = withdrawals(i)
        percentage = round(((one / total_spent)*10 // 1)*10) #need for rounding to 10s
        percentages.append(percentage)

    max_length = max(len(category.budget) for category in categories)   # Determine the longest category name for proper spacing
    chart = "Percentage spent by category\n" # Create the chart
    for i in range(100, -1, -10): #The percentages, vertical |, and 'o's
        chart += str(i).rjust(3) + "| "
        for percentage in percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    chart += "    " + "-" * (3 * len(categories) + 1)  # Add the horizontal line
    for x in range(max_length): #For the vertically written budget category names underneath the horizontal line
        category_names = '  '.join(category.budget[x] if x < len(category.budget) else ' ' for category in categories)
        chart += "\n     " + category_names + "   " 
    return chart
