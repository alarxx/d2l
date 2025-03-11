# D2L

## Python

module - file

packet - directory with files + `__init__.py`

Ссылка модуля на самого себя:
```python
current_module = sys.modules[__name__]
```

## Workflow

Install Git and Python:
```sh
apt install git
apt install python3 python3-pip python3-venv
```

Initialize local git repo:
```sh
git config --global user.name "username"
git config --global user.email email@email.com
git config --global init.defaultBranch main
git init
```

### Python Virtual Environment

Create python virtual environment:
```sh
python3 -m venv .venv
source ./venv/bin/activate
# deactivate
# pip install numpy
```

Add this environment to `.gitignore` (if it's not there already):
```sh
echo "venv/" >> .gitignore
```

freeze current environment packages:
```sh
pip freeze > requirements.txt
```

To recreate environment in future, run:
```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Updating packages in a virtual environment:
```sh
pip install --upgrade -r requirements.txt
```
But, if you added new library, then run `freeze` command.

### Git Remote Repository

```sh
git remote add <origin> <url>
git fetch

# remote name
git remote
# --verbose : fetch and push
git remote -v
# remote branches
git branch -r
# local branches
git branch -v
git branch
```

```sh
# switch
git checkout main
```
