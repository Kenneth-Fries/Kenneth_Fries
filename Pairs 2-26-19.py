"""
Here's the problem and an attached CSV. The revenue column refers to a subscription fee that is renewed every year.

1. Get the average monthly revenue for each customer.
2. Output this average revenue to a csv as a per month amount. For example if Susan was subscribed for 12 months she would have 12 rows with the average amount in each.
3. If a subscription is cancelled before the subscription period is up, all remaining revenues should be attributed to the last month (e.g. if revenue from Susan’s subscription breaks down to $10/month and she cancels with three months remaining, each month should show $10 for revenue except the month of cancellation which should show $30).

*DO NOT USE PANDAS* Use Python standard libraries only.

I was given 70 minutes to complete this, for reference :slightly_smiling_face:


"Client","Service Start","Service Cancellation","Fee"
"Clay",2018-03-08,,680
"Mimi",2018-07-17,2018-09-01,700
"Jon ",2018-02-28,,850
"Byron",2017-11-01,2018-11-11,600
"Brian",2018-10-01,,100
"Yan ",2018-01-29,,1300
"Joel",2018-01-09,2018-09-23,100
"""
flag = 0
result = []
with open('Pairs 2-26-19.csv', 'r') as f: #That's the input file
    x = f.readlines()
for y in x:
    if flag: #flag was to throw out first row
        z1,z2,z3,z4 = y.split(',')
        if z3 == '':    #if date is blank it input today's date
            z3 = '2019-02-19'
        z2dt = z2.split('-')   #this is the date
        z2yr,z2mo,z2dy = z2dt[0],z2dt[1],z2dt[2]
        z3dt = z3.split('-')   #this is the second date
        z3yr,z3mo,z3dy = z3dt[0],z3dt[1],z3dt[2]
                #this calculates the number of months
		months = (int(z3yr) - int(z2yr))*12 +(int(z3mo)-int(z2mo))+1
        if z3dy<z2dy:     #here I deal with the day of the month
            months-=1
        rate = int(z4)/12    #monthly avg fee
        leftover = rate*(12-months%12)+rate   #leftover fee upon cancelation + last month
        result.append(z1)   #start with a name
        for i in range(months-1):
            result.append(round(rate,2))  #then write each fee
        result.append(round(leftover,2))
    flag = 1     #update flag after first line dropped
with open("result.csv", mode='w') as g:
    [g.write(str(x)+"\n") for x in result]    #write to file
    [print(x) for x in result]
