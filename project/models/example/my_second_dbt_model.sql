
-- Use the `ref` function to select from other models

select *
from {{ ref('my_first_dbt_model') }}
where id = 1
/workspaces/DBT/project/models/example/my_second_dbt_model.sql