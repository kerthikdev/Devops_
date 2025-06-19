#!/bin/bash
docker volume create redisdata

docker run --rm \
  -v redisdata:/data \
  -v "$PWD":/backup \
  alpine \
  sh -c "tar xzf /backup/redis-backup.tar.gz -C /data"

echo "✅ Redis volume restored!"
