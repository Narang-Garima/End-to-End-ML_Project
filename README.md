Stepwise Implementation that is done
1. git repo
2. env create
3. setup.py
4. template.py  or use cookiecutter
5. database-> table in mysql
6. data ingetion -> extraction from sql -> train test split -> store in separate folders, in artifacts
7. dvc(data version control), to track larger dataset. “DVC is like Git, but for data and ML models. It tracks large datasets and models without storing them in Git directly.”“We store only small .dvc metadata files in Git, and the actual data goes to remote storage like Google Drive or S3.”“It makes ML experiments reproducible, lets teammates pull the same data/models, and we can roll back to previous versions easily.”
raw_data.csv  -->  preprocess.py  -->  processed_data.csv  -->  train.py  -->  model.pkl
dont put dvc in requirements

## dvc commands
###important-- we dont want git track dvc files so put 
dvc init


