# parser.py

import re

class SQLParser:
    @staticmethod
    def parse(sql):
        sql = sql.strip().rstrip(";")
        upper_sql = sql.upper()

        if not upper_sql.startswith("SELECT"):
            raise ValueError("Query must begin with SELECT")

        # Split SELECT and FROM
        try:
            select_section, rest = re.split(r"\sFROM\s", sql, flags=re.IGNORECASE)
        except:
            raise ValueError("Missing FROM clause")

        # Extract columns
        select_part = select_section[len("SELECT "):].strip()

        is_count = False
        count_column = None

        # COUNT(*) or COUNT(col)
        if select_part.upper().startswith("COUNT("):
            is_count = True
            inside = select_part[6:-1].strip()
            count_column = inside if inside != "*" else "*"
            select_cols = []
        else:
            select_cols = [c.strip() for c in select_part.split(",")]

        # WHERE clause
        if re.search(r"\sWHERE\s", rest, flags=re.IGNORECASE):
            table_section, where_section = re.split(
                r"\sWHERE\s", rest, flags=re.IGNORECASE
            )
            table_name = table_section.strip()
            where_clause = SQLParser.parse_where(where_section.strip())
        else:
            table_name = rest.strip()
            where_clause = None

        return {
            "select_cols": select_cols,
            "from_table": table_name,
            "where": where_clause,
            "is_count": is_count,
            "count_column": count_column
        }

    @staticmethod
    def parse_where(where_str):
        # Allowed operators (longest first)
        valid_ops = ["!=", ">=", "<=", "=", ">", "<"]

        op = None
        for operator in valid_ops:
            # strict operator match: must be surrounded by non-operator characters
            if operator in where_str:
                op = operator
                break

        if op is None:
            raise ValueError("Invalid WHERE clause: Unknown operator")

        parts = where_str.split(op)
        if len(parts) != 2:
            raise ValueError("Invalid WHERE clause syntax")

        col = parts[0].strip()
        val = parts[1].strip().strip("'").strip('"')

        # Convert numeric if applicable
        if val.replace(".", "", 1).isdigit():
            val = float(val) if "." in val else int(val)

        return {
            "column": col,
            "operator": op,
            "value": val
        }
