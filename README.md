# Net Worth Tracker

A Python CLI application for managing personal net worth data stored in Excel.

I built this to avoid repeatedly opening Excel, finding cells, editing amounts, saving, and closing the file. Instead, I can make those updates directly from the terminal.

## Features

* View financial entries
* Calculate net worth
* Update existing amounts
* Add and remove entries
* Save changes to Excel
* Validate user input

## Tech Stack

* **Python** — application logic and CLI
* **pandas** — tabular data manipulation
* **openpyxl** — Excel file handling
* **Excel** — data storage

## Project Structure

```text
net-worth-tracker/
├── main.py
├── helper.py
├── update.py
├── Net Worth Tracker.bat
└── README.md
```

`main.py` handles the program flow and menu, `helper.py` contains input and display functions, and `update.py` handles the Excel data operations.

## How It Works

The program loads the Excel data into a pandas DataFrame and provides a menu for viewing and modifying financial entries.

```text
1. View data
2. Calculate net worth
3. Change an amount
4. Add a row
5. Remove a row
6. Exit
```

Changes are saved back to the Excel file after an update.

## Running

Install the dependencies:

```bash
pip install pandas openpyxl
```

Run the program:

```bash
python main.py
```

On Windows, `Net Worth Tracker.bat` can also be used to launch it.

The personal `net_worth.xlsx` file is excluded from the repository.
