import sys
import re

from matplotlib.pyplot import get
 
def parse_args():
    n = len(sys.argv)
    args = {}
    if n % 2 != 1:
        print("Invalid number of arguments")
        exit(1)
    for i in range(1, n, 2):
        args[sys.argv[i].replace("-", "")] = sys.argv[i + 1]
    return args

def validateProjectName(projectName):
    if not projectName:
        print("Please enter a valid project name")
        exit(1)
    if not re.match("^[a-zA-Z]+", projectName):
        print("Invalid project name: ", projectName)
        exit(1)

def validateProjectDestination(projectDest):
    if not projectDest:
        print("Please enter a valid project path")
        exit(1)

def cleanProjectName(projectName):
    return re.sub("[^0-9a-zA-Z]+", "", projectName) 

def get_value_from_args():
    projectNameKey = 'projectName'
    projectDirKey = 'projectDir'
    args = parse_args()

    if projectNameKey not in args:
        print("Please specify the project Name: --{}=[valid_project_name]".format(projectNameKey))
        exit(1)
    projectName = cleanProjectName(args[projectNameKey])
    validateProjectName(projectName)

    if projectDirKey not in args:
        print("Please specify the project destination: --{}=[absolute_path]".format(projectDirKey))
        exit(1)
    projectDest = args[projectDirKey]
    validateProjectDestination(projectDest)

    return (projectName, projectDest)





