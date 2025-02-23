import subprocess
import os
import string
import random
import sys
import re

# Function to install dependencies
def install_requirements():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Requirements installed successfully.")
    except subprocess.CalledProcessError:
        print("Error occurred while installing requirements.")
        exit(1)

# Run at start of script
if __name__ == "__main__":
    if os.path.exists("requirements.txt"):
        install_requirements()
    else:
        print("requirements.txt not found.")

# Function to run shell commands
def run_command(command):
    """Run a shell command and return the output"""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command:\nExit Code: {result.returncode}\nStandard Output:\n{result.stdout}\n\nStandard Error:\n{result.stderr}")
        exit(1)
    return result.stdout.strip()

# Check Minikube status and start if needed
def check_minikube_status():
    print("<====Checking the Minikube Status===>")
    try:
        print("Starting Minikube...")
        run_command("minikube start --driver=docker")
        print("Minikube started successfully.")
    except Exception as e:
        print(f"Failed to start Minikube: {e}")
        exit(1)

# Set Minikube context
def set_minikube_context():
    print("<====Minikube Context set up===>")
    run_command("kubectl config use-context minikube")
    print("Minikube context set successfully.")

# Check Docker status
def check_docker_status():
    print("<====Checking the Docker status===>")
    try:
        run_command("docker --version")
        print("Docker is installed and running.")
    except:
        print("Docker is not installed. Please install Docker and try again.")
        exit(1)

# Check for existing Docker images
def check_docker_images():
    print("<====Checking the existing Docker images, consider cleanup if there are more than 3===>")
    image_count = int(run_command("docker images -q | wc -l"))
    print(f"Found {image_count} Docker images.")
    if image_count > 3:
        print("Consider cleaning up old Docker images.")

# Generate random tag for Docker image
def generate_random_tag(length=6):
    print("<====Generating a random tag for Docker image===>")
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

# Set Minikube Docker environment
def set_minikube_docker_env():
    print("Setting Minikube Docker environment...")
    result = subprocess.run("minikube docker-env", shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error setting Minikube Docker environment: {result.stderr}")
        exit(1)
    for line in result.stdout.splitlines():
        if line.startswith("export"):
            key_value = line.replace("export ", "").split("=", 1)
            if len(key_value) == 2:
                var_name = key_value[0]
                var_value = key_value[1].strip('"')
                os.environ[var_name] = var_value
    print("Minikube Docker environment set successfully.")

# Build Docker image
def build_docker_image(app_name):
    print("<====Building the Docker image===>")
    tag = generate_random_tag()
    image_name = f"{app_name}:{tag}"
    os.chdir("../../application_code")
    print(f"Navigated to application_code directory: {os.getcwd()}")
    print(f"Building Docker image: {image_name}")
    run_command(f"docker build -t {image_name} -f ./docker/local/Dockerfile .")
    os.chdir("../infra-code/local")
    print(f"Navigated back to local directory: {os.getcwd()}")
    return image_name

# Update Terraform with image and namespace
def update_terraform_with_image(image_name, namespace_name):
    print("<====Updating Terraform===>")
    deployment_file = "main.tf"
    with open(deployment_file, 'r') as file:
        tf_content = file.read()
    updated_content = re.sub(r'(\w+:\w+)', image_name, tf_content)
    updated_content = re.sub(r'(?<=name = )\w+', namespace_name, updated_content)
    with open(deployment_file, 'w') as file:
        file.write(updated_content)
    print(f"Updated Terraform with Docker image: {image_name}")

# Run Terraform commands
def run_terraform():
    try:
        subprocess.run(["terraform", "init"], check=True)
        subprocess.run(["terraform", "apply", "-auto-approve"], check=True)
        print("Terraform applied successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running Terraform: {e}")

# Display Terraform output
def display_terraform_output():
    output = run_command("terraform output")
    print(f"Terraform output:\n{output}")

# Retrieve Kubernetes service name
def get_service_name(namespace_name):
    """Retrieve the Kubernetes service name in the given namespace"""
    print(f"Getting the service name for namespace: {namespace_name}")
    service_name = run_command(f"kubectl get svc -n {namespace_name} -o jsonpath={{.items[0].metadata.name}}")
    print(f"Service name: {service_name}")
    return service_name

# Expose Minikube service
def expose_minikube_service(service_name, namespace_name):
    """Expose Minikube service and open it in the browser"""
    print(f"Exposing Minikube service {service_name} in namespace {namespace_name}...")
    result = run_command(f"minikube service {service_name} -n {namespace_name}")
    print("Service exposed. Application should open in your default browser.")

# Main Deployment Flow
def main():
    print("Starting deployment process...")
    
    # Step 1: Check Minikube status
    check_minikube_status()
    
    # Step 2: Set Minikube context
    set_minikube_context()
    
    # Step 3: Check Docker and build image
    check_docker_status()
    check_docker_images()
    set_minikube_docker_env()
    
    # Step 4: Input application name and namespace
    app_name = input("Enter your application name (e.g., nextjs-app): ")
    namespace_name = input("Enter your namespace name: ")
    
    # Step 5: Build the Docker image
    image_name = build_docker_image(app_name)

    # Step 6: Update Terraform with the image and namespace
    update_terraform_with_image(image_name, namespace_name)

    # Step 7: Run Terraform
    run_terraform()

    # Step 8: Display Terraform output
    display_terraform_output()

    # Step 9: Get the service name
    service_name = get_service_name(namespace_name)

    # Step 10: Expose the service using Minikube
    expose_minikube_service(service_name, namespace_name)

if __name__ == "__main__":
    main()
