def nhap_mang(n):
    arr = []
    for i in range(n):
        num = int(input("Nhập số nguyên thứ %d: " % (i + 1)))
        arr.append(num)
    return arr


def tinh_tong(arr, x):
    tong = 0
    for i in range(x + 1):
        tong = tong + int(arr[i])
    return tong


n = int(input("Nhập số lượng phần tử trong mảng: "))
mang = nhap_mang(n)

q = int(input("Nhập số lượng yêu cầu: "))
yeucaus = []
for i in range(q):
    x = int(input("Nhập số nguyên x thứ %d: " % (i + 1)))
    yeucaus.append(x)

for i, x in enumerate(yeucaus):
    tong = tinh_tong(mang, x)
    print("Tổng các số có index từ 0 đến %d là: %d" % (x, tong))