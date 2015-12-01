# CSE6242/CX4242 Homework 4 Sketch Code
# Please use this outline to implement your decision tree. You can add any code around this.

import csv

# Enter You Name Here
myname = "Yan-Xialin" # or "Doe-Jane-"

def isANumber(inputString):
    try:
        float(inputString)
        return True
    except ValueError:
        return False

# This function is given the set of data returns index of attribute with 
def informationGain(dataArray):
    entropyList = [None] * (len(dataArray[0])-1)
    dataLabels = []
    labelIndex = len(entropyList)
    for x in range(len(dataArray)):
        dataLabels.append(float(dataArray[x][labelIndex]))

    for attribute in range(len(entropyList)):
        currAttribute = []
        for y in range(len(dataArray)):
            currAttribute.append(float(dataArray[y][attribute]))
        minValue = min(currAttribute)
        maxValue = max(currAttribute)
        # We will just assume to split attributes at the center
        splitValue = (minValue+maxValue)/2.0;
        numInstances = len(currAttribute)
        countAttribute0Class0 = 0
        countAttribute0Class1 = 0
        countAttribute1Class0 = 0
        countAttribute1Class1 = 0

        for z in range(len(currAttribute)):
            # attribute 0
            if(currAttribute[z]<splitValue):
                if(dataLabels[x] == 0):
                    countAttribute0Class0++
                else:
                    countAttribute0Class1++
            else:
                if(dataLabels[x] == 0):
                    countAttribute1Class0++
                else:
                    countAttribute1Class1++

# Implement your decision tree below
class DecisionTree():
    tree = {}

    def learn(self, training_set):
        # print(training_set[0]) # This gives us the first row. So to get 1st attribute we iterate training_set[i][0]
        # print()
        # print("\n")
        # print(type(training_set))

        entropyList = [None] * (len(training_set[0])-1)
        test = []
        # for x in range(len(training_set)):
        #     test.append(float(training_set[x][11]))
        for attribute in range(len(entropyList)):
            print(attribute)
        
        self.tree = {}

    # implement this function
    def classify(self, test_instance):
        result = 0 # baseline: always classifies as 0
        return result

def run_decision_tree():

    # Load data set
    with open("hw4-data.csv") as f:
        next(f, None)
        data = [tuple(line) for line in csv.reader(f, delimiter=",")]
    print "Number of records: %d" % len(data)

    # Split training/test sets
    # You need to modify the following code for cross validation.
    K = 10
    training_set = [x for i, x in enumerate(data) if i % K != 9]
    test_set = [x for i, x in enumerate(data) if i % K == 9]
    
    tree = DecisionTree()
    # Construct a tree using training set
    tree.learn( training_set )

    # Classify the test set using the tree we just constructed
    results = []
    for instance in test_set:
        result = tree.classify( instance[:-1] )
        results.append( result == instance[-1])

    # Accuracy
    accuracy = float(results.count(True))/float(len(results))
    print "accuracy: %.4f" % accuracy       
    

    # Writing results to a file (DO NOT CHANGE)
    f = open(myname+"result.txt", "w")
    f.write("accuracy: %.4f" % accuracy)
    f.close()


if __name__ == "__main__":
    run_decision_tree()
    # print(isANumber("ONE")
    # print("\n")
    # print(isANumber("1"))
    # print("\n")
    # print(isANumber("0"))
    # print("\n")
    # print(isANumber("0.0001"))
