from math import floor

#   From my salary, I'm already deducting the debt I have
# from O2 cellphone plan & financing
salary = int(input('Put your salary here(liquid): '))

# [basic rule of three]
# 100         -  total
# percentage  -  desiredAmount
# desiredAmount = (percentage * total) / 100
def percentageOfTotal(percentage):
  amount = (percentage * salary) / 100.00

  return amount

if __name__ == "__main__":
  print("We are going to show the right amount of money you can spent, after we make a 0 sum budget")

  remainingPercentage = 100

  budget = {}
  destinedPercentages = {}
  while remainingPercentage != 0:
    category = input('What is this budge for: ')
    percentage = int(input('Percentage to allocate: '))

    budget[category] = percentageOfTotal(percentage)
    destinedPercentages[category] = percentage

    remainingPercentage -= percentage

    print(f'Remaining percentage: {remainingPercentage}') if remainingPercentage != 0 else print()
    print()

  print('---------------------------------------')
  for category, total in budget.items():
    print(f'Category: {category}')
    print(f'Destined percentage: {destinedPercentages[category]}%')
    print(f'Total available: {floor(total)}€')
    print()
  print('---------------------------------------')