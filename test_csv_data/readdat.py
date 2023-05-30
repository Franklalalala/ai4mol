import os
import time
import pandas as pd
import json
import argparse
import traceback
from rdkit import Chem
from rdkit.Chem import AllChem

def construct_ogdb(alldat, dir_ogdb):
    """
    Construct the original database of molecules from the .smi file
    :param alldat: the list of .dat files which contain id and smi of molecules
    :param dir_ogdb: the path of the original database of molecules
    :return: None (but generate XXX.mol files in the original database directory)
    """
    with open('readdat_error.txt', 'a') as f:
        f.write('\n' + time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(time.time())) + '\n')
    for dat in alldat:
        info = pd.read_csv(dat, header=None)
        print(info)
        for i in info.index:
            # infoi = info.iloc[i, 0].split()
            infoi = info.iloc[i, 0]
            # print(infoi)
            # id = infoi[0]
            smi = infoi
            mol_woH = Chem.MolFromSmiles(smi)
            mol = Chem.AddHs(mol_woH)  # add H atoms
            try:
                AllChem.EmbedMolecule(mol, randomSeed=1)
                AllChem.MMFFOptimizeMolecule(mol)
            except Exception:
                try:
                    AllChem.EmbedMolecule(mol, useRandomCoords=True)
                    AllChem.MMFFOptimizeMolecule(mol)
                    #with open('random.txt', 'a') as fr:
                    #    fr.write(id + '\n')
                except Exception:
                    try:
                        AllChem.EmbedMolecule(mol, maxAttempts=5000, useRandomCoords=True)
                        AllChem.MMFFOptimizeMolecule(mol)
                        #with open('random+max.txt', 'a') as fr:
                        #    fr.write(id + '\n')
                    except Exception:
                        with open('readdat_error.txt', 'a') as f:
                            f.write(smi + '\n')
                        continue
            a = Chem.MolToXYZBlock(mol)  # string type information
            if list(a)[1] != '\n':
                b = a[4:]  # exclude the first 4 characters in a if the total atom number > 9
                c = b.split('\n')
            else:
                b = a[3:]  # exclude the first 3 characters in a if the total atom number < 10
                c = b.split('\n')
            del c[-1]
            # del c[0]
            dict = {'SMILE': smi, 'name': str(id), 'coordinate': c}
            dir_ogmol = os.path.join(dir_ogdb, '%s.mol' % smi)
            with open(dir_ogmol, 'w') as f1:
                f1.write(a)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', help="The name of the folder containing .dat files", type=str, default=None)
    parser.add_argument('-o', help="The name of original_mol_database folder", type=str, default=None)
    args = parser.parse_args()

    #dir = args.d
    dir = os.getcwd()
    args.o = os.getcwd()
    files = os.listdir(dir)
    alldat = []
    for file in files:
        if '.smi' in file:
            dir_dat = os.path.join(dir, file)
            alldat.append(dir_dat)

    construct_ogdb(alldat, args.o)
    

