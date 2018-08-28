import ..util.constants as Const


def populate_file(folder, dictionary, sessions=[]):
    assert folder == "Func" or folder == "Anat", "folder has to be 'Anat' or 'Func'"
    pass    
    

def build_file(dictionary, filepath):
    with open(filepath, "w") as f:
        for key, val in dictionary.items():
            s = key + "\t" + val
            f.write(s + "\n")

