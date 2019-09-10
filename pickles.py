import pickle


def write_pickle(data, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)


def load_pickle(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)


def append_pickle(data, file_path):
    old = load_pickle(file_path)
    old.append(data)
    write_pickle(old, file_path)