import mlflow.pyfunc

# Replace with your run ID and artifact path (manually added right now)
run_id = "d274cca7facf4fe69e249eab36290314"
artifact_path = "artifacts"
model_name = "Random Forest2-reg"

# Construct the model URI
model_uri = f"runs:/{run_id}/{artifact_path}"

# Register the model
model_version = mlflow.register_model(model_uri, model_name)

model = mlflow.pyfunc.load_model(model_uri=f"models:/{model_name}/{model_version}")

model.predict('Low', 2000.0,70.70,500.00,35.75,40.00)