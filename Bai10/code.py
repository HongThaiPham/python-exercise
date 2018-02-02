'''
Câu hỏi:

Viết một chương trình có 2 chữ số, X, Y nhận giá trị từ đầu vào và tạo ra một mảng 2 chiều. Giá trị phần tử trong hàng thứ i và cột thứ j của mảng phải là i*j.

Lưu ý: i=0,1,...,X-1; j=0,1,...,Y-1. 

Ví dụ: Giá trị X, Y nhập vào là 3,5 thì đầu ra là: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

Gợi ý:

Viết lệnh để nhận giá trị X, Y từ giao diện điều khiển do người dùng nhập vào.
'''

xy = input("nhapX,Y: ")
dimentions = [int(x) for x in xy.split(",")]
rowNum = dimentions[0]
colNum = dimentions[1]

mang2chieu = [[0 for col in range(colNum)] for row in range(rowNum)]

for row in range(rowNum):
    for col in range(colNum):
        mang2chieu[row][col] = row*col

print(mang2chieu)
