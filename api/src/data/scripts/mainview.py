import os
import mysql.connector
import time

create_view_query = """
CREATE VIEW main_view AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;
"""


