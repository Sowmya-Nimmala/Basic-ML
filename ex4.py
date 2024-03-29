{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOnm+1giQpN3waApAo0T+79",
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
        "<a href=\"https://colab.research.google.com/github/Sowmya-Nimmala/Basic-ML/blob/main/ex4.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FlrN4zLptTcd",
        "outputId": "b7c4d4fd-955d-4c3c-ca88-410af3bd3794"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "S->iEtSZ'\n",
            "Z'->ε |eS\n",
            "S->aY'\n",
            "Y'->ε \n"
          ]
        }
      ],
      "source": [
        "from itertools import takewhile\n",
        "\n",
        "s= \"S->iEtS|iEtSeS|a\"\n",
        "\n",
        "def groupby(ls):\n",
        "    d = {}\n",
        "    ls = [ y[0] for y in rules ]\n",
        "    initial = list(set(ls))\n",
        "    for y in initial:\n",
        "        for i in rules:\n",
        "            if i.startswith(y):\n",
        "                if y not in d:\n",
        "                    d[y] = []\n",
        "                d[y].append(i)\n",
        "    return d\n",
        "\n",
        "def prefix(x):\n",
        "    return len(set(x)) == 1\n",
        "\n",
        "\n",
        "starting=\"\"\n",
        "rules=[]\n",
        "common=[]\n",
        "alphabetset=[\"A'\",\"B'\",\"C'\",\"D'\",\"E'\",\"F'\",\"G'\",\"H'\",\"I'\",\"J'\",\"K'\",\"L'\",\"M'\",\"N'\",\"O'\",\"P'\",\"Q'\",\"R'\",\"S'\",\"T'\",\"U'\",\"V'\",\"W'\",\"X'\",\"Y'\",\"Z'\"]\n",
        "s = s.replace(\" \", \"\").replace(\"\t\", \"\").replace(\"\\n\", \"\")\n",
        "\n",
        "while(True):\n",
        "    rules=[]\n",
        "    common=[]\n",
        "    split=s.split(\"->\")\n",
        "    starting=split[0]\n",
        "    for i in split[1].split(\"|\"):\n",
        "        rules.append(i)\n",
        "\n",
        "#logic for taking commons out\n",
        "    for k, l in groupby(rules).items():\n",
        "        r = [l[0] for l in takewhile(prefix, zip(*l))]\n",
        "        common.append(''.join(r))\n",
        "#end of taking commons\n",
        "    for i in common:\n",
        "        newalphabet=alphabetset.pop()\n",
        "        print(starting+\"->\"+i+newalphabet)\n",
        "        index=[]\n",
        "        for k in rules:\n",
        "            if(k.startswith(i)):\n",
        "                index.append(k)\n",
        "        print(newalphabet+\"->\",end=\"\")\n",
        "        for j in index[:-1]:\n",
        "            stringtoprint=j.replace(i,\"\", 1)+\"|\"\n",
        "            if stringtoprint==\"|\":\n",
        "                print(\"\\u03B5\",\"|\",end=\"\")\n",
        "            else:\n",
        "                print(j.replace(i,\"\", 1)+\"|\",end=\"\")\n",
        "        stringtoprint=index[-1].replace(i,\"\", 1)+\"|\"\n",
        "        if stringtoprint==\"|\":\n",
        "            print(\"\\u03B5\",\"\",end=\"\")\n",
        "        else:\n",
        "            print(index[-1].replace(i,\"\", 1)+\"\",end=\"\")\n",
        "        print(\"\")\n",
        "    break"
      ]
    }
  ]
}