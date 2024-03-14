# Создаем DataFrame
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создаем one-hot кодирование
one_hot = pd.get_dummies(data['whoAmI'], prefix='whoAmI')

# Объединяем с исходным DataFrame
data_encoded = pd.concat([data, one_hot], axis=1)

# Удаляем исходный столбец 'whoAmI'
data_encoded.drop(columns=['whoAmI'], inplace=True)

# Выводим результат
data_encoded.head()
