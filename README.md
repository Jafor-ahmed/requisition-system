# Requisition System

This is my Assessment 2 project (Software Development Project). It is a Python program that handles staff requisitions using a class called Requisition.

## What it does

A staff member submits a requisition with item names and prices, and the program adds up the total. If the total is under $500, the requisition is approved straight away and gets a reference number made from the staff ID and the last 3 digits of the requisition ID. If the total is $500 or more, it stays Pending until a manager approves or rejects it. Items priced at $0 or less are skipped.

The program can print all the requisitions and show how many are submitted, approved, pending and not approved.

## Files

- `requisition_system.py` has the Requisition class.
- `test_requisition.py` creates 6 requisitions to test the program.
- `.gitignore` keeps Python's `__pycache__` folder out of the repository.

## Methods

- `__init__` sets up the date, staff ID, staff name, requisition ID, items, total, status and approval reference.
- `add_requisition` takes the item names and prices, skips bad prices and returns the total.
- `approve_requisition` approves totals under $500 and leaves the rest Pending.
- `respond_to_requisition` lets a manager approve or reject a Pending requisition.
- `show_requisition` prints one requisition in the format from the brief.
- `display_requisitions` prints all of them.
- `requisition_statistics` prints the four counts.

## How to run

Install Python, open the project folder in VS Code, open `test_requisition.py` and click Run.

## Testing

The test file has 6 requisitions with totals under $500, exactly $500 and over $500, plus decimal prices and a negative price. It then answers the Pending ones, including one invalid response, and prints the requisitions and statistics before and after.

## Design

- Encapsulation: each requisition keeps its own data and only the class changes its status.
- Single responsibility: each method does one job.
- Reusability: the same class is used for every requisition.
- Separate tests: the test code is in its own file.
