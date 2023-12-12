from typing import Tuple

from fastapi import HTTPException

from db.model import Model

from db.db import PgDatabase


def update_data_in_table(table_name: str, data: dict, **kwargs) -> Tuple[bool, str]:
    query = f"""UPDATE {table_name} SET {", ".join([f'{k} = %s' for k, v in data.items() if v is not None])} 
        WHERE {" and ".join([f'{k} = %s' for k, v in kwargs.items() if v is not None])};"""
    print(query)
    with PgDatabase() as db:
        try:
            db.cursor.execute(query, [v for v in data.values(
            ) if v is not None] + [v for v in kwargs.values() if v is not None])
            updated_rows = db.cursor.rowcount
            if updated_rows == 0:
                raise HTTPException(status_code=404, detail="Not found")
            db.connection.commit()
            return True, f"{updated_rows} row(s) updated successfully"
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e.with_traceback))


def update(table: str, model: Model, **kwargs):
    return update_data_in_table(table, model.to_dict(), **kwargs)
