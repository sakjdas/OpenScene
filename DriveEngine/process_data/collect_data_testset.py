import pickle
import os

if __name__ == '__main__':
    # remember to change the path accordingly
    current_file_path = os.path.abspath(__file__)
    parent_directory = os.path.abspath(os.path.join(current_file_path, os.pardir))
    grandparent_directory = os.path.abspath(os.path.join(parent_directory, os.pardir))
    great_grandparent_directory = os.path.abspath(os.path.join(grandparent_directory, os.pardir))

    test_infos = os.listdir(os.path.join(great_grandparent_directory, 'dataset/openscene-v1.1/meta_datas/test'))
    testset_paths = [os.path.join(great_grandparent_directory, 'dataset/openscene-v1.1/meta_datas/test', each)
                     for each in test_infos if each.endswith('.pkl')]

    testing_infos = []
    for file in testset_paths:
        with open(file, 'rb') as f:
            testing_infos.extend(pickle.load(f))

    with open(os.path.join(great_grandparent_directory, "dataset", 'data/openscene_test.pkl'), 'wb') as f:
        pickle.dump(testing_infos, f)
