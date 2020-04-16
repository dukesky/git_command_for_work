# Git and Github Practice on project use

## why this?
In my first work with git, I feel confused frequently. Even though I study some online course about git and github, and I believe I'm clear with basic git and github conception such as branch, merge, pull, push, remote, etc, problems keep coming up in real world use of git, expecially when I'm in charge of a production, which has multiple stages(production, dev, new_feature, etc), so I need to switch from stage to stage, from version to version to meet production and development requirement. So I thought why don't I conculde how to use git in practice and list some real world scenario that every software engineer may face in their work.  Hope it help me to clear my mind and help readers like you.

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
When you have committed your work several time, you may want to trace back to previous version, use `git checkout` \
To go back to a specific previous step, can use `git log` to see previous commit record, and copy the [SHA-1] code, then use this code by: \
`git checkout <SHA-1>`\
To jump to step of this commit.

## 5.Clone a github project to local
To clone a github repo to local, you can run:\
`git clone https://github.com/user_name/repo_name.git` \
If you want to clone a specific branch, you can run:\
`git clone -branch <branch_name> https://github.com/user_name/repo_name.git`

## 6.work with branch
### create a new branch
To create a new branch, simple with:\
`git branch <new_branch_name>`
Or you can go with:\
`git checkout <new_branch_name>` \
witch will create a new branch if git not detect the input branch name and switch to this branch
### push branch to github
When you have some work on a new branch, you may want to:
#### 1.push existing branch to github
This is easy, simply:\
`git push <remote> <branch>`
#### 2.push new branch to github
This is the same as add a new branch to github. To setup remote branch, we can use upstream. First checkout to branch, and: \
`git push -u <remote> <branch>` to push local branch to remote new branch with name <branch>

#### 3.push branch to another remote branch
`git push <remote> <local_branch>:<remote_branch>`
### delete branch
If you want to delete a branch, use:\
`git branch -d <branch_name>`
If you want to delete remote branch:\
`git push <remote> --delete <delete_branch_name>` 



## 7.merge branch to master in local 


### merge local branch to remote when remote master also change


## 8.merge a local clone repository to github branch/master

## 9.merge a local download repo to github (local don't share same commit history)

## 10.branch change
1. [Cherry-pick](https://git-scm.com/docs/git-cherry-pick)
Cherry-pick apply some change introduced by existing commits
2. 


## rebate



## status check commands
### check local status
1. check which file has been changed since last commit (remember to save file before check) \
 `git status`
2.  check difference between two branch : \
`git diff branch1..branch2`
3. show commit history or show commit history each commit in one line (shorter version) \
`git log` or `git log --oneline` 
4. check what branches are in local and which is current branch, or for more details \
 `git branch` or `git branch -vv`


### check remote(github) status
1. show all remote references (pointers)  \
`git ls-remote` 
2. show all remote branches \
`git remote show`



## status setup commands
### setup local 
1.  set git variable \
`git config --global alias.variablename "command you want to write down"`\
, then you can use it by \
 `git variablename` 
2. delete local branch \
`git branch -d localBranchName`

### setup remote 
1. setup upstream branch \ 
`git push --set-upstream <remote> <branch>` or `git push -u <remote> <branch>` 
2. create a new local branch and link to existing remote branch (origin/branch)\
`git checkout --track origin/branch` 
3. link an existing local branch to remote branch (origin/branch)\
`fir branch -u <remote>/<branch>`
4. delete remote branch\
`git push origin --delete remoteBranchName`

## reference
[git document](https://git-scm.com/book/en/v2) official git guide
[Bitbucket](https://www.atlassian.com/git/tutorials): It is a tutorial appeared frequently in my git search, it has clear guide and detail example to illustrate git problems if you don't want spend too much time on git document