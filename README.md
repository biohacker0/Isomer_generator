# RDKit Isomer Generator

# Blog - [https://corvus-ikshana.hashnode.dev/isomer-generations-using-rdkit-library-for-mass-molecular-docking-tests-part-1]

This Python script is designed to generate and visualize isomers of a given molecule in Simplified Molecular Input Line Entry System (SMILES) format using the RDKit library. It also generates IUPAC-like names for each isomer and stores the results in a JSON file.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Generated Output](#generated-output)
  - [JSON Data](#json-data)
  - [Isomer Images](#isomer-images)
- [License](#license)

## Prerequisites
Before using this script, ensure you have the following prerequisites installed:

- RDKit: The RDKit library must be installed. You can follow the installation guide provided on their website.

## Installation
Clone this repository to your local machine using the following command:

```shell
git clone https://github.com/yourusername/rdkit-isomer-generator.git
```

Navigate to the project directory:

```shell
cd rdkit-isomer-generator
```

Install the required Python packages (assuming you have Python installed):

```shell
pip install rdkit-pypi
```

## Usage
Edit the `input_smiles` variable in the script to specify the SMILES notation of the molecule for which you want to generate isomers. For example:

```python
input_smiles = "CCC(Cl)C(Cl)C"
```

Run the script using the following command:

```shell
python isomer_generator.py
```

After running the script, you will get the following output:

- A JSON file named `isomer_data.json` containing information about the generated isomers and their IUPAC-like names.
- PNG image files for each isomer, e.g., `Isomer_1.png`, `Isomer_2.png`, etc., showing the visual representation of each isomer.

## Generated Output
The script generates two types of output:

### JSON Data
The JSON file `isomer_data.json` contains a dictionary with information about each generated isomer, including its SMILES notation and an IUPAC-like name.

```json
{
  "Isomer_1": {
    "SMILES": "CCC(Cl)C(Cl)C",
    "IUPAC_Like_Name": "CCC(Cl)[C@H](C)Cl"
  },
  "Isomer_2": {
    "SMILES": "CCC(Cl)[C@H](C)Cl",
    "IUPAC_Like_Name": "CCC(Cl)[C@@H](C)Cl"
  },
  ...
}
```

### Isomer Images
PNG images are generated for each isomer, showing their structural representation. These images are saved as `Isomer_1.png`, `Isomer_2.png`, etc.

![Isomer_1.png]

![Isomer_2.png]

...

