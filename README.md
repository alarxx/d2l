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

---

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

---

### Anaconda

**Зачем нужна Anaconda?**

И Anaconda и PIP являются являются менеджерами среды и пакетов.

**Conda** устанавливает предварительно скомпилированные бинарные пакеты.
С Python VENV некоторые библиотеки могут требовать компиляции или внешних C-библиотек, что отностельно долго и может быть проблемой на разных OS.

**Conda** управляет версией python, python-библиотеками и главное отличие - ==системными зависимостями==, как версия CUDA, например.

**Anaconda** идет с множеством предустановленных библиотек:
NumPy, Pandas, Matplotlib/Seaborn, Scikit-learn, TensorFlow/PyTorch.

**Miniconda**: `conda install`.

#### Miniconda
https://www.anaconda.com/docs/getting-started/miniconda/install

```sh
mkdir ~/miniconda3
cd ~/miniconda3
# wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh > miniconda.sh
# bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
bash ./miniconda.sh
rm ./miniconda.sh
```

Там потом спросят хотите ли вы, чтобы `conda` всегда автоматически инициализировалась в терминале.
Если ответил 'no' -> Manual Shell Initialization:
```sh
source ~/miniconda3/bin/activate
conda init --all # initialize on all available shells
```

Re-open terminal or run:
```sh
source ~/.bashrc
```

Теперь по умолчанию (base) environment, чтобы убрать run:
```sh
conda deactivate
```
or:
```sh
conda config --set auto_activate_base false
```
and to return:
```sh
conda activate base
```

#### Environments
https://docs.anaconda.com/working-with-conda/environments/

**Creating (transaction):**
```sh
conda create -n <ENV_NAME> python=<VERSION> <PACKAGE>=<VERSION>
```

```sh
conda create -n myenv python=3.11 numpy
```

```sh
conda info --envs # available envs
conda activate <ENV_NAME>

conda deactivate
```

**Sharing an environment**

Export env config:
```sh
conda env export > environment.yml
```

>This file handles both the environment’s pip packages and conda packages.

Creating from .yml:
```sh
conda env create -f environment.yml
```

Кажется, <ENV_NAME> должно быть уникальным для каждого проекта?
Вроде необязательно.

Странно, можно скачивать в окружении conda, как с помощью **conda**, так и с помощью **pip**, но не рекомендуется скачивать с pip, только если бинарников библиотеки нет в conda репозиториях.

Как сменить версию python:
```sh
conda uninstall python # кажется это удаляет все зависимости
conda install python=3.9
```

```sh
conda install anaconda::jupyter
```
- defaults
- conda-forge
- anaconda - поддерживаемая Anaconda Inc.

---

## Install Dependencies

```sh
conda activate myenv
pip install d2l
# https://pytorch.org/get-started
pip install torch torchvision torchaudio
```
