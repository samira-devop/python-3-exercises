from ValidationException import ValidationException

def validate_file(file_path):
    non_integer_mileages = []
    with open(file_path, 'r') as file:
        next(file)  # Skip the header line
        for line in file:
            car_id, mileage = line.strip().split(',')
            try:
                mileage_float = float(mileage.strip())
                if not mileage_float.is_integer():
                    non_integer_mileages.append(mileage_float)
            except ValueError:
                print(mileage)
    return non_integer_mileages



def ex1():
    try:
        non_integer_mileages = validate_file("./files/input.txt")
        for mileage in non_integer_mileages:
            print("Invalid mileage: " + str(mileage))
    except ValidationException as ve:
        print(ve)


ex1()
