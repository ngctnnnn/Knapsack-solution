import numpy as np
import data

class Knapsack01Problem:
    def __init__(self):

        # initialize instance variables:
        self.items = []
        self.maxCapacity = 0

        # initialize the data:
        self.__initData()

    def __len__(self):
        #return: the total number of items defined in the problem
        return len(self.items)

    def __initData(self):
        
        inp = data.input_data()
        file_number = 1

        #Read files
        with open(inp[file_number - 1] + ".kp") as level_file:
            rows = level_file.read().split('\n')

        number_of_items = (int)(rows[1])
        self.items = []

        for i in range(4, number_of_items + 5 - 1):
            x = rows[i].split(" ")[0]
            y = rows[i].split(" ")[1]
            self.items.append(((int)(x), (int)(y)))


        self.maxCapacity = (int)(rows[2])

    def getValue(self, zeroOneList):
        """
        Calculates the value of the selected items in the list, while ignoring items that will cause the accumulating weight to exceed the maximum weight
        :param zeroOneList: a list of 0/1 values corresponding to the list of the problem's items. '1' means that item was selected.
        :return: the calculated value
        """

        totalWeight = totalValue = 0

        for i in range(len(zeroOneList)):
            weight, value = self.items[i]
            if totalWeight + weight <= self.maxCapacity:
                totalWeight += zeroOneList[i] * weight
                totalValue += zeroOneList[i] * value
        return totalValue

    def printItems(self, zeroOneList):
        """
        Prints the selected items in the list, while ignoring items that will cause the accumulating weight to exceed the maximum weight
        :param zeroOneList: a list of 0/1 values corresponding to the list of the problem's items. '1' means that item was selected.
        """
        totalWeight = totalValue = 0

        for i in range(len(zeroOneList)):
            weight, value = self.items[i]
            if totalWeight + weight <= self.maxCapacity:
                if zeroOneList[i] > 0:
                    totalWeight += weight
                    totalValue += value
                    print("weight = {}, value = {}, accumulated weight = {}, accumulated value = {}".format(weight, value, totalWeight, totalValue))
        print("- Total weight = {}, Total value = {}".format(totalWeight, totalValue))


# testing the class:
def main():
    # create a problem instance:
    knapsack = Knapsack01Problem()

    # creaete a random solution and evaluate it:
    randomSolution = np.random.randint(2, size=len(knapsack))
    print("Random Solution = ", end = '')
    print(randomSolution)
    knapsack.printItems(randomSolution)


if __name__ == "__main__":
    main()