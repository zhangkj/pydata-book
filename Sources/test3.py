


    thread_num = 100
    pool = threadpool.ThreadPool(thread_num)
    requests = threadpool.makeRequests(run, DATA, callback2)
    [pool.putRequest(req) for req in requests]
    pool.wait()
    pool.dismissWorkers(thread_num, do_join=True)