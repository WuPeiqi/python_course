def func(*args, **kwargs):
    print(args, kwargs)


params = {"k1": "v2", "k2": "v2"}
func(params)  # ({"k1":"v2","k2":"v2"}, ) {}
func(**params)  # (), {"k1":"v2","k2":"v2"}