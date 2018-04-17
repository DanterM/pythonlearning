import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
train_df = pd.read_csv('lsoa-data1.csv')
print(train_df)