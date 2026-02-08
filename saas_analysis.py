


df=pd.read_csv("ravenstack_subscriptions.csv")
df.head()

df["start_date"]=pd.to_datetime(df["start_date"])
df["month"]= df['start_date'].dt.month
df["year"]=df['start_date'].dt.year


df[df['churn_flag'] == False].groupby(["month","year"])["mrr_amount"].sum().sort_values(ascending=False)
df["year"].value_counts()

df[df['churn_flag'] == False].shape[0]# aktif kullanıcı sayısı.

df[df['churn_flag'] == False]["mrr_amount"].sum()

df[df['churn_flag'] == False]["mrr_amount"].sum()/ df[df['churn_flag'] == False].shape[0]#ARRPU değeri.


df[df['churn_flag'] == False].groupby(["month","year"])["mrr_amount"].sum().sort_values(ascending=False)/df[df['churn_flag'] == False].shape[0]# yıllık ve aylık arrpu değeri.


churned=df[df["churn_flag"]== True].shape[0]

total=df.shape[0]#tooplam kullanıcı sayısı.

churn_rate = churned / total  #DÖNÜŞÜM ORANI.



#LTV
df[df['churn_flag'] == False]["mrr_amount"].sum()/ df[df['churn_flag'] == False].shape[0]/0.0972






mrr_monthly = (
    df[df['churn_flag'] == False].groupby(['year','month'])['mrr_amount']
    .sum()
    .reset_index()
)

plt.figure()
plt.plot(mrr_monthly['month'], mrr_monthly['mrr_amount'])
plt.title("Aylık MRR")
plt.xlabel("Ay")
plt.ylabel("MRR")
plt.show()



churn_monthly = (
    df.groupby(['year','month'])['churn_flag']
    .mean()
    .reset_index()
)

plt.figure()
plt.bar(churn_monthly['month'], churn_monthly['churn_flag'])
plt.title("Aylık Churn Oranı")
plt.xlabel("Ay")
plt.ylabel("Churn Rate")
plt.show()



