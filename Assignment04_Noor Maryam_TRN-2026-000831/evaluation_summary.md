# Evaluation summary

The stratified split used 224 training rows and 56 test rows with seed 42. All three models used the same 56 held-out rows. F1 treats Pass as the positive class.

| Model | Accuracy | Pass F1 | True Fail | False Pass | False Fail | True Pass |
|---|---:|---:|---:|---:|---:|---:|
| Dummy baseline | 0.554 | 0.000 | 31 | 0 | 25 | 0 |
| Logistic regression | 0.750 | 0.720 | 24 | 7 | 7 | 18 |
| Random forest | 0.768 | 0.735 | 25 | 6 | 7 | 18 |

The saved pipeline uses **Logistic regression**. Its mean training-fold F1 was **0.797**, the higher of the two candidate scores. The holdout contained **7 false passes** and **7 false fails** for this model.

A false Pass can hide a need for help. A false Fail can unfairly flag a student. The baseline predicts only Fail, so its Pass F1 is zero.
