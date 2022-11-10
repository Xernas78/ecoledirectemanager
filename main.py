import rich
import getpass
from EcoleDirecteManager import EcoleDirecteManager

user = input("Nom d'utilisateur : ")
password = getpass.getpass(prompt="Mot de passe : ")

manager = EcoleDirecteManager(user, password)
