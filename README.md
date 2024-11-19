# Projet Annonces

## Description

Ce projet utilise Django pour gérer une application de gestion d'annonces avec une base de données PostgreSQL. Il comprend également un processus de scraping pour récupérer des données externes.

---

## Prérequis

Avant de commencer, assurez-vous d'avoir installé :

- **Docker** : [Installation Docker](https://docs.docker.com/get-docker/)
- **Docker Compose** : [Installation Docker Compose](https://docs.docker.com/compose/install/)

---

## Démarrer le projet

Suivez ces étapes pour démarrer votre projet.

### 1. Cloner le projet

Clonez ce projet sur votre machine locale :

```bash
git clone <URL_DU_REPOSITORY>
cd <Dossier_Du_Projet>

2. Construire les images Docker
Construisez les images Docker nécessaires pour l'application et la base de données :

```bash
docker-compose build
```

### 3. Lancer les conteneurs Docker
Démarrez les services en arrière-plan avec Docker Compose :

```bash
docker-compose up -d
```

Cette commande lance deux services : l'application web Django et la base de données PostgreSQL.

### 4. Appliquer les migrations de la base de données
Pour configurer la base de données avec les bonnes tables, exécutez les migrations Django :

```bash
docker-compose exec web python manage.py migrate
```

### 5. Accéder à l'application web
L'applicati on sera accessible via le navigateur à l'adresse suivante :

```bash
http://localhost:8080/annonces/start-scraping/
```

### 6. Se connecter à la base de données PostgreSQL
Pour interagir directement avec la base de données PostgreSQL, vous pouvez vous connecter à PostgreSQL à l'intérieur du conteneur Docker avec cette commande :

```bash
docker exec -it postgres_db psql -U admin -d database_avito
```

Cela vous connecte à la base de données database_avito en tant qu'utilisateur admin. Vous pouvez ensuite exécuter des requêtes SQL, comme afficher les tables disponibles :

```sql
\dt
```

Arrêter les services
Pour arrêter les conteneurs Docker et tous les services associés, utilisez cette commande :

```bash
docker-compose down
```

Cela arrêtera et supprimera les conteneurs.

Commandes Docker utiles
Construire les images Docker :

```bash
docker-compose build
```

Lancer les conteneurs Docker :

```bash
docker-compose up -d
```

Appliquer les migrations de la base de données :

```bash
docker-compose exec web python manage.py migrate
```


Se connecter à la base de données PostgreSQL :

```bash
docker exec -it postgres_db psql -U admin -d database_avito
```

Arrêter les services Docker :

```bash
docker-compose down
```

Ressources supplémentaires
Django Documentation
PostgreSQL Documentation
Docker Documentation
Docker Compose Documentation
