import json
from datetime import datetime
import os

# This class stores basic information of a person
class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    # Just shows name and email
    def display_info(self):
        print(f"Name: {self.name}, Email: {self.email}")


# This class is for our client – it extends Person
class Client(Person):
    def __init__(self, name, email, company_name):
        super().__init__(name, email)
        self.company_name = company_name
        self.projects = []  # Stores all projects of this client


# This class handles a project assigned to a client
class Project:
    def __init__(self, client, project_name, budget, deadline):
        self.client = client
        self.project_name = project_name
        self.budget = budget
        self.deadline = datetime.strptime(deadline, "%Y-%m-%d")
        self.status = "Ongoing"  # Default status

    # We use this to mark a project as completed
    def mark_complete(self):
        self.status = "Completed"

    # Checks if the deadline has passed and it's still not completed
    def is_overdue(self):
        return self.deadline < datetime.now() and self.status != "Completed"


# This class is for generating invoice for a project
class Invoice:
    def __init__(self, project):
        self.project = project
        self.amount = project.budget
        self.date = datetime.now()  # Today's date

    # This method gives us the invoice in text format
    def generate_invoice_text(self):
        return (
            f"\n--- Invoice ---\n"
            f"Client: {self.project.client.name}\n"
            f"Company: {self.project.client.company_name}\n"
            f"Project: {self.project.project_name}\n"
            f"Amount: ${self.project.budget}\n"
            f"Date: {self.date.strftime('%Y-%m-%d')}\n"
            f"Status: {self.project.status}\n"
        )


# This is the main class that manages everything
class FreelanceManager:
    def __init__(self):
        self.clients = []   # Stores all clients
        self.projects = []  # Stores all projects
        self.load_clients()  # Loads existing clients when program starts

    # Load clients from a file if it exists
    def load_clients(self):
        if os.path.exists("clients.json"):
            with open("clients.json", "r") as file:
                data = json.load(file)
                for c in data:
                    client = Client(c['name'], c['email'], c['company_name'])
                    self.clients.append(client)
            print(f"📂 Loaded {len(self.clients)} client(s) from file.")

    # Save current clients to a file
    def save_clients(self):
        data = [{'name': c.name, 'email': c.email, 'company_name': c.company_name} for c in self.clients]
        with open("clients.json", "w") as file:
            json.dump(data, file)

    # Lets us add a new client
    def add_client(self):
        name = input("Client Name: ")
        email = input("Email: ")
        company = input("Company Name: ")
        client = Client(name, email, company)
        self.clients.append(client)
        self.save_clients()  # Save to file immediately
        print("✅ Client added and saved to file!")

    # Create a new project for an existing client
    def create_project(self):
        title = input("Project Title: ")
        client_name = input("Client Name: ")

        # Find client by name
        client = next((c for c in self.clients if c.name == client_name), None)

        if not client:
            print("❌ Client not found.")
            return

        deadline = input("Deadline (YYYY-MM-DD): ")
        budget = float(input("Budget: $"))
        project = Project(client, title, budget, deadline)
        client.projects.append(project)  # Also attach it to the client
        self.projects.append(project)    # Add to main list too
        print("✅ Project created!")

    # Show all projects in a list
    def view_projects(self):
        if not self.projects:
            print("📭 No projects found.")
            return
        for i, project in enumerate(self.projects, 1):
            status = "⚠️ Overdue" if project.is_overdue() else project.status
            print(f"{i}. {project.project_name} ({status}) - ${project.budget} - Due: {project.deadline.date()}")

    # Mark any project as completed
    def mark_project_complete(self):
        self.view_projects()
        if not self.projects:
            return
        try:
            choice = int(input("Enter project number to mark complete: ")) - 1
            if 0 <= choice < len(self.projects):
                self.projects[choice].mark_complete()
                print("✅ Project marked as completed!")
            else:
                print("❌ Invalid choice.")
        except ValueError:
            print("❌ Please enter a valid number.")

    # Create an invoice for any project
    def generate_invoice(self):
        self.view_projects()
        if not self.projects:
            return
        try:
            choice = int(input("Enter project number to generate invoice: ")) - 1
            if 0 <= choice < len(self.projects):
                invoice = Invoice(self.projects[choice])
                print(invoice.generate_invoice_text())
            else:
                print("❌ Invalid choice.")
        except ValueError:
            print("❌ Please enter a valid number.")

    # Show all completed project earnings for a given month and year
    def monthly_earnings(self):
        month = input("Enter month (e.g. 04 for April): ")
        year = input("Enter year (e.g. 2025): ")
        total = 0
        print(f"\n💰 Earnings for {month}/{year}:")
        for project in self.projects:
            if (
                project.status == "Completed"
                and project.deadline.strftime("%m") == month
                and project.deadline.strftime("%Y") == year
            ):
                print(f"- {project.project_name}: ${project.budget}")
                total += project.budget
        print(f"Total: ${total}")


# This is the main function – it runs the menu
def main():
    manager = FreelanceManager()

    while True:
        print("\n===== Freelancer Project Manager =====")
        print("1. Add New Client")
        print("2. Create New Project")
        print("3. View All Projects")
        print("4. Mark Project as Complete")
        print("5. Generate Invoice")
        print("6. Monthly Earnings Report")
        print("7. Exit")

        choice = input(">> ")

        # Depending on the user's input, we call the right function
        if choice == "1":
            manager.add_client()
        elif choice == "2":
            manager.create_project()
        elif choice == "3":
            manager.view_projects()
        elif choice == "4":
            manager.mark_project_complete()
        elif choice == "5":
            manager.generate_invoice()
        elif choice == "6":
            manager.monthly_earnings()
        elif choice == "7":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice.")


# This makes sure our app runs when we execute the file
if __name__ == "__main__":
    main()
