
def getAllClient(df):
    return df['CLI_ID'].unique()


def getAllTicketClient(df):
    return df['TICKET_ID'].unique()


# Trouver un client en fonction de l'input client
def getProfil(input_clientID, df):
    df_copy = df.copy(deep = True)
    df_copy['PRIX_TOTAL'] = df_copy.groupby(['CLI_ID'])['PRIX_NET'].transform('sum')
    filter = df_copy["CLI_ID"]== int(input_clientID)
    df_profil = df_copy.where(filter)
    return df_profil.dropna()


