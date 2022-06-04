from log_utils import log
from git import Repo
from file_utils import exists

def clone_repo(repository_link, dest_dir):
    if exists(dest_dir):
        log("not cloning. the directory is not empty " + dest_dir)
        return
    log("cloning from {} to {}".format(repository_link, dest_dir))
    Repo.clone_from(repository_link, dest_dir)