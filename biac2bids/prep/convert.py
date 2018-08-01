from translation import trans_dict
from generate_json import generate_json



def run_all(subjects, session, study_path, trans_file, output_path):
    for subject in subjects:
        generate_json(subject, session, study_path + "Data/", trans_dict(trans_file, subject, study_path + "Data/"), output_path)



def main():
    print("### generating json files ###")
    # study_path = input("Please enter the path to the Study folder: ")
    # subjects = input("Please enter subjects, separately by commas: ")
    # subjects = [subject for subject in subjects.split(",")]
    # session = input("Please enter session number: ")
    # trans_file = input("Please enter the file name which contains task code: ")
    # output_path = input("Please enter the path to save the json file: ")

    run_all(
        ["19338", "19492", "19497", "19589", "19671"], 
        "", 
        "/Users/lpjiang/Research/CBT/", 
        "series_order_note.txt", 
        "/Users/lpjiang/Research/CBT/JSONS/")




main()


