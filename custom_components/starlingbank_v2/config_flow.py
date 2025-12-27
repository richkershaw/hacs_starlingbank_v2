"""Config flow for Starling Bank v2."""

from __future__ import annotations

from typing import Any

import voluptuous as vol

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.const import CONF_ACCESS_TOKEN, CONF_NAME

from .const import CONF_SPACE_NAME

CONFIG_SCHEMA = vol.Schema(
    {vol.Required(CONF_ACCESS_TOKEN, default=""): str},
    {vol.Required(CONF_NAME, default=""): str},
    {vol.Required(CONF_SPACE_NAME, default=""): str}
)

class StarlingConfigFlow(ConfigFlow, domain="starlingbank_v2"):
    """The configuration flow for a Starling Bank account."""

    VERSION = 1
    MINOR_VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Ask the user for an access token and an account name for the system."""
        errors = {}
        if user_input:
            return self.async_create_entry(
                title="Starling Bank v2",
                data=user_input,
            )
        return self.async_show_form(
            step_id="user", data_schema=CONFIG_SCHEMA, errors=errors
        )

