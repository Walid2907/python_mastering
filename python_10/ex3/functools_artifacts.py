import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    ops = {
        'add': operator.add,   # a + b
        'multiply': operator.mul,  # a * b
        'max': lambda a, b: a if a > b else b,
        'min': lambda a, b: a if a < b else b
    }
    return functools.reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    # return a dict of precooked fumctions neeed only a
    return {
        'fire_enchant': functools.partial(
            base_enchantment, power=50, element='fire'),
        'ice_enchant': functools.partial(
            base_enchantment, power=50, element='ice'),
        'lightning_enchant': functools.partial(
            base_enchantment, power=50, element='lightning')
    }


# the needed funct dor partial enchanter
def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{element} enchantment on {target} with power {power}"


# automatically stores the return value of a function for each unique set of
# arguments
@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @functools.singledispatch
    def dispatch(value):
        return f"Unknown spell type: {type(value)}"

    @dispatch.register(int)
    def _(value):
        return f"{value} damage dealt"

    @dispatch.register(str)
    def _(value):
        return f"{value} played"

    @dispatch.register(list)
    def _(value):
        return (f"Multi-cast: {len(value)} "
                f"spells cast: {', '.join(v for v in value)}")

    return dispatch


if __name__ == "__main__":
    spell_powers = [38, 43, 34, 15, 17, 13]
    fibonacci_tests = [14, 13, 17]

    total = spell_reducer(spell_powers, "add")
    product = spell_reducer(spell_powers, "multiply")
    maximum = spell_reducer(spell_powers, "max")
    minimum = spell_reducer(spell_powers, "min")

    print(f"Sum: {total}")
    print(f"Product: {product}")
    print(f"Max: {maximum}")
    print(f"Min: {minimum}")

    print("\nTesting memoized fibonacci...")
    for fib in fibonacci_tests:
        print(f"fib({fib}): {memoized_fibonacci(fib)}")

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher(["1", "2", "3"]))
