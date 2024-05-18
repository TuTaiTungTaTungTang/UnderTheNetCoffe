	-- Tao database

	CREATE DATABASE CoffeeShopManagement;
	USE CoffeeShopManagement;
	SET GLOBAL log_bin_trust_function_creators = 1;
	SET SQL_SAFE_UPDATES = 0;


	-- Tao tables
	CREATE TABLE category (
		id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
		title NVARCHAR(50) NOT NULL,
		UNIQUE (title)
	);
	CREATE TABLE product (
		id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
		title NVARCHAR(150),
		price FLOAT,
		created_at DATE,
		updated_at DATE,
		content TEXT,
		id_cat INT,
		FOREIGN KEY (id_cat) REFERENCES category(id),
		UNIQUE (title)
	);
	CREATE TABLE staff (
		id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
		fullname NVARCHAR(100),
		birthday DATE,
		address NVARCHAR(100),
		phone_number VARCHAR(15),
		email NVARCHAR(100),
		education_profile TEXT,
		pw VARCHAR(16),
		position NVARCHAR(100),
		UNIQUE (email),
		UNIQUE (phone_number)
	);
	CREATE TABLE tab (
		id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
		tabname NVARCHAR(100),
		slot INT,
		stat INT
	);
	CREATE TABLE orders (
		id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
		table_id INT,
		orders_date DATE,
		total_price FLOAT,
		paid INT,
		staff_id INT,
		FOREIGN KEY (table_id) REFERENCES tab(id),
		FOREIGN KEY (staff_id) REFERENCES staff(id)
	);
	CREATE TABLE order_detail (
		id INT,
		product_id INT,
		amount INT,
		price FLOAT,
		total_price INT,
		FOREIGN KEY (id) REFERENCES orders(id),
		FOREIGN KEY (product_id) REFERENCES product(id)
	);
	CREATE TABLE timekeeping (
		id INT PRIMARY KEY AUTO_INCREMENT,
		staff_id INT,
		work_date DATE,
		start_time TIME,
		end_time TIME,
		overtime FLOAT,
		FOREIGN KEY (staff_id) REFERENCES staff(id)
	);
	CREATE TABLE salary (
		id INT PRIMARY KEY AUTO_INCREMENT,
		staff_id INT,
		base_salary DECIMAL(10, 2),
		bonus DECIMAL(10, 2),
		allowance DECIMAL(10, 2),
		tax_deduction DECIMAL(10, 2),
		total_salary DECIMAL(10, 2),
		hourly_rate DECIMAL(10, 2),
		FOREIGN KEY (staff_id) REFERENCES staff(id)
	);

	-- Bước 1: Tạo bảng cho việc quản lý nghỉ phép
	CREATE TABLE leave_request (
		id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
		staff_id INT,
		leave_date DATE,
		reason TEXT,
		status INT
	);

	-- Bước 2: Thêm dữ liệu cho yêu cầu nghỉ phép
	INSERT INTO leave_request (staff_id, leave_date, reason, status)
	VALUES
		(1, '2023-11-15', 'Nghỉ phép gia đình', 0),
		(2, '2023-11-17', 'Nghỉ phép cá nhân', 0),
		(3, '2023-11-20', 'Nghỉ phép sức khỏe', 0);

	-- Bước 3: Cập nhật trạng thái yêu cầu nghỉ phép (ví dụ: từ chối hoặc chấp nhận)
	-- Điều này có thể được thực hiện bằng cách sử dụng các thủ tục hoặc câu lệnh SQL riêng biệt.

	-- Thêm thông tin loại sản phẩm
	INSERT INTO category (title)
	VALUES
		('Trà'),
		('Cà Phê'),
		('Nước Ép'),
		('Nước Ngọt'),
		('Khác');
		
	-- Thêm thông tin sản phẩm
	INSERT INTO product (title, price, created_at, updated_at, content, id_cat)
	VALUES
		('Trà đào', 16000, '2023-01-10', '2023-01-20', 'abcxyz', 1),
		('Hồng trà', 16000, '2023-01-10', '2023-01-20', 'abcxyz', 1),
		('Trà Lipton', 16000, '2023-01-10', '2023-01-20', 'abcxyz', 1),
		('Cà phê đá', 18000, '2023-01-10', '2023-01-20', 'abcxyz', 2),
		('Cà phê sữa đá', 22000, '2023-01-10', '2023-01-20', 'abcxyz', 2),
		('Bạc xỉu', 22000, '2023-01-10', '2023-01-20', 'abcxyz', 2),
		('Nước ép cam', 20000, '2023-01-10', '2023-01-20', 'abcxyz', 3),
		('Nước ép ổi', 20000, '2023-01-10', '2023-01-20', 'abcxyz', 3),
		('Nước ép dưa hấu', 20000, '2023-01-10', '2023-01-20', 'abcxyz', 3),
		('Coca Cola', 18000, '2023-01-10', '2023-01-20', 'abcxyz', 4),
		('Pepsi', 18000, '2023-01-10', '2023-01-20', 'abcxyz', 4),
		('7 Up', 18000, '2023-01-10', '2023-01-20', 'abcxyz', 4),
		('Warior', 18000, '2023-01-10', '2023-01-20', 'abcxyz', 4),
		('Sữa chua đá', 22000, '2023-01-10', '2023-01-20', 'abcxyz', 5),
		('Cacao đá xay', 22000, '2023-01-10', '2023-01-20', 'abcxyz', 5);
		-- Thêm thông tin bàn
	INSERT INTO tab (tabname, slot, stat)
	VALUES
		('BET1', 6, 1),
		('BET2', 6, 1),
		('BET3', 6, 1),
		('BET4', 6, 1),
		('LAU1', 4, 0),
		('LAU2', 4, 0),
		('LAU3', 2, 1),
		('LAU4', 2, 1);
		
	insert into staff(fullname,birthday,address,pw,phone_number, email, education_profile,position)
	values
	('Huỳnh Tú Tài','2003-09-21','An Giang','123', '0939554486','taib2105559@student.ctu.edu.vn','Sinh viên Trường CNTT&TT','quản lý'),
	('Văn Tiến Lộc','2003-08-01','Vĩnh Long','234', '0123456789','locb2105550@student.ctu.edu.vn','Sinh viên Trường CNTT&TT','nhân viên'),
	('Nguyễn Văn Mặn','2003-03-11','Kiên Giang','345', '0987654321','Manb2105550@student.ctu.edu.vn','Sinh viên Trường CNTT&TT','nhân viên'),
	('Đỗ Trung Kiên','2003-08-27','Sóc Trăng','456', '0543216789','kienb2105558@student.ctu.edu.vn','Sinh viên Trường CNTT&TT', 'nhân viên');
	-- Thêm thông tin đơn đặt hàng

	INSERT INTO orders (table_id, orders_date, total_price, paid, staff_id)
	VALUES
		(1, '2023-05-10', 32000, 0, 1),
		(2, '2023-05-10', 16000, 0, 2),
		(3, '2023-05-10', 48000, 0, 1),
		(4, '2023-05-10', 54000, 0, 3),
		(7, '2023-05-10', 16000, 1, 3),
		(8, '2023-05-10', 56000, 0, 4);

		
	-- Thêm thông tin chi tiết đơn đặt hàng
	INSERT INTO order_detail (id, product_id, amount, price, total_price)
	VALUES
		(1, 2, 2, 16000, 32000),
		(2, 1, 1, 16000, 16000),
		(3, 2, 3, 16000, 48000),
		(4, 3, 3, 18000, 54000),
		(5, 1, 1, 16000, 16000),
		(6, 3, 1, 16000, 16000),
		(6, 4, 1, 18000, 18000),
		(6, 6, 1, 22000, 22000);
	-- Thêm thông tin lương cho nhân viên có ID là 1
	INSERT INTO salary (staff_id, base_salary, bonus, allowance, tax_deduction)
	VALUES 
		(1, 3000.00, 500.00, 200.00, 400.00),
		(2, 3200.00, 600.00, 250.00, 450.00),
		(3, 3500.00, 550.00, 210.00, 420.00),
		(4, 3300.00, 520.00, 220.00, 430.00);
	-- Thêm thông tin chấm công
	INSERT INTO timekeeping (staff_id, work_date, start_time, end_time, overtime)
	VALUES
		(1, '2023-11-10', '08:00:00', '16:00:00', 0),
		(2, '2023-11-10', '09:00:00', '17:00:00', 0),
		(3, '2023-11-10', '08:30:00', '16:30:00', 1),
		(4, '2023-11-10', '09:15:00', '16:15:00', 0);


	ALTER TABLE salary
	ADD COLUMN total_salary DECIMAL(10, 2) NOT NULL,
	ADD COLUMN hourly_rate DECIMAL(10, 2) NOT NULL;


	-- Sử dụng hàm CalculateHourlyRate để tính và cập nhật hourly_rate cho từng nhân viên trong bảng salary
	UPDATE salary AS s
	JOIN (
		SELECT s.staff_id, SUM(IFNULL(TIMESTAMPDIFF(SECOND, tk.start_time, tk.end_time) / 3600, 0)) AS total_work_hours
		FROM salary AS s
		LEFT JOIN timekeeping AS tk ON s.staff_id = tk.staff_id
		GROUP BY s.staff_id
	) AS calculated_rates
	ON s.staff_id = calculated_rates.staff_id
	SET s.hourly_rate = s.base_salary / calculated_rates.total_work_hours;

	-- hàm thủ tục: Liệt kê thông tin gọi món của một bàn
	delimiter $
	create procedure proc_view_order(idTab int)
	begin
		select product.id, product.title, order_detail.amount, order_detail.price, order_detail.total_price from product, order_detail
		where product.id = order_detail.product_id and order_detail.id = (select id from orders
																			where orders.table_id = idTab and orders.paid != 1);
	end$

	-- Hien thi tong tien
	delimiter $
	create function orders_view_money(order_id int)
	returns float
	begin
		declare tp float;
		select sum(total_price) into tp
		from order_detail
			where order_detail.id = order_id;
		return tp;
	end$

	-- Procedure để tính toán lương hàng tháng cho nhân viên dựa trên thời gian làm việc:
DELIMITER //
CREATE PROCEDURE CalculateMonthlySalary_final(staffId INT, month INT, year INT)
BEGIN
    DECLARE baseSalary DECIMAL(10, 2);
    DECLARE bonus DECIMAL(10, 2);
    DECLARE allowance DECIMAL(10, 2);
    DECLARE taxDeduction DECIMAL(10, 2);
    DECLARE hourlyRate DECIMAL(10, 2);
    DECLARE monthlySalary DECIMAL(10, 2);
    DECLARE totalWorkHours DECIMAL(10, 2);
    DECLARE totalOvertimeHours DECIMAL(10, 2);
    DECLARE overtimeRate DECIMAL(10, 2);

    -- Lấy các giá trị từ bảng salary
    SELECT IFNULL(base_salary, 0), IFNULL(bonus, 0), IFNULL(allowance, 0), IFNULL(tax_deduction, 0), IFNULL(hourly_rate, 0)
    INTO baseSalary, bonus, allowance, taxDeduction, hourlyRate
    FROM salary
    WHERE staff_id = staffId;

    -- Tính tổng số giờ làm việc trong tháng và năm cụ thể
    SELECT IFNULL(SUM(TIMESTAMPDIFF(SECOND, start_time, end_time) / 3600), 0) INTO totalWorkHours
    FROM timekeeping
    WHERE staff_id = staffId
    AND MONTH(work_date) = month
    AND YEAR(work_date) = year;

    -- Tính tổng số giờ làm thêm giờ trong tháng và năm cụ thể
    SELECT IFNULL(SUM(overtime), 0) INTO totalOvertimeHours
    FROM timekeeping
    WHERE staff_id = staffId
    AND MONTH(work_date) = month
    AND YEAR(work_date) = year;

    -- Tính lương hàng tháng dựa trên các giá trị này
    SET overtimeRate = hourlyRate * 1.5; -- Giả sử giờ làm thêm giờ có mức lương là 1.5 lần giờ làm thường
    SET monthlySalary = baseSalary + bonus + allowance - taxDeduction + (totalWorkHours * hourlyRate) + (totalOvertimeHours * overtimeRate);

    -- Cập nhật giá trị lương hàng tháng vào bảng salary
    UPDATE salary
    SET total_salary = monthlySalary
    WHERE staff_id = staffId;
END;
//
DELIMITER ;

-- procedure cho Trigger để tự động tính lương hàng tháng khi có thông tin thời gian làm việc mới:
 

DELIMITER $
CREATE PROCEDURE CalculateMonthlySalaryWithOvertime(staffId INT, month INT, year INT)
BEGIN
    DECLARE baseSalary DECIMAL(10, 2);
    DECLARE bonus DECIMAL(10, 2);
    DECLARE allowance DECIMAL(10, 2);
    DECLARE taxDeduction DECIMAL(10, 2);
    DECLARE hourlyRate DECIMAL(10, 2);
    DECLARE totalWorkHours DECIMAL(10, 2);
    DECLARE monthlySalary DECIMAL(10, 2);
    DECLARE totalOvertimeHours DECIMAL(10, 2);
    DECLARE overtimeRate DECIMAL(10, 2);

    -- Retrieve salary components from the salary table
    SELECT IFNULL(base_salary, 0), IFNULL(bonus, 0), IFNULL(allowance, 0), IFNULL(tax_deduction, 0), IFNULL(hourly_rate, 0)
    INTO baseSalary, bonus, allowance, taxDeduction, hourlyRate
    FROM salary
    WHERE staff_id = staffId;

    -- Calculate total work hours in the specified month and year
    SELECT IFNULL(SUM(TIMESTAMPDIFF(SECOND, start_time, end_time) / 3600), 0) INTO totalWorkHours
    FROM timekeeping
    WHERE staff_id = staffId
    AND MONTH(work_date) = month
    AND YEAR(work_date) = year;

    -- Calculate total overtime hours in the specified month and year
    SELECT IFNULL(SUM(overtime), 0) INTO totalOvertimeHours
    FROM timekeeping
    WHERE staff_id = staffId
    AND MONTH(work_date) = month
    AND YEAR(work_date) = year;

    -- Assume overtime rate is 1.5 times the hourly rate (you can adjust this as needed)
    SET overtimeRate = hourlyRate * 1.5;

    -- Calculate monthly salary including overtime
    SET monthlySalary = baseSalary + bonus + allowance - taxDeduction + (totalWorkHours * hourlyRate) + (totalOvertimeHours * overtimeRate);

    -- Update the total salary in the salary table
    UPDATE salary
    SET total_salary = monthlySalary
    WHERE staff_id = staffId;
END;
$
DELIMITER ;



 -- Trigger để tự động tính lương hàng tháng khi có thông tin thời gian làm việc mới:
DELIMITER //
CREATE TRIGGER CalculateMonthlySalaryTrigger
AFTER INSERT ON timekeeping
FOR EACH ROW
BEGIN
    DECLARE staffId INT;
    DECLARE month INT;
    DECLARE year INT;

    -- Lấy staff_id, tháng và năm từ thông tin thời gian làm việc mới được thêm vào
    SET staffId = NEW.staff_id;
    SET month = MONTH(NEW.work_date);
    SET year = YEAR(NEW.work_date);

    -- Gọi Procedure để tính lương hàng tháng
    CALL CalculateMonthlySalaryWithOvertime(staffId, month, year);
END;
//
DELIMITER ;

-- hàm tính lương tháng
DELIMITER //
CREATE FUNCTION CalculateMonthlySalaryForStaff(staffId INT, month INT, year INT)
RETURNS DECIMAL(10, 2)
BEGIN
    DECLARE baseSalary DECIMAL(10, 2);
    DECLARE bonus DECIMAL(10, 2);
    DECLARE allowance DECIMAL(10, 2);
    DECLARE taxDeduction DECIMAL(10, 2);
    DECLARE hourlyRate DECIMAL(10, 2);
    DECLARE monthlySalary DECIMAL(10, 2);
    DECLARE totalWorkHours DECIMAL(10, 2);
    DECLARE totalOvertimeHours DECIMAL(10, 2);
    DECLARE overtimeRate DECIMAL(10, 2);

    -- Lấy các giá trị từ bảng salary
    SELECT base_salary, bonus, allowance, tax_deduction, hourly_rate
    INTO baseSalary, bonus, allowance, taxDeduction, hourlyRate
    FROM salary
    WHERE staff_id = staffId;

    -- Tính tổng số giờ làm việc trong tháng và năm cụ thể
    SELECT IFNULL(SUM(TIMESTAMPDIFF(SECOND, start_time, end_time) / 3600), 0) INTO totalWorkHours
    FROM timekeeping
    WHERE staff_id = staffId
    AND MONTH(work_date) = month
    AND YEAR(work_date) = year;

    -- Tính tổng số giờ làm thêm giờ trong tháng và năm cụ thể
    SELECT IFNULL(SUM(overtime), 0) INTO totalOvertimeHours
    FROM timekeeping
    WHERE staff_id = staffId
    AND MONTH(work_date) = month
    AND YEAR(work_date) = year;

    -- Tính lương hàng tháng dựa trên các giá trị này
    SET overtimeRate = hourlyRate * 1.5; -- Giả sử giờ làm thêm giờ có mức lương là 1.5 lần giờ làm thường
    SET monthlySalary = baseSalary + bonus + allowance - taxDeduction + (totalWorkHours * hourlyRate) + (totalOvertimeHours * overtimeRate);

    RETURN monthlySalary;
END;
//
DELIMITER ;
SELECT CalculateMonthlySalaryForStaff(2, 11, 2023);


-- Procedure để xem thông tin lương của nhân viên:

DELIMITER //
CREATE PROCEDURE ViewSalary(staff_id INT)
BEGIN
    SELECT *
    FROM salary
    WHERE staff_id = staff_id;
END;
//
DELIMITER ;

 
 -- Procedure để thêm thông tin chấm công:
DELIMITER //
CREATE PROCEDURE ClockIn(staff_id INT, work_date DATE, start_time TIME, end_time TIME)
BEGIN
    INSERT INTO timekeeping (staff_id, work_date, start_time, end_time)
    VALUES (staff_id, work_date, start_time, end_time);
END;
//
DELIMITER ;

 
-- Procedure để quản lý nghỉ phép:

DELIMITER //
CREATE PROCEDURE LeaveManagement(staff_id INT, leave_date DATE, reason TEXT, status INT)
BEGIN
    INSERT INTO leave_request (staff_id, leave_date, reason, status)
    VALUES (staff_id, leave_date, reason, status);
END;
//
DELIMITER ;

-- Procedure để liệt kê thông tin nhân viên:

DELIMITER //
CREATE PROCEDURE ListStaffInfo()
BEGIN
    SELECT id, fullname, birthday, address, phone_number, email, education_profile, position
    FROM staff;
END;
//
DELIMITER ;


-- Tạo một trigger trước khi chèn (BEFORE INSERT) để kiểm tra xem email được chèn có đúng định dạng không.
DELIMITER //
CREATE TRIGGER check_email_format
BEFORE INSERT ON staff
FOR EACH ROW
BEGIN
    DECLARE email_regex VARCHAR(100);
    SET email_regex = '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$';

    IF NEW.email REGEXP email_regex = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Email không đúng định dạng';
    END IF;
END;
//
DELIMITER ;


-- kiểm tra xem số điện thoại phải bắt đầu bằng "0" và phải có đúng 10 chữ số.
DELIMITER //
CREATE TRIGGER check_phone_number_format
BEFORE INSERT ON staff
FOR EACH ROW
BEGIN
    DECLARE phone_regex VARCHAR(100);
    SET phone_regex = '^(0[0-9]{9,9})$';

    IF NEW.phone_number REGEXP phone_regex = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Số điện thoại không đúng định dạng';
    END IF;
END;
//
DELIMITER ;

-- Tạo một trigger để kiểm tra độ dài của mật khẩu
DELIMITER //
CREATE TRIGGER check_password_length
BEFORE INSERT ON staff
FOR EACH ROW
BEGIN
    IF LENGTH(NEW.pw) < 3 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Mật khẩu phải có ít nhất 3 ký tự';
    END IF;
END;
//
DELIMITER ;

-- Tạo một trigger để kiểm tra định dạng ngày tháng của ngày sinh
DELIMITER //
CREATE TRIGGER check_birthday_format
BEFORE INSERT ON staff
FOR EACH ROW
BEGIN
    DECLARE birthday_regex VARCHAR(100);
    SET birthday_regex = '^\d{4}-\d{2}-\d{2}$';

    IF NEW.birthday REGEXP birthday_regex = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Ngày sinh phải theo định dạng YYYY-MM-DD';
    END IF;
END;
//
DELIMITER ;

-- transaction 
-- Bước 1: Bắt đầu một giao dịch
START TRANSACTION;

-- Bước 2: Thực hiện các câu lệnh SQL
-- Tạo đơn đặt hàng
INSERT INTO orders (table_id, orders_date, total_price, paid, staff_id)
VALUES (5, '2023-11-15', 24000, 0, 2);

-- Lấy ID của đơn đặt hàng vừa tạo
SELECT LAST_INSERT_ID() INTO @order_id;

-- Tạo chi tiết đơn đặt hàng
INSERT INTO order_detail (id, product_id, amount, price, total_price)
VALUES (@order_id, 3, 2, 12000, 24000);

-- Bước 3: Kết thúc giao dịch
COMMIT;

-- Hoặc hủy giao dịch nếu có lỗi xảy ra
-- ROLLBACK;

#hàm thêm vào CLockIn

DELIMITER $
CREATE PROCEDURE CalculateMonthlySalaryWithOvertime(staffId INT, month INT, year INT)
BEGIN
    DECLARE baseSalary DECIMAL(10, 2);
    DECLARE bonus DECIMAL(10, 2);
    DECLARE allowance DECIMAL(10, 2);
    DECLARE taxDeduction DECIMAL(10, 2);
    DECLARE hourlyRate DECIMAL(10, 2);
    DECLARE totalWorkHours DECIMAL(10, 2);
    DECLARE monthlySalary DECIMAL(10, 2);
    DECLARE totalOvertimeHours DECIMAL(10, 2);
    DECLARE overtimeRate DECIMAL(10, 2);

    -- Retrieve salary components from the salary table
    SELECT IFNULL(base_salary, 0), IFNULL(bonus, 0), IFNULL(allowance, 0), IFNULL(tax_deduction, 0), IFNULL(hourly_rate, 0)
    INTO baseSalary, bonus, allowance, taxDeduction, hourlyRate
    FROM salary
    WHERE staff_id = staffId;

    -- Calculate total work hours in the specified month and year
    SELECT IFNULL(SUM(TIMESTAMPDIFF(SECOND, start_time, end_time) / 3600), 0) INTO totalWorkHours
    FROM timekeeping
    WHERE staff_id = staffId
    AND MONTH(work_date) = month
    AND YEAR(work_date) = year;

    -- Calculate total overtime hours in the specified month and year
    SELECT IFNULL(SUM(overtime), 0) INTO totalOvertimeHours
    FROM timekeeping
    WHERE staff_id = staffId
    AND MONTH(work_date) = month
    AND YEAR(work_date) = year;

    -- Assume overtime rate is 1.5 times the hourly rate (you can adjust this as needed)
    SET overtimeRate = hourlyRate * 1.5;

    -- Calculate monthly salary including overtime
    SET monthlySalary = baseSalary + bonus + allowance - taxDeduction + (totalWorkHours * hourlyRate) + (totalOvertimeHours * overtimeRate);

    -- Update the total salary in the salary table
    UPDATE salary
    SET total_salary = monthlySalary
    WHERE staff_id = staffId;
END;
$
DELIMITER ;







