import json
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw

# Defining the input molecule in SMILES format
# 2,3-dichlorobutane  "CCC(Cl)C(Cl)C"
# pantoprazole -> "O=C(O)C(CC1=CC=C(C=C1)N)N[C@@H](C(=O)N)C(=O)N"
input_smiles = "CCC(Cl)C(Cl)C"

# Parsing the input SMILES to create an RDKit molecule
input_molecule = Chem.MolFromSmiles(input_smiles)

# Generate isomers
isomers = list(AllChem.EnumerateStereoisomers(input_molecule))

# dictionary to store isomers and their IUPAC-like names
isomer_data = {}

# Generate IUPAC-kinda names for each isomer and store them in the dictionary
for idx, isomer in enumerate(isomers):
    iupac_like_name = Chem.MolToSmiles(isomer, isomericSmiles=True)
    isomer_data[f"Isomer_{idx + 1}"] = {
        "SMILES": Chem.MolToSmiles(isomer),
        "IUPAC_Like_Name": iupac_like_name,
    }

# Serialize the dictionary to JSON
json_data = json.dumps(isomer_data, indent=2)

# this Saves the json data to a file
with open("isomer_data.json", "w") as json_file:
    json_file.write(json_data)

#   visualize the isomers with diagram
for idx, isomer in enumerate(isomers):
    img = Draw.MolToImage(isomer, size=(300, 300))
    img.save(f"Isomer_{idx + 1}.png")
