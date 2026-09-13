# Git Cheat Sheet (DevOps Edition)

This document contains essential Git commands for daily workflows, along with advanced tools for rewriting history and rescuing repositories in critical situations.

## ⚙️ 1. Global Configuration

Always verify your Git author details before starting work in a new environment (e.g., a fresh WSL instance) to ensure GitHub attributes your commits correctly.

```bash
# Check current configured email
git config user.email

# Set global name and email
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## 📝 2. Daily Workflow

The standard cycle for committing new features and documentation.

```bash
# Check repository status (modified, staged, and untracked files)
git status

# Stage a specific file (or use 'git add .' for all changes)
git add <file_name>

# Commit changes with a descriptive message

# Common commit prefixes (Conventional Commits):
# feat:     A new feature (e.g., new script, new infrastructure setup)
# fix:      A bug fix (e.g., fixing a broken loop or typo in a script)
# docs:     Documentation only changes (e.g., updating README or Runbooks)
# chore:    Routine tasks, maintenance, or config changes (e.g., updating requirements.txt or .gitignore)
# refactor: A code change that neither fixes a bug nor adds a feature (e.g., rewriting a script to be cleaner)

git commit -m "feat: add dockerfile for python dashboard"

# Push changes to the remote repository
git push origin main
```

## 🌿 3. Branching

Use branches to safely develop new features or test configurations without breaking the production code.

```bash
# List all local branches
git branch

# Create and immediately switch to a new branch
git checkout -b feature/docker-setup

# Switch back to the main branch
git checkout main

# Merge changes from the feature branch into main
git merge feature/docker-setup
```

## ⏳ 4. Rewriting History

**Warning:** Only use `push -f` on personal branches! Never force push to shared production branches.

```bash
# Change the commit message or author of the VERY LAST commit
git commit --amend --reset-author

# Start an interactive rebase for the last 5 commits
git rebase -i HEAD~5

# Force push rewritten history to the remote server
git push -f origin main
```

## 🚨 5. Panic Buttons (Rescue Commands)

Use these when you are stuck or need to undo a catastrophic mistake.

```bash
# 1. Stuck in a rebase loop? Abort the entire process:
git rebase --abort

# 2. Detached HEAD state? Create an anchor, reset, and clean up:
git branch temp-fix
git checkout main
git reset --hard temp-fix
git branch -d temp-fix

# 3. Discard all local uncommitted changes (reset to server state):
git reset --hard origin/main

# 4. The secret Git ledger (shows every action, even deleted ones):
git reflog
```
