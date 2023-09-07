from typing import Any, Dict, Type

import humps
from typing import Any, Dict

from generators.api.models import StructureModel
from generators.enums import *
from generators.target import TargetStructureModel


class Go(TargetStructureModel):
    template_file = "go.jinja2"
    type = TargetType.go
    language = Language.go

    @classmethod
    def _type_convert(cls, type_: Type):
        if type_ is int:
            return "int"
        if type_ is str:
            return "string"
        if type_ is bool:
            return "bool"
        if type_ is float:
            return "float"

    def _parse_model(self, models: Dict[str, Any], model: StructureModel):
        fields = []
        for field in model.fields:
            name = field.name
            pascalize_name = humps.pascalize(field.name)
            if isinstance(field.type, StructureModel):
                type_ = pascalize_name
                models[pascalize_name] = self._parse_model(models, field.type)
            elif isinstance(field.type, list):
                if isinstance(field.type[0], StructureModel):
                    type_ = f"[]{pascalize_name}"
                    models[pascalize_name] = self._parse_model(models, field.type[0])
                else:
                    type_ = f"[]{self._type_convert(field.type[0])}"
            elif field.type is type(Any):
                type_ = "interface{}"
            else:
                type_ = self._type_convert(field.type)

            field_str = f'{pascalize_name} {type_} `{self.source_type}:"{name}"`'
            fields.append(field_str)
        return fields

    def render(self):
        model = self.model
        models = {}
        models[self.model_name] = self._parse_model(models, model)
        return self.template.render(models=models)
