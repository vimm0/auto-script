Build frontend
- `scp -r dist username@ip_address:/root/app/`

Update Backend
- `git push server --all`

In Server
- `docker-compose up -d --build`
