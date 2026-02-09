"""Sensor platform for Agent Swarm."""
from __future__ import annotations

from homeassistant.components.sensor import SensorEntity, SensorEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import (
    DOMAIN,
    SENSOR_KEY_TOTAL_AGENTS,
    SENSOR_KEY_ACTIVE_TASKS,
    SENSOR_KEY_COMPLETED_TASKS,
)
from .coordinator import AgentSwarmCoordinator

SENSORS = [
    SensorEntityDescription(
        key=SENSOR_KEY_TOTAL_AGENTS,
        name="Total Agents",
        icon="mdi:robot",
    ),
    SensorEntityDescription(
        key=SENSOR_KEY_ACTIVE_TASKS,
        name="Active Tasks",
        icon="mdi:clipboard-list",
    ),
    SensorEntityDescription(
        key=SENSOR_KEY_COMPLETED_TASKS,
        name="Completed Tasks",
        icon="mdi:clipboard-check",
    ),
]


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Agent Swarm sensor based on a config entry."""
    coordinator: AgentSwarmCoordinator = hass.data[DOMAIN][entry.entry_id]
    
    entities = [
        AgentSwarmSensor(coordinator, description, entry.entry_id)
        for description in SENSORS
    ]
    async_add_entities(entities)


class AgentSwarmSensor(CoordinatorEntity, SensorEntity):
    """Representation of an Agent Swarm sensor."""

    def __init__(
        self,
        coordinator: AgentSwarmCoordinator,
        description: SensorEntityDescription,
        entry_id: str,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        self.entity_description = description
        self._attr_unique_id = f"{entry_id}_{description.key}"
        self._attr_device_info = {
            "identifiers": {(DOMAIN, entry_id)},
            "name": "Agent Swarm",
            "manufacturer": "iret33",
            "model": "Agent Swarm API",
        }

    @property
    def native_value(self):
        """Return the state of the sensor."""
        data = self.coordinator.data
        if data is None:
            return None
            
        if self.entity_description.key == SENSOR_KEY_TOTAL_AGENTS:
            return data.get("total_agents", 0)
        elif self.entity_description.key == SENSOR_KEY_ACTIVE_TASKS:
            return data.get("total_tasks", 0)
        elif self.entity_description.key == SENSOR_KEY_COMPLETED_TASKS:
            # Demo value - would come from API
            return 42
        return None
