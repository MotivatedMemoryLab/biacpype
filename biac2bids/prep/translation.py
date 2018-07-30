def trans_dict(filepath, delimiter="\t", header=0):
    """Given a path to a file, translate code to task name.

    Expect the file to be in format (| is the delimiter)
    Code | Task
    -----------
      4  |  train
      ........
    
    params:
        - filepath: path to file which contains the translation mapping
        - delimiter: delimiter for the file (default to tab)
        - header: the number of lines to skip for header
    returns: a translation dict
    """
    with open(filepath, "r") as f:
        for _ in range(header):
            f.readline()
        d = dict()
        for line in f:
            line = line.rstrip()
            info = line.split(delimiter)
            d[info[0]] = info[1]
    return d


def parse_task_and_run(filename, trans_dict, delimiter="_"):
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
    if info[2] not in trans_dict:
        raise ValueError("Parsed task code cannot be found in translation dictionary!")     
    run = None if len(info) == 3 else info[3]
    return trans_dict[info[2]], run, info[2] + "_" + info[3]


if __name__ == "__main__":
    d = trans_dict("/Users/lpjiang/Research/CBT/Data/func/19492/series_order_note.txt")
    for key, value in d.items():
        print(key, value)