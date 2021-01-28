### a simple example of how to read in a data file and store it in a list of lists.
### We'll also use pandas to do some of this later on.

### We'll use the restaurant dataset here - we'll return to this later in the semester.

def getRestaurantData() :
    variables = {}
    varOrder = {}
    data = []
    try :
        ### first get the variable names and possible values
        with open("restaurant.txt") as f :
            lineCounter = 0  ## we need to keep track of which column corresponds to each variable.
            for line in f.readlines() :
                if not line.startswith("#") and len(line) > 1 : ## # is a comment character
                    name, vals = line.split(":")
                    variables[name.strip()] = vals.split(',')
                    varOrder[name.strip()] = lineCounter
                    lineCounter+= 1
        ## now let's get the data. We'll make a list of lists - one list for each row
        with open("restaurant.data") as f2 :
            for line in f2.readlines() :
                if len(line) > 1: ## skip blank lines
                    data.append(line.split(","))
        return variables, varOrder, data
    except :
        print("Error reading files")
        return None

def sliceData(varNames, varOrder, data) :

    ## let's print the third row.
    print(data[2])

    ### let's print the first element in each row
    print([row[0] for row in data])

    ### let's print elements 2-5 in each row
    print([row[1:5] for row in data])

    ## let's print the last element in each row.
    print([row[-1] for row in data])

    ### now let's print the data in the 'Price' column
    index = varOrder['Price']
    print([item[index] for item in data])

    ## now let's check to see if all values are present for a variable
    vals = varNames['Type']
    index = varOrder['Type']
    valsPresent = [row[index] for row in data]
    for val in vals :
        if val not in valsPresent :
            print("value missing: %s" % val)

    ### or ...
    print("Missing values: %s" % [val for val in vals if val not in valsPresent])

if __name__ == "__main__" :
    names, order, data = getRestaurantData()
    sliceData(names, order, data)