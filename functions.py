import pandas as pd

def save_as_csv():
    code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0]
    # print(code_df)

    code_df.종목코드 = code_df.종목코드.map('{:06d}'.format)

    code_df = code_df[['회사명', '종목코드']]

    code_df = code_df.rename(columns={'회사명': 'name', '종목코드': 'code'})
    # print(code_df)
    # print(type(code_df))

    code_df.to_csv('code_df.csv')

def get_url(stock_name, code_df):
    code = code_df.query("name=='{}'".format(stock_name))['code'].to_string(index=False)
    code = code.zfill(6)
    print(stock_name + ": " + code)

    url = 'http://finance.naver.com/item/sise_day.nhn?code={code}'.format(code=code)
    # print("URL = {}".format(url))

    return url

def draw_plot(stock_name, df):
    import matplotlib.pyplot as plt
    from matplotlib import font_manager, rc

    # YOU HAVE TO CHANGE FOLLOWING LINE
    ## for macOS - sample
    # font_location = '/Library/Fonts/NanumBarunGothic.otf'
    ## for Windows - sample
    font_location = 'C:/Windows/Fonts/NanumBarunGothic.ttf'

    font_name = font_manager.FontProperties(fname=font_location).get_name()

    rc('font', family=font_name)

    plt.plot(df.date, df.close)

    plt.title(stock_name)
    plt.xlabel('Date')
    plt.ylabel('Close')

    plt.show()
