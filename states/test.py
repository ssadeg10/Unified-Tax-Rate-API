import requests

from state_mapper import register


@register("test")
def test():
    return "it works"