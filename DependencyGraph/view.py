def replace_variables(html_str,**kwargs):
    # replace {varname} with the value of the variable

    for key in kwargs:
        html_str = html_str.replace("{"+f"{key}"+"}",kwargs[key])

    return html_str
