# engine.py

import csv

class SQLEngine:

    @staticmethod
    def load_csv(filename):
        try:
            with open(filename, newline="") as f:
                return list(csv.DictReader(f))
        except FileNotFoundError:
            raise ValueError(f"CSV file '{filename}' not found.")

    @staticmethod
    def apply_where(rows, where):
        if where is None:
            return rows

        col = where["column"]
        op = where["operator"]
        val = where["value"]

        output = []
        for row in rows:
            if col not in row:
                raise ValueError(f"Column '{col}' does not exist.")

            cell = row[col]

            # Convert CSV cell to numeric if needed
            if isinstance(val, (int, float)):
                try:
                    cell = float(cell) if "." in cell else int(cell)
                except:
                    continue

            if SQLEngine.compare(cell, op, val):
                output.append(row)

        return output

    @staticmethod
    def compare(a, op, b):
        ops = {
            "=": a == b,
            "!=": a != b,
            ">": a > b,
            "<": a < b,
            ">=": a >= b,
            "<=": a <= b,
        }
        return ops[op]

    @staticmethod
    def apply_select(rows, columns):
        if columns == [] or columns == ["*"]:
            return rows
        
        result = []
        for row in rows:
            new_row = {}
            for col in columns:
                if col not in row:
                    raise ValueError(f"Column '{col}' not found.")
                new_row[col] = row[col]
            result.append(new_row)
        return result

    @staticmethod
    def apply_count(rows, col):
        if col == "*" or col is None:
            return [{"COUNT": len(rows)}]

        count = sum(1 for r in rows if r.get(col) not in ("", None))
        return [{"COUNT": count}]
