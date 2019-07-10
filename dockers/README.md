# Cours sur Docker
ce répository va contenir le cours sur Docker du 10/07/19

`https://hub.docker.com/`
La principale différence entre VM et docker
VM: on virtualise une machine car on simule logiciel + hardware
Docker: s'appuye sur les ressources de la machine existante poursimuler le logiciel. Sur le s conteneurs on va mettre des images toutes petites pour faciliter la tache. Permet d'avoir un même environnement de dév pour tout le monde

Calques: Un calque est une modification de fichiers

Docker est comme un zip avec des méta-données

Docker-hub: plateforme avec plein d'images disponibles

### lors de la suppression d'un conteneur vous perdrez l'ensemble des informations utiles (bdd, logs..) .
Pour pallier à ça on utilise des volumes, qui fait un mapping entre répertoire locale d'un ordi et le répertoire remote du docker
