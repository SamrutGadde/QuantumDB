from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import Aer, execute
import numpy as np
from tabulate import tabulate


class Table:
    qc = None

    def __init__(self, tableName, cols):
        self.tableName = tableName
        self.cols = cols
        self.qc = QuantumCircuit(len(cols))
    
    def printTable(self):
        print(self.tableName)
        # print(tabulate(self.cols, headers=["Key", "Value"], tablefmt='fancy_grid'))
    
    def insert(col1, col2, val1, val2):
        pass
def main():
    table = Table("test", ["a", "b", "c"])
    table.printTable()

if __name__ == "__main__":
    main()  
