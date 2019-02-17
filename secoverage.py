coverage_file = open("testcoverage.txt", "w+")
def init():
    global coverage_file
    #coverage_file = open("testcoverage.txt", "w+")

def write_coverage(str):
    global coverage_file
    coverage_file.write(str + '\n')

def coverage_file_close():
    global coverage_file
    coverage_file.close()

