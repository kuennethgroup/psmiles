from psmiles import PolymerSmiles as PS


def test_similarity():
    fp_names = [ 
        "ci",
        "rdkit",
    ]

    similarity_score = []
    for fp in fp_names:
        score = PS("[*]COCC[*]").is_similar(PS("[*]CCO[*]"), fp)
        similarity_score.append(score)

    assert similarity_score == [0.80257, 0.70296]
