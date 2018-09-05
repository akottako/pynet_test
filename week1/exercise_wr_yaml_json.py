import yaml
import json

mylist = []
for i in range(5):
  mylist.append(i)
mylist[-1] = {}
mylist[-1]['ip_addr'] = '10.30.40.198'
mylist[-1]['mask'] = '255.255.255.0'
mylist[-1]['gateway'] = '10.30.40.1'

with open("mylist.yml", "w") as f:
  f.write(yaml.dump(mylist, default_flow_style=False))

with open("mylist.json", "w") as f:
  json.dump(mylist, f)
