from file_utils import join_path, list_recursively, delete_recursive, exists, rename
from git_utils import clone_repo
from log_utils import log

class ApplicationSetup:

    src_package_relative_path = "app/src/main/java/tech/jknair/app"
    application_file = "app/src/main/java/tech/jknair/app/ui/App.kt"
    projectNameTemplate = "##projectName##"
    projectNameLowerTemplate = "##project_name##"
    valid_file_exts = ["xml", "java", "kt", "kts", "gradle"]
    
    def __init__(self, projectName, projectDest):
        self.projectName = projectName
        self.projectNameLower = projectName.lower()
        self.projectDest = projectDest
    
    def run(self):
        self.__replace_project_name_in_files()
        self.__change_file_dir_names()

    def __replace_project_name_in_files(self):
        for file_path in list_recursively(self.projectDest):
            self.__replace_project_name_in_file(file_path)
            
    def __replace_project_name_in_file(self, file_path):
        splits = file_path.split(".")
        if splits[-1] not in self.valid_file_exts:
            log("ignoring file: " + file_path)
            return
        # log("checking file: " + file_path)
        with open(file_path, 'r') as fr:
            file_content = fr.read()
        updated_file_content = self.__replace_templates(file_content) 
        with open(file_path, 'w') as fw:
            fw.write(updated_file_content)
    
    def __replace_templates(self, file_content):
        updated_file_content = file_content
        updated_file_content = file_content.replace(self.projectNameTemplate, self.projectName)
        updated_file_content = updated_file_content.replace(self.projectNameLowerTemplate, self.projectNameLower)
        return updated_file_content
    
    def __change_file_dir_names(self):
        self.__change_file_names()
        self.__change_dir_names()
        
    def __change_file_names(self):
        self.__change_application_class_name()

    def __change_dir_names(self):
        self.__change_package_name_post_fix()

    def __change_package_name_post_fix(self):
        srcPackage = join_path(self.projectDest, self.src_package_relative_path)
        rename(srcPackage, join_path(projectDest, "app/src/main/java/tech/jknair/" + self.projectNameLower))
    
    def __change_application_class_name(self):
        application_file_path = join_path(self.projectDest, self.application_file)
        destination = join_path(self.projectDest, "app/src/main/java/tech/jknair/app/ui/"+self.projectName+"App.kt")
        rename(application_file_path, destination)

projectName =  "MistyProject"
projectDest = "/Users/jayakrishnannairkaarakulangara/testTrash/MistyProject"
template_repo_link = "https://github.com/jknair0/AppTemplate.git"

clone_repo(template_repo_link, projectDest)

git_root = join_path(projectDest, ".git")
delete_recursive(git_root)
idea_root = join_path(projectDest, ".idea")
delete_recursive(idea_root)

ApplicationSetup(projectName, projectDest).run()


