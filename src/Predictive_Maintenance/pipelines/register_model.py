import mlflow
import mlflow.sklearn

# Replace with your run ID and artifact path
run_id = "d274cca7facf4fe69e249eab36290314"
artifact_path = "artifacts"
model_name = "Random Forest2-reg"

# Construct the model URI
model_uri = f"runs:/{run_id}/{artifact_path}"

# Register the model
mlflow.register_model(model_uri, model_name)
