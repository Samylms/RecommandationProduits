def findProductByClient(idClient, rs_df):
    new = rs_df.loc[rs_df['CLI_ID'] == idClient]
    return new.index.values.tolist()


def countProductByClient(products):
    my_dict = {i: products.count(i) for i in products}
    return my_dict


def topProductByClient(products):
    bestProduct = sorted(products.items(), key=lambda x: x[1], reverse=True)
    return bestProduct[0]


def unique_counts(df):
    for i in df.columns:
        count = df[i].nunique()
        print(i, ": ", count)
    unique_counts(df)


def getColumn(df, column):
    return df[column].unique()
