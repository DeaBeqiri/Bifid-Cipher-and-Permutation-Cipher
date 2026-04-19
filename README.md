# Bifid Cipher and Permutation Cipher

## Permutation Cipher

### Enkriptimi
Permutation Cipher është një algoritëm klasik kriptografik që:
- Përdor një key (permutation e indekseve)
- Riorganizon karakteret sipas key-t
- Nuk ndryshon shkronjat, vetëm pozicionin
- Gjeneron ciphertext

### Dekriptimi
Procesi i kundërt:
- Përdoret inverse e key-t
- Karakteret vendosen në pozicionet origjinale
- Rikthehet teksti fillestar

### Shembull
Teksti: mystery  
Key: 2 0 3 1  
Output: smtyyexr  

---

## Bifid Cipher

### Enkriptimi
Bifid Cipher është një algoritëm që:
- Përdor një matricë 5x5 (Polybius Square)
- Shndërron shkronjat në koordinata
- Kombinon rreshtat dhe kolonat
- Gjeneron ciphertext

### Dekriptimi
Procesi i kundërt:
- Ciphertext kthehet në koordinata
- Ndahen në rreshta dhe kolona
- Rikthehet teksti origjinal

### Shembull
Teksti: soteshtedite  
Key: crypto  
Period: 5  
Output: mrstzfahzqrz  

---

## Vizualizimi

Projekti përfshin vizualizim grafik me Turtle:
- Tregon hapat e enkriptimit dhe dekriptimit
- Vizualizon lëvizjen e shkronjave
- Shërben si mjet edukativ

---

## Main Page

Mainpage është komponenti kryesor që:
- Menaxhon menunë
- Merr input nga përdoruesi
- Zgjedh algoritmin (Permutation ose Bifid)
- Thërret funksionet përkatëse
- Kontrollon vizualizimin

---

## Struktura e Projektit

- mainpage.py  
- permutation_cipher.py  
- bifid_encrypt.py  
- bifid_decrypt.py  
- visualization.py  