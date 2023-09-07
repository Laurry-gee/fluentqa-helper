from jinja2 import Environment, FileSystemLoader, select_autoescape

from generators.enums import Base, TargetType, Language, SourceType
from generators.source import SourceStructureModel

env = Environment(loader=FileSystemLoader("gema/dest/templates"), autoescape=select_autoescape())


class TargetStructureModel(Base):
    template_file: str
    type: TargetType
    language: Language
    model_name: str = "AutoGenerated"

    def __init__(self, model: SourceStructureModel, source_type: SourceType, **kwargs):
        self.model = model
        self.source_type = source_type
        self.template = env.get_template(self.template_file)

    def render(self):
        return self.template.render(model=self.model)
