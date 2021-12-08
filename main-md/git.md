# git
![Git Logo by Jason Long is licensed under the Creative Commons Attribution 3.0 Unported License.](../img/git.png)

git is a version control system.

## Usage
- git [options]

## Examples
- **git config --global -e** Edit the user configuration for git.
- **git init .** Initialize a repository in the root folder.
- **git clone [remote]** Clone a remote repository.
- **git add .** Start tracking all of the files of the repository.
- **git commit -a -m "*message*"** Create a commit, automatically staging all
changes of tracked files.
- **git commit -m "*message*"** Create a commit with all of the staged changes
of tracked files.
- **git log** Shows commit logs. 
- **git push [remote]** Pushes to a remote name or URL. 
- **git pull [remote]** Pulls from a remote name or URL. 
- **git reset --soft HEAD~1** Soft reset to the latest git commit. 
- **git reset --hard HEAD~1** Hard reset to the latest git commit.
- **git reset [file]** Unstage a file.
- **git rm [file]** Stages removing a file and removes it locally. 
- **git rm --cached [file]** Stages removing a file and keeps it locally. 
- **git remote add [name] [url]** Assign a remote repository to a name. 
- **git remote rm [name] ** Remove an assigned remote repository. 
- **git restore [file(s)]** Unstage uncommitted changes (irreversible). 
- **git restore --staged [file(s)]** Undo a git add. 
- **git status** Shows the working tree status. 
- **git update-index --assume-unchanged [path]** Tells git to stop checking for
changes in file(s). 
- **git update-index --skip-worktree [path]** Tells git you want your own
version of file(s); don't overwrite production. 
- **git update-ref -d HEAD** Deletes an initial commit (soft). You can also
delete the .git directory (hard). 
- **git diff [a] [b]** Find the differences between two files and produce a git
diff output. The first file is the less recent file, and the second file is the
more recent file. Should be used in conjunction with applying patches. 
- **git apply [patch]** Apply a patch file.
    The header states the files getting changed. Changes present in b (recent)
    are meant to be applied to a (older). After application, a gets removed if
    it has a different file name, and b is the file that gets changed. Make both
    files have the same name for ease.

## Tips
- Use .gitignore to make git ignore specific files.
- Hooks can be added to a repository.

## Source code
git is in development. You can view its source code
[here.](https://github.com/git/git)

*Page added on 2021-10-07, last edited on: 2021-10-11*

