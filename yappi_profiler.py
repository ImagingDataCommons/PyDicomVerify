import yappi

yappi.set_clock_type("wall") # Use set_clock_type("wall") for wall time

yappi.start()


import ConvertByBigQuery

yappi.stop()

# retrieve thread stats by their thread id (given by yappi)
threads = yappi.get_thread_stats()
for thread in threads:
    print(
        "Function stats for (%s) (%d)" % (thread.name, thread.id)
    )  # it is the Thread.__class__.__name__
    yappi.get_func_stats(ctx_id=thread.id).print_all()