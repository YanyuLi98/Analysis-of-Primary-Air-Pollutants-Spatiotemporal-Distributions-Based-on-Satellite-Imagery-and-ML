import os
import pandas as pd

# Define the parameters
dataPath = 'E:\1' 
print(dataPath)
# targets = ['1462A','1463A','1464A','1465A','1466A','1467A','1468A','1469A','1470A',
#           '1471A','1472A','1473A','1474A','1918A','1919A','1920A','1921A','1922A',
#           '1923A','1924A','1925A','1930A','1931A','1932A','1933A','1934A','1935A','1936A',
#           '1937A','1938A','1939A','1940A','1941A','3165A','3524A','3525A','3605A',
#           '3606A','3607A','3608A','3651A'] # Destination site
targets = ['3165A','3524A','3525A','3605A','3606A','3607A','3608A','3651A']
result = [[] for i in range(len(targets))]

for filepath in os.listdir(dataPath): 
    for filename in os.listdir('%s/%s'%(dataPath,filepath)):
        if not filename.endswith('.csv'): 
            continue
        data = pd.read_csv('%s/%s/%s'%(dataPath,filepath,filename))
        for i in range(0,len(data),15):
            for k in range(len(targets)):
                try:
                    item = {'date':data['date'][i], # Date
                            'hour':data['hour'][i]} # Hour
                    for j in range(i,i+15):
                        item[data['type'][j]] = data[targets[k]][j]
                    result[k].append(item)
                except:
                    pass
        print('%s Processing complete'%filename)
            
df_all = pd.DataFrame()
for i in range(len(targets)):
    df = pd.DataFrame(result[i])
    df.insert(0,'ID','%s'%targets[i]) # df['ID']='%s'%targets[i]
    df_all = df_all.append(df,ignore_index=True)
df_all.to_csv('E:\%s.csv'%'GZ8 Air quality 2015-2017',index=False)
print('kk')


