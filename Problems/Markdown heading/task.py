def heading(a, level=1):
    if level < 1:
        return f"# {a}"
    elif level > 6:
        return f"###### {a}"
    else:
        return f"{'#' * level} {a}"
