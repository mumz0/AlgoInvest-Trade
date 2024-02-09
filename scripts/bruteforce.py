import csv
import itertools

dataset = "./data/basic_data.csv"
dataset1 = "./data/dataset1_Python+P7.csv"
dataset2 = "./data/dataset2_Python+P7.csv"


def best_yield_combo(data_file, budget_limit):
    """Find the best combination of items that maximizes profit within a budget limit.

    This function searches through all possible combinations of items in the provided dataset,
    selecting the combination that yields the highest profit without exceeding the budget limit.

    Args:
        data_file (str): The path to the CSV file containing items with their prices and profit percentages.
        budget_limit (float): The maximum budget allowed for purchasing items.
    """

    # Initialize variables to track the best combination, maximum profit, and total spent
    best_combo = ()
    max_profit = 0
    total_spent = 0

    # Load data from CSV file
    with open(data_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip header row
        data = list(csv.reader(csv_file))

        # Iterate over different combo sizes
        for combo_size in range(1, len(data) + 1):
            # Generate combinations of items
            for combo in itertools.combinations(data, combo_size):
                # Convert prices and profits to float
                combo = [(item[0], float(item[1]), float(item[2])) for item in combo]

                # Check if the total price of the combination is within the budget limit
                if sum(row[1] for row in combo) <= budget_limit:
                    # Calculate the current profit of the combination
                    current_profit = sum((row[2] / 100) * row[1] for row in combo)

                    # Update the best combination, maximum profit, and total spent if the current profit is higher
                    if current_profit > max_profit:
                        max_profit = current_profit
                        best_combo = combo
                        total_spent = sum(action[1] for action in combo)

    # Print the best combination, maximum profit, and total spent
    [print(item[0]) for item in best_combo]
    print("Max Profit:", max_profit)
    print("Total Spent:", total_spent)


best_yield_combo(dataset, 500)
