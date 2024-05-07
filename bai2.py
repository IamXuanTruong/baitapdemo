def add_city(city, city_list):
    if city in city_list:
        print("Thành phố đã tồn tại trong danh sách!")
    else:
        city_list.append(city)
        print("Đã thêm thành phố", city)

def save_to_file(city_list, filename):
    with open(filename, "w") as file:
        for city in city_list:
            file.write(city + "\n")
    print("Danh sách thành phố đã được lưu vào tệp", filename)

def read_from_file(filename):
    with open(filename, "r") as file:
        cities = file.readlines()
        for city in cities:
            print(city.strip())

def main():
    city_list = ["Hanoi", "Ho Chi Minh City", "Da Nang", "Hai Phong"]

    # Thêm một thành phố nhập từ bàn phím vào danh sách
    new_city = input("Nhập tên thành phố muốn thêm vào danh sách: ")
    add_city(new_city, city_list)

    # Lưu danh sách vào tệp tin .txt
    save_to_file(city_list, "cities.txt")

    # Đọc tệp tin .txt ra màn hình
    print("Danh sách thành phố từ tệp tin:")
    read_from_file("cities.txt")

if __name__ == "__main__":
    main()