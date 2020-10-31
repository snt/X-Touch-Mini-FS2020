
from jinja2 import Environment, select_autoescape
from globalstorage import GlobalStorage

env = Environment(
    autoescape=select_autoescape(['html', 'xml'])
)


class ConditionalRunner:
    def __init__(self, template):
        template_str = "".join(template)
        self._template = env.from_string(template_str)
        self._ae = GlobalStorage().aircraft_events
        self._aq = GlobalStorage().aircraft_requests

    def get_simvar_value(self, name: str):
        value = self._aq.get(name)
        print("get_simvar_value", name, value)
        return value

    def set_simvar_value(self, name: str, value):
        print("set_simvar_value", name, value)
        self._aq.set(name, value)

    def trigger_event(self, name: str, value):
        print("trigger_event", name, value)
        self._ae.find(name)(int(value))

    @staticmethod
    def trigger_encoder_alternate(index: int, value: bool):
        print("trigger_encoder_alternate", index, value)
        GlobalStorage().encoders[index-1].on_alternate(value)

    def execute(self):
        self._template.render(data=self)

    def __call__(self, *args, **kwargs):
        self.execute()
