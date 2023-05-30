import csv
import os

import ase
import rdkit
from ase.db import connect
from ase.io import read
from ase.visualize import view
from rdkit import Chem
from rdkit.Chem import AllChem
from ase.atoms import Atoms
from ase.atom import Atom


def get_atoms_from_conf(conf, mol):
    an_atoms = Atoms()
    for i in range(conf.GetNumAtoms()):
        position = conf.GetAtomPosition(i)
        atom = mol.GetAtoms()[i]
        a_symbol = atom.GetSymbol()
        an_new_atom = Atom(symbol=a_symbol, position=(position.x, position.y, position.z))
        an_atoms.append(an_new_atom)
    return an_atoms


if os.path.exists('test.db'):
    os.remove('test.db')

if os.path.exists('fail_smile'):
    os.remove('fail_smile')

real_count = 0
fail_count = 0
with connect('temp.db') as db, open(r'SMILES_properties.csv', 'r') as f_csv:
    for i, row in enumerate(csv.reader(f_csv)):
        if i == 0:
            continue
        a_smile = row[1]
        a_mol = Chem.MolFromSmiles(a_smile)
        a_mol_with_H = Chem.AddHs(a_mol)
        try:
            AllChem.EmbedMolecule(a_mol_with_H, randomSeed=1)
            AllChem.MMFFOptimizeMolecule(a_mol_with_H)
        except Exception:
            try:
                AllChem.EmbedMolecule(a_mol_with_H, useRandomCoords=True)
                AllChem.MMFFOptimizeMolecule(a_mol_with_H)
                # with open('random.txt', 'a') as fr:
                #    fr.write(id + '\n')
            except Exception:
                try:
                    AllChem.EmbedMolecule(a_mol_with_H, maxAttempts=50000, useRandomCoords=True)
                    AllChem.MMFFOptimizeMolecule(a_mol_with_H)
                except Exception as e:
                    print(e)
                    fail_count = fail_count + 1
                    print(f'real: {real_count}')
                    print(f'fail: {fail_count}')
                    with open('fail_smile', 'a') as f_f:
                        f_f.write(a_smile)
                        f_f.write('\n')
                    continue

        a_conf = a_mol_with_H.GetConformer()
        an_atoms = get_atoms_from_conf(a_conf, mol=a_mol_with_H)

        an_id = row[0]
        an_id = int(an_id.split('-')[1])
        a_binding_e = float(row[2])
        a_viscosity = float(row[3])

        db.write(atoms=an_atoms, binding_e=a_binding_e, viscosity=a_viscosity, smile=a_smile, ep_id=an_id)
        real_count = real_count + 1
