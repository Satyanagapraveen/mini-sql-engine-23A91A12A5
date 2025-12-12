# cli.py

from parser import SQLParser
from engine import SQLEngine

def main():
    print("Mini SQL Engine — Type 'exit' to quit.\n")

    while True:
        sql = input("sql> ")

        if sql.lower() in ("exit", "quit"):
            print("Goodbye!")
            break

        try:
            parsed = SQLParser.parse(sql)
            filename = parsed["from_table"] + ".csv"

            rows = SQLEngine.load_csv(filename)
            filtered = SQLEngine.apply_where(rows, parsed["where"])

            if parsed["is_count"]:
                result = SQLEngine.apply_count(filtered, parsed["count_column"])
            else:
                result = SQLEngine.apply_select(filtered, parsed["select_cols"])

            for r in result:
                print(r)

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
