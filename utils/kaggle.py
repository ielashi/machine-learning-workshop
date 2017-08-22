import pandas as pd

def write_kaggle_submissions_file(predictions):
  submissions=pd.DataFrame({"ImageId": list(range(1,len(predictions)+1)),
                            "Label": predictions})
  submissions.to_csv("submission.csv", index=False, header=True)
