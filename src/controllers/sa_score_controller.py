"""
Copyright (C) Iktos - All Rights Reserved
Unauthorized copying of this file, via any medium is strictly prohibited
Proprietary and confidential
"""

from typing import Dict, List

from rdkit.Chem import MolFromSmiles

from src.use_cases.compute_sa_score import compute_sa_score


def sa_score_controller(smiles_list: List[str]) -> Dict[str, list]:
    results = {}
    for smiles in smiles_list:
        results[smiles] = [compute_sa_score(MolFromSmiles(smiles))]
    return results
