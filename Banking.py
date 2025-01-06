class Loan:
    def __init__(self, loan_id, customer_name, loan_amount, interest_rate, tenure):
        self.loan_id = loan_id
        self.customer_name = customer_name
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.tenure = tenure  # tenure in months
        self.repaid_amount = 0  # amount already repaid
        self.status = "Pending"  # loan status: Pending, Approved, Paid off

    def calculate_monthly_payment(self):
        # Formula for calculating monthly EMI (Equated Monthly Installment)
        r = self.interest_rate / (12 * 100)  # monthly interest rate
        emi = self.loan_amount * r * (1 + r) ** self.tenure / ((1 + r) ** self.tenure - 1)
        return emi

    def make_repayment(self, amount):
        self.repaid_amount += amount
        if self.repaid_amount >= self.loan_amount:
            self.repaid_amount = self.loan_amount
            self.status = "Paid off"
        elif self.repaid_amount > 0:
            self.status = "Repaying"

    def loan_balance(self):
        return self.loan_amount - self.repaid_amount

    def get_loan_info(self):
        return f"Loan ID: {self.loan_id}\nCustomer: {self.customer_name}\nAmount: {self.loan_amount}\n" \
               f"Interest Rate: {self.interest_rate}%\nTenure: {self.tenure} months\nRepaid: {self.repaid_amount}\n" \
               f"Loan Status: {self.status}"


class LoanManagementSystem:
    def __init__(self):
        self.loans = []
        self.loan_counter = 1

    def apply_for_loan(self, customer_name, loan_amount, interest_rate, tenure):
        loan = Loan(self.loan_counter, customer_name, loan_amount, interest_rate, tenure)
        self.loans.append(loan)
        self.loan_counter += 1
        return loan

    def get_loan_by_id(self, loan_id):
        for loan in self.loans:
            if loan.loan_id == loan_id:
                return loan
        return None

    def display_all_loans(self):
        if not self.loans:
            print("No loans available.")
            return
        for loan in self.loans:
            print(loan.get_loan_info())
            print("-" * 40)


def main():
    system = LoanManagementSystem()

    # Sample loop for loan application and management
    while True:
        print("\n=== Loan Management System ===")
        print("1. Apply for a Loan")
        print("2. Make Repayment")
        print("3. View Loan Information")
        print("4. View All Loans")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            customer_name = input("Enter customer name: ")
            loan_amount = float(input("Enter loan amount: "))
            interest_rate = float(input("Enter interest rate: "))
            tenure = int(input("Enter loan tenure in months: "))
            loan = system.apply_for_loan(customer_name, loan_amount, interest_rate, tenure)
            print(f"Loan applied successfully! Loan ID: {loan.loan_id}")
            print(f"Monthly EMI: {loan.calculate_monthly_payment():.2f}")

        elif choice == '2':
            loan_id = int(input("Enter Loan ID for repayment: "))
            loan = system.get_loan_by_id(loan_id)
            if loan:
                amount = float(input(f"Enter repayment amount for Loan ID {loan_id}: "))
                loan.make_repayment(amount)
                print(f"Repayment successful! Current Balance: {loan.loan_balance():.2f}")
            else:
                print("Loan ID not found!")

        elif choice == '3':
            loan_id = int(input("Enter Loan ID to view details: "))
            loan = system.get_loan_by_id(loan_id)
            if loan:
                print(loan.get_loan_info())
            else:
                print("Loan ID not found!")

        elif choice == '4':
            system.display_all_loans()

        elif choice == '5':
            print("Exiting Loan Management System.")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
