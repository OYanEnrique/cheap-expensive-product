# cheap-expensive-product
A Python script that simulates a shopping cart, calculating total cost, identifying the cheapest product, and counting items over $1000.

# 🛒 Shopping Cart Analyzer

A command-line Python script that simulates adding products to a shopping cart and provides a running analysis of the costs.

This program allows a user to continuously enter product names and prices. After each entry, it provides an updated summary including the total cost, the name of the cheapest product entered so far, and a count of all products that cost more than $1,000.

## Features

* **Continuous Product Entry**: Add as many products as you want in a single session.
* **Total Cost Calculation**: Keeps a running total of the value of all products.
* **Cheapest Product Tracking**: Always knows which product entered has the lowest price.
* **Expensive Item Counter**: Counts how many products cost $1,000 or more.
* **User-Controlled Loop**: A simple `[Y/N]` prompt allows the user to continue adding items or finish the session.

## How to Use

1.  Ensure you have Python installed on your system.
2.  Save the code as a `.py` file (e.g., `cheap_expensive_product.py`).
3.  Run the script from your terminal:
    ```sh
    python cheap-expensive-product.py
    ```
4.  The program will prompt you to enter a `Product name:` and `Product price:`.
5.  After each entry, an updated summary of the cart's status will be displayed.
6.  You will then be asked `Continue? [Y or N]`.
7.  Enter `Y` to add another product, or `N` to stop the program.
