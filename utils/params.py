import os

#folder_path = os.path.dirname(__file__).replace('utils', 'data')

# folder_path = os.path.dirname(__file__).split('\\')
# folder_path[-1] = 'data'
# folder_path = "\\".join(folder_path)

folder_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')



