# SEYNARA - Site Web Django

Site web premium pour SEYNARA, maison événementielle basée à Dakar.

## Installation

### 1. Créer un environnement virtuel
```bash
python -m venv venv
source venv/Scripts/activate  # Windows
```

### 2. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 3. Appliquer les migrations
```bash
python manage.py migrate
```

### 4. Créer un superutilisateur
```bash
python manage.py createsuperuser
```

### 5. Lancer le serveur de développement
```bash
python manage.py runserver
```

Accédez à `http://localhost:8000/`

## Administration

Accédez à `http://localhost:8000/admin/` avec les identifiants du superutilisateur pour gérer :
- Les services
- Les événements
- Les demandes de contact

## Structure du projet

```
seynara_django/
├── seynara/                 # Configuration du projet
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── events/                  # Application principale
│   ├── models.py           # Service, Event, Contact
│   ├── views.py            # Vues et logique
│   ├── urls.py             # Routes
│   └── admin.py            # Configuration admin
├── templates/              # Fichiers HTML
│   ├── base.html           # Template de base
│   └── events/
│       ├── home.html
│       ├── services.html
│       ├── contact.html
│       ├── about.html
│       ├── events_list.html
│       └── event_detail.html
├── manage.py
└── requirements.txt
```

## Modèles de données

### Service
- title: Titre du service
- description: Description complète
- pillar: Type (Élégance, Émotion, Design, Détail)
- order: Ordre d'affichage

### Event
- title: Titre de l'événement
- description: Description
- image: Image (optionnel)
- date: Date de l'événement
- location: Localisation
- featured: Afficher en vedette

### Contact
- name: Nom
- email: Email
- phone: Téléphone (optionnel)
- message: Message
- created_at: Date de création

## Personnalisation

### Couleurs
Modifier les variables CSS dans `templates/base.html` :
```css
:root {
    --bg-primary: #F7F2EA;
    --accent: #C5A46D;
    /* ... */
}
```

### Emails
Configurer l'envoi d'emails en production dans `settings.py` :
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'votre-serveur-smtp.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
```

## Déploiement

Pour déployer en production :
1. Définir `DEBUG = False` dans `settings.py`
2. Définir une clé secrète sécurisée
3. Configurer `ALLOWED_HOSTS`
4. Utiliser un serveur WSGI (Gunicorn, uWSGI)
5. Configurer un reverse proxy (Nginx)

## Support

Contact : contact@seynara.sn
