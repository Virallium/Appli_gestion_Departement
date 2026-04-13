# Accueil Nouveau Project

Application Django pour la gestion des ouvriers et de la communauté.

## Déploiement sur Render

### Prérequis
- Compte Render (https://render.com)
- Base de données PostgreSQL (Render ou Supabase)

### Étapes de déploiement

1. **Connectez votre repository GitHub à Render**
   - Allez sur https://dashboard.render.com
   - Cliquez sur "New +" > "Web Service"
   - Connectez votre repo GitHub

2. **Configuration du service**
   - **Name**: accueil-nouveau-project
   - **Environment**: Python
   - **Region**: Oregon (US West)
   - **Branch**: main (ou votre branche principale)
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - **Start Command**: `gunicorn AccueilnouveauProject.wsgi:application`

3. **Variables d'environnement**
   Ajoutez ces variables dans l'onglet "Environment" :

   ```
   SECRET_KEY=votre-cle-secrete-unique
   DEBUG=False
   ALLOWED_HOSTS=votre-app.onrender.com
   DATABASE_URL=votre-url-postgresql
   ```

4. **Base de données**
   - Créez une base PostgreSQL sur Render OU
   - Utilisez votre base Supabase existante
   - Copiez l'URL de connexion dans `DATABASE_URL`

5. **Déploiement**
   - Cliquez sur "Create Web Service"
   - Render va builder et déployer automatiquement

### Migration de la base de données

Après le premier déploiement, exécutez les migrations :

```bash
# Via Render Shell (dans le dashboard)
python manage.py migrate
python manage.py createsuperuser
```

### Fichiers statiques

Les fichiers statiques sont automatiquement collectés pendant le build grâce à `collectstatic --noinput`.

### Dépannage

- **Erreur de base de données**: Vérifiez `DATABASE_URL`
- **Erreur 500**: Vérifiez les logs dans Render
- **Fichiers statiques non chargés**: Vérifiez que `collectstatic` s'exécute

### Développement local

```bash
# Installation
pip install -r requirements.txt

# Configuration
cp .env.example .env
# Éditez .env avec vos valeurs locales

# Migration
python manage.py migrate

# Lancement
python manage.py runserver
```