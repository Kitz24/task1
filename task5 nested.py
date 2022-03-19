def find_len(list1):
    length = len(list1)
    list1.sort(key=lambda x: x[1])
    print("Second Smallest grade student is:", list1[1])
    z=list1[1]
    for i in list1:
        if i[1]==z[1]:
            pp.append(i)
        else:
            pass
    pp.sort(key=lambda x:x[0])
    v=[item[0] for item in pp]
    o=' '.join(v)
    for i in o.split():
        print(i)
pp=[]
list1=[['Raju',5],['Harry',37],['Berry',37],['Tina',38],['Akriti',41],['Harsh',39]]
Largest = find_len(list1)
