def process_revenue_report(order_list): 
    total_revenue = 0 
    successful_orders = 0
    for order in order_list:
        if order["status"] == "DELIVERED":
            total_revenue += order["fee"]
            successful_orders += 1
    if successful_orders > 0:
        avg_revenue = total_revenue / successful_orders
    else:
        avg_revenue = 0
    return { 
        "total_revenue": total_revenue,
        "successful_orders": successful_orders, 
        "avg_revenue": avg_revenue 
        }

order_data = [
    {"order_id": "01", "fee": 15000, "status": "DELIVERED"},
    {"order_id": "02", "fee": 20000, "status": "DELIVERED"},
    {"order_id": "03", "fee": 0, "status": "CANCELLED"},       # Đơn bị khách hủy
    {"order_id": "04", "fee": -5000, "status": "RETURNED"},    # Đơn hoàn phát sinh phí
    {"order_id": "05", "fee": 25000, "status": "DELIVERED"}
]
result = process_revenue_report(order_data)
print("=== BÁO CÁO DOANH THU ===") 
print(f"Tổng doanh thu: {result['total_revenue']:,}đ") 
print(f"Số đơn giao thành công: {result['successful_orders']} đơn") 
print( f"Doanh thu trung bình/đơn: " f"{result['avg_revenue']:,.0f}đ" )