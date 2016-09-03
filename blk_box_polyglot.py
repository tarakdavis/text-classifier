from sklearn.feature_extraction.text import CountVectorizer as CV
from sklearn.feature_extraction.text import TfidfTransformer as TF
from sklearn.naive_bayes import MultinomialNB as MNB
from sklearn.pipeline import Pipeline


english_list = ['the', 'of', 'and', 'a', 'to', 'in', 'is', 'you', 'that', 'it', 'he', 'was', 'for', 'on', 'are', 'as', 'with', 'his', 'they', 'I', 'at', 'be', 'this', 'have', 'from', 'or', 'one', 'had', 'by', 'word', 'but', 'not', 'what', 'all', 'were', 'we', 'when', 'your', 'can', 'said', 'there', 'use', 'an', 'each', 'which', 'she', 'do', 'how', 'their', 'if', 'will', 'up', 'there', 'about', 'out', 'many', 'then', 'them', 'these', 'so', 'some', 'her', 'would', 'make', 'like', 'him', 'into', 'time', 'has', 'look', 'two', 'more', 'write', 'go', 'see', 'number', 'no', 'way', 'could', 'people', 'my', 'than', 'first', 'water', 'been', 'call', 'who', 'oil', 'its', 'now', 'find', 'long', 'down', 'day', 'did', 'get', 'come', 'made', 'may', 'part']

spanish_list = ['el', 'la', 'de', 'que', 'y', 'a', 'en', 'un', 'ser', 'se', 'no', 'haber', 'por', 'con', 'su', 'para', 'como', 'estar', 'tener', 'le', 'lo', 'lo', 'todo', 'pero', 'más', 'hacer', 'o', 'poder', 'decir', 'este', 'ir', 'otro', 'ese', 'la', 'si', 'me', 'ya', 'ver', 'porque', 'dar', 'cuando', 'él', 'muy', 'sin', 'vez', 'mucho', 'saber', 'qué', 'sobre', 'mi', 'alguno', 'mismo', 'yo', 'también', 'hasta', 'año', 'dos', 'querer', 'entre', 'así', 'primero', 'desde', 'grande', 'eso', 'ni', 'nos', 'llegar', 'pasar', 'tiempo', 'ella', 'sí', 'día', 'uno', 'bien', 'poco', 'deber', 'entonces', 'poner', 'cosa', 'tanto', 'hombre', 'parecer', 'nuestro', 'tan', 'donde', 'ahora', 'parte', 'después', 'vida', 'quedar', 'siempre', 'creer', 'hablar', 'llevar', 'dejar', 'nada', 'cada', 'seguir', 'menos', 'nuevo', 'encontrar']

X_english_training_data = english_list
y_english_training_data = ['english'] * len(X_english_training_data)

sample_eng_text = """
That said, Ford has invested over $2 billion in India and plans to spend more to set up a global engineering center in the southern city of Chennai that will help tweak products for the local market and more swiftly adapt to changing consumer trends.
The carmaker is also ramping up exports, including to Europe, to maximize usage of its two plants in India.
"India is a key market for us in Asia Pacific," said the spokesman, adding that the carmaker is committed to introducing new products and technologies in the South Asian nation.
But instead of the bigger plan for the key markets of India and China, Ford will focus on updating existing models and develop and build more SUVs and crossovers, moving away from sedans and hatchbacks, the U.S. sources said.
That would allow the carmaker to boost profit margins.
"The global shift to crossovers makes competing in small cars a tough proposition for GM and Ford," said Sam Fiorani, vice president of global vehicle forecasting at U.S.-based AutoForecast Solutions.
"It makes more sense for them to refresh older products now, harness lower development costs in China in the mid-term, and move toward small crossovers over the long haul."
Chinese buyers have flocked to SUVs, as they grow wealthier and are often restricted to one vehicle in major cities, at the expense of contracting sedan sales.
SUV sales rose 52 percent last year, although a glut of new model launches in the segment is already leading to discounts and lower margins.
Growing competition in the small SUV segment from local Chinese carmakers is also putting more pressure on pricing.
"""
X_english_test_data = sample_eng_text.split()
print(len(X_english_test_data))
y_english_test_data = ['english'] * len(X_english_test_data)

py_pipeline = Pipeline([("count", CV()), ("tfid", TF()), ("multi", MNB())])

print(py_pipeline.fit(X_english_training_data, y_english_training_data))
print(py_pipeline.score(X_english_test_data, y_english_test_data))

print(py_pipeline.predict(X_english_test_data), "\n")  # this is real english text
# ===========================================
X_spanish_training_data = spanish_list
y_spanish_training_data = ['spanish'] * len(X_spanish_training_data)

print(py_pipeline.fit(X_spanish_training_data, y_spanish_training_data))
# print(py_pipeline.score(X_spanish_test_data, y_spanish_test_data))

print(py_pipeline.predict("porque es su madre un puta"))



for idx, each in enumerate(all_labels):
    X_train[idx]
self.y_train = [self.label] * len(self.X_train)
self.y_test = [self.label] * len(self.X_test)
