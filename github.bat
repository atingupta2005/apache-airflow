git checkout main
git pull github-origin main
del .gitignore
copy .gitignore-github .gitignore
git add *
git commit -am "-"
git push github-origin main
