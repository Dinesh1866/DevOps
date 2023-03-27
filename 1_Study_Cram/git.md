# Git

Git is an Distributed open source version control system which allow us to work on different versions of the same file or to work on the histories of a file. allow us to have backup.

different types of version control system,
 1. Local VCS - in local file/server eg:filename_with_time_and_date
 2. centralized VCS - have common server and allow users to have certain code and allow user to lock the code base which they are working, but here everyone don't have whole code eg: CVS, subversion, Preforce
 3. Distributed VCS - everyone has a same updated version of code eg:Git locally and remote- GitHub, GitLab

Commands
1. git init - to initialize the local repository
2. git config --global user.email "email" - to add the user email
3. git config --global user.name "name/id" - to add the user id
4. git config --global --list - to see the added username and email
5. git remote add origin url - to add the remote repository
6. git remote -v - to check the remote repo url
7. git remote remove origin - to remove the remote repo
8. git add filename/. - to add the files to the staging area
9. git status - to see the status of the file in stagin area or files history of commits
10. git commit -m "msg" - to commit the files in staging area
11. git push -u origin main/branchname - to push the commited changes to the remote repo
12. git branch -M main - to change the master branch as main branch
13. git push --all origin - to push all the branches
14. git pull url  - to pull the remote repo to local or to pull specific remote branch to local and this will also update the local repo
15. git clone url - to have complete copy of the remote repo, mostly it will clone the main branch
16. git clone -b branchname url - to clone the exact branch we want and can also save it in name as we want
17. git fetch url - fetch all the latest changes to the repo but won't update it unlike pull
18. git pull origin main --allow-unrelated-histories - to overcome the non fast forward error
19. git log - to see all the previous commits
20. git log --online - to see logs in less format and with less id characters
21. git show commitd - to see the changes we did in the particular commit
22. git branch - to see all the local branches
23. git branch -a - to see both local and remote branches
24. git branch -C branchname - to create a new branch
25. git checkout/switch branchname - to switch between branches
26. git merge bname - to merge the given branch with the current branch
27. git merge bname -m "msg" - merge branch with cmt msg
28. git merge --no-ff bname - merge thebbranch without ff error
29. .gitignore - this file can be used for exception, if we don't want a file to be VC then use this file and mention those files inside this eg: like key, pswd
30. git checkout filename - to revert the file to previous version even if not made to staging area
31. git rm filename - to remove the file
32. git diff - shows the changes we did before staging and now
33. git diff --cached - to revert back to prev version if the file is staged
34. git restore --staged filename - to revert back after staged
35. git revert cmtid - to get back to the cmt id but will leave a history
36. git revert HEAD - to get back to the previous commit
37. git reset --hard cmtid - revert back and don't leave any history and even del histories after the id
38. ssh -keygen.exe - to generate an ssh pub and priv key
39. ssh -keygen -t rsa -C email - will create an rsa based ssh pub and private key
40. git update -git-for-windows - to update the git