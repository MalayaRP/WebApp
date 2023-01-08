import streamlit as st
import rdkit 
from rdkit import Chem
from rdkit.Chem import Draw
st.title("Enter Smiles")
smile = st.text_input("")
st.write("Molecule")
mols = Chem.MolFromSmiles(smile)
im=Draw.MolToImage(mols)

st.image(im)
