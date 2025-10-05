import os
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

project_name = "MLProject"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_integestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitoring.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/utils.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt", 
    "setup.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for file: {filename}")
    
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, 'w') as f:
            if filename == "__init__.py":
                pass  # Leave __init__.py files empty
            else:
                f.write(f"# {filename}\n")
                logging.info(f"Created file: {filepath}")
    else:
        logging.info(f"File already exists and is not empty: {filepath}")