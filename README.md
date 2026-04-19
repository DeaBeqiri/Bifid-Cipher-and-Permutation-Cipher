# Bifid-Cipher-and-Permutation-Cipher

Permutation Cipher (Enkriptim)
Permutation Cipher është një algoritëm klasik kriptografik që:

Përdor një key (permutation e indekseve)
Çdo shkronjë e tekstit riorganizohet sipas key-t
Karakteret nuk zëvendësohen, vetëm ndryshojnë pozicion
Krijohet një tekst i enkriptuar (ciphertext)

Permutation Cipher (Dekriptim)

Procesi i kundërt:

Përdoret inverse e key-t
Karakteret vendosen në pozicionet origjinale
Rikrijohet teksti fillestar


Shembuj ekzekutimi
Enkriptim
Teksti: mystery
Key: 2 0 3 1
Output: smtyyexr

Dekriptim
Input:
Ciphertext: (outputi i mësipërm)
Key: 2 0 3 1
Output: mystery

Shënime:
Key duhet të jetë permutation valide (pa përsëritje)
Algoritmi punon vetëm me pozicione, jo me ndryshim shkronjash
Hapësirat zakonisht hiqen ose injorohen në implementim

-------------------------

Bifid Cipher (Enkriptim)
Bifid Cipher është një algoritëm klasik kriptografik që:

Përdor një 5x5 Polybius Square
Çdo shkronjë shndërrohet në koordinata (rresht, kolonë)
Të gjitha rreshtat dhe kolonat kombinohen
Nga këto krijohet teksti i enkriptuar
 Bifid Cipher (Dekriptim)

Procesi i kundërt:

Ciphertext kthehet në koordinata
Koordinatat ndahen në rreshta dhe kolona
Kombinohen përsëri për të marrë tekstin origjinal


Shembuj ekzekutimi
Enkriptim
Teksti: soteshtedite
Key: crypto
Period: 5
Output: mrstzfahzqrz

Dekriptim
Ciphertext: (outputi i mësipërm)
Key: crypto
Period: 5
Output: soteshtedite
Shënime:
Shkronja "j" zëvendësohet me "i"
Hapësirat dhe karakteret jo-alfabetike hiqen
Algoritmi punon vetëm me shkronja

---------------------------

Vizualizimi (Visualization)
Ky projekt përfshin edhe vizualizim grafik me Turtle:

Tregon hapat e enkriptimit dhe dekriptimit
Shfaq lëvizjen e shkronjave sipas key-t
Vizualizon procesin hap pas hapi për të kuptuar algoritmin
Punon si mjet edukativ për kriptografi

---------------------------

Main Page (mainpage.py)

Mainpage është pjesa kryesore e programit dhe funksionon si “kontroller” i gjithë sistemit të cipher-ave.

Roli i mainpage:
- Menaxhon menunë kryesore të programit
- Merr input nga përdoruesi (tekst, key, zgjedhje)
- Vendos cilin algoritëm të përdorë (Permutation ose Bifid)
- Thërret funksionet nga file të tjerë
- Kontrollon nëse përdoruesi dëshiron vizualizim
- Koordinon gjithë rrjedhën e programit

Struktura e Mainpage

Menu kryesore
Programi fillon me një menu ku përdoruesi zgjedh:

1. Permutation Cipher
2. Bifid Cipher
0. Exit

Çdo opsion e dërgon përdoruesin në një funksion të veçantë.

---------------------------

Struktura e projektit
mainpage.py – Menu kryesore dhe kontrolli i programit
permutation_cipher.py – Implementimi i Permutation Cipher
bifid_encrypt.py – Enkriptimi i Bifid Cipher
bifid_decrypt.py – Dekriptimi i Bifid Cipher
visualization.py – Animimet me Turtle Graphics