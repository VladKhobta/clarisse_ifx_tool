# module for running by batch-script
import os
import sys


# parent dir for all clarisse projects
PROJECTS_DIR = r"D:\clarisse_projects"


def saving_project(app: ix.api.ClarisseApp, file_path: str) -> bool:
    return app.save_project(file_path)


# universal function for adding any scripts to the 'custom' shelf
def add_to_shelf(app, path: str,  name: str = '', description: str = ''):
    shelf = app.get_shelf()
    shelf.add_item(0, 'custom', name, description, path, )


if __name__ == "__main__":
    clarisse_app = ix.application

    # building if necessary directories structure
    full_path = PROJECTS_DIR + r"\assets\Prop\bui_a\clarisse"
    if not os.path.exists(full_path):
        os.makedirs(full_path)

    # checking if command line arguments from batch-script have passed and getting current dir with ref script
    if len(sys.argv) > 1:
        current_dir = sys.argv[1]
        add_to_shelf(clarisse_app, current_dir + r"\reference_script.py", "making reference to the picked object")

    saving_project(clarisse_app, full_path + r"\bui_a_geo_v001.project")
