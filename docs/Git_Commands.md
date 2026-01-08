```bash
# ╔══════════════════════════════════════════════════════╗
# ║   GIT BASH ENVIRONMENT SETUP (WINDOWS)               ║
# ╚══════════════════════════════════════════════════════╝

# Clone from remote
git clone <url>

# Initialize a new git repository (if needed)
git init

# Create virtual environment
python -m venv venv

# Activate virtual environment (Git Bash on Windows)
source venv/Scripts/activate

# Upgrade pip
python.exe -m pip install --upgrade pip

pip install fastapi uvicorn
pip install fastapi psycopg2-binary
pip install uvicorn

# Install dependencies
pip install -r requirements.txt

# Freeze current dependencies
pip freeze > requirements.txt

# Initial commit and push
git add .
git commit -m "initial commit"
git push -u origin main
```

```bash
# ╔══════════════════════════════════════════════════════╗
# ║   BASIC GIT COMMANDS                                 ║
# ╚══════════════════════════════════════════════════════╝

git add .
git commit -m "Commit message"
git push
```

```bash
# ╔══════════════════════════════════════════════════════╗
# ║   GIT BRANCH WORKFLOW                                ║
# ╚══════════════════════════════════════════════════════╝

# Check current branch
git branch

# Create a new branch
git checkout -b title/branch_purpose
git checkout -b dev/Refine_FastApi_code

# Stage changes
git add .

# Commit changes
git commit -m "Descriptive commit message"

# Push branch to remote
git push -u origin title/branch_purpose
git push -u origin dev/Refine_FastApi_code

# Switch between branches
git checkout main
git checkout title/branch_purpose

# Merge branch into main
git checkout main
git pull                      # ensure main is up-to-date
git merge route/update
git merge dev/api_local_mongo_image

# Delete branch (optional)
git branch -d title/branch_purpose              # delete local branch
git push origin --delete title/branch_purpose   # delete remote branch

# Useful commands
git status                      # View changes
git log --oneline               # Condensed history
git remote -v                   # Show remote URL
```

```bash
# ╔══════════════════════════════════════════════════════╗
# ║   GIT: GO BACK TO OLD VERSIONS & PUSH TO GITHUB      ║
# ╚══════════════════════════════════════════════════════╝

# Save current work
git status
git add .
git commit -m "Current working version"

# View commit history
git log --oneline

## ✅ Option A — Revert (Keep History, Create New Commit)
# Revert a range of commits, creating new commits that undo them
git revert <old_commit_hash>..HEAD

# Example:
git revert 8a61c0c8360841b8ef1a5f47f41854adc48f12d3..HEAD

# Push reverted history
git push

# Abort revert if stuck in conflicts, etc.
git revert --abort

## 🔴 Option B — Reset (Full Move Back, Rewrite History)
# Hard reset to an old commit (DANGEROUS: rewrites history)
git reset --hard <old_commit_hash>

# Force push rewritten history
git push --force

## Push project to GitHub (new or re-linked repo)

# Initialize repo (if not already)
git init

# Add remote
git remote add origin https://github.com/AharonSegal/..

# Stage and commit
git add .
git commit -m "Initial Push"

# Ensure branch is named main
git branch -M main

# Push to GitHub
git push -u origin main

# If push fails due to remote changes
git pull origin main --rebase
git push -u origin main
```

```bash
# ╔══════════════════════════════════════════════════════╗
# ║   GIT: PUSHING TO MAIN & CREATING NEW REPO (CLI)     ║
# ╚══════════════════════════════════════════════════════╝

## 🚀 Push Local Project to `main` Branch (Existing Repo)

# Check current status
git status

# Stage and commit changes
git add .
git commit -m "Update project"

# Ensure branch is main
git branch -M main

# Add remote if not already added
git remote add origin https://github.com/<username>/<repo>.git

# Push to main
git push -u origin main

# If push is rejected (remote has commits)
git pull origin main --rebase
git push origin main
```

```bash
# 🆕 Create a NEW GitHub Repository from an Existing Project (CLI Only)

# 1️⃣ Initialize Git (if not already)
git init
git branch -M main

# 2️⃣ Commit the project
git add .
git commit -m "Initial commit"

# 3️⃣ (On GitHub: create EMPTY repo — no README, no .gitignore)

# 4️⃣ Link local project to the new repo
git remote add origin https://github.com/AharonSegal/<new-repo>.git



# 5️⃣ Push to GitHub
git push -u origin main

# 🔄 Verify Remote Configuration
git remote -v
```

```bash
# ╔══════════════════════════════════════════════════════╗
# ║   GIT LOGGING & VIEWING HISTORY                      ║
# ╚══════════════════════════════════════════════════════╝

# View current branch status
git status

# View full commit history
git log

# View condensed history (one line per commit)
git log --oneline

# Show commits with graph
git log --oneline --graph --decorate --all

# View last N commits
git log -n 5

# View changes in a specific commit
git show <commit-hash>

# View differences in working directory (unstaged changes)
git diff

# View staged changes
git diff --cached

# Show remote repositories
git remote -v

# View detailed commit history for a specific file
git log -- <file-path>
```

