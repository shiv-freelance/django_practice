from fastapi import FastAPI

app = FastAPI()

import asyncio

import redis.asyncio as redis

from aiocache import caches, Cache
from aiocache.serializers import StringSerializer, PickleSerializer

caches.set_config({
    'default': {
        'cache': "aiocache.SimpleMemoryCache",
        'serializer': {
            'class': "aiocache.serializers.StringSerializer"
        }
    },
    'redis_alt': {
        'cache': "aiocache.RedisCache",
        "host": "127.0.0.1",
        'port': 6379,
        "socket_connect_timeout": 1,
        'serializer': {
            'class': "aiocache.serializers.PickleSerializer"
        },
        'plugins': [
            {'class': "aiocache.plugins.HitMissRatioPlugin"},
            {'class': "aiocache.plugins.TimingPlugin"}
        ]
    }
})


async def default_cache():
    cache = caches.get('default')   # This always returns the same instance
    await cache.set("key", "value")
    print(await cache.get("ky")) # if key not found, results None
    assert await cache.get("key") == "value"
    assert isinstance(cache, Cache.MEMORY)
    assert isinstance(cache.serializer, StringSerializer)

@app.get('/')
async def health():
    await default_cache()
    cache = caches.get('default')
    if await cache.get("response") is not None:
        return await cache.get("response")
    result = {"message": "Healthy!"}
    await cache.set("response", result)
    return result
