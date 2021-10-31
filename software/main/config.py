from dataclasses import make_dataclass

from omegaconf import OmegaConf


class Configurable:
    def get_config(self) -> object:
        base = getattr(self, "Config", object)
        configurable_fields = filter(lambda x: issubclass(type(x[1]), Configurable), self.__dict__.items())
        fields = map(lambda x: (x[0], x[1].get_config()), configurable_fields)
        Config = make_dataclass("Config", fields, bases=(base,))
        return Config
    
    def get_config_schema(self) -> OmegaConf:
        cfg = self.get_config()
        return OmegaConf.structured(cfg)
