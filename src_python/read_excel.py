import pandas as pd
from prettytable import PrettyTable

# Đọc dữ liệu từ file Excel và sắp xếp theo trường tên
data = pd.read_excel("Book1.xlsx")
data = data.sort_values(by=["Name"])

print(data)

def interpolation_search_all(arr, x):
    lo = 0
    hi = len(arr) - 1
    result = []
    
    while lo <= hi and x >= arr[lo]["Name"] and x <= arr[hi]["Name"]:
        pos = lo + int(((float(hi - lo) / (ord(arr[hi]["Name"][0]) - ord(arr[lo]["Name"][0]))) * (ord(x[0]) - ord(arr[lo]["Name"][0]))))

        if arr[pos]["Name"].lower().startswith(x.lower()):
            result.append((arr[pos]["ID"],arr[pos]["Name"], arr[pos]["Age"], arr[pos]["Address"]))
            i = pos - 1
            while i >= lo and arr[i]["Name"].lower().startswith(x.lower()):
                result.append((arr[i]["ID"],arr[i]["Name"],arr[i]["Age"], arr[i]["Address"]))
                i -= 1
            i = pos + 1
            while i <= hi and arr[i]["Name"].lower().startswith(x.lower()):
                result.append((arr[i]["ID"],arr[i]["Name"],arr[i]["Age"], arr[i]["Address"]))
                i += 1
            return result
        if arr[pos]["Name"] < x:
            lo = pos + 1
        else:
            hi = pos - 1

    return None

# Tìm kiếm thông tin của những người có tên bắt đầu bằng "P"
result = interpolation_search_all(data.to_dict("records"), "Phan")

# Xuất kết quả thành bảng
table = PrettyTable()
table.field_names = ["ID","Name", "Age", "Address"]

if result is not None and len(result) > 0:
    for r in result:
        table.add_row([r[0], r[1], r[2],r[3]])
else:
    table.add_row(["Không tìm thấy thông tin", "", "",""])

print(table)