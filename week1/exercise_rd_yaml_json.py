import yaml
import json
from pprint import pprint

with open("mylist.yml") as f:
  mylist = yaml.load(f)
  print "### Output from mylist.yml ###"
  pprint(mylist)

with open("mylist.json") as f:
  mylist = json.load(f)
  print "### Output from mylist.json ###"
  pprint(mylist)
