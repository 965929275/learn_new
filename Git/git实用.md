git仓库与远程仓库是一一对应的

1. 在远程客户端手动创建一个仓库，eg:`test`
2. 在本地建立仓库，仓库名字嘛，emmm...最好一样吧
3. 在本地执行`git remote add origin git@github.com:965929275/test.git`
4. `git remote -v`可以查看远程仓库的信息，确认是否关联成功。
5. 将本地文件`git commit`
6. `git push -u origin master`第一次push要加参数**-u**

如此一来,test就被推送到远程仓库了,以后就可以直接`git push`了

----

删除远程仓库的文件时，不要手动删除，这样会导致本地仓库与远程仓库状态不一致。步骤如下：

1. `git pull`，保证了本地仓库的状态是一致的。
2. `git rm test.txt`删除文件
3. `git commit -m "delete"`提交
4. `git push`

这下子就删除了

撤销`git add`: `git reset`

----

编写 gitignore 文件：[如何编写 gitignore 文件](https://www.cnblogs.com/jingtyu/p/6831772.html)

