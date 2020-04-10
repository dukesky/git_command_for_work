# Git and Github Practice on project use

## 1.create a project
To create a project, we need to create two part: 
1. local repository
2. github repository
and linked them by 
open command shell and go to your local project folder and type：
`git init` to initate git
`git add .` to add all files in this folder to git
`git commit -m "write things you want to commit here"`
`git remote add origin https://github.com/username/projectname.git`
then you can check if you typeing github url correctly by typeing:
`git remote -v`
if everything goes well, you can push your code to github now, by typeing
`git push origin master`

## 2.link an exsiting project to github
You may already have a pretty good project and you want to upload to github, in that condition, you can do:
1. create a repository in github by click the top bar '+' icon --> 'New repository' and give your project name and distription and click create repository
2. copy the HTTP url in the top Quick setup such as `https://github.com/dukesky/git_command_for_work.git`
3. go to your local project dir, open command shell type:
`git init` to initate git
`git add .` to add all files in this folder to git
`git commit -m "write things you want to commit here"`
`git remote add origin https://github.com/dukesky/git_command_for_work.git` of course your url
`git push origin master`

job done!