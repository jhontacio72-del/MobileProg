# Jhon Patrick Tacio
# ClassProg - pandas, matplotlib, openpyxl version

import pandas as pd
import matplotlib.pyplot as plt
import os

class PersonInfo:
    def __init__(self):
        self.filename = "C:\\Users\\Admin\\Downloads\\Tacio\\data.xlsx"
        self.df = None 

    def categorize_age(self, age):
        if 0 <= age <= 14:
            return "Minor"
        elif 15 <= age <= 24:
            return "Youth"
        elif 25 <= age <= 64:
            return "Adult"
        else:
            return "Senior"

    def loadFile(self):
        try:
            if not os.path.exists(self.filename):
                print(f"File not found: {self.filename}")
                print("Please create the Excel file first.")
                return
            
        
            self.df = pd.read_excel(self.filename, engine='openpyxl')
            
           
            self.df.columns = [c.lower().strip() for c in self.df.columns]
            
            
            self.df['category'] = self.df['age'].apply(self.categorize_age)
            
            print(f"\nSuccessfully loaded {len(self.df)} records!")
            print(f"File: {self.filename}")
            print(self.df.to_string(index=False))

        except Exception as e:
            print(f"Error loading file: {e}")
            self.df = None

    def viewByGender(self):
        gender_counts = self.df['gender'].value_counts()
        print("\n--- Count by Gender ---")
        # FIXED: don't print the Series, print clean format
        for gender, count in gender_counts.items():
            print(f"{gender}: {count}")

        # Chart 1: Bar
        plt.figure(figsize=(10, 4))
        plt.subplot(1, 2, 1)
        gender_counts.plot(kind='bar', color=['skyblue', 'pink', 'gray'])
        plt.title('Count by Gender (Bar)')
        plt.ylabel('Count')
        plt.xticks(rotation=0)

        # Chart 2: Pie
        plt.subplot(1, 2, 2)
        gender_counts.plot(kind='pie', autopct='%1.1f%%')
        plt.title('Count by Gender (Pie)')
        plt.ylabel('')
        plt.tight_layout()
        plt.show()

    def viewByCategory(self):
        category_counts = self.df['category'].value_counts()
        order = ["Minor", "Youth", "Adult", "Senior"]
        category_counts = category_counts.reindex([c for c in order if c in category_counts.index])

        print("\n--- Count by Category ---")
        # FIXED
        for cat, count in category_counts.items():
            print(f"{cat}: {count}")

        plt.figure(figsize=(10, 4))
        plt.subplot(1, 2, 1)
        category_counts.plot(kind='bar', color=['orange', 'green', 'blue', 'red'])
        plt.title('Count by Category (Bar)')
        plt.ylabel('Count')
        plt.xticks(rotation=0)

        plt.subplot(1, 2, 2)
        category_counts.plot(kind='pie', autopct='%1.1f%%')
        plt.title('Count by Category (Pie)')
        plt.ylabel('')
        plt.tight_layout()
        plt.show()

    def viewByGenderAndCategory(self):
        grouped = pd.crosstab(self.df['category'], self.df['gender'])
        print("\n--- Count by Gender and Category ---")
        print(grouped.to_string()) # FIXED: use to_string() for DataFrame

        # Chart 1: Grouped Bar
        grouped.plot(kind='bar', figsize=(8, 5))
        plt.title('Gender and Category (Grouped Bar)')
        plt.ylabel('Count')
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.show()

        # Chart 2: Stacked Bar
        grouped.plot(kind='bar', stacked=True, figsize=(8, 5))
        plt.title('Gender and Category (Stacked Bar)')
        plt.ylabel('Count')
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.show()

system = PersonInfo()

while True:
    print("\n===== MENU =====")
    print("1. Load")
    print("2. View")
    print("3. Exit")
    
    try:
        c = int(input("Enter (1-3): "))
    except ValueError:
        print("Invalid input, enter a number.")
        continue

    if c == 1:
        system.loadFile()

    elif c == 2:
       
        if system.df is None:
            print("No data loaded yet! Please press 1. Load first.")
            continue
        
        while True:
            print("\n--- VIEW MENU ---")
            print("a) by gender")
            print("b) by category")
            print("c) by gender and category")
            print("d) Back to main menu")
            choice = input("Enter choice (a-d): ").lower()

            if choice == 'a':
                system.viewByGender()
            elif choice == 'b':
                system.viewByCategory()
            elif choice == 'c':
                system.viewByGenderAndCategory()
            elif choice == 'd':
                break
            else:
                print("Invalid choice.")

    elif c == 3:
        print("Program ended.")
        break
    else:
        print("Invalid choice.")