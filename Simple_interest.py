# program to calculate Simple interest
P = input('Princriple value for P')  # remember input type in 3.5 accepts everything as String hence we need to parse
n = input('number of years')
r = input('rate of interest')
Pi = int(P)
ni = int(n)
ri = int(r)
SI = (Pi*ni*ri)/100
Amount = P+SI
print ('SI = ', SI)
print ('Amount = ', Amount)