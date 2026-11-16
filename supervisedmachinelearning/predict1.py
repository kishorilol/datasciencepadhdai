import pickle
model=pickle.load(open('multiplelinearreg.pkl','rb'))
def predictPrice():
    MedInc=float(input("Enter MedInc"))
    HouseAge=float(input("Enter HouseAge"))
    AveRooms=float(input("Enter AveRooms"))
    AveBedrms=float(input("Enter AveBedrms"))
    Population=float(input("Enter Population"))
    AveOccup=float(input("Enter AveOccup"))
    Latitude=float(input("Enter Latitude"))
    Longitude=float(input("Enter Longitude"))
    Price=model.predict([[MedInc,HouseAge,AveRooms,AveBedrms,Population,AveOccup,Latitude,Longitude]])
    print(Price)
while True:
    print('1 for predict any other key for exit')
    choice=int(input('Enter your Choise'))
    match choice:
        case 1:
            predictPrice()
        case _:
            break