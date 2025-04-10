from homeassistant import config_entries
from homeassistant.core import callback
import voluptuous as vol
import re

from .const import DOMAIN


class BlindsConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    @callback
    def _get_entity_ids(self):
        return self.hass.states.async_entity_ids()

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            return self.async_create_entry(
                title=user_input["ent_name"],
                data=user_input,
            )
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required("ent_name"): str,
                    vol.Required("entity_up", default=None): vol.In(self._get_entity_ids()),
                    vol.Required("entity_down", default=None): vol.In(self._get_entity_ids()),
                    vol.Required("time_up"): vol.All(vol.Coerce(float), vol.Range(min=0)),
                    vol.Required("time_down"): vol.All(vol.Coerce(float), vol.Range(min=0)),
                    vol.Required("tilt_open"): vol.All(vol.Coerce(float), vol.Range(min=0)),
                    vol.Required("tilt_closed"): vol.All(vol.Coerce(float), vol.Range(min=0)),
                    vol.Required("time_up_nonlinear", default=0): vol.All(vol.Coerce(float), vol.Range(min=0)),
                    vol.Required("time_down_nonlinear", default=0): vol.All(vol.Coerce(float), vol.Range(min=0)),
                    vol.Required("percent_up_nonlinear", default=0): vol.All(vol.Coerce(float), vol.Range(min=0,max=10)),
                    vol.Required("percent_down_nonlinear", default=0): vol.All(vol.Coerce(float), vol.Range(min=0,max=10)),

                    vol.Required("send_stop_at_end", default=True): bool,
                    vol.Required("delay_stop_final_position", default=0): vol.All(vol.Coerce(float), vol.Range(min=0, max=5))
                }
            ),
            errors=errors,
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return BlindsOptionsFlow(config_entry)

class BlindsOptionsFlow(config_entries.OptionsFlow):
    def __init__(self, config_entry):
        self.config_entry = config_entry

    @callback
    def _get_entity_ids(self):
        return self.hass.states.async_entity_ids()

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            updated_data = dict(self.config_entry.data)
            updated_data.update(user_input)
            self.hass.config_entries.async_update_entry(entry=self.config_entry, data=updated_data)
            return self.async_create_entry(title="", data={})

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(
                {
                    vol.Required("ent_name", default=self.config_entry.data.get("ent_name", "")): str,
                    vol.Required("entity_up", default=self.config_entry.data.get("entity_up", "")): vol.In(self._get_entity_ids()),
                    vol.Required("entity_down", default=self.config_entry.data.get("entity_down", "")): vol.In(self._get_entity_ids()),
                    vol.Required("time_up", default=self.config_entry.data.get("time_up", 0.0)): vol.All(vol.Coerce(float), vol.Range(min=0)),
                    vol.Required("time_down", default=self.config_entry.data.get("time_down", 0.0)): vol.All(vol.Coerce(float), vol.Range(min=0)),
                    vol.Required("tilt_open", default=self.config_entry.data.get("tilt_open", 0.0)): vol.All(vol.Coerce(float), vol.Range(min=0)),
                    vol.Required("tilt_closed", default=self.config_entry.data.get("tilt_closed", 0.0)): vol.All(vol.Coerce(float), vol.Range(min=0)),
                    vol.Required("time_up_nonlinear", default=self.config_entry.data.get("time_up_nonlinear", 0.0)): vol.All(vol.Coerce(float), vol.Range(min=0)),
                    vol.Required("time_down_nonlinear", default=self.config_entry.data.get("time_down_nonlinear", 0.0)): vol.All(vol.Coerce(float), vol.Range(min=0)),
                    vol.Required("percent_up_nonlinear", default=self.config_entry.data.get("percent_up_nonlinear", 0.0)): vol.All(vol.Coerce(float), vol.Range(min=0, max=10)),
                    vol.Required("percent_down_nonlinear", default=self.config_entry.data.get("percent_down_nonlinear", 0.0)): vol.All(vol.Coerce(float), vol.Range(min=0, max=10)),
                    
                    vol.Required("send_stop_at_end", default=self.config_entry.data.get("send_stop_at_end")): bool,
                    vol.Required("delay_stop_final_position", default=self.config_entry.data.get("delay_stop_final_position", 0.0)): vol.All(vol.Coerce(float), vol.Range(min=0, max=10)),
                }
            ),
        )
