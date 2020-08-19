for item in range(1,101):   
    if item % 7 == 0:        
        continue
    elif item // 10 == 7 or item % 10 == 7:
        continue
    else:
        print(item)
