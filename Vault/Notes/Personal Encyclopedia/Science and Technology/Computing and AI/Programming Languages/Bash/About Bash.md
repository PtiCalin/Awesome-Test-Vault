


---
# 🐚 Bash Learning Guide

> A beginner-friendly and structured guide to navigating your system and scripting with Bash. This is not just a cheat sheet — it's a growing, modular knowledge base for your command-line fluency.

---

BASH stands for 



## 🗂️ Navigation with `cd`

### Move around your file system

```bash
cd ~
```
🏠 Go to your **home** directory.

```bash
cd ..
```
🔙 Move **up one level** from your current location.

```bash
cd /path/to/directory
```
🚪 Jump directly to a **specific path**.

```bash
cd Documents
```
📁 Move into the `Documents` folder (if it exists in your current location).

```bash
cd ObsidianVault
```
🔐 Enter your `ObsidianVault` directory.

---

## 🏗️ Creating Folders with `mkdir`

### Organize your files into directories

```bash
mkdir new_directory
```
Create a new directory.

```bash
mkdir -p /path/to/new_directory
```
📌 Create a directory *and* all necessary parent directories.

```bash
mkdir -v new_directory
```
🗣️ Verbose mode — confirms each created folder.

```bash
mkdir -m 755 new_directory
```
🔐 Create a directory with specific permissions.

> Example structure creation:
```bash
mkdir -p ~/Documents/ObsidianVault/notes/2023/January/01
```
📁 Builds a full nested folder path for note-taking by date.

---

## 📂 Listing Files with `ls`

### See what's inside a folder

📃 Basic listing
```bash
ls
```

📋 Detailed view with permissions, size, date
```bash
ls -l
```

👀 List all includincluding hidden files (those starting with `.`)
```bash
ls -a
```

📏 Human-readable sizes in detailed listing
```bash
ls -lh
```

🔁 Recursively list contents of subdirectories
```bash
ls -R
```


> Combine flags like so:
```bash
#Shows all files with details.
ls -la
```


---

## 🔧 Git Essentials

### Version control in the command line

```bash
git init
```
🧬 Start a new Git repo in the current directory

```bash
git remote add origin <url>
```
🔗 Connect your repo to a remote (e.g., GitHub)

```bash
git remote -v
```
🔍 View linked remotes

```bash
git checkout -b main
```
🌱 Create a new branch called `main`

```bash
git add .
```
➕ Stage all changes

```bash
git commit -m "Initial commit"
```
💬 Commit changes with a message

```bash
git push -u origin main
```
🚀 Push your code and set tracking to remote `main`

> ⚠️ Replace `<url>` with your actual Git repository URL.

---

## 📝 Scripting & Comments

### Shebang & annotations

```bash
#!/bin/bash
```
🪧 This tells your system to run the script using Bash. It goes at the top of the file.

```bash
# This is a comment in Bash
```
💬 Use comments to explain what your code does.

---

## 📚 Resources for Going Deeper

- [Bash Guide (TLDP)](https://tldp.org/LDP/Bash-Beginners-Guide/html/)
- [Git Book](https://git-scm.com/book/en/v2)
- [Ryan's Bash Tutorial](https://ryanstutorials.net/bash-scripting-tutorial/)
- [Bash Cheat Sheet (Devhints)](https://devhints.io/bash)
- [Bash CLI Sheet (Cheatography)](https://www.cheatography.com/davechild/cheat-sheets/bash-command-line/)
- [Shell scripting tutorials](https://www.shellscript.sh/)

---

## 💡 What Else Can Bash Do?

Bash isn’t just for navigating. It can:

- Automate backups & tasks
- Schedule jobs via `cron`
- Deploy projects
- Manage users, permissions, or networks
- Launch system diagnostics or maintenance
- Monitor logs or resource usage
- Handle Git workflows
- Run development test suites
- Move, rename, and process files in bulk

> Bash grows with you. The more you script, the more powerful you become.

---
🧩 **Next Steps**:
- add a section on `cp`, `mv`, and `rm`?
- include `chmod`, `chown`, or `cron` usage?
