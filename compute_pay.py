def compute_pay(hours, rate=7.25):
    try:
        hours = float(hours)
        rate = float(rate)
    except:
        print("Please enter a number greater than 0.")

    overtime_pay = 0 #assigned to ensure error-free calculation of total_pay

    if hours > 40:
        overtime_hours = hours - 40
        hours = hours - overtime_hours
        overtime_rate = rate * 1.5
        overtime_pay = overtime_hours * overtime_rate
        
    base_pay = hours * rate

    total_pay = base_pay + overtime_pay

    return total_pay
