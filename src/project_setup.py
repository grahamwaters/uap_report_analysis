import os
# setup the folder structure

def create_folder_structure():
    project_folder = './'
    data_folder = 'data'
    raw_folder = 'raw'
    processed_folder = 'processed'
    external_folder = 'external'
    models_folder = 'models'
    notebooks_folder = 'notebooks'
    reports_folder = 'reports'
    src_folder = 'src'
    # data_src_folder = 'data'
    # features_src_folder = 'features'
    # models_src_folder = 'models'
    # visualization_src_folder = 'visualization'

    # make the files
    if not os.path.exists(os.path.join(project_folder, 'environment.yml')):
        with open(os.path.join(project_folder, 'environment.yml'), 'w') as f:
            pass
    if not os.path.exists(os.path.join(project_folder, 'README.md')):
        with open(os.path.join(project_folder, 'README.md'), 'w') as f:
            pass
    if not os.path.exists(os.path.join(project_folder, 'LICENSE')):
        with open(os.path.join(project_folder, 'LICENSE'), 'w') as f:
            pass
    if not os.path.exists(os.path.join(project_folder, '.gitignore')):
        with open(os.path.join(project_folder, '.gitignore'), 'w') as f:
            pass
    if not os.path.exists(os.path.join(project_folder, 'setup.py')):
        with open(os.path.join(project_folder, 'setup.py'), 'w') as f:
            pass
    if not os.path.exists(os.path.join(project_folder, 'requirements.txt')):
        with open(os.path.join(project_folder, 'requirements.txt'), 'w') as f:
            pass

    # make the folders
    if not os.path.exists(project_folder): # if the project folder doesn't exist
        os.mkdir(project_folder) # make the project folder
    if not os.path.exists(f'{project_folder}/{data_folder}'): # if the data folder doesn't exist
        os.mkdir(f'{project_folder}/{data_folder}') # make the data folder
    if not os.path.exists(f'{project_folder}/{data_folder}/{raw_folder}'): # if the raw folder doesn't exist
        os.mkdir(f'{project_folder}/{data_folder}/{raw_folder}') # make the raw folder
    if not os.path.exists(f'{project_folder}/{data_folder}/{processed_folder}'):
        os.mkdir(f'{project_folder}/{data_folder}/{processed_folder}')
    if not os.path.exists(f'{project_folder}/{data_folder}/{external_folder}'): # if the external folder doesn't exist, make it
        os.mkdir(f'{project_folder}/{data_folder}/{external_folder}')
    if not os.path.exists(f'{project_folder}/{models_folder}'):
        os.mkdir(f'{project_folder}/{models_folder}')
    if not os.path.exists(f'{project_folder}/{notebooks_folder}'):
        os.mkdir(f'{project_folder}/{notebooks_folder}')
    if not os.path.exists(f'{project_folder}/{reports_folder}'):
        os.mkdir(f'{project_folder}/{reports_folder}')
    if not os.path.exists(f'{project_folder}/{src_folder}'):
        os.mkdir(f'{project_folder}/{src_folder}')
    # move the .py files into the src folder
    for file in os.listdir(): # for each file in the current directory
        if file.endswith('.py'): # if the file ends with .py
            os.rename(file, f'{project_folder}/{src_folder}/{file}') # move the file into the src folder

    # create the following notebooks in the notebooks folder
    notebook_names = ['data_cleaning', 'data_exploration', 'data_preprocessing', 'feature_engineering', 'modeling', 'visualization']
    for notebook in notebook_names:
        if not os.path.exists(f'{project_folder}/{notebooks_folder}/{notebook}.ipynb'):
            with open(f'{project_folder}/{notebooks_folder}/{notebook}.ipynb', 'w') as f:
                pass

    # create the following files in the src folder
    src_file_names = ['test', 'train', 'predict']
    for src_file in src_file_names:
        if not os.path.exists(f'{project_folder}/{src_folder}/{src_file}.py'):
            with open(f'{project_folder}/{src_folder}/{src_file}.py', 'w') as f:
                pass



    # in each subdirectory at level 1 of the project folder, create a folder_description.md file with the name of the folder as the title
    for folder in os.listdir(project_folder):
        if os.path.isdir(folder):
            if not os.path.exists(f'{project_folder}/{folder}/folder_description.md'):
                # # delete the simple_readme.md file if it exists
                # if os.path.exists(f'{project_folder}/{folder}/simple_readme.md'):
                #     os.remove(f'{project_folder}/{folder}/simple_readme.md')
                with open(f'{project_folder}/{folder}/folder_description.md', 'w') as f:
                    f.write(f'# {folder}')
                    f.write('\n') # new line
                    f.write('-' * (len(folder) + 10)) # write a line of dashes the length of the folder name
            else: # if the folder_description.md file already exists in the folder (which it should), overwrite it in case the folder name has changed.
                with open(f'{project_folder}/{folder}/folder_description.md', 'w') as f:
                    f.write(f'# {folder}')
                    f.write('\n') # new line
                    f.write('-' * (len(folder) + 10)) # write a line of dashes the length of the folder name




create_folder_structure()
