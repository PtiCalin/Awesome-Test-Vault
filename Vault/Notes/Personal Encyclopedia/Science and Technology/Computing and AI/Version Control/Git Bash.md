---
title: "Git Bash"
created: 2025-05-30
type: note
tags: [git, bash, version-control]
parent: "Version Control"
children: []
---

# Git Bash

Git Bash is a Windows application that bundles the GNU Bash shell with the Git distributed version-control system. It provides a Unix-style command-line environment on Windows so developers can run familiar Git workflows without needing a full Linux setup.

## Context

- **Git** snapshots project history as commits so changes can be tracked, branched, and collaborated on.
- **Bash** (Bourne Again SHell) is the standard command-line interpreter on many Unix systems.
- Git Bash stitches these together using the MSYS2 POSIX layer, bringing tools like `grep`, `ssh`, and `vim` to Windows while embedding the Git executable.

## Why It Matters

| Benefit            | Impact                                              |
| ------------------ | --------------------------------------------------- |
| Unified tooling    | Same Git commands work across macOS, Linux, Windows |
| Scriptability      | Bash lets you automate repetitive Git tasks         |
| Minimal footprint  | Lightweight alternative to WSL or a full VM         |
| Built-in OpenSSH   | Secure authentication to GitHub and other remotes   |

## Core Commands (Quick Glance)

| Task                    | Command                                   |
| ----------------------- | ----------------------------------------- |
| Initialise repository   | `git init`                                |
| Stage changes           | `git add <file>`                          |
| Commit snapshot         | `git commit -m "message"`                 |
| View status             | `git status -sb`                          |
| Branch management       | `git switch -c new-branch ; git merge branch` |
| Push to remote          | `git push -u origin main`                 |
| Pull with rebase        | `git pull --rebase`                       |
| Undo last commit (keep) | `git reset --soft HEAD~1`                 |
| Stash work              | `git stash push -m "wip" ; git stash pop` |

Tip: Use the up-arrow in Git Bash to cycle command history.

## Example Session

```bash
# clone a repository
$ git clone https://github.com/PtiCalin/awesome-test-vault.git
$ cd awesome-test-vault

# create a feature branch and make changes
$ git switch -c feat/encyclopedia-notes
$ echo "New entry" >> notes.md
$ git add notes.md
$ git commit -m "Add encyclopedia draft"

# push and open a pull request on GitHub
$ git push -u origin feat/encyclopedia-notes
```

## Related Concepts

- Git GUI clients (GitHub Desktop, Sourcetree)
- WSL + Git for a full Linux environment on Windows
- GitHub CLI (`gh`) for issue and PR automation
- Other shells: PowerShell, Zsh, Fish

See also: [[Git Bash Learning Module]] for step-by-step drills and an extended cheatsheet. Official references: <https://gitforwindows.org> and <https://git-scm.com>.
