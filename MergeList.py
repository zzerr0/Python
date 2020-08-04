def mergelist(flist, slist):
 tlist = []
 for i in flist:
   if i % 2 != 0:
      tlist.append(i)
 for i in slist:
    if i % 2 == 0:
        tlist.append(i)
 return tlist

flist = [10, 20, 23, 11, 17]
slist = [13, 43, 24, 36, 12] 
print(mergelist(flist, slist))  
