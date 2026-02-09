"""DataUpdateCoordinator for Agent Swarm."""
from __future__ import annotations

import logging
from datetime import timedelta

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import DOMAIN, CONF_API_URL, CONF_API_KEY, DEFAULT_SCAN_INTERVAL

_LOGGER = logging.getLogger(__name__)


class AgentSwarmCoordinator(DataUpdateCoordinator):
    """Class to manage fetching data from Agent Swarm API."""

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        """Initialize."""
        self.entry = entry
        self.api_url = entry.data.get(CONF_API_URL, "https://api.moltbook.com")
        self.api_key = entry.data.get(CONF_API_KEY, "")
        
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=DEFAULT_SCAN_INTERVAL),
        )

    async def _async_update_data(self):
        """Update data via API."""
        try:
            # For now, return demo data. In production, this fetches from your API
            agents = [
                {"id": "shadow_01", "name": "Shadow", "status": "online", "tasks": 3},
                {"id": "echo_01", "name": "Echo", "status": "busy", "tasks": 1},
            ]
            
            total_tasks = sum(a["tasks"] for a in agents)
            online_agents = len([a for a in agents if a["status"] == "online"])
            
            return {
                "agents": agents,
                "total_agents": len(agents),
                "online_agents": online_agents,
                "total_tasks": total_tasks,
                "online": True,
            }
        except Exception as err:
            _LOGGER.error("Error fetching data: %s", err)
            raise UpdateFailed(f"Error fetching data: {err}") from err

    async def async_shutdown(self):
        """Shutdown coordinator."""
        await super().async_shutdown()
