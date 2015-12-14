i=0 
j=0 
while i<12:
    print((" " *(12-i)) + ("*" * (i*2 + 1)))
    if i>=11:
      while j<5:
        print((" " * 10) + ("*" * 5))
        j=j+1
    i=i+1 