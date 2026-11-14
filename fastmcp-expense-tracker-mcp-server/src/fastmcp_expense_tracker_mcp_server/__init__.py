from fastmcp import FastMCP

mcp = FastMCP("Expense-Tracker")

EXPENSES = [
    {"category": "Food", "amount": 350.0},
    {"category": "Travel", "amount": 100.0},
    {"category": "Food", "amount": 250.0},
]


@mcp.tool
def total_expenses(category: str) -> float:
    """Calculate total expenses for a category."""
    return sum(
        expense["amount"]
        for expense in EXPENSES
        if expense["category"].lower() == category.lower()
    )


if __name__ == "__main__":
    mcp.run()