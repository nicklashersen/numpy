import os
#coverage_file = open("testcoverage.txt", "w+")
def init():
    #global coverage_file
    if os.path.exists("testcoverage.txt"):
        os.remove("testcoverage.txt")
    #coverage_file = open("testcoverage.txt", "w+")

def write_coverage(str):
    #global coverage_file
    coverage_file = open("testcoverage.txt", "a")
    coverage_file.write(str + '\n')
    coverage_file.close()

def coverage_file_close():
    #global coverage_file
    #coverage_file.close()
    return

