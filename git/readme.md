# GIT

## Clone
to create a copy of codes from remote repository to local repository

```git 
git clone <remote repository url>
```
> git clone will clone the repository to the current directory and create a new folder with the name of the repository. 

> this will clone from the defualt branch i.e: master/main and this will initialize the local repository with the remote repository. and also create a remote branch called origin. and add remote origin url to the local repository.

### Clone specific branch
to clone a specific branch from the remote repository

```git 
git clone -b <branch name> <remote repository url>
```
or
```git
git clone <remote repository url> -b <branch name>
```

### clone to specific folder
to clone the repository to a specific folder

```git
git clone <remote repository url> <folder name>
```

### clone to specific branch and folder
to clone a specific branch to a specific folder

```git
git clone -b <branch name> <remote repository url> <folder name>
```
or
```git
git clone <remote repository url> -b <branch name> <folder name>
```


### Clone specific folder
to clone a specific folder from the remote repository

```git
git clone --single-branch --branch <branch name> --depth 1 <remote repository url> <folder name>
```



## fetch
```git
git fetch origin
```
or 
```git
git fetch origin <branch name>
```
> git fetch will fetch the latest changes from the remote repository. and will not merge the changes to the local repository.


## pull
```git
git pull origin
```
or 
```git
git pull origin <branch name>
```

> git pull will fetch/retrive the latest changes from the remote repository and will merge the changes to the local repository.



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

### merge a branch 
```git
git merge --no-ff <branch_name>
```
> * --no-ff is a flag that tells git to always create a merge commit when merging two branches. By default, git merges using a fast-forward if possible. A fast-forward merge is when the tip of the current branch is set to point to the tip of the merged branch. This is only possible if the merged branch was a descendant of the current branch. If the current branch and the merged branch have diverged, git will not perform a fast-forward merge. Instead, it will create a new merge commit.

> fast-forward merge is a special case of a merge where the target branch was already a descendant of the current branch. In this case, there is no need to create a new commit object – the current branch pointer can simply be moved forward to point to the same commit as the target branch.

> decent explanation of fast-forward merge: https://www.atlassian.com/git/tutorials/using-branches/git-merge



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
