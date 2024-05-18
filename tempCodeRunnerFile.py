   layout = [
        [sg.Text(f'CẬP NHẬT LƯƠNG - {staff_record[1]}', size=(25, 1), font="Ariel 25")],
        [sg.Table(values=data_rows, headings=headings, auto_size_columns=True,
                  justification='left',
                  num_rows=min(25, len(data_rows)),
                  alternating_row_color='lightblue',
                  key='-TABLE-',
                  row_height=30,
                  display_row_numbers=False)],
        [sg.Button("CHỈNH SỬA", size=(15, 2)), sg.Button("HỦY", size=(15, 2))]
    ]
    
    layout = [
    [sg.Text('', size=(25, 1))],  # Dòng trống để tạo khoảng cách
    *layout,  # Bảng và các phần khác
    [sg.Text('', size=(25, 1))]  # Dòng trống cuối cùng để tạo khoảng cách
]