"""
Implements a decorator which applies exponential backoff to a function which sometimes fails for example
because of rate limits

fail = 5
TRY = 10
SLEEP = 1


# Function that we wanna apply exponential backoff
def success_after_fails():

    global fail
    print(f"success_after_fails(), fail: {fail}")

    if fail != 1:
        print("fail")
        fail -= 1
        raise Exception
    else:
        print("success")
        pass


# Exponential backoff without decorator
t, s, r = TRY, SLEEP, 1
while t:
    try:
        success_after_fails()
        break
    except:
        print(f"Retry: {r}")
        print(f"Sleep {s} seconds")
        time.sleep(s)
        t -= 1
        s *= BACKOFF
"""

import time

fail = 5
MAX_RETRY = 10
BACKOFF = 2


def exponential_backoff(max_retry=MAX_RETRY, backoff=BACKOFF):
    def wrapper(func):
        def internal_wrapper(*args):
            sleep = 1
            r = max_retry
            while r:
                try:
                    func(*args)
                    break
                except:
                    print(f"Sleep {sleep} seconds for retry")
                    time.sleep(sleep)
                    sleep *= backoff
                    r -= 1
            else:
                print("Max retry reached")
        return internal_wrapper

    return wrapper


# Exponential backoff with decorator
@exponential_backoff()
def success_after_fails():

    global fail
    print(f"success_after_fails(), fail: {fail}")

    if fail != 1:
        print("fail")
        fail -= 1
        raise Exception
    else:
        print("success")
        pass


success_after_fails()
