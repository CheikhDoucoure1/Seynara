# SEYNARA Django - Démarrage rapide

## 🚀 Lancer le projet en 5 minutes

### 1️⃣ Cloner/Accéder au projet
```bash
cd C:\Users\cdoucoure\seynara_django
```

### 2️⃣ Créer et activer l'environnement virtuel
```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4️⃣ Initialiser la base de données
```bash
python manage.py migrate
```

### 5️⃣ Créer un compte admin
```bash
python manage.py createsuperuser
# Entrez: username, email, password
```

### 6️⃣ Lancer le serveur
```bash
python manage.py runserver
```

### 7️⃣ Accéder au site
- Site principal: http://localhost:8000/
- Admin: http://localhost:8000/admin/

## 📝 Ajouter du contenu

1. Allez sur http://localhost:8000/admin/
2. Connectez-vous avec les identifiants créés
3. Ajoutez des Services, Événements, etc.

## 📁 Architecture du site

```
├── Accueil (/)
│   ├── Héros
│   ├── Piliers (Élégance, Émotion, Design, Détail)
│   └── Événements en vedette
├── Services (/services/)
├── Portfolio (/events/)
├── Détail événement (/events/1/)
├── À propos (/about/)
└── Contact (/contact/)
```

## 🎨 Sections principales

### Home
- Hero avec message "L'art de créer l'exception"
- 4 piliers avec icônes
- 3 événements en vedette

### Services
- Liste numérotée des services (01, 02, 03, 04)
- Chaque service a un pilier associé

### Portfolio
- Grille d'événements
- Pagination automatique (12 par page)
- Lien vers chaque événement

### Contact
- Formulaire de contact
- Sauvegarde en base de données
- Envoi d'email (configurable)

## 🎯 Prochaines étapes

1. Ajouter des images pour les événements
2. Configurer l'envoi d'emails en production
3. Personnaliser les textes et contenus
4. Ajouter votre logo SEYNARA
5. Déployer sur un serveur (Heroku, PythonAnywhere, etc.)

## 💡 Besoin d'aide?

Consultez `README.md` pour plus de détails sur la configuration et le déploiement.
