# Student Pass/Fail Prediction | Assignment 04

This project compares a dummy baseline, logistic regression and a random forest using 280 synthetic student records. It predicts `passed` from five features available before the final result. The final score is excluded.

## Run locally

Extract the ZIP and open the extracted folder in VS Code. Use Python 3.12 or 3.13 and install the dependencies in the environment you will use:

```powershell
python -m pip install -r requirements.txt
```

Open `Student_Pass_Fail.ipynb`, select that Python environment as the kernel and choose **Run All**. Keep both CSV inputs next to the notebook. The last code cell saves the fitted pipeline, reloads it and writes the predictions to `new_student_predictions.csv`.

To use the saved model without training it again, run:

```powershell
python -m streamlit run app.py
```

Open the local address printed in the terminal, enter the five values and click **Predict**. Keep `student_pipeline.joblib` beside `app.py`. To see a Pass example, try 8 hours studied, 94% attendance, 5 practice tests, 7.5 hours of sleep and self study.

## Run the notebook in Colab

Upload `Student_Pass_Fail.ipynb` as a notebook. After connecting, upload `student_learning.csv` and `new_student_records.csv` into the session's Files panel (default working folder). Run all cells. The notebook trains and saves a fresh pipeline using the Colab environment. Run the Streamlit app locally using the pinned dependencies and the model included in the ZIP.

## Results and responsible use

The saved logistic regression pipeline scored 75.0% accuracy and 0.720 Pass F1 on 56 test records. It was selected using training cross-validation. See `evaluation_summary.md` for all three models and `model_card.md` for limitations. This is a classroom demonstration. Do not use its predictions to grade or penalize real students.

GitHub repository: [https://github.com/Noor-Maryam/Student-Learning-Prediction]
