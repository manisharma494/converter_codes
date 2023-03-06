from easy_exchange_rates import API


def currency_converter():
    api = API()
    enter_date = str(input("enter current date in YYYY-MM-DD format :"))            #2023-03-06
    amount_value = float(input("Enter amount: "))
    base_currency = str(input("Enter Base Currency: ")).upper()
    target_currency = str(input("Enter target Currency: ")).upper()
    time_series = api.get_exchange_rates(
        base_currency=base_currency,
        start_date=enter_date,
        end_date=enter_date,
        targets=[target_currency]
        )
    data_frame = api.to_dataframe(time_series)
    final_amount = data_frame * amount_value
    amount = final_amount[target_currency].to_list()
    for _ in amount:
        result = "{:.2f}".format(_)
        print(f"From : {base_currency} {amount_value}")
        print(f"To : {target_currency}")
        print(f" = {target_currency} {result}")
currency_converter()