# Finance Management CLI Application

This project is a simple **Finance Management** command-line interface (CLI) application that allows users to track their income and expenses using an SQLite database. The program provides a summary of transactions and can also generate plots for visual representation using **Pandas** and **Matplotlib**.

## Features
- Add new income or expense transactions.
- View a summary of all transactions.
- Visualize income vs. expenses using bar charts and pie charts.
- Clear transaction history.

## Requirements
- Python 3 (or higher)
- `SQLite`
- `Pandas`
- `Matplotlib`

## Installation

  - Clone the repository:
    ```bash
      git clone https://github.com/gaborvida-stack/Finance-Management-CLI-Application.git
    ```
    ```bash
      cd Finance-Management-CLI-Application
    ```
  - Install the dependencies
    ```bash
      pip install -r requirements.txt
    ```

## How to Use
- **Start the program**:

  ```bash
    python expenseTrack.py
  ```

- Main Menu Options:

    - Add new transaction: Input a new income or expense.
    - See summary: View all transactions along with total income, expenses, and balance.
    - See summary in a plot: Visualize your transactions with bar charts and pie charts.
    - Clear history: Deletes all transactions from the database.
    - Exit: Exit the program.
  
## Example Usage:
  - Adding a new transaction:
    - You will be prompted to enter the transaction amount and specify if it's income or expense.
  
  - Viewing the summary:
    - You will see a table of all transactions, as well as total income, expenses, and balance.
     
  - Plotting the summary:
    - Two plots will be generated, one showing the total income vs. expenses as a bar chart, and another showing their distribution as a pie chart.


## Database Structure
  - The application uses an `SQLite` database (finance_data.db) with a single table transactions, which stores:
    - id: Unique identifier for each transaction.
    - amount: The monetary value of the transaction.
    - type: Whether the transaction is "income" or "expend".
