import json

data = '''
{
  "name" : "Chunk",
  "phone" : {
   "type" : "intl",
   "number" : "+1 734303 4456"
},
   "email" : {
     "hide" : "yes"
   
   }

}'''  

info = json.loads(data)
print('Name:', info ["name"] )
print('Hide:',  info["email"]["hide"])


