# arr = ["Taj Mahal", "Gateway of India", "India Gate", "Golden Temple", "Hawa Mahal", "Charminar", 'Meenakshi Temple', "Akshardham Temple", 'Somnath Temple', "Agra Fort", "City Palace Udaipur", "Victoria Memorial", "Khajuraho Temple", "Ajanta & Ellora Cave", "Amer Fort", "Lotus Temple", "Qutub Minar", "Brihadishwara Temple", "Dilwara Temple", "Sanchi Stupa", "Jantar Mantar", "Kashi Vishwanath Temple", "Sun Temple", "Nalanda University", "Red Fort", "Jantar Mantar Delhi", "Rashtrapati Bhavan"]

# print(len(arr))
import os
#DirA files have .jpg extension
dir_a = []
#DirB files have .json extension
dir_b = []
for fileA in os.listdir("object_data_1\\images\\train"):
  dir_a.append(fileA.split('.')[0])
for fileB in os.listdir("object_data_1\\labels\\train"):
  dir_b.append(fileB.split('.')[0])

for fileA in dir_a:
  if not fileA in dir_b:
    try:
        os.remove(os.path.join("object_data_1\\images\\train",(fileA+'.jpg')))
        print("done")
    except:
        print("Error")