# caddy_ai2_ros2_common

## Uso desde otro paquete ROS 2

En C++ (CMakeLists.txt):

```cmake
find_package(caddy_ai2_ros2_common REQUIRED)

target_link_libraries(my_driver_node
  socketcan_interface
)
```

```cpp
#include "caddy_ai2_ros2_common/socket_can_interface.hpp"
```

En Python:

```python
from caddy_ai2_ros2_common.launch_utils import read_update_rate_from_controller_yaml
```