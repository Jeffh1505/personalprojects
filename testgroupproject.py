import csv
def load_air_quality_data(filename=r"C:\Users\summe\Downloads\air_quality.csv"):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        dict_geo_id, dict_date = {}, {}
        for row in reader:
            geo_id, geo_desc, date, pm = row
            tuple_row = (geo_id, geo_desc, date, pm)
            dict_geo_id.setdefault(geo_id, []).append(tuple_row)
            dict_date.setdefault(date, []).append(tuple_row)
        return dict_geo_id, dict_date

def load_uhf_data(filename=r"C:\Users\summe\Downloads\uhf.csv"):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        dict_zip, dict_borough = {}, {}
        for row in reader:
            borough, uhf_type, uhf_id, *zip_codes = row
            for zip_code in zip_codes:
                dict_zip.setdefault(zip_code, []).append(uhf_id)
            dict_borough.setdefault(borough, []).append(uhf_id)
        return dict_zip, dict_borough

def main():
    dict_geo_id, dict_date = load_air_quality_data()
    dict_zip, dict_borough = load_uhf_data()

    choice = input("Search by zip code, UHF ID, borough, or date: ").lower()
    query = input("Enter your query: ").strip()

    uhf_ids, results = [], []

    if choice == "zip code":
        uhf_ids = dict_zip.get(query, [])
    elif choice == "uhf id":
        uhf_ids = [query]
    elif choice == "borough":
        uhf_ids = dict_borough.get(query.title(), [])
    elif choice == "date":
        results = dict_date.get(query, [])
    else:
        print("Invalid choice. Please enter zip code, UHF ID, borough, or date.")
        return

    if choice != "date":
        results = []
        for uhf_id in uhf_ids:
            results.extend(dict_geo_id.get(uhf_id, []))

    if not results:
        print("No results found for your query.")
    else:
        for result in results:
            print(f"{result[2]} UHF {result[0]} {result[1]} {result[3]} mcg/m^3")

if __name__ == "__main__":
    main()


