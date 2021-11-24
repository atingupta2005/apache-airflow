git checkout am1
git pull gitlab-origin am1
del .gitignore
copy .gitignore-gitlab .gitignore
git add *
git commit -am "-"
git push gitlab-origin am1