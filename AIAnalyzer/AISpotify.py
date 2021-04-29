import pandas as pd
from sklearn.tree import DecisionTreeRegressor

music_data = pd.read_csv('spotifyDataRounded.csv')

X = music_data.drop(columns=['acouround','danceround','loudround','temporound','key'])
y = music_data[['acouround','danceround','loudround','temporound','key']]

model = DecisionTreeRegressor()
model.fit(X,y)
print(model.predict([[100]]))
array_results = model.predict([[100]])

acoustic = array_results[0,0]
dance = array_results[0,1]
loud = array_results[0,2]
tempo = array_results[0,3]
key = array_results[0,4]

if acoustic > 0.5:
    print("Acoustic")
else:
    print("Non-Acoustic")

if dance > 0.5:
    print("Danceable Songs")
else:
    print("Non-Danceable Songs")

if loud > -20:
    print("Louder Songs")
elif loud > -40:
    print("Moderate Volume Songs")
else:
    print("Quieter Songs")

#Tempo
if tempo > 120:
    print("High Tempo: ", tempo)
elif tempo > 100:
    print("Moderate Tempo: ", tempo)
else:
    print("Low Tempo: ", tempo)

key_array = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']
rounded_key = int(round(key,0))
print("Key of", key_array[rounded_key])
