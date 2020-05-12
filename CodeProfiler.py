import yappi
import RecursiveFix
yappi.set_clock_type("cpu") # Use set_clock_type("wall") for wall time
yappi.start()

RecursiveFix
yappi.get_func_stats().print_all()
yappi.get_thread_stats().print_all()