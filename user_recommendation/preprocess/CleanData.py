def cleanData(rs_df):
    columnSpec = ["MAILLE", "UNIVERS", "LIBELLE"]
    columnSpace = ["MAILLE", "UNIVERS", "FAMILLE"]
    columnLower = ["MAILLE", "UNIVERS", "FAMILLE", "LIBELLE"]

    if rs_df.empty:
        print("Data frame empty")
    else:
        for i in columnSpec:
            rs_df = removeSpecialCarac(rs_df, i)

        for i in columnSpace:
            rs_df = removeSpace(rs_df, i)

        for i in columnLower:
            rs_df = toLowercase(rs_df, i)

        print(rs_df)
    return rs_df


def removeSpecialCarac(rs_df, column):
    spec_chars = ["!", '"', "#", "%", "&", "'", "(", ")",
                  "*", "+", ",", "-", ".", "/", ":", ";", "<",
                  "=", ">", "?", "@", "[", "\\", "]", "^", "_",
                  "`", "{", "|", "}", "~", "–"]

    for char in spec_chars:
        rs_df[column] = rs_df[column].str.replace(char, ' ')
    return rs_df


def removeSpace(rs_df, column):
    rs_df[column] = rs_df[column].str.replace(" ", "")
    return rs_df


def toLowercase(rs_df, column):
    rs_df[column] = rs_df[column].str.lower()
    return rs_df


def toInt32(rs_df, columns):
    rs_df[columns] = rs_df[columns].astype('int32')


def toString(rs_df, column):
    rs_df[column] = rs_df[column].astype('string')
