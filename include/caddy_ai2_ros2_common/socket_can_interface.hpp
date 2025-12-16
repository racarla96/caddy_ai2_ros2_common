#pragma once

#include <string>
#include <vector>
#include <linux/can.h>

class SocketCANInterface
{
public:
  explicit SocketCANInterface(const std::string& interface_name = "can0");
  ~SocketCANInterface();

  bool init();
  void close();

  int read(std::vector<struct can_frame>& frames, int timeout_ms = 100);
  bool write(const struct can_frame& frame);

  bool isInitialized() const { return initialized_; }

private:
  std::string interface_name_;
  int socket_fd_;
  int epoll_fd_;
  bool initialized_;
};