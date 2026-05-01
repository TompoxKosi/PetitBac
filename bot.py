import discord
from discord import app_commands
import random
import os

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

liste_1 = [
            "Villes : ", 
            "Monuments et sites historiques ou naturelles : ", 
            "Cours/étendues d'eau (rivières, lacs, mers, ...) : ", 
            "Animaux : ", 
            "Plantes et champignons : ", 
            "Métiers : ",
            "Couleurs et teintes : ", 
            "Plats cuisinés : ", 
            "Boissons (pas de marque) : ",
            "Fromages et épices : ", 
            "Prénoms : ", 
            "Célébrités (nom de famille/pseudo) : ",
            "Personnages fictifs : ", 
            "Marques : ", 
            "Matériaux : ", 
            "Véhicules et moyens de transport : ", 
            "Vêtements et accessoires : ",
            "Sports : ",
            "Titres de films/série (web/audio)/émission : ",
            "Titres de roman/BD/pièce de théâtre : ", 
            "Titres de musique/album : ", 
            "Titres de jeu vidéo : "
            ]
liste_2 = [
            "Choses qui vont par pair : ", 
            "Choses qui tiennet dans la main : ", 
            "Choses qui rentrent dans autre chose  : ",
            "Choses qui sont recouvertes de quelque chose : ", 
            "Choses qui se plient : ", 
            "Choses qui s'empilent : ", 
            "Choses avec un ou des pieds : ",
            "Choses avec un ou des trous", 
            "Choses à la verticale : ", 
            "Choses à l'horizontal : "
            ]
liste_3 = [
            "Catégories X : ", 
            "Titres de films nuls (inventés) : ", 
            "Motifs de rupture : ", 
            "Noms de chat : ", 
            "Noms de drag queen : ",
            "Synonymes de 'pénis' (existants ou inventés) : ", 
            "Insultes : ", 
            "Mots rares ou bizarres : "
            ]

@tree.command(name="petitbac", description="Génère une sélection de 10 éléments")
async def petitbac(interaction: discord.Interaction):
    selection1 = random.sample(liste_1, 6)
    selection2 = random.sample(liste_2, 2)
    selection3 = random.sample(liste_3, 2)

    tirage = selection1 + selection2 + selection3
    random.shuffle(tirage)

    lignes = ["**Sélection :**"]
    for e in tirage:
        lignes.append(e)

    await interaction.response.send_message("\n".join(lignes))

@client.event
async def on_ready():
    await tree.sync()
    print(f"Connecté en tant que {client.user}")

client.run(os.environ["TOKEN"])
