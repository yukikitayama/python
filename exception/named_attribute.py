try:
    import abcd
except ImportError as e:
    print(f"args: {e.args}")
    print(f"name: {e.name}")
    print(f"path: {e.path}")
