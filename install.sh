#!/bin/bash

# Print each command before executing it
set -e  # Exit script if any command fails
set -x  # Print commands as they are executed

# Function to check if a program is installed
function check_installed() {
    if ! command -v $1 &> /dev/null; then
        echo "$1 not found, installing..."
        return 1
    else
        echo "$1 is already installed."
        return 0
    fi
}

# Update the package list
echo "Updating package lists..."
sudo apt update -y

# Install dependencies (example: git, curl, and build-essential)
DEPENDENCIES=("git" "curl" "build-essential")

for package in "${DEPENDENCIES[@]}"; do
    check_installed $package || sudo apt install -y $package
done

# Clone a GitHub repository (replace with the actual repo)
REPO_URL="https://github.com/your-repo/your-project.git"
DEST_DIR="$HOME/your-project"

if [ ! -d "$DEST_DIR" ]; then
    echo "Cloning repository from $REPO_URL..."
    git clone $REPO_URL $DEST_DIR
else
    echo "Repository already exists at $DEST_DIR"
fi

# Change directory to the project folder
cd $DEST_DIR

# Run additional setup commands (e.g., building the project)
echo "Running project setup..."
# Example: make or custom setup commands
# make build

# Print success message
echo "Installation and setup complete!"
