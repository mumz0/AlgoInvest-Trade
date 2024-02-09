import csv 
import time

dataset = "./data/basic_data.csv"
dataset1 = "./data/dataset1_Python+P7.csv"
dataset2 = "./data/dataset2_Python+P7.csv"

def format_data(file):
    """ Extracting data from csv

    Args:
        file (str): PATH of the file containing data

    Returns:
        list: List of data extracted from file
    """
    with open(file) as csv_file:
        csv_list = list(csv.reader(csv_file))
        actions_list = []
        for row in csv_list[1:]:
            if float(row[1]) > 0 and float(row[2]) > 0:
                round_profit = round(float(row[1]) * float(row[2]))
                actions_list.append([row[0], round(float(row[1]) * 100), round_profit])
    return actions_list

def best_yield_combo(elements, max_budget):
    """_summary_

    Args:
        elements (list): List of data extracted from csv
        max_budget (int): Budget limit regarding actions to buy

    Returns:
        dict: Dictionnary containing the budget spent,
        the realized profit and the best combo of actions to buy to realized this profit.
    """
    budget_limit = max_budget * 100
    matrice = [[0 for x in range(budget_limit + 1)] for x in range(len(elements) + 1)]

    for index in range(1, len(elements) + 1):
        action_price = elements[index-1][1]
        for budget in range(1, budget_limit + 1):
            if action_price <= budget:
                matrice[index][budget] = max(elements[index-1][2] + matrice[index-1][budget-action_price], matrice[index-1][budget])
            else:
                matrice[index][budget] = matrice[index-1][budget]

    profit = matrice[-1][-1]
    best_yield_combo = []
    budget = budget_limit
    len_elems = len(elements)

    while budget >= 0 and len_elems >= 0:
        elem = elements[len_elems-1]
        if matrice[len_elems][budget] == matrice[len_elems-1][budget-elem[1]] + elem[2]:
            best_yield_combo.append(elem[0])
            budget -= elem[1]

        len_elems -= 1

    return {"BUDGET SPENT": (budget_limit / 100 - budget / 100), "PROFIT": (profit / 100), "BEST YIELD COMBINATION": best_yield_combo}
            
            
data = format_data(dataset1)
start_time = time.time()     
result_dict = best_yield_combo(data, 500)
end_time = time.time()
execution_time = end_time - start_time

print(f"Temps d'exécution : {execution_time} secondes")

for key, value in result_dict.items():
    print(key,": ", value)
