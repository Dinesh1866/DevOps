# GIT
Git is a distributed version control system for tracking changes in source code during software development. It is designed for coordinating work among programmers, but it can be used to track changes in any set of files. Its goals include speed, data integrity, and support for distributed, non-linear workflows.

## Git Commands

### Git Config

```bash
# Git Config
# git config --global user.name "John Doe"
# git config --global user.email
# git config --global core.editor "code --wait"
# git config --global color.ui true
# git config --global alias.co checkout
# git config --global alias.br branch
# git config --global alias.ci commit
# git config --global alias.st status
# git config --global alias.unstage 'reset HEAD --'
# git config --global alias.last 'log -1 HEAD'
# git config --global alias.visual '!gitk'
# git config --global alias.graph "log --graph --decorate --pretty=oneline --abbrev-commit --all"
# git config --global alias.graph2 "log --graph --decorate --pretty=oneline --abbrev-commit --all --branches"
```

### Git Init

```git
git init
git init --bare
```

### Git Status
      
      ```git
      git status
      git status -s
      git status -s -b
      git status -s -b -u
      git status -s -b -uall
      git status -s -b -uall --ignored
      ```

### Git Add
      
      ```git
      git add .
      git add -A
      git add -u
      git add -p
      git add -i
      git add --all
      git add --update
      git add --patch
      git add --interactive
      git add --ignore-removal
      git add --ignore-errors
      git add --renormalize
      git add --chmod=+x
      ```

### Git Commit
      
      ```git
      git commit -m "message"
      git commit -a -m "message"
      git commit -v
      git commit -a -v
      git commit -a -v -m "message"
      git commit -a -v -m "message" --amend
      git commit -a -v -m "message" --amend --no-edit
      git commit -a -v -m "message" --amend --no-edit --allow-empty
      git commit -a -v -m "message" --amend --no-edit --allow-empty --no-verify
      git commit -a -v -m "message" --amend --no-edit --allow-empty --no-verify --no-gpg-sign
      git commit -a -v -m "message" --amend --no-edit --allow-empty --no-verify --no-gpg-sign --date="2021-01-01 00:00:00"
      ```

### Git Log
      
      ```git
      git log
      git log --oneline
      git log --oneline --decorate
      git log --oneline --decorate --graph
      git log --oneline --decorate --graph --all
      git log --oneline --decorate --graph --all --branches

      git log --oneline --decorate --graph --all --branches --since="2021-01-01 00:00:00"
      git log --oneline --decorate --graph --all --branches --since="2021-01-01 00:00:00" --until="2021-01-01 00:00:00"
      git log --oneline --decorate --graph --all --branches --since="2021-01-01 00:00:00" --until="2021-01-01 00:00:00" --author="John Doe"
      ```

### Git Show
      
      ```git
      git show
      git show HEAD
      git show HEAD~1
      git show HEAD~2
      ```

### Git Diff
      
      ```git
      git diff
      git diff --staged
      git diff --cached
      git diff --name-only
      git diff --name-status
      git diff --name-status --cached
      git diff --name-status --staged
      git diff --name-status --cached --ignore-submodules
      git diff --name-status --staged --ignore-submodules
      git diff --name-status --cached --ignore-submodules --ignore-space-at-eol
      git diff --name-status --staged --ignore-submodules --ignore-space-at-eol
      ```

### Git Reset
      
      ```git
      git reset
      git reset --soft
      git reset --mixed
      git reset --hard
      git reset --merge
      git reset --keep
      git reset --patch
      git reset --recurse-submodules
      git reset --recurse-submodules=on-demand
      ```

### Git Checkout
      
      ```git
      git checkout
      git checkout -- .
      git checkout -- <file>
      git checkout -- <file> <file>
      git checkout -- <file> <file> <file>
      git checkout -- <file> <file> <file> <file>
      ```

### Git Branch
      
      ```git
      git branch
      git branch -a
      git branch -r
      git branch -v
      git branch -vv
      git branch -vvv
      git branch -vvvv
      ```

### Git Tag
      
      ```git
      git tag
      git tag -l
      git tag -l "v1.8.5*"
      git tag -l "v1.8.5*" --points-at HEAD
      git tag -l "v1.8.5*" --points-at HEAD --contains 2b9d75c
      git tag -l "v1.8.5*" --points-at HEAD --contains 2b9d75c --merged
      git tag -l "v1.8.5*" --points-at HEAD --contains 2b9d75c --merged --no-merged
      git tag -l "v1.8.5*" --points-at HEAD --contains 2b9d75c --merged --no-merged --column
      git tag -l "v1.8.5*" --points-at HEAD --contains 2b9d75c --merged --no-merged --column --sort=-creatordate
      ```

### Git Merge
      
      ```git
      git merge
      git merge --no-ff
      git merge --no-ff --no-commit
      git merge --no-ff --no-commit --no-edit
      git merge --no-ff --no-commit --no-edit --no-verify
      git merge --no-ff --no-commit --no-edit --no-verify --no-gpg-sign
      git merge --no-ff --no-commit --no-edit --no-verify --no-gpg-sign --allow-unrelated-histories
      git merge --no-ff --no-commit --no-edit --no-verify --no-gpg-sign --allow-unrelated-histories --allow-empty
      git merge --no-ff --no-commit --no-edit --no-verify --no-gpg-sign --allow-unrelated-histories --allow-empty --no-edit
      git merge --no-ff --no-commit --no-edit --no-verify --no-gpg-sign --allow-unrelated-histories --allow-empty --no-edit --no-verify
      git merge --no-ff --no-commit --no-edit --no-verify --no-gpg-sign --allow-unrelated-histories --allow-empty --no-edit --no-verify --no-gpg-sign
      ```

### Git Rebase
      
      ```git
      git rebase
      git rebase --interactive
      git rebase --interactive --root
      git rebase --interactive --root --autosquash
      git rebase --interactive --root --autosquash --no-ff
      git rebase --interactive --root --autosquash --no-ff --no-verify
      ```

### Git Cherry-Pick
      
      ```git
      git cherry-pick
      git cherry-pick --no-commit
      git cherry-pick --no-commit --no-edit
      git cherry-pick --no-commit --no-edit --no-verify
      ```

### Git Revert
      
      ```git
      git revert
      git revert --no-commit
      git revert --no-commit --no-edit
      git revert --no-commit --no-edit --no-verify
      ```

### Git Clean
      
      ```git
      git clean
      git clean -f
      git clean -f -d
      git clean -f -d -x
      git clean -f -d -x -n
      git clean -f -d -x -n -e <file>
      git clean -f -d -x -n -e <file> -e <file>
      ```

### Git Stash
      
      ```git
      git stash
      git stash list
      git stash list --stat
      git stash list --stat --patch
      git stash list --stat --patch --no-abbrev

      git stash show
      git stash show --stat
      git stash show --stat --patch


      git stash apply
      git stash apply --index
      git stash apply --index --patch
      git stash apply --index --patch --stat
      git stash apply --index --patch --stat --no-abbrev

      git stash pop
      git stash pop --index
      git stash pop --index --patch
      git stash pop --index --patch --stat
      git stash pop --index --patch --stat --no-abbrev

      git stash drop
      git stash drop --index
      git stash drop --index --patch
      git stash drop --index --patch --stat
      git stash drop --index --patch --stat --no-abbrev

      git stash clear
      git stash clear --index
      git stash clear --index --patch

      git stash branch
      git stash branch --index
      git stash branch --index --patch

      git stash save
      git stash save --index
      git stash save --index --patch

      git stash create
      git stash create --index
      git stash create --index --patch

      git stash store
      git stash store --index
      git stash store --index --patch
      ```

      

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

## fork
to create a copy of a repository from remote repository to your own remote repository



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


## SSH
ssh stands for secure shell. it is a protocol that allows you to securely connect to a remote computer. it is used to connect to a remote server and execute commands on it. it is also used to transfer files between the local computer and the remote server.

this will allow securec connection to the remote server. and will not ask for username and password everytime you push or pull.

RSA means Rivest–Shamir–Adleman. it is an algorithm used by modern computers to encrypt and decrypt messages. it is an asymmetric cryptographic algorithm. it is one of the first public-key cryptosystems and is widely used for secure data transmission. in simple words, it is a way to encrypt and decrypt messages. it is used to generate a public and private key pair. the public key can be given to anyone and the private key must be kept secret. the public key is used to encrypt the message and the private key is used to decrypt the message.

### generate ssh key
```git
ssh-keygen -t rsa -C email"

### generate ssh key
```git
ssh-keygen -t rsa -b 4096 -C "
```

### add ssh key to ssh-agent
```git
eval "$(ssh -agent -s)"
```

### add ssh key to ssh-agent
```git
ssh-add ~/.ssh/id_rsa
```

### copy ssh key to clipboard
```git
clip < ~/.ssh/id_rsa.pub
```

### copy ssh key to clipboard
```git
pbcopy < ~/.ssh/id_rsa.pub
```

### copy ssh key to clipboard
```git
xclip -sel clip < ~/.ssh/id_rsa.pub
```