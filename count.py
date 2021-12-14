git clone https://github.com/soothingzsx/demo-repo.git

#change the path
cd demo-repo

#count the .py file
git ls-files "./*.py" | wc -l

#count the lines seperately 
git ls-files | xargs wc -l

