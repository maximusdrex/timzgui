rm dist/*
python -m build
pip install --force-reinstall dist/*.whl