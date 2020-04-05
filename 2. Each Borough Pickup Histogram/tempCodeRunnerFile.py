for i in enumerate(df["pickup_dt"]):
    # print(i)
    modified_date = datetime.datetime.strptime(i[1], "%Y-%m-%d %H:%M:%S").date()
    all_date.append(modified_date)