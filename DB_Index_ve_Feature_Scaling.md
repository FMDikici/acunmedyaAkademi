
# Davies-Bouldin İndeksi Nedir?

Davies-Bouldin (DB) İndeksi, kümeleme algoritmalarının ne kadar başarılı olduğunu ölçmek için kullanılan bir değerlendirme yöntemidir. Temel olarak, kümelerin birbirinden ne kadar farklı ve kendi içlerinde ne kadar tutarlı olduğunu ölçer.

## Nasıl Çalışır?

- Her küme için kendi içindeki yayılım (benzerlik) ve diğer kümelere olan uzaklık hesaplanır.
- Bu değerlere göre kümeler arası farklar bulunur.
- Sonuçta 0’a yakın bir DB indeksi, iyi kümelenmiş veri anlamına gelir. Yani kümeler birbirinden uzak ve içlerinde tutarlıdır.

## Python Uygulaması

```python
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import davies_bouldin_score

# Veri seti oluşturalım
X, _ = make_blobs(n_samples=300, centers=3, random_state=42)

# K-Means kümeleme
kmeans = KMeans(n_clusters=3, random_state=42)
labels = kmeans.fit_predict(X)

# Davies-Bouldin skoru
db_score = davies_bouldin_score(X, labels)
print("Davies-Bouldin Skoru:", db_score)
```

---

# Özellik Ölçekleme (Feature Scaling) Nedir?

Veri setindeki sayısal özelliklerin birbirinden çok farklı ölçeklerde olması bazı algoritmaların doğru çalışmamasına neden olabilir. Bu yüzden veriler benzer ölçeklere getirilmelidir. Bu işleme **özellik ölçekleme** denir.

## Neden Gerekli?

- Özellikle KNN, K-Means gibi mesafeye dayalı algoritmalarda ölçü birimleri algoritmayı etkileyebilir.
- Ölçeklenmemiş veriler, bazı özelliklerin modelde baskın hale gelmesine yol açar.

## Yaygın Yöntemler

### 1. Min-Max Scaling (Normalization)

Verileri 0 ile 1 arasına çeker.

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
```

### 2. Standardizasyon (Z-Score)

Verilerin ortalaması 0, standart sapması 1 olacak şekilde dönüşüm yapar.

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

### 3. Robust Scaling

Aykırı değerlere karşı daha dayanıklı bir yöntemdir.

```python
from sklearn.preprocessing import RobustScaler

scaler = RobustScaler()
X_scaled = scaler.fit_transform(X)
```

---

**Not:** Özellik ölçekleme, modelden önce uygulanan bir ön işlem adımıdır ve modelin başarımını önemli ölçüde etkileyebilir.
