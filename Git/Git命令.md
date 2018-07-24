# Git命令
1. `git config --global user.name "Your Name"`创建用户名
2. `git config --global user.email "email@example.com"`创建邮箱
3. `git init`初始化git仓库
4. `git add [filename]`将文件从工作区添加到缓存区
5. `git commit -m "description"`将文件从缓存区添加到仓库，并添加description
6. `git diff`可以查看修改内容
7. `git status`查看状态
8. `git diff HEAD -- [filename]`命令可以查看工作区和版本库里面最新版本的区别
9. `git log`查看提交的日志
10. `git reset --hard HEAD^`回退到最近一次的版本，==注意^==
11. `git reset --hard [commit id]`回退到某一版本
12. `git reflog`查看每一次命令
13. `git log --pretty=online`减少输出信息
14. `git checkout -- [filename]`可以丢弃工作区的修改，将版本库中的文件迁出
15. `git reset HEAD file`将提交到暂存区的版本丢弃
16. `rm [filename]`删除本地文件
17. `git rm [filename]`从版本库中删除文件
18. `git remote add origin git@github.com:[用户名]/learn_git.git`将本地库关联到远程库
19. `git remote rm origin`取消关联
20. `git push -u origin master`将本地库同步到远程库(第一次使用需要加`--u`以后就不用了)
21. `git clone git@github.com:[用户名]/gitskills.git`从远程库克隆到本地
22. `cat [filename]`查看文件内容
23. `git checkout -b [分支名字]`创建并切换到新分支
24. `git checkout [新分支名字]`切换分支
25. `git branch`查看当前分支
26. `git merge [新分支名字]`合并到原来的分支
27. ` git log --graph --pretty=oneline --abbrev-commit`查看分支合并情况
28. `git branch -d [分支名字]`删除分支
    `git branch -D [分支名字]`强行删除分支
29. `git merge --no-ff -m "描述" [分支名字]`表示禁用**Fast forward**合并分支
30. `vi [filename]`命令行编辑器
31. `Esc -> :wq`保存文件并推出命令行编辑器
32. `git stash`将当前的工作环境保存
33. `git stash list`查看已经保存的工作环境
34. `git stash pop`将stash删除，并恢复到原来的工作状态
35. `git stash apply stash@{0}`恢复指定的stash
36. `git remote`查看远程仓库信息
    `git remote -v`查看更详细的信息
37. `git push origin [分支名字]`推送分支到远程仓库
38. `git tag [name]`打名字为name的标签
39. `git tag`查看所有标签
40. `git tag [name] [版本号]`为历史版本打标签
41. `git show [tagname]`查看标签信息
42. `git tag -a [name] -m "description" [版本号]`为指定标签添加说明
43. `git tag -d [name]`删除标签
44. `git push origin [tagname]`推送某一标签到远程仓库
45. `git push origin --tags`一次性推送全部尚未推送到远程的本地标签
46. `git tag -d [name]`+`git push origin :refs/tags/[name]`删除远程的标签
    