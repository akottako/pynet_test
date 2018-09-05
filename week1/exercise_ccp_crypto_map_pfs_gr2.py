from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

crypto_map_crypto = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"set pfs group2")

for parent in crypto_map_crypto:
  print parent.text
#  for child in parent.children:
#    print child.text
