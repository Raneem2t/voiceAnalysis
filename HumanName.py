
import csv

def isPerson(name):

    with open('test.csv', 'rt') as f:
        reader = csv.reader(f, delimiter=',')

        for row in reader:
            for field in row:
                if field == name:
                    return True

    return False


s = "اتصلت على محمد علي فرد أخوه فيصل بن محمد قال لي أنه مشغول مع صديقه علي بنت فيصل"
s = s.lower()
tokens = s.split(" ")

postName = ""
previousName = ""
isPersonName = False
preP = []

for name in tokens:
    if name == "بن" or name == "بنت" or name == "ولد" or name == "ولدن" or name == "بنتن":
        if isPerson(previousName):
            preP.append(previousName)
            # print("has "+name +","+previousName + ",")

    if isPerson(name):
        print(name + " is a name for person")
        if isPerson(previousName):
            print(name + " and " + previousName +" are two consequence names")
        if previousName == "بن" or previousName == "بنت" or previousName =="ولد" or previousName =="ولدن" or previousName =="بنتن":
            print("he is " + name + " " +previousName + " "+preP[0])
        else:
            preP = []

    # else:
    #     print(name + " is not a name for a person")

    previousName = name
