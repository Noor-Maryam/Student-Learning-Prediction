# Model card | Student Pass/Fail

**Purpose.** Classroom demonstration of binary classification with synthetic student records.

**Data and inputs.** 280 synthetic rows (157 Fail, 123 Pass). The five inputs are hours studied, attendance, practice tests, sleep hours and study method. The final score is excluded to avoid leakage.

**Model.** Logistic regression, selected by five-fold cross-validation on the training data. Numeric blanks use the training median, numeric inputs are scaled, and missing study methods use the most frequent training category before one-hot encoding.

**Performance.** Accuracy 0.750 and Pass F1 0.720 on 56 held-out records. See evaluation_summary.md for the confusion counts for all three models.

**Limits.** The sample is small and synthetic. Performance on real students and fairness across groups are unknown. Study habits are not evidence of what caused a particular grade. There is no measured accuracy for the hand-written demo records.

**Responsible use.** Use the model to demonstrate the workflow. Do not use it to grade, rank, penalize or make decisions about real students. Keep real student records out of the demo.
