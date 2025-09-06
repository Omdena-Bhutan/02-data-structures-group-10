{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO1N9lBc1NJS8WSVW6Tq8Wl",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Omdena-Bhutan/02-data-structures-group-10/blob/main/Team_10.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# PART 1"
      ],
      "metadata": {
        "id": "D2ZfmvxoJTGf"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "character_profile = { \"name\": \"Alistair the Brave\", \"level\": 1, \"health\": 100, \"mana\": 50, \"gold\": 50.75, \"is_alive\": True}"
      ],
      "metadata": {
        "id": "CjDCuq_sJYyA"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "character_profile"
      ],
      "metadata": {
        "id": "uXeDI_I3T3MK"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(f\"Character Name: {character_profile['name']}\")"
      ],
      "metadata": {
        "id": "RKFcABapUre_"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(f\"Character level:{character_profile['level']}\")"
      ],
      "metadata": {
        "id": "qiVnYHg9WSYg"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "character_profile[\"health\"] = 85"
      ],
      "metadata": {
        "id": "3_MmUcoNW8Ll"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(f\"Character Health: {character_profile['health']}\")"
      ],
      "metadata": {
        "id": "xl-oX67tW9_7"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "character_profile[\"friend\"] = 2"
      ],
      "metadata": {
        "id": "DmPm9bexXbVS"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(f\"Character friend: {character_profile['friend']}\")"
      ],
      "metadata": {
        "id": "4nmwmZe_Xi08"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print (character_profile)"
      ],
      "metadata": {
        "id": "RYfhSX9hX2SA"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# PART 2"
      ],
      "metadata": {
        "id": "5TLiuCSIJkMf"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "Inventory= ['Dagger','Riffel','Poison']"
      ],
      "metadata": {
        "id": "w8Y6cypXJmMm"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(Inventory)"
      ],
      "metadata": {
        "id": "NoqrBvXvK_jm"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "Inventory.append('Health Poition')"
      ],
      "metadata": {
        "id": "CRhPPJthLJLb"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "Inventory"
      ],
      "metadata": {
        "id": "99cHn6xhMRIV"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "Inventory.remove('Dagger')"
      ],
      "metadata": {
        "id": "z5WcDQfuMWXW"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(Inventory)"
      ],
      "metadata": {
        "id": "cg3Ed5uHMhgG"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"inventory:\")\n",
        "for item in Inventory:\n",
        "  print(\"_\", item)\n"
      ],
      "metadata": {
        "id": "zivuD2gLM5jr"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# PART 3"
      ],
      "metadata": {
        "id": "szwfGR2vOjA1"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Tuples are a good choice for base stats because they are immutable, meaning the values won't changed.\")"
      ],
      "metadata": {
        "id": "sXYCtOLnPmrh"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "base_stats = (10, 8, 12)  # (strength, dexterity, intelligence)"
      ],
      "metadata": {
        "id": "pUZ8SdRqP2-m"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "base_stats"
      ],
      "metadata": {
        "id": "ywKg6EjWQX-w"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Alistair's intelligence stat is:\", base_stats[2])"
      ],
      "metadata": {
        "id": "S8QNKFSNQaf5"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "base_stats[0] = 15  # Attempt to change strength\n"
      ],
      "metadata": {
        "id": "CsnCtiOTQoOG"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "TypeError: 'tuple' object does not support item assignment"
      ],
      "metadata": {
        "id": "YFWLDjOgTFHq"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Part 4"
      ],
      "metadata": {
        "id": "n8Wj7wfjTJWP"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "quest_log = {\"Defeat the Goblin King\", \"Find the Lost Amulet\"}"
      ],
      "metadata": {
        "id": "f4sKoZtKTLoD"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "quest_log"
      ],
      "metadata": {
        "id": "9YAucLVnUHa8"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "quest_log.add(\"Deliver the Old Scroll\")"
      ],
      "metadata": {
        "id": "dRMvBdoeT0Ag"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "quest_log"
      ],
      "metadata": {
        "id": "NY8DTMC0UJ4l"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "quest_log.add(\"Deliver the Old Scroll\")"
      ],
      "metadata": {
        "id": "eJImRzWUULzI"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "quest_log"
      ],
      "metadata": {
        "id": "0DZzpTAMUa7F"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "quest_log.discard('Find the Lost Amulet')"
      ],
      "metadata": {
        "id": "tmr6tdubUpaR"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "quest_log"
      ],
      "metadata": {
        "id": "_U8kTnSuUvPW"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Final Quest Log:\", quest_log)"
      ],
      "metadata": {
        "id": "SHvcW_QtVOT4"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# PART 5"
      ],
      "metadata": {
        "id": "61PjVMHjV6iE"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "character_sheet = {\n",
        "    \"profile\": character_profile,\n",
        "    \"inventory\": Inventory,\n",
        "    \"stats\": base_stats,\n",
        "    \"quests\": quest_log\n",
        "}\n"
      ],
      "metadata": {
        "id": "zKzS3c7tV-T1"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Full Character Sheet:\")\n",
        "print(character_sheet)"
      ],
      "metadata": {
        "id": "i9912vAyWZkz"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "https://colab.research.google.com/drive/1VluH49k3uTbWBj4ClxRpE2S6QtAPjLC_?usp=drive_link"
      ],
      "metadata": {
        "id": "Csboc1G9kE00"
      }
    }
  ]
}