# module for running by batch-script
import os

# parent dir for all clarisse projects
PROJECTS_DIR = r"D:\clarisse_projects"


def saving_project(app: ix.api.ClarisseApp, file_path: str) -> bool:
    return app.save_project(file_path)


if __name__ == "__main__":
    clarisse_app = ix.application

    # building if necessary directories structure
    full_path = PROJECTS_DIR + r"\assets\Prop\bui_a\clarisse"
    if not os.path.exists(full_path):
        os.makedirs(full_path)

    saving_project(clarisse_app, full_path + r"\bui_a_geo_v001.project")
