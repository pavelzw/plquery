def test_hard():
    import plquery  # noqa

    # this is just a demo that pytest can produce good error messages just by
    # parsing assert statements
    assert {"a": 1, "b": 2} == {"a": 1, "b": 2}
