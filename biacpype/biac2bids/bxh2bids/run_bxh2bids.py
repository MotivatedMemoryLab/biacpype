from .bxh2bids import multi_bxhtobids
import os
import json


def run(hopes_dreams_file):
    """Convert data to BIDS format.

    params:
        -hopes_dreams_file: the path to the hopes_dreams json file (if you used auto json generation, it 
            would be in the your json output path)
    """
    with open(hopes_dreams_file) as fd:
        hopes_dreams = json.loads(fd.read())

    source_study_dir = hopes_dreams['source_study_dir']
    target_study_dir = hopes_dreams['target_study_dir']
    ses_info_dir = hopes_dreams['ses_info_dir']
    ses_files = hopes_dreams['ses_files']
    to_run = list(ses_files.keys())
    log_dir = hopes_dreams['log_dir']

    bad_data = []
    good_data = []
    for unique_id in to_run:
        dataid = unique_id
        ses_info_file = os.path.join(ses_info_dir, hopes_dreams['ses_files'][dataid])
        with open(ses_info_file) as fd:
            ses_dict = json.loads(fd.read())
        try:
            multi_bxhtobids(dataid, ses_dict, source_study_dir, target_study_dir, log_dir)
            good_data.append(dataid)
        except Exception as ex:
            print('Data set failed to run: '+str(dataid))
            print(ex)
            bad_data.append(dataid)

    print('Data that ran: '+str(good_data))
    print('Data that did NOT run: '+str(bad_data))
