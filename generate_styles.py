#!/usr/bin/env python
from xmltodict import unparse
import json

colors = {
  'BuPu': ['#edf8fb','#bfd3e6','#9ebcda','#8c96c6','#8856a7','#810f7c'],
  'OrRd': ['#fef0d9','#fdd49e','#fdbb84','#fc8d59','#e34a33','#b30000'],
  'RdYlGn': ['#d73027','#fc8d59','#fee08b','#d9ef8b','#91cf60','#1a9850']
}

attributes = ["AccRank", "CrimeRank", "EduRank", "EmpRank", "HlthRank", "HouseRank", "IncomeRank", "NZIMDRank"]

for c in colors:
  for a in attributes:
    rules = []
    for i in range(0,6000,1000):
      r = {
        'Filter': {
          '#text': '[{}] > {}'.format(a, i)
        },
        'PolygonSymbolizer': {
          '@fill': colors[c][i/1000]
        },
        'LineSymbolizer': {
          '@stroke': 'black',
          '@stroke-width': '0.1'
        }
      }
      rules.append(r)
    d = {
      'Map': {
        '@background-color': 'transparent',
        '@srs': '+init=epsg:3857', # output projection
        'Style': {
          '@name': '{}_{}'.format(c, a),
          'Rule': rules
        },
        'Layer': {
          '@name': 'layer',
          '@srs': '+init=epsg:3857', # input projection
          'StyleName': {
            '#text': '{}_{}'.format(c, a)
          },
          'Datasource': {
            'Parameter': [
              {
                '@name': 'file',
                '#text': '../nzimddata_3857/NZIMD_3857.shp'
              },
              {
                '@name': 'type',
                '#text': 'shape'
              }
            ]
          }
        }
      }
    }
    with open('styles/{}_{}.xml'.format(c, a), 'wb') as f:
      unparse(d, f, pretty=True, full_document=False)

with open('tilestache.cfg', 'r') as f:
  cfg = json.load(f)

layers = {}
for c in colors:
  for a in attributes:
    name = '{}_{}'.format(c, a)
    layers[name] = {
      'provider': {
        'name': 'mapnik',
        'mapfile': 'styles/{}.xml'.format(name)
      }
    }
    cfg['layers'] = layers

with open('tilestache.cfg', 'w') as f:
  json.dump(cfg, f, indent=4)
