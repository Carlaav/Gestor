import sys

DATABASE_PATH = r"datos\clientes.csv"

if "pytest" in sys.argv[0]:
    DATABASE_PATH = r"datos\clientes_test.csv"
