import sqlite3
import random
from base64 import b64encode
from objects.wallet import newWallet

names = ["Aaliyah", "Agnes", "Agneta", "Alberte", "Almira", "Amelia", "Anika", "Arvada", "Asta", "Astrid", "Belinde", "Dorothea", "Elise", "Ellinor", "Embla", "Grete", "Heidi", "Hella", "Jensine", "Jonna", "Karina", "Karyn", "Karen", "Katrine", "Kirsten", "Kirstine", "Lisbet", "Margareta", "Mari", "Mikaela", "Runa", "Terese", "Thrya", "Viola", "Ada", "Alba", "Ane", "Ase", "Elin", "Else", "Erika", "Eva", "Ida", "Lene", "Tove", "Vita", "Vivi", "Alma", "Anna", "Anne", "Clara", "Ella", "Emma", "Freja", "Isabelle", "Josefine", "Laura", "Liva", "Maja", "Olivia", "Rebekka", "Sofia", "Sofie", "Alvilda", "Birgit", "Birte", "Britt", "Caroline", "Gunda", "Karla", "Lovise", "Lulla", "Nanna", "Solvej", "Ulla", "Victoria", "Alfred", "Arne", "Axel", "Bendt", "Bertram", "Birger", "Bjorn", "Christen", "Christer", "Christian", "Edvin", "Frans", "Franz", "Frode", "Georg", "Gregers", "Gregos", "Hagen", "Hemming", "Jerrik", "Jesper", "Johan", "Joren", "Knud", "Kresten", "Madsen", "Mikkel", "Nikolai", "Oluf", "Odin", "Palle", "Rolf", "Ruben", "Salomon", "Soren", "Stefan", "Svante", "Aren", "Bo", "Dag", "Emil", "Jory", "Lars", "Nohr", "Orn", "Reno", "Tue", "Aksel", "August", "Casper", "Christiansen", "Elias", "Elliot", "Erling", "Felix", "Harald", "Jorgen", "Kai", "Lucas", "Milas", "Noah", "Oliver", "Oscar", "Peter", "Rasmus", "William", "Alexander", "Amberson", "Arthur", "Asmund", "Carl", "Edvard", "Einar", "Frederik", "Harald", "Magnus", "Malthe", "Sibbi", "Tore", "Thor", "Valdemar", "Victor", "Vidar", "Villads", "Vilmar", "Willamar"]

conn = con = sqlite3.connect('users.db')

cur = conn.cursor()

cur.execute('''CREATE TABLE users (name text, cpr text, publicKey text, privateKey text)''')

for i,name in enumerate(names):

    print(f"{str(i)}/{str(len(names))}")

    cpr = f"{random.randint(0,999999):06}-{random.randint(0,9999):04}"
    currentWallet = newWallet()
    publicKey, privateKey = b64encode(currentWallet.publicKey).decode("utf-8"), b64encode(currentWallet.privateKey).decode("utf-8")

    cur.execute(f"INSERT INTO users (name, cpr, publicKey, privateKey) VALUES ('{name}','{cpr}','{publicKey}','{privateKey}')")

conn.commit()
conn.close()
