# Net Worth Tracker

A simple Python CLI application for tracking personal net worth using an Excel spreadsheet.

I made this because I was repeatedly opening the Excel file, finding the right cell, changing an amount, saving it, and closing the file. This program lets me make those updates directly from the terminal instead.

## Features

* View financial entries
* Calculate total net worth
* Change an existing amount
* Add a new financial entry
* Remove an entry
* Save changes directly to Excel
* Validate user input

## Tech Stack

* **Python** — application logic and CLI
* **pandas** — working with tabular data
* **openpyxl** — reading and writing Excel files
* **Excel** — data storage

## Project Structure

```text
net-worth-tracker/
├── main.py
├── helper.py
├── update.py
├── net_worth.xlsx
└── README.md
```

### `main.py`

Handles the main program flow, menu, and user interaction.

### `helper.py`

Contains functions for displaying the menu and handling user input.

### `update.py`

Contains functions for reading, modifying, calculating, and saving the financial data.

### `net_worth.xlsx`

Stores the financial entries used by the program.

## How It Works

The program loads the Excel file into a pandas DataFrame when it starts.

From the terminal, I can choose what I want to do:

```text
1. View data
2. Calculate net worth
3. Change an amount
4. Add a row
5. Remove a row
6. Exit
```

After making a change, the program saves the updated DataFrame back to the Excel file.

## Running the Project

Install the required libraries:

```bash
pip install pandas openpyxl
```

Then run:

```bash
python main.py
```

The `net_worth.xlsx` file should be in the same directory as the Python files.

## Why I Built It

This started as a small personal automation.

I regularly update my financial information, but doing it manually meant repeatedly opening Excel, locating cells, editing values, saving the file, and closing it.

Instead of doing the same thing over and over, I built a small CLI tool to handle the updates for me.
