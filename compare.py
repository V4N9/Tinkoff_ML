import numpy
import ast
import argparse
import sys


# PARAMS
POINTS = {
    "SAME_IMPORT_POINT": 0.01,
    "": 0.005
}

MAX_DISTANCE = 1e+9


class ImportChecker(ast.NodeVisitor):
    '''
    Gathers names of all modules
    '''

    def __init__(self) -> None:
        super().__init__()
        self.modules = []

    def visit_Import(self, node: ast.Import) -> None:
        # add names of the imported modules
        self.modules.extend(list(map(lambda x: x.name, node.names)))

        # return super().generic_visit(node)


class FunctionChecker(ast.NodeVisitor):
    pass


class ForLoopChecker(ast.NodeVisitor):
    pass


class ForLoopChecker(ast.NodeVisitor):
    pass


class Comparator():
    '''
    This class compare two given files by different syntax structures (imports, functions, classes, e.t.c)
    '''

    def __init__(self, filename1: str, filename2: str) -> None:
        self.filename1 = filename1
        self.filename2 = filename2
        self.import_points = 0
        self.function_points = 0

    def compare_files(self) -> float:
        result_similarity_score = MAX_DISTANCE

        # Read from two files
        with open(file=self.filename1, mode='r') as file:
            first_file = ast.parse(
                source=file.read(),
                filename=self.filename1
            )

        with open(file=self.filename2, mode='r') as file:
            second_file = ast.parse(
                source=file.read(),
                filename=self.filename2
            )

        # TODO: implement comparing through different syntax structures
        return self.compute_import_similarity(first_file, second_file)

    def compute_import_similarity(self, first: ast.Module, second: ast.Module) -> float:
        ic1 = ImportChecker()
        ic1.visit(first)

        ic2 = ImportChecker()
        ic2.visit(second)

        return len(set(ic1.modules) & set(ic2.modules)) * POINTS["SAME_IMPORT_POINT"]

    def compute_function_similarity(self, func1, func2) -> float:
        pass


def main() -> None:
    ''' 
    This function open and read first file and write scores from comparing files in second file line by line    
    '''
    input_filename = sys.argv[1]
    scores_filename = sys.argv[2]

    with open(file=input_filename, mode="r") as input_file, open(file=scores_filename, mode="w") as scores_file:

        for line in input_file:
            first_filename, second_filename = line.split()
            comp = Comparator(first_filename, second_filename)

            score = comp.compare_files()

            scores_file.write(f"{score}\n")


def lev_dist(str1: str, str2: str) -> int:
    pass


def print_module(module: ast.Module) -> None:
    print(ast.dump(node=module, indent=4))


if __name__ == '__main__':
    main()
