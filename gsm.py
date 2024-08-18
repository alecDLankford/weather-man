from google.cloud import secretmanager

def get_secret(secret_id):
    project_id = "groovy-autumn-432923-k6"
    version_id = "latest"

    client = secretmanager.SecretManagerServiceClient()

    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

    response = client.access_secret_version(request={"name": name})

    payload = response.payload.data.decode("UTF-8")
    return payload
