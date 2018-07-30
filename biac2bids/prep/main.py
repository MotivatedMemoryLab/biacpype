from translation import trans_dict
from generate_json import generate_json

def main():

    print("### generating json files ###")
    data_path = input("Please enter the path to the Data folder, finishing with / (e.g. /Users/lpjiang/....../Study/Data/): ")
    subject = input("Please enter subject number: ")
    session = input("Please enter session number: ")
    trans_file = input("Please enter the file name which contains task code: ")
    trans_d = trans_dict(trans_file, subject, data_path)
    output_path = input("Please enter the path to save the json file: ")

    generate_json(subject, session, data_path, trans_d, output_path)


main()


