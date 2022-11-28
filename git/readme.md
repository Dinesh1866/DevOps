# GIT

## branch
branching is a way to work on different versions of a repository at one time.

### just create a new branch
```git
git branch <branchname>
```

### show all branches
```git
git branch
```
> * the current branch is marked with an asterisk (*) i.e: show all the local branches
with higlighting the branch in use (current branch) in green and others in white

### show all branches and the current branch
```git
git branch -a
```
> * the current branch is marked with an asterisk (*) i.e: show all the local and remote branches

### show branch with last commit
'''git
git show-branch
'''
> show-branch is a command that shows the commit history of a branch. It is similar to git log, but it shows the commit history in a tree format.




### command to create a branch and switch to it
```git 
git checkout -b <branch_name>
```

### command to push a branch
```git
git push origin <branch_name>
```

### command to delete a branch
```git
git branch -d <branch_name>
```

### command to delete a remote branch
```git
git push origin --delete <branch_name>
```

### command to merge a branch
```git
git merge <branch_name>
```

### command to merge a branch with a commit message
```git
git merge <branch_name> -m "<commit_message>"
```

### command to merge a branch with a commit message and squash
```git
git merge <branch_name> -m "<commit_message>" --squash
```

### command to merge a branch with a commit message and squash and rebase
```git
git merge <branch_name> -m "<commit_message>" --squash --rebase
```

### command to merge a branch with a commit message and squash and rebase and push
```git
git merge <branch_name> -m "<commit_message>" --squash --rebase && git push
```

### command to merge a branch with a commit message and squash and rebase and push to a remote branch
```git
git merge <branch_name> -m "<commit_message>" --squash --rebase && git push origin <branch_name>
```

### command to merge a branch with a commit message and squash and rebase and push to a remote branch and delete the local branch
```git
git merge <branch_name> -m "<commit_message>" --squash --rebase && git push origin <branch_name> && git branch -d <branch_name>
```

### switch to a branch
```git
git checkout <branch_name>
```

### switch to a branch and create it if it doesn't exist
```git
git checkout -b <branch_name>
```

### rename a branch
```git
git branch -m <old_branch_name> <new_branch_name>
```
