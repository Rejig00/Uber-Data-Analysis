for row in df.iterrows():
#     row[1]["pickup_dt"] = datetime.datetime.strptime(row[1]["pickup_dt"], "%Y-%m-%d %H:%M:%S").date().month
#     all_month.append(row[1]["pickup_dt"])
# df["pickup_dt"] = all_month
# new_df = pd.pivot_table(df, index=["pickup_dt", "borough"], values=['pickups'], aggfunc=np.sum)