#!/usr/bin/env python
# coding: utf-8

# In[13]:


import matplotlib.pyplot as plt
animali = ["Leone", "Orso", "tigri", "scimmie", "zebre"]
numero_animali = [4,3,2,8,15]
plt.bar(animali, numero_animali, color="lightblue")
plt.show()


# In[12]:


import matplotlib.pyplot as plt
animali = ["Leone", "Orso", "tigri", "scimmie", "zebre"]
numero_animali = [4,3,2,8,15]
plt.bar(animali, numero_animali, color="lightblue")
plt.title("Numero di animali in uno zoo")
plt.xlabel("Animali")
plt.ylabel("Numero")

plt.show()


# In[15]:


import matplotlib.pyplot as plt
mese = ["gennaio", "febbraio", "marzo", "aprile", "maggio"]
temperatura_media = [14,8,11,20,22]
plt.plot(mese, temperatura_media, marker="s", linestyle="-", color="lightpink")
plt.title("andamento temp. mensili")
plt.xlabel("mese")
plt.ylabel("temp. media (c°)")
plt.grid(True, axis="y")
plt.show()


# In[4]:


vendite_mensili={
    "gen":1200,
    "feb":1000,
    "mar":3300,
    "apr":4555
}
plt.bar(vendite_mensili.keys(), vendite_mensili.values(), color="blue")
plt.show()


# In[17]:


colori= ["gold", "lightcoral", "lightskyblue", "lightgreen", "pink"]
mese = ["gennaio", "febbraio", "marzo", "aprile", "maggio"]
temperatura_media = [14,8,11,20,22]
plt.pie(temperatura_media, labels=mese, colors=colori) #dati, colori (ordine così)
plt.title("Percentuale di temp media mensile")
plt.show()


# In[18]:


import matplotlib.pyplot as plt

colori = ["gold", "lightcoral", "lightskyblue", "lightgreen", "pink"]
mese = {
    "gennaio": 14,
    "febbraio": 8,
    "marzo": 11,
    "aprile": 20,
    "maggio": 22
}

plt.pie(mese.values(), labels=mese.keys(), colors=colori)
plt.title('Percentuale di temperatura media mensile')
plt.show()


# In[7]:


import matplotlib.pyplot as plt
eta = [14,15,16,17,18,19]
altezza = [160,165,170,175,180,185]
plt.scatter(eta,altezza,color="red",marker="o")
plt.title("Scatter Riot - eta vs altezza")
plt.xlabel("Eta")
plt.ylabel("altezza cm")
plt.grid(True)
plt.show()


# In[22]:


import matplotlib.pyplot as plt
nomi_studenti = ['Francesco', 'Valentina', 'Stefano', 'David', 'Alessio']
punteggi = [85, 92, 70, 88, 95]

plt.barh(nomi_studenti, punteggi, color='lightgreen')
plt.title('punteggi studenti')
plt.xlabel("punteggi")
plt.ylabel("nomi")
plt.show()


# In[23]:


import matplotlib.pyplot as plt
import pandas as pd

nomi_studenti = ['Francesco', 'Valentina', 'Stefano', 'David', 'Alessio']
punteggi = [85, 92, 70, 88, 95]

#crea un dataframe con nomi e punteggi
data = {'nome dello studente': nomi_studenti, 'punteggio': punteggi}
df = pd.DataFrame(data)
#ordina il ataframe per punteggio in ordine crescente
df.sort_values(by='punteggio', inplace=True)
df


# In[24]:


plt.barh(df['nome dello studente'], df['punteggio'], color='lightgreen')
plt.title('punteggi studenti')
plt.xlabel("punteggi")
plt.ylabel("nomi")
plt.show()


# In[26]:


import matplotlib.pyplot as plt
import pandas as pd

nomi_studenti = ['Francesco', 'Valentina', 'Stefano', 'David', 'Alessio']
punteggi = [85, 92, 70, 88, 95]

#crea un dataframe con nomi e punteggi
data = {'nome dello studente': nomi_studenti, 'punteggio': punteggi}
df = pd.DataFrame(data)
#ordina il ataframe per punteggio in ordine crescente
df.sort_values(by='punteggio', inplace=False)

plt.barh(df['nome dello studente'], df['punteggio'], color='lightgreen')
plt.title('punteggi studenti')
plt.xlabel("punteggi")
plt.ylabel("nomi")
plt.show()


# In[ ]:




