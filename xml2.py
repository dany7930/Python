import xml.etree.ElementTree as ET

input = '''
<stuff>
    <user>
        <user x="2">
            <id>001</id>
            <name>Dany</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </user>
</stuff> '''

stuff = ET.fromstring(input)
lst = stuff.findall('.//user')  

print('User count:', len(lst))

for item in lst:
    print('Name', item.find('name').text) 
    print('id', item.find('id').text)
    print('Attribute', item.get("x"))



