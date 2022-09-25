l1=[["shan",96],["khan",76],["Don",35]]
higest = -1
higest_scorer = ""
lowest = 101
lowest_scorer =""
for i in range(len(l1)):
      score = l1[i][1]
      name = l1[i][0]
      if score>= higest:
            higest = score
            higest_scorer=name
      if score<=lowest:
            lowest =score
            lowest_scorer =name
print(f"Higest \n\tname:{higest_scorer}\n\tscore:{higest}\nLowest\n\tname:{lowest_scorer}\n\tscore:{lowest}")