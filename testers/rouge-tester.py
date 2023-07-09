from rouge import Rouge 

hypothesis = "this is a dog"

reference = "this is a dog"

rouge = Rouge()
scores = rouge.get_scores(hypothesis, reference, avg=True)

for rouge_type in scores.keys():
    print(rouge_type)
    for score in scores[rouge_type]:
        if(score == 'r'):
            print(f"recall: {scores[rouge_type][score]}")
        if(score == 'p'):
            print(f"precision: {scores[rouge_type][score]}")
        if(score == 'f'):
            print(f"f1_score: {scores[rouge_type][score]}")
    print()
