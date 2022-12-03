# We will define input structure

# We will define ouput for each componenets
# 6 configuration have to be defined
'''
Data Injection --> Data Validation --> Data Transformation --> Model Trainer --> Model Evaluation --> Model Pusher
'''
# three dot means pass keyword

from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    feature_store_file_path:str
    train_file_path:str 
    test_file_path:str

class DataValidationArtifact:...
class DataTransformationArtifact:...
class ModelTrainerArtifact:...
class ModelEvaluationArtifact:...
class ModelPusherArtifact:...