import pickle
import os

if __name__ == '__main__':
    # remember to change the path accordingly
    current_file_path = os.path.abspath(__file__)
    parent_directory = os.path.abspath(os.path.join(current_file_path, os.pardir))
    grandparent_directory = os.path.abspath(os.path.join(parent_directory, os.pardir))
    great_grandparent_directory = os.path.abspath(os.path.join(grandparent_directory, os.pardir))

    mini_infos = os.listdir(os.path.join(great_grandparent_directory, 'dataset/openscene-v1.1/meta_datas/mini'))
    mini_infos = [os.path.join(great_grandparent_directory, 'dataset/openscene-v1.1/meta_datas/mini', each)
                  for each in mini_infos if each.endswith('.pkl')]

    train_paths = mini_infos[:int(len(mini_infos) * 0.85)]
    val_paths = mini_infos[int(len(mini_infos) * 0.85):]
    overfit_paths = mini_infos[:int(len(mini_infos) * 0.02)]
    print("the length of training paths is: ", len(train_paths))
    print("the length of validation paths is: ", len(val_paths))
    print("the length of overfit paths is: ", len(overfit_paths))
    train_infos = []
    for file in train_paths:
        with open(file, 'rb') as f:
            train_infos.extend(pickle.load(f))

    val_infos = []
    for file in val_paths:
        with open(file, 'rb') as f:
            val_infos.extend(pickle.load(f))

    overfit_infos = []
    for file in overfit_paths:
        with open(file, 'rb') as f:
            overfit_infos.extend(pickle.load(f))

    with open(os.path.join(great_grandparent_directory, "dataset", 'data/openscene_mini_train.pkl'), 'wb') as f:
        pickle.dump(train_infos, f)

    with open(os.path.join(great_grandparent_directory, "dataset", 'data/openscene_mini_val.pkl'), 'wb') as f:
        pickle.dump(val_infos, f)

    with open(os.path.join(great_grandparent_directory, "dataset", 'data/openscene_mini_overfit.pkl'), 'wb') as f:
        pickle.dump(overfit_infos, f)
