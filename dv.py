# Gán các dịch vụ (Service) cho các số lựa chọn
DICH_VU = {
    "1": "Dịch vụ Tải xuống Báo cáo (Report Download)",
    "2": "Dịch vụ Chuyển đổi Định dạng (Format Conversion)",
    "3": "Dịch vụ Phân tích Dữ liệu (Data Analysis)"
}

print("Chào mừng đến với Hệ thống Đặt hàng Dịch vụ Tự động!")
print("Vui lòng chọn một trong các dịch vụ sau:")
for key, value in DICH_VU.items():
    print(f"[{key}] {value}")

# --- Bước 1: Chọn dịch vụ ---
while True:
    lua_chon = input("\nVui lòng nhập số dịch vụ bạn muốn (1, 2, hoặc 3): ")
    if lua_chon in DICH_VU:
        print(f"Bạn đã chọn: **{DICH_VU[lua_chon]}**")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")

# --- Bước 2: Nhập liên kết hoặc ID cần xử lý ---
link_id = input(f"Vui lòng nhập **Liên kết/ID** cho {DICH_VU[lua_chon]}: ")

# --- Bước 3: Nhập số lượng hoặc đơn vị cần xử lý ---
while True:
    try:
        so_luong = int(input("Vui lòng nhập **Số lượng/Đơn vị** cần xử lý: "))
        if so_luong > 0:
            break
        else:
            print("Số lượng phải là số nguyên dương.")
    except ValueError:
        print("Đầu vào không hợp lệ. Vui lòng chỉ nhập số.")

# --- Bước 4: Tóm tắt đơn hàng ---
print("\n" + "="*40)
print("✅ **TÓM TẮT ĐƠN HÀNG CỦA BẠN** ✅")
print(f"Dịch vụ: **{DICH_VU[lua_chon]}**")
print(f"Liên kết/ID: **{link_id}**")
print(f"Số lượng: **{so_luong}**")
print("Đơn hàng của bạn đã được ghi nhận và đang được xử lý...")
print("="*40)
