import mlflow
import mlflow.sklearn
from mlflow.tracking import MlflowClient


# Model Registry Automation:
# Adding an MLflow Model to the Model Registry

client = MlflowClient()

# Replace with your run ID and artifact path (manually added right now)
run_id = "d274cca7facf4fe69e249eab36290314"
artifact_path = "artifacts"
model_name = "Random Forest2-reg"

# Construct the model URI
model_uri = f"runs:/{run_id}/{artifact_path}"

# Register the model
model_version = mlflow.register_model(model_uri, model_name)

# Add description
client.update_model_version(
    name=model_name,
    version=model_version.version,
    description="This model predicts equipment failures using historical sensor data."
)

# Transition model stage
client.transition_model_version_stage(
    name=model_name,
    version=model_version.version,
    stage="Staging"
)

# Add tags
client.set_model_version_tag(
    name=model_name,
    version=model_version.version,
    key="algorithm",
    value="RandomForest"
)
