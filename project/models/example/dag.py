import yaml

file_path='/workspaces/DBT/project/models/example/my_first_dbt_model.yml'


with open(file_path,"r") as file:
    config=yaml.safe_load(file)

print(config)

