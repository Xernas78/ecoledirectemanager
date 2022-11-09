import rich
import getpass
from EcoleDirecteManager import EcoleDirecteManager

user = input("Nom d'utilisateur : ")
password = getpass.getpass(prompt="Mot de passe : ")

manager = EcoleDirecteManager(user, password)

print("Voici votre moyenne : " + str(manager.totalAverage))
print("Voici la moyenne de la classe : " + str(manager.totalClassAverage))