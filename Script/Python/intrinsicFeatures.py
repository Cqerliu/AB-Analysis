import pandas as pd
import os
def intrinsicFeatures(file):
    for filepath in file:
        content = pd.read_excel(filepath)
        protein = content["pro"].values
		gene = content["gene"].values	
        for num in range(len(protein)):
            lenPro = len(protein[num])
			lenGene = len(gene[num])
        
        
        