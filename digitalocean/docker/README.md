###### Deployment Part One

- Create droplet using marketplace option and choose docker
- You will receive email with Ip Address, password and other important credentials
- `ssh username@ip_address`

In Server,
```
$ mkdir repo.git app conf logs media static
$ cd repo.git
$ git init --bare
$ git --bare update-server-info
$ git config core.bare false
$ git config receive.denycurrentbranch ignore
$ git config core.worktree /root/app/ <--- directory in remote
$ cat > hooks/post-receive
#!/bin/sh
git checkout -f
cd ../app
./deploy.sh
$ chmod +x hooks/post-receive
```

In localhost, create remote link (Backend)
- `git remote add server ssh://username@ip_address:/root/repo.git/`
- `git push server --all`

Now build and copy (Frontend),
- Build directory `dist/`
- `scp -r dist username@ip_address:/root/app/`

In Server,
```
docker-compose up -d --build

docker logs -f <CONTAINER>
docker exec -it <mycontainer> bash
```

Note: Make sure Nginx bind port to `80`, Otherwise it won't be public.
