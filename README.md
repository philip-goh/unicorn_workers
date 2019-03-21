# unicorn_workers

Testing Gunicorn workers and how they scale. Run _one_ `gunicorn_*` script at a time. Then run the
`launch_clients.sh` to make _n_ concurrent requests (I think it's 24).

## Sync worker

The default worker. Handles 1 request per worker at a time.

## Threads

This appears to be the simplest way of scaling out requests that are IO bound. As we have 10 threads,
we can handle 10 concurrent requests.

The added benefit of this is that we can also handle multiple connections that are not IO bound.

## eventlet

If monkey_patch works, then we can handle loads of concurrent requests. In the test case, we can handle 24 requests concurrently.

Scaling works, but the long running calls need to be monkey patchable. If you comment out
the `eventlet.monkey_patch()` call in app.py, the requests end up being handled in a synchronous
manner, 1 after the other.

However, if we encounter CPU bound code or code that is not eventlet aware then we fall back to synchronous
behaviour.

## Discussion

It would appear that threads provide the simplest and most reliable method of scaling. It will work with
any code, no special patching needed.

Eventlet will scale very phenomenally well provided that the long IO bound functions are patchable. If they aren't,
then this will revert back to _synchronous_ behaviour. If you can't guarantee that all functions are patchable
it might be safer to go with threads.

Turns out that gunicorn used to automatically `monkey_patch`. But there has been a bug since August 2018 that means that gunicorn isn't monkey patching. See [this bug](https://github.com/benoitc/gunicorn/issues/1847)
