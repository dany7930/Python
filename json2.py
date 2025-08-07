import json

input = '''
{
   {"id" : "001"
    "x"  : "2",
    "name" : "Chuck"
    } ,
    {"id" : "7",
    "name" : "Chunk"
    }    
   
   }'''


info = json.loads(input)
print('User count:', len(info) )

for item in info:
    print('Name', item['name'])
    print('id', item ['id'])
    print('Attribute', item['x'])
    
