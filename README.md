### Requirements
1. Docker==27.0.3
2. Helm==3.7.2

### Docker image

To build the Docker image for the `web` folder, use the following command:

```bash
    docker run --privileged --rm tonistiigi/binfmt --install all
    docker buildx create --use
    cd web
    docker buildx build --platform linux/amd64,linux/arm64 -t retrorb/backend:{tag} .
```

### Starting Docker Compose

To start Docker Compose and run your application, use the following command:

```bash
    cd web
    docker compose up -d
```

### Checking the Application

To check if your application is running correctly, open the browser and visit http://locahost:5001

### Helm

To work with Helm:

1. Go to the `helm` directory.
2. Install the Helm chart using the command:
```bash
    helm install tango poc
```
3. Test the Helm chart using the command:
```bash
    helm test tango
```
4. Forward the port using the command:
```bash 
    kubectl port-forward --address=0.0.0.0 svc/tango-frontend 8080:80
```
5. Open the application in the browser by visiting http://localhost:8080.
