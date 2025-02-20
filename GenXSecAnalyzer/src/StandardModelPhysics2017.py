import numpy as np
import json

with open('matches.txt') as f:
  matches2017 = f.read().splitlines()

json_file_path = "CMS-2017-mc-datasets.json"
with open(json_file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

data_keys = ['B physics and Quarkonia', 'Higgs Physics/Standard Model', 'Higgs Physics/Beyond Standard Model',
        'Standard Model Physics/Drell-Yan',
        'Standard Model Physics/ElectroWeak', 'Standard Model Physics/Forward and Small-x QCD Physics',
        'Standard Model Physics/Minimum Bias', 'Standard Model Physics/QCD', 'Standard Model Physics/Top physics',
        'Standard Model Physics/Miscellaneous', 'Heavy-Ion Physics', 'Beyond 2 Generations',
        'Exotica/Colorons, Axigluons, Diquarks', 'Exotica/Contact Interaction', 'Exotica/Dark Matter',
        'Exotica/Excited Fermions', 'Exotica/Extra Dimensions', 'Exotica/Gravitons',
        'Exotica/Heavy Fermions, Heavy Righ-Handed Neutrinos', 'Exotica/Heavy Gauge Bosons',
        'Exotica/Leptoquarks', 'Exotica/Resonances', 'Exotica/Miscellaneous', 'Supersymmetry',
        'Physics Modelling', 'Miscellaneous']

MC_keys_Standard = [i for i in data_keys if 'Higgs' not in i if 'Standard' in i]

MC_keys_Standard


sampleInfo = {}
sum=0

for i in MC_keys_Standard:
  name = i.split('/')[1].replace(' ', '')
  try:
    if len(data[i]['datasets']) > 0:
      sampleInfo[name] = np.array([])
    for j in data[i]['datasets']:
      if j['name'] not in matches2017:
        sampleInfo[name] = np.append(sampleInfo[name], j['name'])
      else:
        sum+=1
  except:
    pass

print(sum)