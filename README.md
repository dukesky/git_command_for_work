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



## 5.new branch

## 6.merge branch to master in local and github

## 7.merge a local clone repository to github branch/master

## 8.status check commands
### check local status
1. `git status` check what
2. ``
### check remote(github) status
1. `git ls-remote` show all remote references (pointers)  
2. `git remote show` show all remote branches

## 9.status setup commands
### setup local 

### setup remote 