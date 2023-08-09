from kubernetes import client, config

def list_namespaces():
    config.load_incluster_config()  # Charge la configuration du cluster depuis le service account du pod
    v1 = client.CoreV1Api()
    print("Liste des namespaces:")
    ret = v1.list_namespace()
    for ns in ret.items:
        print(f"- {ns.metadata.name}")

if __name__ == "__main__":
    list_namespaces()
