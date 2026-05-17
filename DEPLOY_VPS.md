# Déploiement Argus-IA sur VPS Ubuntu 24.04

Guide complet pour installer Argus-IA (backend Python + frontend Next.js) sur un VPS Ubuntu 24.04 avec nom de domaine, HTTPS, et pipeline automatique.

---

## 1. Préparation du VPS

Connectez-vous en SSH :

```bash
ssh root@votre-ip
```

### Mises à jour système

```bash
apt update && apt upgrade -y
apt install -y curl wget git nginx certbot python3-certbot-nginx ufw fail2ban
```

### Créer un utilisateur dédié (recommandé)

```bash
adduser argus
usermod -aG sudo argus
su - argus
```

---

## 2. Installer Python 3.12+ et Node.js 20+

### Python

Ubuntu 24.04 shippe Python 3.12 — vérifiez :

```bash
python3 --version   # doit afficher 3.12.x
```

Si besoin d'une version plus récente :

```bash
sudo apt install -y software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.14 python3.14-venv python3.14-dev
```

### Node.js 20 LTS

```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs
node --version   # v20.x.x
npm --version    # 10.x.x
```

---

## 3. Cloner le repository

```bash
cd ~
git clone https://github.com/Wzxgreed/argus-ia.git
cd argus-ia
```

---

## 4. Configuration Backend (Python)

### Créer le virtualenv

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Clés API

```bash
cp .env .env.local
nano .env.local
```

Remplissez au minimum :

```env
FMP_API_KEY=votre_cle_fmp_si_vous_en_avez_une
# Les autres clés sont optionnelles pour le fonctionnement de base
```

> **Note :** Sans clé FMP, le pipeline fonctionne quand même (Yahoo Finance = source principale). FMP ajoute juste des données institutionnelles (consensus analystes, ratios, etc.).

### Test du fetch

```bash
source .venv/bin/activate
python3 scripts/fetch_prices.py
```

Vous devez voir :
```
[fetch_prices] Fetching N tickers...
[fetch_prices] Written data/YYYY-MM-DD.json (N OK, 0 KO)
```

---

## 5. Build du Frontend (Next.js)

```bash
cd ~/argus-ia/frontend
npm install
npm run build
```

Le build génère le dossier `~/argus-ia/frontend/dist/` (fichiers statiques prêts à servir).

### Copier les données dans dist

```bash
cd ~/argus-ia/frontend
npm run postbuild   # ou : node scripts/copy-data.js
```

---

## 6. Nginx — Reverse Proxy + Domaine

### Configurer le domaine

Assurez-vous que votre nom de domaine pointe vers l'IP du VPS (enregistrement A).

### Créer la config Nginx

```bash
sudo nano /etc/nginx/sites-available/argus-ia
```

Collez :

```nginx
server {
    listen 80;
    server_name votredomaine.com www.votredomaine.com;

    root /home/argus/argus-ia/frontend/dist;
    index index.html;

    # Sécurité de base
    server_tokens off;
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;

    # Servir les fichiers statiques Next.js
    location / {
        try_files $uri $uri/ /index.html;
    }

    # Données JSON du pipeline (cache court)
    location /data/ {
        alias /home/argus/argus-ia/frontend/dist/data/;
        add_header Cache-Control "public, max-age=60";
        try_files $uri =404;
    }

    # Chunks JS/CSS Next.js (cache agressif)
    location /_next/ {
        alias /home/argus/argus-ia/frontend/dist/_next/;
        expires 1y;
        add_header Cache-Control "public, immutable";
        access_log off;
    }

    # Fontes (cache agressif)
    location /_next/static/media/ {
        alias /home/argus/argus-ia/frontend/dist/_next/static/media/;
        expires 1y;
        add_header Cache-Control "public, immutable";
        access_log off;
    }

    # Dashboard trailing slash (Next.js exporté avec trailingSlash: true)
    location /dashboard {
        return 301 /dashboard/;
    }

    location /dashboard/ {
        alias /home/argus/argus-ia/frontend/dist/dashboard/;
        try_files $uri $uri/ /dashboard/index.html;
    }
}
```

Activer le site :

```bash
sudo ln -s /etc/nginx/sites-available/argus-ia /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

### SSL avec Let's Encrypt

```bash
sudo certbot --nginx -d votredomaine.com -d www.votredomaine.com
```

Certbot modifie automatiquement la config Nginx pour ajouter le bloc `listen 443 ssl`.

### Renouvellement auto SSL

Certbot installe déjà un cron, vérifiez :

```bash
sudo certbot renew --dry-run
```

---

## 7. Firewall (UFW)

```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow 'Nginx Full'   # 80 + 443
sudo ufw enable
```

---

## 8. Pipeline Automatique — Cron

Le pipeline du matin doit s'exécuter automatiquement. Deux options :

### Option A : Cron simple (recommandé)

```bash
crontab -e
```

Ajoutez (lancement à 9h00 heure du VPS, ajustez selon votre timezone) :

```cron
# Argus-IA — Pipeline du matin
0 9 * * * cd /home/argus/argus-ia && /home/argus/argus-ia/.venv/bin/python scripts/fetch_prices.py >> /home/argus/argus-ia/logs/cron_fetch.log 2>&1
5 9 * * * cd /home/argus/argus-ia && /home/argus/argus-ia/.venv/bin/python scripts/fetch_macro.py >> /home/argus/argus-ia/logs/cron_macro.log 2>&1
10 9 * * * cd /home/argus/argus-ia && /home/argus/argus-ia/.venv/bin/python scripts/fetch_calendar.py >> /home/argus/argus-ia/logs/cron_calendar.log 2>&1
15 9 * * * cd /home/argus/argus-ia && /home/argus/argus-ia/.venv/bin/python scripts/validate.py >> /home/argus/argus-ia/logs/cron_validate.log 2>&1
20 9 * * * cd /home/argus/argus-ia/frontend && npm run build >> /home/argus/argus-ia/logs/cron_build.log 2>&1
```

Créer le dossier logs :

```bash
mkdir -p ~/argus-ia/logs
```

### Option B : Orchestrateur complet (DAG)

Si vous utilisez l'orchestrateur Python (`agents/orchestrator.py`) :

```cron
0 9 * * * cd /home/argus/argus-ia && PYTHONPATH=/home/argus/argus-ia/agents:/home/argus/argus-ia/scripts /home/argus/argus-ia/.venv/bin/python agents/orchestrator.py >> /home/argus/argus-ia/logs/cron_orchestrator.log 2>&1
```

---

## 9. Rebuild auto post-pipeline

Après chaque run du pipeline, le frontend doit être rebuildé pour inclure les nouvelles données JSON dans `dist/data/`.

Créez un script wrapper :

```bash
nano ~/argus-ia/scripts/deploy_pipeline.sh
```

```bash
#!/bin/bash
set -euo pipefail

cd /home/argus/argus-ia
source .venv/bin/activate

echo "=== $(date) — Pipeline Argus-IA ==="

# 1. Fetch
python scripts/fetch_prices.py
python scripts/fetch_macro.py
python scripts/fetch_calendar.py
python scripts/validate.py

# 2. Agents (optionnel — si vous les lancez manuellement)
# python agents/orchestrator.py

# 3. Rebuild frontend
cd frontend
npm run build

# 4. Reload Nginx (pas nécessaire pour fichiers statiques, mais safe)
sudo systemctl reload nginx

echo "=== $(date) — Pipeline terminé ==="
```

```bash
chmod +x ~/argus-ia/scripts/deploy_pipeline.sh
```

Et dans le cron :

```cron
0 9 * * * /home/argus/argus-ia/scripts/deploy_pipeline.sh >> /home/argus/argus-ia/logs/pipeline.log 2>&1
```

---

## 10. Accès au Dashboard

Après déploiement :

```
https://votredomaine.com/dashboard/
```

Le dashboard est un export statique Next.js — aucun serveur Node.js n'a besoin de tourner en permanence. Nginx sert directement les fichiers HTML/JS/CSS.

---

## 11. Mise à jour du code (git pull)

Quand vous poussez des changements depuis votre machine locale :

```bash
# Sur le VPS
su - argus
cd ~/argus-ia
git pull origin main
source .venv/bin/activate
pip install -r requirements.txt   # si requirements changé
cd frontend && npm install && npm run build
sudo systemctl reload nginx
```

---

## 12. Sécurité supplémentaire

### Fail2ban (déjà installé)

```bash
sudo systemctl enable fail2ban
sudo systemctl start fail2ban
sudo fail2ban-client status
```

### Désactiver l'accès root SSH (optionnel mais recommandé)

```bash
sudo nano /etc/ssh/sshd_config
```

```
PermitRootLogin no
PasswordAuthentication no   # si vous utilisez une clé SSH
```

```bash
sudo systemctl reload sshd
```

### Permissions des fichiers sensibles

```bash
chmod 600 ~/.env.local
chmod 700 ~/.ssh
```

---

## 13. Dépannage VPS

### Erreur 403 sur /data/

Vérifiez les permissions :

```bash
ls -la ~/argus-ia/frontend/dist/data/
# Doit être lisible par www-data (nginx)
chmod -R 755 ~/argus-ia/frontend/dist/data/
```

### Erreur 404 sur /dashboard/

Vérifiez que `trailingSlash: true` est dans `next.config.js` et que le dossier `dist/dashboard/` existe avec `index.html`.

### Pipeline cron ne s'exécute pas

Vérifiez les logs :

```bash
cat ~/argus-ia/logs/pipeline.log
cat ~/argus-ia/logs/cron_*.log
```

Vérifiez que le venv est bien activé dans le script et que les chemins sont absolus.

### Nginx ne sert pas les nouveaux fichiers

Nginx sert les fichiers statiques directement — pas besoin de reload. Mais si vous avez modifié la config :

```bash
sudo nginx -t
sudo systemctl reload nginx
```

---

## Architecture finale

```
VPS Ubuntu 24.04
├── Nginx (80 → 443 SSL)
│   ├── / → /home/argus/argus-ia/frontend/dist/
│   ├── /dashboard/ → dist/dashboard/
│   ├── /data/ → dist/data/ (JSON reports)
│   └── /_next/ → dist/_next/ (chunks JS/CSS)
├── Python 3.12 + venv
│   ├── requirements.txt installés
│   └── scripts/fetch_prices.py (cron 9h00)
├── Node.js 20
│   └── frontend/ → npm run build → dist/
├── Cron
│   └── Pipeline quotidien 9h00 + rebuild
└── Certbot (SSL auto-renew)
```

---

## Checklist de validation

- [ ] `https://votredomaine.com/` — page d'accueil OK
- [ ] `https://votredomaine.com/dashboard/` — dashboard OK
- [ ] `https://votredomaine.com/data/latest.json` — données JSON OK
- [ ] SSL valide (cadenas vert)
- [ ] Pipeline cron exécuté ce matin → logs présents
- [ ] UFW actif : `sudo ufw status`
- [ ] Fail2ban actif : `sudo fail2ban-client status`

---

*Dernière mise à jour : 2026-05-17*
