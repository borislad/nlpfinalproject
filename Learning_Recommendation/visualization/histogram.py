from matplotlib import pyplot as plt

# def plot_sorted_dict(my_dict, title):
#     sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
#     keys = list(sorted_dict.keys())
#     values = list(sorted_dict.values())
#
#     plt.bar(keys, values)
#     plt.xlabel(title)
#     plt.ylabel('Num. of tries')
#     plt.title(title + " plot")
#     plt.savefig(f"{title}_plot/" + title + "_histogram.png")
#     plt.show()

import os
from word_verification_module.file_utils import build_file_path

def plot_sorted_dict(my_dict, title):
    sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
    keys = list(sorted_dict.keys())
    values = list(sorted_dict.values())

    plt.bar(keys, values)
    plt.xlabel(title)
    plt.ylabel('Num. of tries')
    plt.title(title + " plot")

    directory = os.path.join('\Learning_Recommendation', 'visualization', f"{title}_plot")
    file_path= build_file_path(directory, f"{title}_histogram")
    plt.savefig(file_path)
    plt.show()


# Example usage
# my_dict = {'Conscience': 4, 'Resilience': 3, 'Competence': 2, 'Providence': 3, 'Elegance': 1}
# plot_sorted_dict(my_dict, "word")

# After creating the visualization function, we need to save it as a png file.
# We will use the savefig() function to save the plot as a png file.
