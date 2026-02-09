"""Constants for the Agent Swarm integration."""

DOMAIN = "agent_swarm"
PLATFORMS = ["sensor", "binary_sensor"]

CONF_API_URL = "api_url"
CONF_API_KEY = "api_key"

DEFAULT_API_URL = "https://api.moltbook.com"
DEFAULT_SCAN_INTERVAL = 30

SENSOR_KEY_TOTAL_AGENTS = "total_agents"
SENSOR_KEY_ACTIVE_TASKS = "active_tasks"
SENSOR_KEY_COMPLETED_TASKS = "completed_tasks"

BINARY_SENSOR_KEY_ONLINE = "online"

ATTR_AGENT_ID = "agent_id"
ATTR_AGENT_NAME = "agent_name"
ATTR_STATUS = "status"
ATTR_LAST_SEEN = "last_seen"

SERVICE_REFRESH = "refresh"
