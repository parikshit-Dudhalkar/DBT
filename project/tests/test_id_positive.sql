with cte as (select id
from {{ ref('my_first_dbt_model') }}
where id <= 0
)
select id from cte
