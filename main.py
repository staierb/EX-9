fname = input('Enter File:')
if len(fname) < 1: fname = 'clown.txt'
hand = open(fname)
#organizing text into dictionary
di = dict()
for lin in hand:
  lin = lin.rstrip()
  #print(lin)

  wds = lin.split()
  #print (wds)
  for w in wds:
   
    #idiom: retrieve/create/update counter
    di[w] = di.get(w,0) + 1
    
#now we want to find the most common word
largest = -1
theword = None
for k,v in di.items():
 # print (k,v)
  if v > largest:
    largest = v
    #capture/remember the largest word
    theword = k     
print (theword, largest)

