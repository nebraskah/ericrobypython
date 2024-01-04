"""
Exception Handling
"""

try:
    # x = 10 * (1/0)
    x = '2' + 2
    print(x)
except ZeroDivisionError as err:
    print(f'I can\'t believe you attempted this >>> {err}')
except Exception as e:
    print('An error occurred')
finally:
    print('Close DB connections and tighten up loose ends')



try:
    x = None
    if x is None:
        raise Exception
except Exception as e:
    print(f'x is really NONE')

