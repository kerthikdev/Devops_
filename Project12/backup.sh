#!/bin/bash
docker run --rm \
  -v redisdata:/data \
  -v "$PWD":/backup \
  alpine \
  sh -c "tar czf /backup/redis-backup.tar.gz -C /data ."

echo "✅ Redis volume backed up!"
