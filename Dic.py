D = {'food':'bread','quantity':4}
print D
print D['food']
print D["food"]

Dic = {}
Dic['name']="Apple"
Dic['quantity']=2300
Dic['food']="Apple Pie"
print Dic

rec = {'name':{'first':'Bob','last':'Smith'},
       'job':['dev','mgr'],
       'age':40.5,
       }
print rec

rec['job'].append('janitor');
rec['job'].append('writer');
print rec
for x in rec:
    print x+'\t'
    
