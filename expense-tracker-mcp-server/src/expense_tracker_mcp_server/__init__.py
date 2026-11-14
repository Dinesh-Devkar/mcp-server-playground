from mcp.server import MCPServer

mcp=MCPServer(name='local-expense-tracker')

EXPENSES = [
    {"category": "Food", "amount": 350.0},
    {"category": "Travel", "amount": 100.0},
    {"category": "Food", "amount": 250.0},
    {"category": "Shopping", "amount": 800.0},
]


@mcp.tool()
def get_all_expenses()->list:
    '''return a list of all the expenses'''
    return EXPENSES

@mcp.tool()
def get_total_expense(category:str)->float:
    '''return the sum of total expense for specific category'''
    return sum([expense['amount'] for expense in EXPENSES if expense['category'].lower()==category.lower()])

if __name__ == '__main__':
    mcp.run()