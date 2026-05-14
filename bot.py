import discord
from discord import app_commands
import random
import os
import threading
import urllib.request
import json
from datetime import datetime, timezone
from pathlib import Path
from listes import liste_1, liste_2, liste_3

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

FICHIER_DONNEES = "donnees.json"

def charger_donnees():
    if Path(FICHIER_DONNEES).exists():
        with open(FICHIER_DONNEES, "r") as f:
            return json.load(f)
    return {"tentatives": {}, "gagnant": {"date": None, "user_id": None}}

def sauvegarder_donnees(donnees):
    with open(FICHIER_DONNEES, "w") as f:
        json.dump(donnees, f)

messages_perdant = [
    "Désolé {mention}, tu n'as pas les cramptés aujourd'hui, essaie une autre fois.",
    "Bien essayé {mention}, mais ça ne sera pas pour cette fois...",
    "Pas de chance {mention}, tu n'as pas les cramptés, retente ta chance demain !",
    "Raté {mention}, les cramptés t'ont glissé entre les doigts pour cette fois...",
    "Dommage {mention}, tu es crampté-less aujourd'hui...",
]

@tree.command(name="cramptés", description="Est-ce que tu les as ?")
async def xxx(interaction: discord.Interaction):
    aujourd_hui = str(datetime.now(timezone.utc).date())
    user_id = str(interaction.user.id)
    mention = interaction.user.mention

    donnees = charger_donnees()

    # Vérifie si quelqu'un a déjà gagné aujourd'hui
    if donnees["gagnant"]["date"] == aujourd_hui:
        if donnees["gagnant"]["user_id"] == user_id:
            await interaction.response.send_message(
                f"Tu sais déjà que tu as gagné {mention}, pas besoin de retenter aujourd'hui !"
            )
        else:
            gagnant_mention = f"<@{donnees['gagnant']['user_id']}>"
            await interaction.response.send_message(
                f"Désolé {mention}, {gagnant_mention} a déjà gagné aujourd'hui. Il faudra réessayer demain !"
            )
        return

    # Vérifie si cette personne a déjà tenté aujourd'hui
    if donnees["tentatives"].get(user_id) == aujourd_hui:
        await interaction.response.send_message(
            f"Tu sais déjà que tu n'as pas les cramptés aujourd'hui, {mention}, reviens demain."
        )
        return

    # Enregistre la tentative
    donnees["tentatives"][user_id] = aujourd_hui

    # Tirage
    if random.randint(1, 6) == 1:
        donnees["gagnant"]["date"] = aujourd_hui
        donnees["gagnant"]["user_id"] = user_id
        sauvegarder_donnees(donnees)
        await interaction.response.send_message(
            f" Bravo {mention}, c'est toi qui as les cramptés aujourd'hui !"
        )
    else:
        sauvegarder_donnees(donnees)
        message = random.choice(messages_perdant).format(mention=mention)
        await interaction.response.send_message(message)

@tree.command(name="acab", description="Génère une sélection de 10 éléments")
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

@tree.command(name="lettre", description="Génère une lettre aléatoire")
async def lettre(interaction: discord.Interaction):
    lettre_aleatoire = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    await interaction.response.send_message(f"**Lettre : {lettre_aleatoire}**")

@tree.command(name="ping", description="Vérifie si le bot est en ligne")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Les cramptés sont ouverts !")

@client.event
async def on_ready():
    await tree.sync()
    print(f"Connecté en tant que {client.user}")

def keep_alive():
    def ping():
        while True:
            try:
                urllib.request.urlopen("https://petitbac-hmym.onrender.com")
            except:
                pass
            import time
            time.sleep(600)  # toutes les 10 minutes
    
    t = threading.Thread(target=ping)
    t.daemon = True
    t.start()

keep_alive()

client.run(os.environ["TOKEN"])
