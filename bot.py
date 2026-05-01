import discord
import random
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

liste1 = [
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
liste2 = [
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
liste3 = [
            "Catégories X : ", 
            "Titres de films nuls (inventés) : ", 
            "Motifs de rupture : ", 
            "Noms de chat : ", 
            "Noms de drag queen : ",
            "Synonymes de 'pénis' (existants ou inventés) : ", 
            "Insultes : ", 
            "Mots rares ou bizarres : "
            ]


@client.event
async def on_ready():
    print(f"Connecté en tant que {client.user}")


@client.event
async def on_message(message):
    # Ignore les autres bots
    if message.author.bot:
        return

    # Vérifie si le message commence par - et mentionne le bot
    content = message.content.strip()
    bot_mention = f"<@{client.user.id}>"

    if not content.startswith("-") or bot_mention not in content:
        return

    selection1 = random.sample(liste1, 6)
    selection2 = random.sample(liste2, 2)
    selection3 = random.sample(liste3, 2)

    tirage = selection1 + selection2 + selection3
    random.shuffle(tirage)

    lignes = ["**Sélection :**"]
    for e in tirage:
        lignes.append(e)

    await message.reply("\n".join(lignes))


client.run(os.environ["TOKEN"])
