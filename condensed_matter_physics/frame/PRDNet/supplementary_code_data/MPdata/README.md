
## Due to the 100 MB size limit for supplementary materials, the data is hosted on the repository instead of being included directly. The data in this folder can be downloaded from an anonymous Hugging Face account at: [https://huggingface.co/datasets/anonymous-hugface/openreview\_data\_mp/tree/main](https://huggingface.co/datasets/anonymous-hugface/openreview_data_mp/tree/main). The dataset is provided as **MPdata.zip**. 



## Task Overview

This MP benchmark includes **6 primary tasks** for evaluating CPP models in crystal property prediction, divided into regression and classification missions.

### **Mission Settings**

#### Regression Tasks

1. **T1**: Formation Energy Prediction (`float`) | `eV/atom`
2. **T2**: Band Gap Prediction (`float`) | `eV`
3. **T3**: Bulk Modulus Prediction (`float`) | `Gpa`
4. **T4**: Shear Modulus Prediction (`float`) | `Gpa`
5. **T5**: Young’s Modulus Prediction (`float`) | `Gpa`



#### Classification Task

6. **T6**: Metal/Non-metal Classification (`int`, binary classification)

---

## Dataset Description

Its ASE database (`.db`) format. Each database includes crystal structures and corresponding property labels.

### `fe_bandg/`

* **Train:** `MP_100_bgfe_train.db` (86,071 crystals)
* **Val:** `MP_100_bgfe_val.db` (12,295 crystals)
* **Test:** `MP_100_bgfe_test.db` (24,593 crystals)
* **Tasks:** T1, T2 

  * Keys: `formation_energy`, `band_gap`

### `modulus/`

* **Train:** `MP_modulus_train.db` (6,631 crystals)
* **Val:** `MP_modulus_val.db` (947 crystals)
* **Test:** `MP_modulus_test.db` (1,895 crystals)
* **Tasks:** T3–T5

  * Keys: `bulk_modulus`, `shear_modulus`, `youngs_modulus` 

### `metal_nometal/`

* **Train:** `MP_100_metal_train.db` (86,071 crystals)
* **Val:** `MP_100_metal_val.db` (12,295 crystals)
* **Test:** `MP_100_metal_test.db` (24,593 crystals)
* **Task:** T6 (label: `0` or `1`)
  
  * Keys: `metal`
---



## Example: Reading Data from an ASE Database

You can read data using the `ase.db` module as follows:

```python
from ase.db import connect

# Load the database
db = connect('MP_100_bgfe_train.db')

# Iterate through entries
for row in db.select():
    atoms = row.toatoms()  # ASE Atoms object
    formation_energy = row.formation_energy
    band_gap = row.band_gap

    print(f'Formula: {atoms.get_chemical_formula()}')
    print(f'Formation Energy: {formation_energy:.3f} eV')
    print(f'Band Gap: {band_gap:.3f} eV')
    break  # remove this if you want to iterate over all entries
```

