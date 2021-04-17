from ortools.linear_solver import pywraplp
from ortools.algorithms import pywrapknapsack_solver
import seaborn as sns
import matplotlib.pyplot as plt
import time

def main():
	inp =  ["data/00Uncorrelated/1/R01000/s000", 
			"data/00Uncorrelated/2/R01000/s000",
			"data/00Uncorrelated/3/R01000/s000",
			"data/00Uncorrelated/4/R01000/s000",
			"data/00Uncorrelated/5/R01000/s000",
			"data/00Uncorrelated/6/R01000/s000",
			"data/00Uncorrelated/7/R01000/s000",
			"data/00Uncorrelated/8/R01000/s000",
			"data/01WeaklyCorrelated/1/R01000/s000",
			"data/01WeaklyCorrelated/2/R01000/s000",
			"data/01WeaklyCorrelated/3/R01000/s000",
			"data/01WeaklyCorrelated/4/R01000/s000",
			"data/01WeaklyCorrelated/5/R01000/s000",
			"data/01WeaklyCorrelated/6/R01000/s000",
			"data/01WeaklyCorrelated/7/R01000/s000",
			"data/01WeaklyCorrelated/8/R01000/s000",
		]

	for name in range(len(inp)):
		print('Package number: ' + str(name + 1))
		with open(inp[name] + ".kp") as level_file:
			rows = level_file.read().split('\n')
		
		number_items = (int)(rows[1])
		capacities = [(int)(rows[2])]
		values = []
		weights = [[]]
		cnt = 0
		for i in range(4, number_items + 5 - 1):
			x = rows[i].split(" ")[0]
			y = rows[i].split(" ")[1]
			values.append((int)(x))
			weights[0].append((int)(y))
			

		solver = pywrapknapsack_solver.KnapsackSolver(
			pywrapknapsack_solver.KnapsackSolver.
			KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')


		#Set time limit
		solver.set_time_limit(100)

		solver.Init(values, weights, capacities)
		computed_value = solver.Solve()

		packed_items = []
		packed_weights = []
		total_weight = 0
		print('Total value =', computed_value)
		for i in range(len(values)):
			if solver.BestSolutionContains(i):
				packed_items.append(i)	
				packed_weights.append(weights[0][i])
				total_weight += weights[0][i]

		print('Capacity = ' + str(capacities[0]))
		print('Total weight = ' + str(total_weight))
		print('Number of items: ' + str(len(packed_items)))
		# print('Packed items:', packed_items)
		# print('Packed_weights:', packed_weights)
		print()

if __name__ == '__main__':
	main()