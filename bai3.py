import mysql.connector

#  dinh nghia ham ket noi 
def connectdatabase(db=''):
    if(db==''):
        connection =mysql.connector.connect(
            host ='localhost',
            user = 'root',
            password=''
        )
        print('database not exists')
    else:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database=db
        )
        print('database is ',db)
    return connection

# dinh nghia ham tao database
def create_database(db):
    con = connectdatabase()
    cursor = con.cursor()
    cursor.execute('create database if not exists '+db)
    print('Tao thanh cong')



def create_table():
    con= connectdatabase('bkap01')
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Computer (ComputerId INT AUTO_INCREMENT PRIMARY KEY, \
                    ComputerName VARCHAR(255), Price DECIMAL(10, 2), Quantity INT, Brand VARCHAR(255))")
    print('Tao thanh cong')

create_database('bkap01')
create_table()

def insert_computer():
    con = connectdatabase('bkap01') 
    cursor = con.cursor()
    computer_id = input("Nhập mã máy tính: ")
    cursor.execute("SELECT * FROM Computer WHERE ComputerId = %s", (computer_id,))
    if cursor.fetchone() is not None:
        print("Mã máy tính đã tồn tại!")
        return

    computer_name = input("Nhập tên máy tính: ")
    price = float(input("Nhập giá máy tính: "))
    quantity = int(input("Nhập số lượng máy tính: "))
    brand = input("Nhập hãng sản xuất: ")

    sql = "INSERT INTO Computer (ComputerId, ComputerName, Price, Quantity, Brand) VALUES (%s, %s, %s, %s, %s)"
    val = (computer_id, computer_name, price, quantity, brand)
    cursor.execute(sql, val)
    con.commit()
    print("Đã thêm dữ liệu thành công!")
    con.close()

def show_computer():
    con = connectdatabase('bkap01') 
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Computer")
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("Het hang nhe!")
    else:
        print("{:<6} {:<20} {:<15} {:<10} {:<15}".format("ID","Computer Name","Price","Quantity","Brand"))
        for row in rows:
            print("{:<6} {:<20} {:<15} {:<10} {:<15}".format(row[0], row[1], row[2], row[3], row[4]))
    cursor.close()
    con.close()

def delete_computer():
    con = connectdatabase('bkap01') 
    cursor = con.cursor()
    computer_id = input("Nhập mã máy tính muốn xóa: ")
    cursor.execute("SELECT * FROM Computer WHERE ComputerId = %s", (computer_id,))
    if cursor.fetchone() is None:
        print("Không tìm thấy máy tính có mã", computer_id)
        return

    cursor.execute("DELETE FROM Computer WHERE ComputerId = %s", (computer_id,))
    con.commit()
    print("Đã xóa máy tính có mã", computer_id)
    cursor.close()
    con.close()

def display_expensive_computers():
    con = connectdatabase('bkap01') 
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Computer WHERE Price > 200")
    computers = cursor.fetchall()
    if not computers:
        print("Không có máy tính nào có giá trên 200$")
    else:
        print("Các máy tính có giá trên 200$ là:")
        for computer in computers:
            print(computer)
    cursor.close()
    con.close()

def main():
    create_table()
    while True:
        print("\nMenu:")
        print("1. Thêm máy tính")
        print("2. Hien thi du lieu")
        print("3. Xóa máy tính")
        print("4. Hiển thị máy tính có giá >200$")
        print("5. Thoát")

        choice = input("Nhập lựa chọn của bạn: ")

        if choice == "1":
            insert_computer()
        elif choice == "2":
            show_computer()
        elif choice == "3":
            delete_computer()
        elif choice == "4":
            display_expensive_computers()
        elif choice == "5":
            break
        else:
            print("Lựa chọn không hợp lệ!")

    # connection.close()

if __name__ == "__main__":
    main()