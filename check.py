import mlflow
client = mlflow.tracking.MlflowClient()
model_versions = client.search_model_versions("name='RandomForestModel'")
for version in model_versions:
    print(f"version: {version.version}, stage: {version.current_stage}")
