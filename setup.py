from dataclasses import replace
from git import Repo
import os


# clone the template repo
# repo = Repo.clone_from("https://github.com/jknair0/AppTemplate.git", projectDest)
# todo remove .git folder

class ApplicationSetup:

    src_package_relative_path = "app/src/main/java/tech/jknair/app"
    application_file = "app/src/main/java/tech/jknair/mistyproject/ui/App.kt"
    template_files_relative_paths = [
        "settings.gradle", 
        "app/build.gradle"
    ]
    
    def __init__(self, projectName, projectDest):
        self.projectName = projectName
        self.projectDest = projectDest
        self.app_folder = os.path.join(self.projectDest, "app")
        self.projectNameLower = projectName.lower()
    
    def run(self):
        self.__replace_in_templates()

    def __replace_in_templates(self):
        self.__replace_project_name()
        self.__change_project_file_names()

    def __replace_project_name(self):
        for file in self.template_files_relative_paths:
            self.__replace_project_name_in_file(file)
        print(self.app_folder)
        for root, subdirs, files in os.walk(self.app_folder):
            print(root)
            
    def __replace_project_name_in_file(self, file):
        file_path = os.path.join(self.projectDest, file)
        print("updating file at ", file_path)
        with open(file_path, 'r') as fr:
            file_content = fr.read()
        updated_file_content = file_content.replace("##projectName##", self.projectName).replace("##project_name##", self.projectNameLower)
        with open(file_path, 'w') as fw:
            fw.write(updated_file_content)
    
    def __change_project_file_names(self):
        self.__change_application_class_name()
        self.__change_package_name_post_fix()
    
    def __change_package_name_post_fix(self):
        srcPackage = os.path.join(self.projectDest, self.src_package_relative_path)
        if (os.path.exists(srcPackage)):
            os.rename(srcPackage, os.path.join(projectDest, "app/src/main/java/tech/jknair/" + self.projectNameLower))
    
    def __change_application_class_name(self):
        application_file_path = os.path.join(self.projectDest, self.application_file)
        if (os.path.exists(application_file_path)):
            destination = os.path.join(self.projectDest, "app/src/main/java/tech/jknair/mistyproject/ui/"+self.projectName+"App.kt")
            os.rename(application_file_path, destination)
    

projectName =  "MistyProject"
projectDest = "/Users/jayakrishnannairkaarakulangara/testTrash/MistyProject"

ApplicationSetup(projectName, projectDest).run()


