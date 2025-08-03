#pragma once

#include "esphome/core/helpers.h"
#include "esphome/core/component.h"
#include "esphome/components/text_sensor/text_sensor.h"

namespace esphome {
namespace git_ref {


class GitRefTextSensor : public text_sensor::TextSensor, public PollingComponent {
 public:
  explicit GitRefTextSensor(const char* git_ref_string)
      : _git_ref_string(git_ref_string) {
        //nothing
      }

  void setup() override {
    update();
  }

  void update() override {
    publish_state(_git_ref_string);
  }

  void dump_config() override {
    ESP_LOGCONFIG(TAG, "GitRefTextSensor:");
    ESP_LOGCONFIG(TAG, "   Ref: %s", this->_git_ref_string);
  }

 protected:
  const char *const _git_ref_string;
  static constexpr const char * TAG = "GitRefSensor";
};

}  // namespace git_ref
}  // namespace esphome
