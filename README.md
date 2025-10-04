# 🧠 Git Commands Guide

A complete reference of essential **Git commands** for version control, branching, and collaboration.

---

## 🪜 Basic Git Commands

| Command | Description |
|----------|-------------|
| `git init` | Initializes a new Git repository in your current folder. |
| `git add <filename>` | Stages a specific file for commit. |
| `git add .` | Stages all modified and new files for commit. |
| `git status` | Displays the current state of your working directory and staging area. |
| `git commit -m "message"` | Commits staged changes with a descriptive message. |
| `git log` | Shows the commit history of the repository. |
| `git diff` | Displays differences between the working directory and staged changes. |
| `git rm <filename>` | Removes a file from the working directory and from Git tracking. |

---

## 🌐 Connecting to Remote Repositories

| Command | Description |
|----------|-------------|
| `git remote add origin <repo_URL>` | Links your local repo to a remote GitHub repository. |
| `git remote -v` | Lists all remotes and their associated URLs. |
| `git remote remove origin` | Removes the current remote connection. |
| `git config --global user.name "Your Name"` | Sets your global Git username. |
| `git config --global user.email "your_email@example.com"` | Sets your global Git email. |
| `git push -u origin <branch>` | Pushes the branch to the remote repository and sets it as the default upstream branch. |
| `git pull origin <branch>` | Fetches and merges the latest changes from the remote branch. |
| `git fetch` | Downloads changes from the remote repository without merging them. |

---

## 🌿 Branching and Merging

| Command | Description |
|----------|-------------|
| `git branch` | Lists all local branches. |
| `git branch <branch_name>` | Creates a new branch from the current branch. |
| `git checkout <branch_name>` | Switches to the specified branch. |
| `git checkout -b <branch_name>` | Creates and switches to a new branch immediately. |
| `git merge <branch_name>` | Merges the specified branch into your current branch. |
| `git branch -d <branch_name>` | Deletes a local branch (only if it has been merged). |
| `git branch -D <branch_name>` | Force-deletes a local branch (even if not merged). |
| `git push origin --delete <branch_name>` | Deletes a remote branch from GitHub. |
| `git worktree prune` | Cleans up leftover worktree references. |

---

## 🧱 Creating a Replica of the Main Branch

To create a branch that is a **replica of the main branch**, run the following commands:

```bash
git checkout main          # Switch to the main branch
git pull origin main       # Ensure main is up to date
git checkout -b new_branch # Create and switch to a new branch


## env comnd
- conda create -p venv python=3.11 -y
- conda activate <env name>
- conda env list 