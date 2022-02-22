import flask_sqlalchemy
import sqlalchemy.engine.row
from database.core import db
from utils.http.code import ResponseCode


def get_data(query: flask_sqlalchemy.BaseQuery, query_type: str) -> tuple[str, list[dict]]:
    data_list = []
    if query_type == 'one':
        query_data = query.first()
        if query_data:
            s_dict = {}
            if isinstance(query_data, sqlalchemy.engine.row.Row):
                for key in query_data._asdict():
                    data_label = key
                    data_data = query_data[key]
                    if isinstance(data_data, db.Model):
                        for p in data_data.__mapper__.iterate_properties:
                            key = data_data.__tablename__ + "_" + p.key
                            s_dict[key] = getattr(data_data, p.key)
                    else:
                        s_dict[data_label] = data_data
            elif isinstance(query_data, db.Model):
                for p in query_data.__mapper__.iterate_properties:
                    key = query_data.__tablename__ + "_" + p.key
                    s_dict[key] = getattr(query_data, p.key)
            data_list.append(s_dict)
        else:
            return ResponseCode.NoResourceFound, data_list
    elif query_type == 'all':
        pass
    return ResponseCode.Success, data_list
