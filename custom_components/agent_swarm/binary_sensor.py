"""Binary sensor platform for Agent Swarm."""
from __future__ import annotations

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
    BinarySensorEntityDescription,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, BINARY_SENSOR_KEY_ONLINE
from .coordinator import AgentSwarmCoordinator

BINARY_SENSORS = [
    BinarySensorEntityDescription(
        key=BINARY_SENSOR_KEY_ONLINE,
        name="API Online",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
    ),
]


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Agent Swarm binary sensor based on a config entry."""
    coordinator: AgentSwarmCoordinator = hass.data[DOMAIN][entry.entry_id]
    
    entities = [
        AgentSwarmBinarySensor(coordinator, description, entry.entry_id)
        for description in BINARY_SENSORS
    ]
    async_add_entities(entities)


class AgentSwarmBinarySensor(CoordinatorEntity, BinarySensorEntity):
    """Representation of an Agent Swarm binary sensor."""

    def __init__(
        self,
        coordinator: AgentSwarmCoordinator,
        description: BinarySensorEntityDescription,
        entry_id: str,
    ) -> None:
        """Initialize the binary sensor."""
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
    def is_on(self):
        """Return true if the binary sensor is on."""
        data = self.coordinator.data
        if data is None:
            return False
        
        if self.entity_description.key == BINARY_SENSOR_KEY_ONLINE:
            return data.get("online", False)
        return False
