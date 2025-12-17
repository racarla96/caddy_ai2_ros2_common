import yaml
from launch import LaunchContext

def read_update_rate_from_controller_yaml(
    yaml_substitution,  # ← Remove type hint; just accept any substitution-like object
    default: int = 100
) -> int:
    """
    Read controller_manager.ros__parameters.update_rate from a YAML file.
    """
    context = LaunchContext()
    path = yaml_substitution.perform(context)

    try:
        with open(path, "r") as f:
            data = yaml.safe_load(f)

        return (
            data
            .get("controller_manager", {})
            .get("ros__parameters", {})
            .get("update_rate", default)
        )

    except Exception as e:
        print(f"[caddy_ai2_ros2_common] YAML error: {e}")
        return default
