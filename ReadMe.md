# ReadMe

This is a light forum for the application of AI in molecule science.

For related review, see `./review` folder.

For models, see `./model` folder.

Here presents a short description.

[TOC]

## Tips

For users from Chinese Mainland, a [GitHub Proxy](https://ghproxy.com/) will speed up the clone from github:

```
git clone https://ghproxy.com/https://github.com/Franklalalala/ai4mol
```



## Database

### 2020 ChemDataExtractor

**Comment**: Extract experimental data to construct a database.

### 2020 experiment-oriented

**Comment**: Extract experimental data to construct a database. Trained an AI to predict new electrolytes.

### 2022 RedDB

**Comment**: Construct a database with a specified core.



## ML Review

### 2020 Descriptor

Physics-Inspired Structural Representations for Molecules and Materials  

Cite This: https://doi.org/10.1021/acs.chemrev.1c00021  

**Comment**:

A summary of cutting-edge descriptors.

A very detailed guide to building the description module with respect to Symmetry, Smoothness, Completeness, Locality, and Additivity.

### 2020 4generation

Four Generations of High-Dimensional Neural Network Potentials.

Cite This: https://doi.org/10.1021/acs.chemrev.0c00868  

**Comment**:

A very much detailed description of the history of NNP. 

1: without any symmetry considered.

2: with symmetry considered, yet limited to the local environment. 

3: with long-range electrostatic interactions considered.

4: with non-local charge transfer considered.

Some description is hard to understand.

### 2020 MLFF

Machine Learning Force Fields  

Cite This: https://dx.doi.org/10.1021/acs.chemrev.0c01111  

**Comment**:

Focusing on FF(sGDML), which is a relatively cheap.

2020 October. not cutting-edge.

Focusing on the work of Klaus-Robert Müller.

### 2021 DIG

DIG: A Turnkey Library for Diving into Graph Deep Learning Research  

Journal of Machine Learning Research 22 (2021) 1-9  

**Comment**:

Focusing on the work of Shuiwang Ji, Texas A&M University.

A summary of GNN-related works, including graph generation, self-supervised learning, interpretability, and deep learning.

### 2022 road_map

Roadmap on Machine learning in electronic structure. Electron. Struct. 4 (2022) 023004  

**Comment**:

Covered multiple applications: 

* Predicting material properties
* Construction of accurate force fields and beyond
* Solving the many-body problem with machine learning, etc.

An overview of current research hotspots is brought out, yet the description is relatively short.

### 2023 SchNetPack 2.0 

SchNetPack 2.0: A neural network toolbox for atomistic machine learning  

J. Chem. Phys. 158, 144801 (2023)
https://doi.org/10.1063/5.0138367  

**Comment**:

Focusing on the work of Klaus-Robert Müller. 

A summary of cutting-edge models, including SchNet and multiple successors.



## Model

A summary of recent models. (To do: add DeepMD community works)

They are divided into pro-DFT and pro-GNN models. Some tricks are summarized in the trick folder.

### pro-DFT

#### 2017 DTNN

**Comment**: The Quantum-chemical inspired model. Father of schnet.

#### 2018 SchNet_JCP

**Comment**: Schnet.

Add a continuous-filter convolutional layer for better simulation of the basis set in DFT.

#### 2019 SchNOrb
**Comment**: Extension to predict HOMO-LUMO

#### 2021 FieldSchNet
**Comment**: Extension to predict solvent effects

#### 2021 SpookyNet (3M parameters)
**Comment**: 

Add support for non-local effects. 

Add support for Charge input.

Add support for multiplicity input.

#### 2022 Kernel-Based MLFF
**Comment**: Update on Kernel-Based MLFF (old-school)

#### 2023 sGDML

**Comment**: MLFF for giant systems (200~400)


#### 2023 SchNetPack 2.0
**Comment**: A summary of schnet techs.

### pro-GNN

#### 2020 DimeNet (key to add ang info)
**Comment**: Directional MPNN (add angular information for the first time)

#### 2020 DimeNet++
**Comment**: update of some key modules to enhance performance.

#### 2022 SMP 

(preprint as spherenet in 2021)

**Comment**: Add torsion information (huge computational cost)  (dis, ang, tor)

#### 2021 PAINN

**Comment**: Add Angular information to schnet but non-directional MPNN (dis, ang)

#### 2022 ComENet

**Comment**: update of spherenet but non-directional MPNN (dis, ang, tor)

#### 2022 NequIP (key to point out E3)

**Comment**: Better integration of E3  (dis, ang)

#### 2022 So3krates
**Comment**: update of PAINN with better integration of SO3 and attention modules. ( **SODA** on MD17 )  (dis, ang)

#### unpublished left_net

**Comment**: update of ComENet, extend SO3 to 3D Isomorphism  

### trick

#### self-supervised learning  

##### 2022 GEM
**Comment**:
(1) the bond lengths prediction;
(2) the bond angles prediction; 
(3) the atomic distance matrices prediction. 
(GEM-2 is outperformed by uni-mol+ in recent months)
(outdated)

##### 2022 MolCLR
**Comment**:
(1) Atom masking 
(2) Bond deletion 
(3) Subgraph removal

##### 2023 uni_mol (47M parameters)
**Comment**: add noise on atom positions

##### 2023 uni_mol +
**Comment**: very few steps to optimize (within the model, no need for optimizers) the geometry to an equrilibrim state. 


#### Molecule generation

##### 2019 G-Schnet

**Comment**: Extension of schnet to generate molecules.

##### 2022 G-SphereNet

**Comment**: Extension of spherenet to generate molecules.

#### Moieties_ML

##### 2023 ProNet
**Comment**: an extension of subgraph-level (moity) GNN for proteins. Better encode of Amino Acid.

##### unpublished_MoINN
**Comment**: Tool for moiety identification and Coarse-graining (CG) MD.

