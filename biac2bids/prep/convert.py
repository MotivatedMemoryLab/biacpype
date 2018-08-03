from .translation import trans_dict
from .generate_json import generate_json
from ..util.check_input import verify_data_dir,  choose_json_dir


def run_all(subjects, session, study_path, trans_file, output_path):

    msg = verify_data_dir(study_path) 
    if not msg:
        print("Error in folder check: " + msg) 
        return

    choose_json_dir(output_path)
        
    for subject in subjects:
        generate_json(subject, session, study_path + "Data/", trans_dict(trans_file, subject, study_path + "Data/"), output_path)
