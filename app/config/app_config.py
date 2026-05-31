import yaml

with open("app/config/application-dev.yaml") as file:
    config = yaml.safe_load(file)

CLIENT_SERVICE_BASE_URL = config["client"]["service"]["base_url"]

if not CLIENT_SERVICE_BASE_URL:
    raise ValueError(
        "client.service.base_url not configured"
    )

print(f"CLIENT_SERVICE_BASE_URL = {CLIENT_SERVICE_BASE_URL}")