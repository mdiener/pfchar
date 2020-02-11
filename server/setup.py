import os
import json
from pfchar.database.connection import r_exists, r_set


if not r_exists('users'):
    r_set('users', {})

if not r_exists('characters'):
    r_set('characters', {})

if not r_exists('templates'):
    r_set('templates', {})

with open(os.path.join('.', 'pfchar', 'definitions', 'character.json'), 'r') as char_f:
    char = json.load(char_f)
    r_set('templates', 'character', char)

with open(os.path.join('.', 'pfchar', 'definitions', 'classes.json'), 'r') as class_f:
    classes = json.load(class_f)
    r_set('templates', 'classes', classes)

with open(os.path.join('.', 'pfchar', 'definitions', 'races.json'), 'r') as races_f:
    races = json.load(races_f)
    r_set('templates', 'races', races)

with open(os.path.join('.', 'pfchar', 'definitions', 'feats.json'), 'r') as feats_f:
    feats = json.load(feats_f)
    r_set('templates', 'feats', feats)

with open(os.path.join('.', 'pfchar', 'definitions', 'mechanics.json'), 'r') as mechanics_f:
    mechanics = json.load(mechanics_f)
    r_set('templates', 'mechanics', mechanics)
