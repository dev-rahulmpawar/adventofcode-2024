#!/bin/bash

# Function to commit and optionally push changes
git_commit() {
    # Check if the user provided a commit message
    if [ -z "$1" ]; then
        echo "Error: Commit message is required."
        echo "Usage: git_commit \"Your commit message\" [push]"
        return 1
    fi

    # Store the commit message
    COMMIT_MESSAGE="$1"

    # Checkout master
    echo "Switching to master..."
    git checkout master
    
    # pull from master
    echo "Taking latest update from master..."
    git pull
    
    # Add all changes to staging
    echo "Adding changes to staging area..."
    git add .

    # Commit the changes with the provided message
    echo "Committing changes with message: '$COMMIT_MESSAGE'"
    git commit -m "$COMMIT_MESSAGE"

    # Check if the user wants to push the changes
    if [ "$2" == "push" ]; then
        # Get the current branch name
        BRANCH_NAME=$(git rev-parse --abbrev-ref HEAD)

        echo "Pushing changes to branch '$BRANCH_NAME'..."
        git push origin "$BRANCH_NAME" --force
    else
        echo "Changes committed locally. Use 'push' as the second argument to push to the remote branch."
    fi
}

# Example usage:
# git_commit "Your commit message" push