import pandas as pd
# writer = pd.ExcelWriter('application.xlsx', engine='xlsxwriter')
# writer.save()

print(".")

def xls_writer(json):
    # dataframe Name and Age columns
    df = pd.DataFrame(json)

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter('application.xlsx', engine='xlsxwriter')

    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name='Sheet1', index=False)

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()

def xls_read():
    reader = pd.read_excel(r'application.xlsx')


if __name__ == '__main__':
    xls_read()