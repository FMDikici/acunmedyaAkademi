
# 🌳 Decision Tree ve Random Forest Algoritmaları

## 1. Decision Tree (Karar Ağacı)

### 🔹 Tanım
Decision Tree, verileri sınıflandırmak veya tahmin etmek için kullanılan, ağaç yapısında bir gözetimli öğrenme algoritmasıdır. Her düğüm bir özelliğe dayalı bir karardır, yaprak düğümler ise sınıfları temsil eder.

### 🔹 Nasıl Çalışır?
1. En iyi özelliği belirle (örneğin, Gini Impurity, Entropy gibi ölçütlerle).
2. Veriyi bu özelliğe göre dallara ayır.
3. Her dal için aynı işlem tekrarlanır.
4. Belirli bir duruma ulaşıldığında (örneğin maksimum derinlik, minimum örnek sayısı) durulur.

### 🔹 Avantajları
- Kolay anlaşılır ve yorumlanabilir.
- Hem sayısal hem kategorik verilerle çalışabilir.
- Özellik ölçeklendirmesi gerekmez.

### 🔹 Dezavantajları
- Aşırı öğrenme (overfitting) riski yüksektir.
- Verideki küçük değişiklikler ağacı büyük ölçüde değiştirebilir.

### 🔹 Kullanım Alanları
- Kredi riski analizi
- Hastalık teşhisi
- Müşteri segmentasyonu

---

## 2. Random Forest (Rassal Orman)

### 🔹 Tanım
Random Forest, birden fazla karar ağacının birleşiminden oluşan bir topluluk (ensemble) yöntemidir. Her ağaç rastgele bir veri altkümesi ve özellik altkümesiyle eğitilir ve sonuçlar birleştirilir.

### 🔹 Nasıl Çalışır?
1. Eğitim verisinden rastgele örnekler (bootstrapping) ile alt kümeler oluşturulur.
2. Her alt küme ile ayrı bir Decision Tree eğitilir.
3. Tahmin aşamasında:
   - Sınıflandırmada: Ağaçların oy çokluğu alınır.
   - Regresyonda: Ağaçların ortalaması alınır.

### 🔹 Avantajları
- Aşırı öğrenmeyi azaltır.
- Genellikle yüksek doğruluk sağlar.
- Verideki eksikliklere karşı daha dayanıklıdır.

### 🔹 Dezavantajları
- Eğitim süresi daha uzundur.
- Modelin yorumlanması tek bir ağaç kadar kolay değildir.

### 🔹 Kullanım Alanları
- Sahtekarlık tespiti
- Borsa tahmini
- Görüntü tanıma

---

## 3. Karşılaştırma Tablosu

| Özellik              | Decision Tree           | Random Forest            |
|----------------------|-------------------------|--------------------------|
| Basitlik             | ✅ Kolay                 | ❌ Daha karmaşık         |
| Aşırı Öğrenme Riski  | ⚠️ Yüksek                | ✅ Düşük                 |
| Doğruluk             | ❌ Düşük olabilir         | ✅ Genelde daha yüksek   |
| Yorumlanabilirlik    | ✅ Yüksek                | ❌ Daha zor              |
| Hesaplama Maliyeti   | ✅ Düşük                 | ❌ Daha yüksek           |

---

## 4. Python ile Örnek Kod

### Decision Tree
```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

iris = load_iris()
X, y = iris.data, iris.target

model = DecisionTreeClassifier()
model.fit(X, y)
```
