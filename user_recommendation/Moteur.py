import pandas as pd
from models.Produits import findProductByClient, countProductByClient, topProductByClient
from preprocess.CleanData import cleanData
from recommenders.ContentBased import contentBased, bagofwords, toString
import time



def process():
    idClient = input("\n""Enter your client ID : ")
    start = time.time()
    rs = True

    df_chunk = pd.read_csv(r'data/KaDo.csv', chunksize=20000)
    if not df_chunk:
         return "kado file not in data folder"
    while rs:
        # Each chunk is in df format
        for chunk in df_chunk:
            rs_df = cleanData(chunk)
            rs_df = bagofwords(rs_df)
            products = findProductByClient(int(idClient), rs_df)
            if not products:
                break
            else:
                nbProducts = countProductByClient(products)
                bestSeller = topProductByClient(nbProducts)
                recommendation = contentBased(rs_df, bestSeller[0])
                toString(recommendation, bestSeller)
                end = time.time()
                print("time elapsed {}".format(end - start))
                rs = False
                break


if __name__ == "__main__":
    process()