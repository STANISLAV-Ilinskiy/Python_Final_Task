# ������� DataFrame
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# ������� one-hot �����������
one_hot = pd.get_dummies(data['whoAmI'], prefix='whoAmI')

# ���������� � �������� DataFrame
data_encoded = pd.concat([data, one_hot], axis=1)

# ������� �������� ������� 'whoAmI'
data_encoded.drop(columns=['whoAmI'], inplace=True)

# ������� ���������
data_encoded.head()
