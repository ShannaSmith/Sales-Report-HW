"""Generate sales report showing total melons each salesperson sold."""


salespeople = [] #<===initalizes list of salespeople
melons_sold = [] #<===initalizes list of number of melons sold by each salesperson

f = open('sales-report.txt') #<=== opens the sales report file that conatins details about recent orders

for line in f:  #<==begins for loop
    line = line.rstrip() #<=== removes trailing white space
    entries = line.split('|') #<===returns a list and separates the name of the salesperson , total amount of order, 
    #and total amount of melons sold into seperate strings for each line of data
    salesperson = entries[0] #<== assigns data at index 0 to salesperson. This is the name of the salesperson
    melons = int(entries[2])#<==assigns data at index 2 to melons. This is the total amt of melons sold.
    if salesperson in salespeople: #<===initialiizes if statement (conditional). Checks if the salesperson is already in the list
        position = salespeople.index(salesperson)#<===find the position where salesperson is stored in salespeople
        melons_sold[position] += melons #???
    else:
        salespeople.append(salesperson) #<===add salesperson to the salespeople list
        melons_sold.append(melons) #<===add melon sold count to melons list


for i in range(len(salespeople)): #<===initialize for statement to run through the salespeople list, loop over indiices of salespeople and use it to index into salespeople and melons_sold
    print(f'{salespeople[i]} sold {melons_sold[i]} melons') #<===print a formatted literal showing the salesperson's name,  and how many melons sold