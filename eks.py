from kubernetes import client, config
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Load Kubernetes configuration
config.load_kube_config()

# Create API client
api_client = client.ApiClient()

# Define deployment object
deployment = client.V1Deployment(
    metadata=client.V1ObjectMeta(name="monitoring-app"),
    spec=client.V1DeploymentSpec(
        replicas=1,
        selector=client.V1LabelSelector(
            match_labels={"app": "monitoring-app"}
        ),
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(
                labels={"app": "monitoring-app"}
            ),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="monitoring-app-container",
                        image="129128298531.dkr.ecr.us-east-1.amazonaws.com/monitoring_app:latest",
                        ports=[client.V1ContainerPort(container_port=5000)]
                    )
                ]
            )
        )
    )
)

# Create deployment
try:
    api_instance = client.AppsV1Api(api_client)
    api_instance.create_namespaced_deployment(
        namespace="default",
        body=deployment
    )
    print("Deployment created successfully.")
except Exception as e:
    print("Error creating deployment:", e)

# Define service object
service = client.V1Service(
    metadata=client.V1ObjectMeta(name="monitoring-app-service"),
    spec=client.V1ServiceSpec(
        selector={"app": "monitoring-app"},
        ports=[client.V1ServicePort(port=5000)]
    )
)

# Create service
try:
    api_instance = client.CoreV1Api(api_client)
    api_instance.create_namespaced_service(
        namespace="default",
        body=service
    )
    print("Service created successfully.")
except Exception as e:
    print("Error creating service:", e)
