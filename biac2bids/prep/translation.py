def trans_dict(filename, subject, data_path, delimiter="\t", header=0):
    """Given filename, translate code to task name.

    Expect the file to be in format (| is the delimiter)
    Code | Task
    -----------
      4  |  train
      ........

    Note: we expect the file to be in folder ....../Data/func/<subject>/<filename>
    
    params:
        - filename: file name
        - subject: subject number
        - data_path: the path to Data folder
        - delimiter: delimiter for the file (default to tab)
        - header: the number of lines to skip for header
    returns: a translation dict
    """
    with open(data_path + "func/" + subject + "/" + filename, "r") as f:
        for _ in range(header):
            f.readline()
        d = dict()
        for line in f:
            line = line.rstrip()
            # not empty line
            if line != "":
                info = line.split(delimiter)
                d[info[0]] = info[1]
    return d



def parse_task_and_run(filename, trans_dict=None, delimiter="_"):
    """Parse a bxh filename to get task name and run (if any)

    Expect the filename to be in format:
        bia5_<subject-id>_<task-code>_<run-number>.bxh
    for instance: bia5_19338_4_01.bxh
    
    params:
        - filename: filename of bxh 
        - trans_dict: dictionary to translate task code to task name
        - delimiter: delimiter of the filename (default to be "_")
    returns: task name and run number (if any)
    """
    assert "/" not in filename, "Please use file name alone (not relative/full path)"
    filename = filename.rstrip(".bxh")
    info = filename.split(delimiter)
    task = info[2]
    if trans_dict and info[2] not in trans_dict:
        raise ValueError("Parsed task code cannot be found in translation dictionary!")     
    run = None if len(info) == 3 else info[3]
    task = trans_dict[task] if trans_dict else task
    return task, run, info[2] + "_" + info[3]
