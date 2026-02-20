winget install --id Python.Python.3 --exact --silent --accept-package-agreements --accept-source-agreements

PYTHON_BASE="/c/Users/$USERNAME/AppData/Local/Programs/Python"
PYTHON_DIR="$(ls -d "$PYTHON_BASE"/Python3*/ | head -n 1)"
export PATH="$(ls -d $PYTHON_DIR/Python3*/ | head -n 1):$PATH"

python -m pip install --upgrade pip


curl -fsSL https://raw.githubusercontent.com/Louchatfroff/VORTEX-AUTOUNNATENDED/refs/heads/autunnatended/requirements.txt
pip install -r requirements.txt

curl -fsSL https://raw.githubusercontent.com/Louchat/VORTEX/refs/heads/main/VORTEX.py -o VORTEX.py
python VORTEX.py
