import discord
from discord import app_commands
import random
import os
from listes import liste_1, liste_2, liste_3

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

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
