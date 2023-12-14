from beerxml.recipe import Recipe
import xmltodict


class BeerxmlHandler:
    def __init__(self, xml_content):
        self._xml_content = xml_content

    def parse_to_beerxml(self) -> Recipe:
        return Recipe(**xmltodict.parse(self._xml_content)["RECIPES"]["RECIPE"])
