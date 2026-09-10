PAY_PER_ORDER = 20_000
BONUS_RATE = 0.10
BONUS_THRESHOLD = 50

def calculate_driver_payout(transactions):
    result = {}

    for transaction in transactions:

        driver_id = transaction.get("driver_id")
        order_id = transaction.get("order_id")
        status = transaction.get("status")

        if not driver_id:
            print(f" Bỏ qua giao dịch {order_id}: thiếu driver_id")
            continue
        if not status:
            print(f" Bỏ qua giao dịch {order_id}: thiếu status")
            continue

        status = status.upper().strip()

        if driver_id not in result:
            result[driver_id] = {
                "delivered_count": 0,
                "base_payout": 0,
                "bonus": 0,
                "held_amount": 0,
                "total_payout": 0
            }

        driver = result[driver_id]

        if status == "DELIVERED":
            driver["delivered_count"] += 1
            driver["base_payout"] += PAY_PER_ORDER

        elif status == "DISPUTED":
            driver["held_amount"] += PAY_PER_ORDER
        elif status in ["CANCELLED", "RETURNED"]:
            continue
        else:
            print(
                f"Giao dịch {order_id} "
                f"có trạng thái không hợp lệ: {status}"
            )
    for driver_id, driver in result.items():
        if driver["delivered_count"] > BONUS_THRESHOLD:
            driver["bonus"] = (
                driver["base_payout"] * BONUS_RATE
            )
        else:
            driver["bonus"] = 0

        driver["total_payout"] = (driver["base_payout"]+ driver["bonus"])
    return result

transactions = [

    {
        "driver_id": "TX01",
        "order_id": "DH001",
        "status": "DELIVERED"
    },

    {
        "driver_id": "TX01",
        "order_id": "DH002",
        "status": "DELIVERED"
    },

    {
        "driver_id": "TX01",
        "order_id": "DH003",
        "status": "DISPUTED"
    },

    {
        "driver_id": "TX01",
        "order_id": "DH004",
        "status": "CANCELLED"
    },-

    {
        "driver_id": "TX02",
        "order_id": "DH005",
        "status": "DELIVERED"
    },

    {
        "driver_id": "TX02",
        "order_id": "DH006",
        "status": "DELIVERED"
    },

    {
        "driver_id": "TX02",
        "order_id": "DH007",
        "status": "DISPUTED"
    }
]

result = calculate_driver_payout(transactions)

print("       BÁO CÁO TỔNG CƯỚC THÙ LAO TÀI XẾ - MIS")
for driver_id, data in result.items():
    print()
    print(f"Tài xế: {driver_id}")
    print(
        f"Số đơn giao thành công : "
        f"{data['delivered_count']}"
    )

    print(
        f"Thù lao cơ bản         : "
        f"{data['base_payout']:,.0f}đ"
    )

    print(
        f"Tiền thưởng            : "
        f"{data['bonus']:,.0f}đ"
    )

    print(
        f"Tiền đang tạm giữ      : "
        f"{data['held_amount']:,.0f}đ"
    )

    print(
        f"TỔNG ĐƯỢC THANH TOÁN  : "
        f"{data['total_payout']:,.0f}đ"
    )

print()
print("Kết thúc báo cáo")