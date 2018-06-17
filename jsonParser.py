import json

with open('json_distros.json', 'r') as f:
    distros_dict = json.load(f)

iCount=0
for distro in distros_dict:
    print(distro['Name'])
    if (distro['Name']=='Fedora'):
        iCount+=1
  
print("\n\n##### iCount = %d\n" % iCount)

print("\nFull Dictionary: ", distros_dict)
