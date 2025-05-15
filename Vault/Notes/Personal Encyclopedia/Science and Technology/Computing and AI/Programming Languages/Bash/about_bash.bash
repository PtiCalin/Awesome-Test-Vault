
## 🧠 Example Bash Script for Git Commands
```bash
#!/bin/bash

---


# This script demonstrates how to use Git commands in a bash script.
# It initializes a Git repository, adds a remote, and creates a new branch.
# It also includes comments explaining each step.
# This script assumes you have Git installed and configured on your system.

#This guide exlores the following sections of commands:
# 1. 🗂️ Navigation (Cd)
# 2. 🏗️ Creating Folders (mkdir)
# 3. 📂 Listing Files (ls)
# 4. 🔧 Git Essentials (Git)


---
🗂️ Navigation (Cd)


# CD Commands
# Change Directory (cd) commands are used to navigate through the file system.
cd ~                     # 🏠 Go to the home directory  
cd ..                    # 🔙 Go up one directory level  
cd /path/to/directory    # 🚪 Go to a specific directory  

# Example: Navigate to the Documents folder
# Note: Replace /path/to/directory with the actual path to your directory.
cd Documents             # 📁 Enter the Documents folder  

# Example : Navigate to the ObsidianVault folder
cd ObsidianVault         # 🔐 Enter the ObsidianVault folder  

---
🏗️ Creating Folders (mkdir)


# MKDIR Commands
# The mkdir command is used to create new directories.

mkdir new_directory    # Create a new directory called new_directory
mkdir -p /path/to/new_directory  # Create a new directory with parent directories if they don't exist
mkdir -v new_directory  # Create a new directory and show a message
mkdir -m 755 new_directory  # Create a new directory with specific permissions

# Example: Create a new directory called ObsidianVault in the Documents folder

mkdir ObsidianVault    # Create a new folder called ObsidianVault
mkdir -p ~/Documents/ObsidianVault  # Create a new directory in the Documents folder
mkdir -p ~/Documents/ObsidianVault/notes  # Create a new directory for notes
mkdir -p ~/Documents/ObsidianVault/notes/2023  # Create a new directory for notes in 2023
mkdir -p ~/Documents/ObsidianVault/notes/2023/January  # Create a new directory for January notes
mkdir -p ~/Documents/ObsidianVault/notes/2023/January/01  # Create a new directory for January 1st notes

---
📂 Listing Files (ls)

# ls Commands
# The ls command is used to list files and directories in the current directory.
ls                     # 📃 List files  
ls -l                  # 📋 Long listing (details)  
ls -a                  # 👀 List showing hidden files  
ls -lh                 # 📏 Human-readable file sizes  
ls -R                  # 🔁 Recursive listing  
ls -t                  # ⏱️ Sort by time  
ls -S                  # ⚖️ Sort by size  
ls -r                  # 🔄 Reverse order  
ls -d */               # 📁 Show only directories  
ls -1                  # 📄 One file per line  
ls -F                  # 🔖 Show type indicators  
ls -i                  # 🆔 Show inode numbers  
ls -G                  # 🎨 Colorized output  
ls -lS                 # ⚖️+📋 Sort by size with details  
ls -lt                 # ⏱️+📋 Sort by time with details 

# Example: List all files in the current directory


# Note: You can combine options. For example, ls -la will list all files with detailed information.

---
🔧 Git Essentials (Git)

# Git Commands
# The following commands are used to manage Git repositories.
git init                       # 🧬 Initialize Git repository  
git remote add origin <url>    # 🔗 Add a remote  
git remote -v                  # 🔍 Verify remotes  
git checkout -b main           # 🌱 Create new branch called main  
git add .                      # ➕ Stage all changes  
git commit -m "Initial commit" # 💬 Commit with message  
git push -u origin main        # 🚀 Push to remote and set upstream  sitory


# Note: You will need to replace <remote-repo-url> with the actual URL of your remote repository.
# This script is a basic example and can be modified to suit your needs.
# You can add more Git commands as needed.
# For example, you can use git pull to fetch and merge changes from the remote repository.
# You can also use git status to check the status of your repository.


---
# 📝 Comments

#🪧 Shebang (#!/bin/bash)
# This line tells your system to run the script using the Bash shell, not any other shell that might be set by default.
# Without it, your script might break on someone else’s machine.

---

# 📚 More Learning Resources

# Git Documentation: https://git-scm.com/doc
# Git Book: https://git-scm.com/book/en/v2
# Bash Guide: https://tldp.org/LDP/Bash-Beginners-Guide/html/
# Bash Cheat Sheet: https://devhints.io/bash
# Bash Scripting Tutorial: https://ryanstutorials.net/bash-scripting-tutorial/
# Bash Command Line Cheat Sheet: https://www.cheatography.com/davechild/cheat-sheets/bash-command-line/
# Bash Scripting Guide: https://www.shellscript.sh/

---
# Other Use Cases and Examples 

# What else can we do using .bash scripts?
# 1. Automate repetitive tasks
# 2. Create backups
# 3. Monitor system performance
# 4. Manage files and directories
# 5. Schedule tasks using cron jobs
# 6. Run system maintenance tasks
# 7. Deploy applications
# 8. Manage user accounts
# 9. Configure system settings
# 10. Generate reports
# 11. Send notifications
# 12. Perform system updates
# 13. Manage network settings
# 14. Automate software installations
# 15. Create and manage virtual environments
# 16. Run tests and quality checks
# 17. Manage databases
# 18. Monitor logs and system events
# 19. Automate data processing
# 20. Create and manage Git repositories
... and much more!

# Here is an example how you could use .bash script to plan and create a directory structure for your Obsidian vault:

# 🗂️ Directory Structure
# Map out your directory structure using this simple marking format.

# This is a simple directory structure for organizing your files.

# ├── Documents
# │   ├── ObsidianVault
# │   │   ├── files and media           <- Files and media for your vault.
# │   │   │   ├── images
# │   │   │   ├── documents
# │   │   │   ├── audios
# │   │   │   ├── videos
# │   │   │   ├── web clippings             <- Location for web clippings through the obsidian web clipper.
# │   │   │   ├── other media
# │   │   ├── notes             <- Note taking, writing, and journaling.
# │   │   │   ├── General notes             <- General notes and writing.
# │   │   │   │   ├── Topic 1
# │   │   │   │   │   ├── Note 1
# │   │   │   │   │   ├── Note 2
# │   │   │   │   ├── Topic 2
# │   │   │   │   │   ├── Note 1
# │   │   │   │   │   ├── Note 2
# │   │   │   │   ├── Topic 3
# │   │   │   │   │   ├── Note 1
# │   │   │   ├── Daily notes           <- Daily journaling and reflection.
# │   │   │   │   ├── 2025
# │   │   │   │   │   ├── 2025-01
# │   │   │   │   │   ├── 2025-02
# │   │   │   │   │   ├── 2025-03
# │   │   │   │   │   ├── 2025-04
# │   │   │   │   │   │   ├── 2025-04-01.md
# │   │   │   │   │   │   ├── 2025-04-02.md
# │   │   │   │   │   │   ├── 2025-04-03.md
# │   │   │   │   │   │   ├── 2025-04-23.md
# │   │   │   ├── Meeting notes        <- Meeting notes and agendas.
# │   │   │   │   ├── YYYY-MM-DD_Meeting title.md
# │   │   │   ├── Brain Dump            <- Brain dump notes and ideas.
# │   │   │   ├── Questions           <- Questions and ideas for future exploration.
# │   │   │   ├── tasks     <- Task management, pulls "- [ ]" items from vault notes into the appropriate dated "Daily tasks" note based on timestamp.
# │   │   │   │   ├── Daily tasks           <- Daily tasks and to-do lists. With planned integration with calendar and events.
# │   │   │   │   │   ├── 2025
# │   │   │   │   │   │   ├── 2025-01
# │   │   │   │   │   │   ├── 2025-02
# │   │   │   │   │   │   ├── 2025-03
# │   │   │   │   │   │   ├── 2025-04
# │   │   │   │   │   │   │   ├── 2025-04-01.md
# │   │   │   │   │   │   │   ├── 2025-04-02.md
# │   │   │   │   │   │   │   ├── 2025-04-03.md
# │   │   │   │   │   │   │   ├── 2025-04-23.md
# │   │   │   ├── events             <- Events management, pulls items from vault notes and external calendar into the appropriate dated "Daily events" note based on timestamp or date mention.
# │   │   ├── temp            <- Temporary files and notes.
# │   │   ├── archive             <- Archive for old notes and files.
# │   │   ├── backend           <- Backend files, scripts, resources and documentation for the system.
# │   │   │   ├── Templates           <- System templates that can be used to create items in the vault.
# │   │   │   │   ├── Notes
# │   │   │   │   │   ├── General notes - Topic_template.md
# │   │   │   │   │   ├── General notes_template.md
# │   │   │   │   │   ├── Daily note_template.md
# │   │   │   │   │   ├── Meeting note_template.md
# │   │   │   │   │   ├── Brain dump note_template.md
# │   │   │   │   │   ├── Questions_template.md
# │   │   │   │   ├── Tasks
# │   │   │   │   ├── Projects
# │   │   │   │   ├── Areas
# │   │   │   ├── System
# │   │   │   │   ├── System languages and scripts
# │   │   │   │   │   ├── bash
# │   │   │   │   │   │   ├── about_bash.bash
# │   │   │   │   │   ├── yaml
# │   │   │   │   │   │   │   ├── about_yaml.yaml
# │   │   │   │   │   ├── json
# │   │   │   │   │   │   ├── about_json.json
# │   │   │   │   │   ├── markdown
# │   │   │   │   │   │   ├── about_markdown.md
# │   │   │   │   │   ├── python
# │   │   │   │   │   │   ├── about_python.py
# │   │   │   │   │   ├── javascript
# │   │   │   │   │   │   ├── about_javascript.js
# │   │   │   │   │   ├── html
# │   │   │   │   │   │   ├── about_html.html
# │   │   │   │   │   ├── css
# │   │   │   │   │   │   ├── about_css.css
# │   │   │   │   │   ├── shell
# │   │   │   │   │   │   ├── about_shell.sh
# │   │   │   │   │   ├── sql
# │   │   │   │   │   │   ├── about_sql.sql
# │   │   │   │   │   ├── php
# │   │   │   │   │   │   ├── about_php.php
# │   │   │   │   │   ├── ruby
# │   │   │   │   │   │   ├── about_ruby.rb
# │   │   │   │   │   ├── java
# │   │   │   │   │   │   ├── about_java.java
# │   │   │   │   │   ├── c
# │   │   │   │   │   │   ├── about_c.c
# │   │   │   │   │   ├── c++
# │   │   │   │   │   │   ├── about_cpp.cpp
# │   │   │   │   │   ├── csharp
# │   │   │   │   │   │   ├── about_csharp.cs
# │   │   │   │   │   ├── go
# │   │   │   │   │   │   ├── about_go.go
# │   │   │   │   │   ├── rust
# │   │   │   │   │   │   ├── about_rust.rs
# │   │   │   │   │   ├── swift
# │   │   │   │   │   │   ├── about_swift.swift
# │   │   │   │   │   ├── kotlin
# │   │   │   │   │   │   ├── about_kotlin.kt
# │   │   │   │   │   ├── typescript
# │   │   │   │   │   │   ├── about_typescript.ts
# │   │   │   │   │   ├── r
# │   │   │   │   │   │   ├── about_r.r
# │   │   │   │   │   ├── scala
# │   │   │   │   │   │   ├── about_scala.scala