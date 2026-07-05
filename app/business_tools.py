def check_expense_policy(amount: float) -> str:
    """
    Check whether an expense follows company policy.
    """

    if amount <= 10000:
        return (
            f"Expense Amount: ₹{amount}\n"
            f"Policy: Auto Approval\n"
            f"Status: Within Company Policy"
        )

    elif amount <= 50000:
        return (
            f"Expense Amount: ₹{amount}\n"
            f"Policy: Manager Approval Required"
        )

    else:
        return (
            f"Expense Amount: ₹{amount}\n"
            f"Policy: Finance Director Approval Required"
        )


def check_budget(department: str, amount: float) -> str:
    """
    Simulate department budget checking.
    """

    budgets = {
        "IT": 100000,
        "HR": 50000,
        "Finance": 75000,
        "Marketing": 60000,
    }

    available = budgets.get(department, 0)

    remaining = available - amount

    if amount <= available:
        return (
            f"Department: {department}\n"
            f"Available Budget: ₹{available}\n"
            f"Requested Amount: ₹{amount}\n"
            f"Remaining Budget: ₹{remaining}"
        )

    return (
        f"Department: {department}\n"
        f"Available Budget: ₹{available}\n"
        f"Requested Amount: ₹{amount}\n"
        f"Budget Exceeded!"
    )


def detect_fraud(amount: float) -> str:
    """
    Simple fraud detection.
    """

    if amount > 80000:
        return "High Risk"

    elif amount > 40000:
        return "Medium Risk"

    return "Low Risk"

def validate_expense(expense_type: str) -> str:
    """
    Check whether the expense category is allowed.
    """

    allowed = [
    "Taxi",
    "Hotel",
    "Flight",
    "Meals",
    "Laptop",
    "Internet",
    "Training",
    "Fuel",
    "Office Supplies",
    "Conference",
    "Medical",
    "Parking"
]

    if expense_type.title() in allowed:
        return f"{expense_type} is an approved expense category."

    return f"{expense_type} is NOT covered under company reimbursement policy."