# Git and Github Practice on project use

## 1.create a project in local PC and github
To create a project, we need to create two parts: 
1. local repository
2. github repository \
and linked them by 
open command shell and go to your local project folder and type： \
`git init` to initate git \
`git add .` to add all files in this folder to git \
`git commit -m "write things you want to commit here"` to commit \
`git remote add origin https://github.com/username/projectname.git` to link local git to remote repository\
then you can check if you typeing github url correctly by typing:\
`git remote -v`\
if everything goes well, you can push your code to github now, by typing:\
`git push origin master`  

## 2.link an exsiting local project to github
You may already have a pretty good project and you want to upload to github, in that condition, you can do: 
1. create a repository in github by click the top bar `+` icon --> `New repository` and give your project name and distription and click create repository
2. copy the HTTP url in the top Quick setup such as `https://github.com/dukesky/git_command_for_work.git`
3. go to your local project dir, open command shell type: \
`git init` \
`git add .` \
`git commit -m "write things you want to commit here"`\
`git remote add origin https://github.com/your_account/your_project.git` \
`git push origin master`

job done!

## 3.commit change in local to github
After we change some code in local repository, we may want to update to github, in command line, go to project folder, input \
`git status` to check what has been changed since last commit \
`git add .` to add all changed file, also can use `git add file_name` to add single file \
`git commit -m "write what you want to describe this commit"` \
`git push origin master` to push to github master branch

## 4.backward and forward version in local and github
we you have some committed your work several time, you may find something wrong and want to trace back to previous version, use `git checkout`

``

## 5.Clone a github project to local


## 6.add new branch

to setup remote branch, we can use upstream, checkout to branch, and: \
`git push -u origin branch` to push local branch to remote new branch with name "branch"

## 7.merge branch to master in local and github


### merge local branch to remote when remote master also change


## 8.merge a local clone repository to github branch/master


## status check commands
### check local status
1. `git status` check which file has been changed since last commit (remember to save file before check)
2. `git diff branch1..branch2` check difference between two branch : \
3. `git log` show commit history `git log --oneline` show commit history each commit in one line (shorter version) \
4. `git branch` check what branches are in local and which is current branch, `git branch -vv` for more details \


### check remote(github) status
1. `git ls-remote` show all remote references (pointers)  
2. `git remote show` show all remote branches



## status setup commands
### setup local 
1. `git config --global alias.variablename "command you want to write down"` set git variable, then you can use it by `git variablename` 

### setup remote 
1. `git push --set-upstream <remote> <branch>` or `git push -u <remote> <branch>` setup upstream branch
2. `git checkout --track origin/branch` create a new local branch and link to existing remote branch (origin/branch)
3. `fir branch -u <remote>/<branch>` link an existing local branch to remote branch (origin/branch)