import src.mysql.connector as sql
import src.PySimpleGUI as sg
from src.mysql.connector import Error
from datetime import date
from datetime import datetime

#connect với databse
def connect():
    db = sql.connect(
        host="127.0.0.1",
        user="root",
        password="234847098",
        database="coffeeshopmanagement"
    )
    return db
myfont = "Ariel 10"
today = str(date.today())

# Dang nhap
def login():
    db = connect()
    mycursor = db.cursor()
    layout = [
        [sg.Text('ĐĂNG NHẬP', justification='center', font="Ariel 20")],
        [sg.Text('Tên đăng nhập', size=(15, 1), font=('Ariel', 10, 'bold')), sg.InputText(key='-usrnm-')],
        [sg.Text('Mật khẩu', size=(15, 1), font=('Ariel', 10, 'bold')), sg.InputText(key='-pwd-', password_char='*')],
        [sg.Text("", key='noti', text_color='Red')],
        [sg.Submit("ĐĂNG NHẬP", button_color="Green", font=('Ariel', 10, 'bold')),
         sg.Button('THOÁT', button_color="Red", font=('Ariel', 10, 'bold'))]
    ]
    window = sg.Window('UNDERTHENET COFFEE', layout)
    while True:
        check = 0
        event,values = window.read()
        if event == "THOÁT" or event == sg.WIN_CLOSED:
            break
        else:
            if event == "ĐĂNG NHẬP":
                mycursor.execute(f"SELECT * FROM staff WHERE id='{values['-usrnm-']}' AND pw='{values['-pwd-']}';") 
                result = mycursor.fetchall()
                if len(result) != 0:
                    check = values['-usrnm-']
                    break
                elif len(result) == 0:
                    window['noti'].Update("Sai tên đăng nhập hoặc mật khẩu!")
    window.close()
    return check

#frame 
def show_List(m, headings, name):
    result = m.fetchall()
    L = [[] for i in range(len(result))]
    p = 0
    for x in result:
        for i in range(len(x)):
            L[p].append(x[i])
        if name == "DANH SÁCH NHÂN SỰ" and x[0] == 1: L[p].append("quản lý")
        p += 1

    if name == "DANH SÁCH BÀN":
        for e in L:
            if e[3] == 1:   e[3] = 'Có khách'
            else: e[3] = 'Trống'
        layout = [[sg.Text(name, justification='center', font="Ariel")],
            [sg.Button("BÀN TRỐNG", button_color="Green", font=('Ariel', 10, 'bold'))],
            [sg.Table(values=L, headings=headings, max_col_width=50,
                auto_size_columns=True,
                justification='left',
                num_rows=5,
                alternating_row_color='royalblue4',
                enable_events = True,
                key='-TABLE-',
                row_height=50,)],
            [sg.Button("Thoát", button_color="Red", font=('Ariel', 10, 'bold'))],
        ]
    elif name == "DANH SÁCH BÀN TRỐNG":
        for e in L:
            if e[3] == 1:   e[3] = 'Có khách'
            else: e[3] = 'Trống'
        layout = [[sg.Text(name, justification='center', font="Ariel")],
            [sg.Table(values=L, headings=headings, max_col_width=50,
                auto_size_columns=True,
                justification='left',
                num_rows=5,
                alternating_row_color='royalblue4',
                enable_events = True,
                key='-TABLE-',
                row_height=50,)],
            [sg.Button("Thoát", button_color="Red", font=('Ariel', 10, 'bold'))],
        ]        
    else:     
        layout = [[sg.Text(name, justification='center', font="Ariel")],
                    [sg.Text("Tìm kiếm"), sg.InputText(size=(40,1), key='search'), sg.Button("Tìm"), sg.Button("Hủy")],
                    [sg.Table(values=L, headings=headings, max_col_width=50,
                        auto_size_columns=True,
                        justification='left',
                        num_rows=5,
                        alternating_row_color='royalblue4',
                        enable_events = True,
                        key='-TABLE-',
                        row_height=50,)],
                    [sg.Button("Thoát", button_color="Red", font=('Ariel', 10, 'bold')), sg.Button("Thêm"), sg.Button("Sửa"), sg.Button("Xóa")],
                ]
    window = sg.Window('UNDERTHENET COFFEE', layout, finalize=True)
    return window

def show_List1(m1, m2, headings, name):
    L1 = [[] for i in range(len(m1))]
    p = 0
    for x in m1:
        for i in range(len(x)):
            L1[p].append(x[i])      
        p += 1
    L2 = [[] for i in range(len(m2))]
    p = 0
    for x in m2:
        for i in range(len(x)):
            L2[p].append(x[i])
        p += 1
    heading2 = [' Mã ', 'Tên thức uống', 'Giá', 'Mô tả']
    layout = [[sg.Text(name, justification='center', font="Ariel")],
                [sg.Table(values=L1, headings=headings, max_col_width=50,
                    auto_size_columns=True,
                    justification='left',
                    num_rows=5,
                    alternating_row_color='royalblue4',
                    enable_events = True,
                    key='-TAB-',
                    row_height=50),
                sg.Table(values=L2, headings=heading2, max_col_width=50,
                    auto_size_columns=True,
                    justification='left',
                    num_rows=5,
                    alternating_row_color='royalblue4',
                    enable_events = True,
                    key='-TABLE-',
                    row_height=50)],
                [sg.Button("Thoát", button_color="Red", font=('Ariel', 10, 'bold')), sg.Button("Thanh toán")],
            ]
    window = sg.Window('UNDERTHENET COFFEE', layout)
    return window

# Quản lý nhân sự
def add_staff():
    add_staff = [
        [sg.Text('THÊM NHÂN SỰ', font=myfont)],
        [sg.Text('Họ và tên:', size =(15, 1), font=myfont), sg.InputText(key='name')],
        [sg.Text('Ngày:', size =(15, 1), font=myfont), sg.InputText(key='day', size =(5, 1)),
         sg.Text('Tháng:', size =(8, 1), font=myfont), sg.InputText(key='month', size =(5, 1)),
         sg.Text('Năm sinh:', size =(8, 1), font=myfont), sg.InputText(key='year', size =(8, 1))],
        [sg.Text('Địa chỉ:', size =(15, 1), font=myfont), sg.InputText(key='addr')],
        [sg.Text('Số điện thoại:', size=(15, 1), font=myfont), sg.InputText(key='phone')],
        [sg.Text('Email:', size=(15, 1), font=myfont), sg.InputText(key='email')],
        [sg.Text('Mật khẩu:', size =(15, 1), font=myfont), sg.InputText(key='pwd', password_char='*')],
        [sg.Cancel(button_color="Red", font=('Ariel', 10, 'bold')), sg.Submit(button_color="Green", font=('Ariel', 10, 'bold'))]
    ]
    window = sg.Window('UNDERTHENET COFFEE', add_staff)
    events, values = window.read()
    birth = str(values['year'])+'-'+str(values['month'])+'-'+str(values['day'])    
    if events == "Submit":
        cursor.execute("""INSERT INTO staff(fullname, birthday, address, phone_number, email, pw, position) 
                                  VALUES(%s, %s, %s, %s, %s, %s, %s)""",
                               (values['name'], birth, values['addr'], values['phone'], values['email'], values['pwd'], 'nhân viên'))
        db.commit()
        window.close()
    if events == sg.WIN_CLOSED or events == "Cancel":  window.close()
    staff_List()    

# hàm sửa nhân sự
def edit_staff(i, staff):
    add_staff = [
        [sg.Text('SỬA THÔNG TIN', font=myfont)],
        [sg.Text('Họ và tên:', size =(15, 1), font=myfont), sg.InputText(staff[1], key='name')],
        [sg.Text('Sinh Ngày:', size =(15, 1), font=myfont), sg.InputText(staff[2].day, key='day', size =(5, 1)),
         sg.Text('Tháng:', size =(8, 1), font=myfont), sg.InputText(staff[2].month, key='month', size =(5, 1)),
         sg.Text('Năm:', size =(8, 1), font=myfont), sg.InputText(staff[2].year, key='year', size =(8, 1))],
        [sg.Text('Địa chỉ:', size =(15, 1), font=myfont), sg.InputText(staff[3], key='addr')],
        [sg.Text('Số điện thoại:', size=(15, 1), font=myfont), sg.InputText(key='phone')],
        [sg.Text('Email:', size=(15, 1), font=myfont), sg.InputText(key='email')],
        [sg.Text('Mật khẩu:', size =(15, 1), font=myfont), sg.InputText(staff[4], key='pwd', password_char='*')],
        [sg.Cancel(button_color="Red", font=('Ariel', 10, 'bold')), sg.Submit(button_color="Green", font=('Ariel', 10, 'bold'))]
    ]
    window = sg.Window('UNDERTHENET COFFEE', add_staff)
    events, values = window.read()
    birth = str(values['year'])+'-'+str(values['month'])+'-'+str(values['day'])
    if events == "Submit":
        cursor.execute("""UPDATE staff 
                      SET fullname=%s, birthday=%s, address=%s, phone_number=%s, email=%s, pw=%s 
                      WHERE id=%s""",
                   (values['name'], birth, values['addr'], values['phone'], values['email'], values['pwd'], i))
        # cursor.execute(f"UPDATE staff SET fullname='{values['name']}',birthday='{birth}',address='{values['addr']}',pw='{values['pwd']}' WHERE id='{i}'")
        db.commit()
        window.close()
    if events == sg.WIN_CLOSED or events == "Cancel":   window.close()
    staff_List()

db = connect()
cursor = db.cursor()

# hàm xóa nhân sự
def del_staff(i):
    cursor.execute(f"UPDATE orders SET staff_id=1 WHERE staff_id='{i}'")
    db.commit()
    cursor.execute(f"DELETE FROM staff WHERE id='{i}'")
    db.commit()
    staff_List()

# hàm kím nhân sự
def search_staff(s):
    cursor.execute(f"SELECT * FROM staff WHERE fullname LIKE '%{s}%';")
    return cursor

# hàm show nhân sự
def staff_List():
    db = connect()
    try:
        cursor = db.cursor()  
        headings = [' Mã ', 'Họ và Tên', '  Năm sinh    ', '    Địa chỉ     ', '    Số điện thoại     ', '    Email    ', '    Vị trí    ']
        cursor.execute("select id, fullname, birthday, address, phone_number, email, position from staff")
        window = show_List(cursor, headings, "DANH SÁCH NHÂN SỰ")
        cursor.execute("select * from staff")
        result = cursor.fetchall()
        i = -1
        while True:
            event, values = window.read()
            if event == "Thêm":
                window.close()
                add_staff()
            if event == '-TABLE-':
                i = values['-TABLE-'][0]
            if event == 'Sửa' and i >= 0:
                window.close()
                edit_staff(result[i][0], result[i])
            if event == 'Xóa' and i >= 0:
                window.close()
                del_staff(result[i][0])
            if event == "Tìm" and values['search'] != None:
                result = search_staff(values['search']).fetchall()
                L = [[] for i in range(len(result))]
                p = 0
                for x in result:
                    for i in range(len(x)):
                        L[p].append(x[i])
                    p += 1
                    layout = [[sg.Text("DANH SÁCH NHÂN VIÊN", justification='center', font="Ariel")],
                        [sg.Text("Tìm kiếm"), sg.InputText(size=(40,1), key='search'), sg.Button("Tìm"), sg.Button("Hủy")],
                        [sg.Table(values=L, headings=headings, max_col_width=50,
                            auto_size_columns=True,
                            justification='left',
                            num_rows=5,
                            alternating_row_color='royalblue4',
                            enable_events = True,
                            key='-TABLE-',
                            row_height=50,)],
                        [sg.Button("Thêm"), sg.Button("Sửa"), sg.Button("Xóa")],
                    ]
                window1 = sg.Window('UNDERTHENET COFFEE', layout)
                window.close()
                window = window1
            if event == "Thoát":
                window.close()
            if event == "Hủy":
                window.close()
                staff_List()
            if event == sg.WIN_CLOSED:
                break
    except Error as e:
        print(e)
    finally:
        cursor.close()
    window.close()


# Quản lý đồ uống

#thêm
def add_product():
    add_product = [
        [sg.Text('THÊM THỨC UỐNG', font=myfont)],
        [sg.Text('Tên thức uống:', size =(15, 1), font=myfont), sg.InputText(key='name')],
        [sg.Text('Giá:', size =(15, 1), font=myfont), sg.InputText(key='pri')],
        [sg.Text('Mô tả:', size =(15, 1), font=myfont), sg.InputText(key='cont')],
        [sg.Text('Loại đồ uống:', size =(15, 1), font=myfont), sg.InputText(key='cat')],
        [sg.Cancel(button_color="Red", font=('Ariel', 10, 'bold')), sg.Submit(button_color="Green", font=('Ariel', 10, 'bold'))]
    ]

    window = sg.Window('UNDERTHENET COFFEE', add_product)
    events, values = window.read()
    if events == "Submit":
        cursor.execute(f"select id from category where title='{values['cat']}'")
        result = cursor.fetchall()
        cursor.execute("""INSERT INTO product(title,price,created_at,updated_at,content,id_cat) values(%s,%s,%s,%s,%s,%s)""", (values['name'], values['pri'], today, today, values['cont'], result[0][0]))
        db.commit()
        window.close()
    if events == sg.WIN_CLOSED or events == "Cancel":  window.close()
    product_List() 

#sửa
def edit_product(i, product):
    edit_product = [
        [sg.Text('THÊM THỨC UỐNG', font=myfont)],
        [sg.Text('Tên thức uống:', size =(15, 1), font=myfont), sg.InputText(product[1], key='name')],
        [sg.Text('Giá:', size =(15, 1), font=myfont), sg.InputText(product[2], key='pri')],
        [sg.Text('Mô tả:', size =(15, 1), font=myfont), sg.InputText(product[5], key='cont')],
        # [sg.Text('Mã loại:', size =(15, 1), font=myfont), sg.InputText(product[6], key='cat')],
        [sg.Cancel(button_color="Red", font=('Ariel', 10, 'bold')), sg.Submit(button_color="Green", font=('Ariel', 10, 'bold'))]
    ]
    window = sg.Window('UNDERTHENET COFFEE', edit_product)
    events, values = window.read()
    if events == "Submit":
        cursor.execute(f"UPDATE product SET title='{values['name']}', price='{values['pri']}',updated_at='{today}',content='{values['cont']}' WHERE id='{i}'")
        db.commit()
        window.close()
    if events == sg.WIN_CLOSED or events == "Cancel":   window.close()
    product_List()

db = connect()
cursor = db.cursor()

#xóa
def del_product(i):
    cursor.execute(f"DELETE FROM product WHERE id='{i}'")
    db.commit()
    product_List()

#tìm
def search_product(s):
    cursor.execute(f"""select product.id, product.title, product.price, product.created_at, product.updated_at, product.content, category.title from product, category
	                    where category.id = product.id_cat and product.title like '%{s}%';""")
    return cursor

#show
def product_List():
    db = connect()
    cursor = db.cursor()
    headings = [' Mã ', 'Tên thức uống', 'Giá', 'Ngày tạo', 'Ngày cập nhật', 'Mô tả', 'Loại']
    cursor.execute("""select product.id, product.title, product.price, product.created_at, product.updated_at, product.content, category.title from product, category
	                    where category.id = product.id_cat;""")
    window = show_List(cursor, headings, "DANH SÁCH THỨC UỐNG")
    cursor.execute("""select product.id, product.title, product.price, product.created_at, product.updated_at, product.content, category.title from product, category
	                    where category.id = product.id_cat;""")
    result = cursor.fetchall()
    i = -1
    while True:
        event, values = window.read()
        if event == "Thêm":
            window.close()
            add_product()
        if event == '-TABLE-':
            i = values['-TABLE-'][0]
        if event == 'Sửa' and i >= 0:
            window.close()
            edit_product(result[i][0], result[i])
        if event == 'Xóa' and i >= 0:
            window.close()
            del_product(result[i][0])
        if event == "Tìm" and values['search'] != None:
            result = search_product(values['search']).fetchall()
            L = [[] for i in range(len(result))]
            p = 0
            for x in result:
                for i in range(len(x)):
                    L[p].append(x[i])
                p += 1
                layout = [[sg.Text("MENU", justification='center', font="Ariel")],
                    [sg.Text("Tìm kiếm"), sg.InputText(size=(40,1), key='search'), sg.Button("Tìm"), sg.Button("Hủy")],
                    [sg.Table(values=L, headings=headings, max_col_width=50,
                        auto_size_columns=True,
                        justification='left',
                        num_rows=5,
                        alternating_row_color='royalblue4',
                        enable_events = True,
                        key='-TABLE-',
                        row_height=50,)],
                    [sg.Button("Thêm"), sg.Button("Sửa"), sg.Button("Xóa")],
                ]
            window1 = sg.Window('UNDERTHENET COFFEE', layout)
            window.close()
            window = window1
        if event == "Hủy":
            window.close()
            product_List()
        if event == "Thoát":
            window.close()
        if event == sg.WIN_CLOSED:
            break
    window.close()

#hàm này viết chơi cho dui
def category_list():
    cursor.execute("select * from category;")
    result = cursor.fetchall()
    headings = ['   Mã loại     ', '    Tên loại    ']
    window = show_List1(result, headings, "DANH SÁCH LOẠI THỨC UỐNG")
    i = -1
    while True:
        event, values = window.read()
        if event == '-TABLE-':
            i = values['-TABLE-'][0]
            window.close()
        if event == sg.WIN_CLOSED or event == "Thoát":
            break       
    window.close()
    return i+1 


# Quản lý bàn

#hàm kiểm tra giá trị id
def check(order_id, prod_id):
    db = connect()
    cursor = db.cursor()
    cursor.execute(f"select * from order_detail where id={order_id} and product_id={prod_id}")
    result = cursor.fetchall()
    if len(result) == 1:
        return 0
    return 1    

#thêm
def add_order(order_id, prod_id, price):
    db = connect()
    edit_product = [
        [sg.Text('NHẬP SỐ LƯỢNG')],
        [sg.Text('Số lượng:', size =(15, 1), font=myfont), sg.InputText(key='amount')],
        [sg.Button("Thêm"), sg.Button("Hủy")]
    ]
    window = sg.Window('UNDERTHENET COFFEE', edit_product)
    event, values = window.read()
    if values['amount'] == '': values['amount']=1
    while True:
        if event == "Thêm":
            if check(order_id, prod_id) == 1:
                cursor = db.cursor()
                total = price*int(values['amount'])
                cursor.execute(f"insert into order_detail(id, product_id, amount, price, total_price) values ({order_id},{prod_id},{values['amount']},{price},{total})")
                db.commit()
                break
            else:
                cur = db.cursor()
                cur.execute(f"select amount, price from order_detail where id={order_id} and product_id={prod_id}")
                res = cur.fetchall()
                amount = res[0][0]+int(values['amount'])
                total = res[0][1]*amount
                cursor = db.cursor()
                cursor.execute(f"update order_detail set amount={amount}, total_price={total} where id={order_id} and product_id={prod_id}")
                db.commit()
                break
        if event == sg.WIN_CLOSED or event == "Hủy":
            break
    window.close()

#thanh toán
def pay(table_id):
    try:
        db = connect()
        cursor = db.cursor()
        cursor.execute(f"select * from orders where table_id = {table_id} and paid=0")
        result = cursor.fetchall()
        cursor.callproc('proc_view_order',[result[0][1],])
        for order in cursor.stored_results():
            res = order.fetchall()
            L = [[] for i in range(len(res))]
            p = 0
            for x in res:
                for i in range(len(x)):
                    L[p].append(x[i])
                p += 1
        heading = [' Mã ', 'Tên thức uống', 'Số lượng', 'Đơn giá', 'Thành tiền']
        cursor.execute(f"select orders_view_money({result[0][0]}) as 'Thanh tien'")
        total = cursor.fetchall()
        cur = db.cursor()        
        cur.execute(f"update orders set total_price={total[0][0]}, paid=1 where table_id={table_id}")
        db.commit()
        cur.execute(f"select staff.fullname from staff where staff.id = (select staff_id from orders where orders.id = {result[0][0]})")
        staff = cur.fetchall()
        layout = [
            [sg.Text('HÓA ĐƠN THANH TOÁN', font=myfont)],
            [sg.Text(f'ID HÓA ĐƠN: {result[0][0]}', font=myfont)],
            [sg.Text(f'BÀN: {result[0][1]}', font=myfont)], 
            [sg.Text(f'NGÀY LẬP: {result[0][2]}', font=myfont)],
            [sg.Text(f'NHÂN VIÊN LẬP: {staff[0][0]}', font=myfont)],
            [sg.Table(values=L, headings=heading, max_col_width=50,
                        auto_size_columns=True,
                        justification='left',
                        num_rows=p,
                        alternating_row_color='royalblue4',
                        enable_events = True,
                        key='-TABLE-',
                        row_height=50,)],
            [sg.Text(f'TỔNG THANH TOÁN: {total[0][0]}', font=myfont)],
            [sg.Button("THOÁT")]            
        ]
        window = sg.Window('UNDERTHENET COFFEE', layout)
        event, values = window.read()    
        while True:         
            if event == sg.WIN_CLOSED or event == "THOÁT":
                cur.execute(f"update tab set stat=0 where id = {table_id}")
                db.commit()
                break
        window.close()
    except Error as e:
        print(e)
    finally:
        cursor.close()

#danh sách oder
def order_List(x, s, usr):
    headings = [' Mã ', 'Tên thức uống', 'Số lượng', 'Đơn giá', 'Tổng tiền']
    try:
        db = connect()     
        cursor = db.cursor()
        cursor.callproc('proc_view_order',[x,])
        for result in cursor.stored_results():
            re = result.fetchall()
        cursor1 = db.cursor()
        cursor1.execute('select id, title, price, content, id_cat from product')
        result = cursor1.fetchall()
        window = show_List1(re, result, headings, f"BÀN: {s}")   
        while True:
            event, values = window.read()
            if event == '-TABLE-':
                i = values['-TABLE-'][0]
                cur = db.cursor()
                cur.execute(f"select id, paid from orders where table_id = {x}")
                res = cur.fetchall()
                c = db.cursor()
                c.execute("select id from orders")
                r = c.fetchall()
                if len(res) == 0:   order_id = len(r)+1
                else:   order_id = res[len(res)-1][0] 
                if len(res) == 0 or res[len(res)-1][1] == 1:
                    cur1 = db.cursor()
                    cur1.execute(f"insert into orders(table_id, orders_date, total_price, paid, staff_id) values ({x}, '{today}', 0, 0, {usr})")
                    db.commit()
                    cur1.execute(f"select id from orders where table_id = {x} and paid != 1")
                    res1 = cur1.fetchall()
                    order_id = res1[0][0]
                add_order(order_id, result[i][0], result[i][2])
                cur.execute(f"update tab set stat=1 where id = {x}")
                db.commit()
                window.close()
                order_List(x, s, usr)
            if event == "Thanh toán" and len(re) > 0:
                pay(x)
                window.close()
                order_List(x, s, usr)
            if event == "Thoát":
                window.close()
            if event == sg.WIN_CLOSED:
                break
        window.close()
    except Error as e:
        print(e)
    finally:
        cursor.close()

#bàn trống
def tab_free(usr):
    db = connect()
    cursor = db.cursor()
    cursor.execute("select * from tab where stat = 0")
    headings = [' Mã ', '  Tên bàn  ', '  Số ghế  ', '  Trạng thái  ']
    window = show_List(cursor, headings, "DANH SÁCH BÀN TRỐNG")
    cursor.execute("select * from tab where stat = 0")
    result = cursor.fetchall()
    i = -1
    while True:
        event, values = window.read()
        if event == '-TABLE-':
            i = values['-TABLE-'][0]
            order_List(result[i][0], result[i][1], usr)
        if event == "Thoát":
            window.close()
        if event == sg.WIN_CLOSED:
            break
    window.close()
    tab_List(usr)

#danh sách bàn
def tab_List(usr):
    db = connect()
    cursor = db.cursor()    
    headings = [' Mã ', '  Tên bàn  ', '  Số ghế  ', '  Trạng thái  ']
    cursor.execute("select * from tab")
    window = show_List(cursor, headings, "DANH SÁCH BÀN")
    cursor.execute("select * from tab")
    result = cursor.fetchall()
    i = -1
    while True:
        event, values = window.read()
        if event == '-TABLE-':
            i = values['-TABLE-'][0]
            window.close()
            order_List(result[i][0], result[i][1], usr)
            tab_List(usr)
        if event == 'BÀN TRỐNG':
            window.close()
            tab_free(usr)
        if event == "Thoát":
            window.close()
        if event == sg.WIN_CLOSED:
            break
    window.close()


# quản lý thời gian làm việc


#thêm thời gian làm việc
def add_timekeeping():
    add_timekeeping_layout = [
        [sg.Text('THÊM THỜI GIAN LÀM VIỆC', font=myfont)],
        [sg.Text('Nhân viên:', size =(15, 1), font=myfont), sg.InputText(key='staff_id')],
        [sg.Text('Ngày làm việc:', size =(15, 1), font=myfont), sg.InputText(key='work_date', size=(10, 1)),
         sg.Text('Giờ bắt đầu:', size =(15, 1), font=myfont), sg.InputText(key='start_time', size=(8, 1)),
         sg.Text('Giờ kết thúc:', size =(15, 1), font=myfont), sg.InputText(key='end_time', size=(8, 1))],
        [sg.Text('Giờ làm thêm:', size =(15, 1), font=myfont), sg.InputText(key='overtime', size=(8, 1))],
        [sg.Cancel(button_color="Red", font=('Ariel', 10, 'bold')), sg.Submit(button_color="Green", font=('Ariel', 10, 'bold'))]
    ]

    window = sg.Window('UNDERTHENET COFFEE', add_timekeeping_layout)
    events, values = window.read()

    if events == "Submit":
        staff_id = values['staff_id']
        work_date = datetime.strptime(values['work_date'], "%Y-%m-%d").date()
        start_time = values['start_time']
        end_time = values['end_time']
        overtime = values['overtime']

        cursor.execute("""INSERT INTO timekeeping(staff_id, work_date, start_time, end_time, overtime) 
                          VALUES(%s, %s, %s, %s, %s)""",
                       (staff_id, work_date, start_time, end_time, overtime))
        db.commit()
        window.close()

    if events == sg.WIN_CLOSED or events == "Cancel":
        window.close()
    timekeeping_list()

#sửa
def edit_timekeeping(i, timekeeping):
    edit_timekeeping_layout = [
        [sg.Text('SỬA THÔNG TIN THỜI GIAN LÀM VIỆC', font=myfont)],
        [sg.Text('Nhân viên:', size =(15, 1), font=myfont), sg.InputText(timekeeping[1], key='staff_id')],
        [sg.Text('Ngày làm việc:', size =(15, 1), font=myfont), sg.InputText(timekeeping[2], key='work_date', size=(10, 1)),
         sg.Text('Giờ bắt đầu:', size =(15, 1), font=myfont), sg.InputText(timekeeping[3], key='start_time', size=(8, 1)),
         sg.Text('Giờ kết thúc:', size =(15, 1), font=myfont), sg.InputText(timekeeping[4], key='end_time', size=(8, 1))],
        [sg.Text('Giờ làm thêm:', size =(15, 1), font=myfont), sg.InputText(timekeeping[5], key='overtime', size=(8, 1))],
        [sg.Cancel(button_color="Red", font=('Ariel', 10, 'bold')), sg.Submit(button_color="Green", font=('Ariel', 10, 'bold'))]
    ]

    window = sg.Window('UNDERTHENET COFFEE', edit_timekeeping_layout)
    events, values = window.read()

    if events == "Submit":
        staff_id = values['staff_id']
        work_date = datetime.strptime(values['work_date'], "%Y-%m-%d").date()
        start_time = values['start_time']
        end_time = values['end_time']
        overtime = values['overtime']

        cursor.execute("""UPDATE timekeeping 
                          SET staff_id=%s, work_date=%s, start_time=%s, end_time=%s, overtime=%s 
                          WHERE id=%s""",
                       (staff_id, work_date, start_time, end_time, overtime, i))
        db.commit()
        window.close()

    if events == sg.WIN_CLOSED or events == "Cancel":
        window.close()
#xóa
def delete_timekeeping(i):
    cursor.execute("DELETE FROM timekeeping WHERE id = %s", (i,))
    db.commit()

# hàm nghỉ phép
def show_leave_request(staff_id):
    headings_leave = ['Mã', 'Nhân viên', 'Ngày nghỉ phép', 'Lý do', 'Trạng thái']
    cursor.execute("SELECT * FROM leave_request WHERE staff_id = %s", (staff_id,)) # Thực hiện truy vấn để lấy thông tin nghỉ phép của nhân viên
    leave_result = cursor.fetchall()
    # Tạo layout cho bảng hiển thị thông tin nghỉ phép
    leave_layout = [
        [sg.Text("THÔNG TIN NGHỈ PHÉP", justification='center', font="Ariel")],
        [sg.Table(values=leave_result, headings=headings_leave, max_col_width=25,
                  auto_size_columns=True,
                  justification='left',
                  num_rows=10,
                  alternating_row_color='royalblue4',
                  key='-LEAVE_TABLE-',
                  row_height=25)],
        [sg.Button("Đóng", font=('Ariel', 10, 'bold'))]
    ]

    leave_window = sg.Window('UNDERTHENET COFFEE', leave_layout)

    while True:
        leave_event, _ = leave_window.read()

        if leave_event == "Đóng" or leave_event == sg.WIN_CLOSED:
            leave_window.close()
            break 

#danh sách  
def timekeeping_list():
    headings = ['Mã', 'Nhân viên', 'Ngày làm việc', 'Bắt đầu', 'Kết thúc', 'Làm thêm']
    cursor.execute("SELECT * FROM timekeeping")
    result = cursor.fetchall()

    timekeeping_layout = [
        [sg.Text("DANH SÁCH THỜI GIAN LÀM VIỆC", justification='center', font="Ariel")],
        [sg.Table(values=result, headings=headings, max_col_width=25,
                  auto_size_columns=True,
                  justification='left',
                  num_rows=10,
                  alternating_row_color='royalblue4',
                  key='-TIMEKEEPING_TABLE-',
                  row_height=25)],
        [ [sg.Button("Thoát", button_color=("white", "red"), font=('Ariel', 10, 'bold')),
           sg.Button("Nghỉ phép", button_color=("white", "blue"), font=('Ariel', 10, 'bold')),
            sg.Button("Thêm"), sg.Button("Sửa"), sg.Button("Xóa")] ]
    ]
    

    timekeeping_window = sg.Window('UNDERTHENET COFFEE', timekeeping_layout)

    while True:
        event, values = timekeeping_window.read()
        if event == "Nghỉ phép" and values['-TIMEKEEPING_TABLE-']:
            print("Button 'Nghỉ phép' pressed")
            selected_index = values['-TIMEKEEPING_TABLE-'][0]
            selected_timekeeping = result[selected_index]
            show_leave_request(selected_timekeeping[1])
        if event == "Thêm":
            timekeeping_window.close()
            add_timekeeping()

        if event == "Sửa" and values['-TIMEKEEPING_TABLE-']:
            selected_index = values['-TIMEKEEPING_TABLE-'][0]
            selected_timekeeping = result[selected_index]
            edit_timekeeping(selected_timekeeping[0], selected_timekeeping)

        if event == "Xóa" and values['-TIMEKEEPING_TABLE-']:
            selected_index = values['-TIMEKEEPING_TABLE-'][0]
            selected_timekeeping_id = result[selected_index][0]
            delete_timekeeping(selected_timekeeping_id)
            cursor.execute("SELECT * FROM timekeeping")
            result = cursor.fetchall()  # Refresh the result after deletion

        if event == "Thoát" or event == sg.WIN_CLOSED:
            timekeeping_window.close()
            break
    timekeeping_window.close()

#QUẢN LÝ LƯƠNG

# Hàm lấy dữ liệu lương từ cơ sở dữ liệu
def get_salary_data():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM salary")
    salary_data = cursor.fetchall()
    db.close()
    return salary_data


# Hàm cập nhật dữ liệu lương trong cơ sở dữ liệu
def update_salary_data(staff_id, new_data):
    db = connect()
    cursor = db.cursor()
    cursor.execute("""
        UPDATE salary 
        SET base_salary=%s, bonus=%s, allowance=%s, tax_deduction=%s, total_salary=%s, hourly_rate=%s 
        WHERE staff_id=%s
    """, (new_data['base_salary'], new_data['bonus'], new_data['allowance'], 
          new_data['tax_deduction'], new_data['total_salary'], new_data['hourly_rate'], staff_id))
    db.commit()
    db.close()



# Hàm lấy dữ liệu nhân viên từ cơ sở dữ liệu
def get_staff_data():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT id, fullname FROM staff")
    staff_data = cursor.fetchall()
    db.close()
    return staff_data

# Hàm quản lý lương
def salary_management():
    salary_data = get_salary_data()  # Lấy dữ liệu lương từ cơ sở dữ liệu   
    staff_data = get_staff_data() # Lấy thông tin nhân viên để hiển thị tên nhân viên trong bảng
    headings = ['Mã nhân viên', 'Họ và tên', 'Lương cơ bản', 'Thưởng', 'Phụ cấp', 'Giảm trừ thuế', 'Lương tổng cộng', 'Mức giờ']
    # Tạo dòng dữ liệu cho bảng
    data_rows = []
    for record in salary_data:
        staff_info = next((info for info in staff_data if info[0] == record[0]), None)
        if staff_info:
            data_rows.append([staff_info[0], staff_info[1], *record[1:]])

    layout = [
        [sg.Text('QUẢN LÝ LƯƠNG', size=(25, 1), justification='center', font="Ariel 25")],
        [sg.Table(values=data_rows, headings=headings, auto_size_columns=True,
                  justification='left',
                  num_rows=min(25, len(data_rows)),
                  alternating_row_color='lightblue',
                  key='-TABLE-',
                  row_height=30,
                  display_row_numbers=False)],
        [sg.Button("CẬP NHẬT LƯƠNG", size=(15, 2)), sg.Button("QUAY LẠI", size=(15, 2))]
    ]

    window = sg.Window('UNDERTHENET COFFEE', layout)

    while True:
        event, values = window.read()

        if event == "CẬP NHẬT LƯƠNG":
            selected_row = values['-TABLE-'][0] if values['-TABLE-'] else None  # Lấy dòng được chọn từ bảng
            if selected_row is not None:          
                update_salary_window(salary_data[selected_row])  # Hiển thị cửa sổ cập nhật lương với thông tin của dòng được chọn

        if event == sg.WIN_CLOSED or event == "THOÁT" or event == "QUAY LẠI":
            break

    window.close()

# Hàm cập nhật lương
def update_salary_window(salary_record):
    headings = ['Thông tin', 'Chi tiết']
    staff_info = get_staff_data()
    staff_record = next((info for info in staff_info if info[0] == salary_record[0]), None)# Lấy thông tin của nhân viên từ bản ghi lương

    data_rows = [
        ['Mã nhân viên', staff_record[0], sg.Text(staff_record[0], key='staff_id')],
        ['Họ và tên', staff_record[1], sg.Text(staff_record[1], key='staff_name')],
        ['Lương cơ bản', salary_record[2], sg.Text(salary_record[2], key='base_salary')],
        ['Thưởng', salary_record[3], sg.Text(salary_record[3], key='bonus')],
        ['Phụ cấp', salary_record[4], sg.Text(salary_record[4], key='allowance')],
        ['Giảm trừ thuế', salary_record[5], sg.Text(salary_record[5], key='tax_deduction')],
        ['Lương tổng cộng', salary_record[6], sg.Text(salary_record[6], key='total_salary')],
        ['Mức giờ', salary_record[7], sg.Text(salary_record[7], key='hourly_rate')]
    ]

    layout = [
        [sg.Text(f'CẬP NHẬT LƯƠNG - {staff_record[1]}', size=(30, 1), font="Ariel 25")],
        [sg.Table(values=data_rows, headings=headings, auto_size_columns=True,
                  justification='left',
                  num_rows=min(25, len(data_rows)),
                  alternating_row_color='lightblue',
                  key='-TABLE-',
                  row_height=30,
                  display_row_numbers=False)],
        [sg.Button("CHỈNH SỬA", size=(15, 2)), sg.Button("HỦY", size=(15, 2))]
    ]
    

    window = sg.Window('UNDERTHENET COFFEE', layout)

    while True:
        event, values = window.read()

        if event == "CHỈNH SỬA":
            # Mở cửa sổ mới để chỉnh sửa các giá trị
            edit_layout = [
                [sg.Text(f'CẬP NHẬT LƯƠNG - {staff_record[1]}', size=(25, 1), font="Ariel 25")],
                [sg.Text('Lương cơ bản:'), sg.InputText(default_text=salary_record[2], key='base_salary')],
                [sg.Text('Thưởng:'), sg.InputText(default_text=salary_record[3], key='bonus')],
                [sg.Text('Phụ cấp:'), sg.InputText(default_text=salary_record[4], key='allowance')],
                [sg.Text('Giảm trừ thuế:'), sg.InputText(default_text=salary_record[5], key='tax_deduction')],
                [sg.Text('Lương tổng cộng:'), sg.InputText(default_text=salary_record[6], key='total_salary')],
                [sg.Text('Mức giờ:'), sg.InputText(default_text=salary_record[7], key='hourly_rate')],
                [sg.Button("LƯU THAY ĐỔI", size=(15, 2)), sg.Button("HỦY", size=(15, 2))]
            ]

            edit_window = sg.Window('UNDERTHENET COFFEE', edit_layout)

            while True:
                edit_event, edit_values = edit_window.read()

                if edit_event == "LƯU THAY ĐỔI":
                    # Lấy dữ liệu mới từ các ô input
                    updated_data = {
                        'base_salary': float(edit_values['base_salary']),
                        'bonus': float(edit_values['bonus']),
                        'allowance': float(edit_values['allowance']),
                        'tax_deduction': float(edit_values['tax_deduction']),
                        'total_salary': float(edit_values['total_salary']),
                        'hourly_rate': float(edit_values['hourly_rate'])
                    }
     
                    update_salary_data(staff_record[0], updated_data) # Cập nhật dữ liệu lương trong cơ sở dữ liệu
                    sg.popup('Dữ liệu đã được cập nhật!', title='Thông báo')
                    edit_window.close()
                    salary_management()
                    break

                if edit_event == sg.WIN_CLOSED or edit_event == "HỦY":
                    break

            edit_window.close()

        if event == sg.WIN_CLOSED or event == "HỦY":
            break

    window.close()

#BẢNG QUẢN LÝ CHÍNH
def coffee_managerment():
    layout1 = [
        [sg.Text("UNTHER DE NET COFFEE", size=(25, 1), justification='center', font="Ariel 25")],
        [sg.Button("NHÂN SỰ", size=(30,2), font="Ariel 20")],
        [sg.Button("MENU", size=(30,2), font="Ariel 20")],
        [sg.Button("BÀN", size=(30,2), font="Ariel 20")],
        [sg.Button("QUẢN LÝ LƯƠNG", size=(30,2), font="Ariel 20")],
        [sg.Button("CHẤM CÔNG", size=(30,2), font="Ariel 20")],
        [sg.Button("ĐĂNG XUẤT", button_color="Green", font=('Ariel', 10, 'bold')),
         sg.Button("THOÁT", button_color="Red", font=('Ariel', 10, 'bold'))]
    ]
    layout2 = [
        [sg.Text("UNTHER DE NET COFFEE", size=(25, 1), justification='center', font="Ariel 25")],
        [sg.Button("MENU", size=(30,2), font="Ariel 20")],
        [sg.Button("BÀN", size=(30,2), font="Ariel 20")],
        [sg.Button("CHẤM CÔNG", size=(30,2), font="Ariel 20")],
        [sg.Button("ĐĂNG XUẤT", button_color="Green", font=('Ariel', 10, 'bold')),
         sg.Button("THOÁT", button_color="Red", font=('Ariel', 10, 'bold'))]
    ]
    usr = login()
    if usr == '1':    layout = layout1
    else:   layout = layout2
    if int(usr) != 0:
        window = sg.Window('UNDERTHENET COFFEE', layout)
        while True:
            event, values = window.read()
            if event == "NHÂN SỰ":
                staff_List()
            if event == "MENU":
                product_List()
            if event == "BÀN":
                tab_List(usr)
            if event == "QUẢN LÝ LƯƠNG":
                salary_management()
            if event == "CHẤM CÔNG":
                timekeeping_list()
            if event == "ĐĂNG XUẤT":
                window.close()
                coffee_managerment()
            if event in (None, 'QUIT') or event == "THOÁT": # if user closes window or clicks cancel
                break
        window.close()

if __name__ == '__main__':
    coffee_managerment()